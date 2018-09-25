# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "metwaly"
app_title = "Metwaly"
app_publisher = "ahmadragheb"
app_description = "hook nameing series jv based on company cusotm series name"
app_icon = "octicon octicon-file-directory"
app_color = "blue"
app_email = "ahmedragheb@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/metwaly/css/metwaly.css"
# app_include_js = "/assets/metwaly/js/metwaly.js"

# include js, css files in header of web template
# web_include_css = "/assets/metwaly/css/metwaly.css"
# web_include_js = "/assets/metwaly/js/metwaly.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "metwaly.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "metwaly.install.before_install"
# after_install = "metwaly.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "metwaly.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }
doc_events = {
	"Journal Entry": {
		"autoname": "metwaly.apiv2.jv_naming_based_on_company",
	},
	"Company": {
		"on_update": "metwaly.apiv2.company_updates_jv",
	}

}

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"metwaly.tasks.all"
# 	],
# 	"daily": [
# 		"metwaly.tasks.daily"
# 	],
# 	"hourly": [
# 		"metwaly.tasks.hourly"
# 	],
# 	"weekly": [
# 		"metwaly.tasks.weekly"
# 	]
# 	"monthly": [
# 		"metwaly.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "metwaly.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "metwaly.event.get_events"
# }

fixtures = ["Custom Script","Custom Field"]

