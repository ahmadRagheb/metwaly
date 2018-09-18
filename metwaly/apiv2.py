# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
# MIT License. See license.txt
from __future__ import unicode_literals

import json
import frappe
import frappe.handler
import frappe.client
from frappe.utils.response import build_response
from frappe import _
from six.moves.urllib.parse import urlparse, urlencode
import base64

def jv_naming_based_on_company(doc,method):
	series = frappe.get_value("Company",doc.company,"journal_entry_naming_series")
	if series:
		doc.naming_series=series
	else:
		frappe.msgprint("No naming_series found in Company {}".format(doc.company))




def company_updates_jv(doc,method):
	company_jv_series = doc.journal_entry_naming_series
	if company_jv_series:
		naming_series = get_options()
		options = naming_series.split("\n")
		if company_jv_series not in options:
			options.append(company_jv_series)
			update_series(options)


def get_options():
	if frappe.get_meta("Journal Entry").get_field("naming_series"):
		return frappe.get_meta("Journal Entry").get_field("naming_series").options


def update_series(options):
	"""update series list"""
	set_series_for("Journal Entry", options)
	# create series
	map(insert_series, [d.split('.')[0] for d in options if d.strip()])
	frappe.msgprint(_("Series Updated"))


def insert_series(series):
	"""insert series if missing"""
	if not frappe.db.get_value('Series', series, 'name', order_by="name"):
		frappe.db.sql("insert into tabSeries (name, current) values (%s, 0)", (series))

def validate_series_name(n):
	import re
	if not re.match("^[\w\- /.#]*$", n, re.UNICODE):
		throw(_('Special Characters except "-", "#", "." and "/" not allowed in naming series'))

def set_series_for(doctype, ol):
	# options = self.scrub_options_list(ol)
	options = ol
	# validate names
	for i in options: validate_series_name(i)

	# if options and self.user_must_always_select:
	# 	options = [''] + options

	default = options[0] if options else ''

	# update in property setter
	prop_dict = {'options': "\n".join(options), 'default': default}

	for prop in prop_dict:
		ps_exists = frappe.db.get_value("Property Setter",
			{"field_name": 'naming_series', 'doc_type': doctype, 'property': prop})

		if ps_exists:
			ps = frappe.get_doc('Property Setter', ps_exists)
			ps.value = prop_dict[prop]
			ps.save()
		else:
			ps = frappe.get_doc({
				'doctype': 'Property Setter',
				'doctype_or_field': 'DocField',
				'doc_type': doctype,
				'field_name': 'naming_series',
				'property': prop,
				'value': prop_dict[prop],
				'property_type': 'Text',
				'__islocal': 1
			})
			ps.save()

	frappe.clear_cache(doctype=doctype)