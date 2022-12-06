# Copyright (c) 2022, koncrete.tech and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class clientscripting(Document):
	pass


@frappe.whitelist()
def frappe_call(msg):
	return "I have to heal myself"