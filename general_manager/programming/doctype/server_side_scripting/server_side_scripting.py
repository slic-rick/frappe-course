# Copyright (c) 2022, koncrete.tech and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class serversidescripting(Document):
	# @frappe.whitelist()
	pass
	# Events for server scripting in frappe
	
	# def validate(self):
	# 	frappe.msgprint("Printing from server side ::::::::::::::::::")


# Before a document gets saved this event gets triggered
	# def before_save(self):
	# 	frappe.msgprint("Showing the before save event, before doc get saved!")

	# Before the form values are inserted in the database
	# def before_insert(self):
	# 	frappe.msgprint("I hope to never use PHP in my life")

	# Called after the values are inserted in db
	# def after_insert(self):
	# 	frappe.msgprint("After the form saved to db")

	# Called when updating the doc

	# def on_update(self):
	# 	frappe.msgprint('On update got called')

	# get called before the doc is submitted
	# def before_submit(self):
	# 	frappe.msgprint("Before the form gets submmited")

	# Get called when the doc got submitted
	# def on_submit(self):
	# 	frappe.msgprint('When the form gets submitted')

	# Gets called when the doc got deleted
	# def on_trash(self):
	# 	frappe.msgprint("The doc got deleted")
	
	# Gets called after the doc got deleted
	# def after_delete(self):
	# 	frappe.msgprint("After the doc got deleted:::::::::::::::::")

	# Getting values from fields

	# def validate(self):
	# 	frappe.msgprint("Hello my name is" + self.server_name )

	# showing the values of the child table

	# def validate(self):
	# 	for row in self.get('table'):
	# 		frappe.msgprint("Table name: " + row.client_name)

	# Getting the doc that is linked to this doc
		#get_doc(doctype name,fieldname for linked doc)

	# def validate(self):
	# 	self.get_document()

	
	# def get_document(self):
		
	# 	# Getting the doc fron client scripting doctype
	# 	doc = frappe.get_doc('client scripting',self.document)
	# 	# frappe.msgprint(doc.id)


	# 	# Getting the table in the linked doc
	# 	for row in doc.get('table'):
	# 		frappe.msgprint(row.new_name)


	# def validate(self):
	# Get new doc from the specified doctype
	# 	doc = frappe.new_doc('client scripting')
	# 	doc.id = 'Nghiinomenwa tiko tiko bukwanwe'
	# 	doc.surname = 'Erikson'
	# 	doc.address = 'Ongha'

	# 	# Add to the table in the doc
	# 	doc.append('table',{
	# 		"new_name":"Mr Nghiinomenwa",
	# 		"new_client":"Koncrete.tech",
	# 		"new_address":"It is becoming clear now"
	# 	})
		
	# 	# Insert the doc in the doctype
	# 	doc.insert()

	# Doc methods

	# updating a doc

	# def validate(self):
	# 	# get the doc before you can update it
	# 	doc = frappe.get_doc('client scripting',self.document)
	# 	# update the doc
	# 	doc.db_set('surname','KONCRETE.TECH')

		# def validate(self):
		# 	doc = frappe.get_doc('client scripting' , self.document)
		# 	# Deleting the selected document
		# 	doc.delete()

	#################################################################################
	# Database API

	# Getting all the doc from a certain doctype
	# db.get_list(doctype,fields=[],filter={ "name" :'slic'},orderby,limit,start)

	# def validate(self):
	# 	self.get_all_docs()
	

	# def get_all_docs(self):
	# 	doc = frappe.db.get_list('client scripting',fields=['id','surname'])

	# 	for d in doc:
	# 	 frappe.msgprint(d.id)

	# setting  and getting values from a doctype

	# def validate(self):
		# name = frappe.db.get_values('client scripting',self.document,['id'])
		# finalprint = str(name)
		# frappe.msgprint(finalprint)	
		# self.set_new_value()
		# self.show_number()
		# self.check_exists()
		#self.sql_queries()

	# def set_new_value(self):
	# 	frappe.db.set_value('client scripting',self.document,'id','General manager W')
	# 	doc = frappe.db.get_value('clients scripting',self.document,['id'])
	# 	frappe.msgprint(str(doc))

	# Show the number of docs in a doc type
	# frappe.db.count(doctype,filters)
	# def show_number(self):
	# 	num = frappe.db.count('client scripting')
	# 	frappe.msgprint('The number of docs is : ' + str(num))

	# Check if a doc exixts in a doctype
	# frapp.db.exists(doctype,docname)

	# def check_exists(self):
	# 	if(frappe.db.exists('client scripting','What the fuck')):
	# 		frappe.msgprint("Document exists")
	# 	else:
	# 		frappe.msgprint("Document does not exist")


							# SQL QUERIES

# Write SQl queries
# frappe.db.sql(""" QUERY """,type)
	# def sql_queries(self):
	# 	data = frappe.db.sql(""" SELECT * 
	# 							FROM `tabclient scripting` 
	# 							""",as_dict=1)
	# 	for d in data:
	# 		frappe.msgprint(d.id)


	# This method get's called by the .js file, receives msg from the frm.call({})

	# def frm_side(self,msg):
	# 	# frappe.msgprint(msg)
	# 	return "Well received. Thank you."

	
	# def  frm_call(self,msg):
	# 	import time
	# 	time.sleep(5)
	# 	return "Sending from python"





