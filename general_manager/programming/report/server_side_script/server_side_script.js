// Copyright (c) 2022, koncrete.tech and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["server side script"] = {
	"filters": [
			{
				"fieldname":"doctype",
				"label":__("server side scripting"),
				"fieldtype":"Link",
				"options":"server side scripting"
			},
			{
				"fieldname":"name",
				"label":__("Name"),
				"fieldtype":"Data",
			},
		{		"fieldname":"surname",
				"label":__("surname"),
				"fieldtype":"Data"
		}
	]
};
