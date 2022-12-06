# Copyright (c) 2022, koncrete.tech and contributors
# For license information, please see license.txt

import frappe
from frappe import _, msgprint


def execute(filters=None):

	if not filters:filters = {}

	columns, data = [], []

	columns = get_column()
	cs_data = get_cs_data(filters)

	if not cs_data:
		msgprint("No data found::")
		return columns, cs_data

	data = []

	for d in cs_data:
		row = frappe._dict({
			'name':d.server_name,
			'surname':d.surname,
			'age':d.age
		})

		data.append(row)

	chart = get_chart(data)
	report_summary = get_report_summary(data)
	return columns, data,None,chart,report_summary


# The columns for displaying fieldtype from a doc in a doctype
def get_column():
	return [
		{
			"fieldname":"server_name",
			"label":_("name"),
			"fieldtype":"Data"

		},
		{
			"fieldname":"surname",
			"label":_("surname"),
			"fieldtype":"Data"
		}
	]


# Getting data from doctype
def get_cs_data(filters):
	conditions = get_conditions(filters)
	data = frappe.get_all(
		doctype = "server reports",
		filters = conditions,
		fields = ["server_name","surname",'age'])

	return data

# Getting the conditions from the filter and storing them in a {}
def get_conditions(filters):
	conditions = {}
	for key,value in filters.items():
		if filters.get(key):
			conditions[key] = value
	return conditions


def get_chart(data):
	if not data:
		return None
	
	labels = ["age > 45","age =< 45"]

	age_data = {
		'age > 45' : 0,
		'age =< 45' : 0
	}

	datasets = []

	for d in data:
		if d.age > 45:
			age_data['age > 45'] += 1
		else:
			age_data["age =< 45"] += 1
	datasets.append({
		'name':'Age status',
		'values':[age_data.get('age > 45'), age_data.get('age =< 45')]
	})

	chart = {
		'data':{
			'labels':labels,
			'datasets':datasets
		},
		'type':'bar',
		'height':300
	}

	return chart



def get_report_summary(data):
	if not data:
		return None
	
	age_below_45,age_above_45 = 0,0

	for d in data:
		if d.age > 45:
			age_above_45 += 1
		else:
			age_below_45 += 1

	return [{
		'value':age_below_45,
		'indicator':'green',
		'label':'Age below 45',
		'datatype':'int'
	 },
	 {
		'value':age_above_45,
		'indicator':'red',
		'label':'Age above 45',
		'datatype':'int'
	 }
	 ]