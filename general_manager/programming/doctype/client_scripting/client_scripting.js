// Copyright (c) 2022, koncrete.tech and contributors
// For license information, please see license.txt

frappe.ui.form.on('client scripting', {


	// refresh: (frm) => {

	// 	// If we are making a new document, then we display a customised intro
	// 	if(frm.is_new()){
	// 		frm.set_intro('This is a new Custom intro');
	// 	}

	// }

	/**
	 * Setting the values of the field when validate gets called
	 */

	// validate: (frm) => {

	// 	frm.set_value('id',"Abraham Erikson");


	// 	let row = frm.add_child('table',{
	// 		client_name:"Koncrete.tech"
	// 	});
	// }

	/**
	 * Changing the properties of the doc field_name in script
	 */

	// surname: function (frm) {
	// 	// frm.set_df_property('id','reqd',1);

	// 	frm.toggle_reqd('id',true)
	// }


	//When the doc get's refreshed
	// refresh: function(frm) {
	// 		frappe.msgprint("Wish uoi good luck");
	// }
	// onload: function(frm){
	// 	frappe.msgprint("ON load event has been called: ");
	// }


	// Called before a doc is saved, prevents the form from being saved if this event get called
	// validate:function (frm) {
	// 	frappe.throw("ON validate event got called:::: ")
	// }


	// Called before a document gets saved
	// before_save: function (frm) {
	// 	frappe.msgprint("Before the doc get's saved ?")
	// }


	// Called after the doc get saved
	// after_save: function (frm) {
	// 	frappe.msgprint('THe document got saved :::::::::::::::::::::::::::::::::::::::::::::::::;;;')
	// }

	/**
	 * Field based events
	 */


	// This will get called when the input of the {field_name:id} becomes active
	// id:function (frm) {
	// 	frappe.msgprint("The name event get triggered ::::::::::::::::::::::::::::::::::::::::::");
	// }

	// before_submit:function () {
	// 	frappe.msgprint("Befofre the message gets submitted :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
	// }

	// on_submit:function (frm) {
	// 	console.log(frm);
	// 	frappe.msgprint('THE DOC GET SUBMITTED ::::::::::::::::::::::::::::::;');
	// }


	// Called before the doc is cancelled
	// before_cancel:function (frm) {
	// 	frappe.msgprint('Can not calcel event');
	// }

	// after_cancel:function (params) {
	// 	frappe.throw('Can not cancel this document ::::::::::::::::::::');
	// }

	/**
	 * For getting values for the fields
	 */
	

	// id:(frm) =>{

	// 	frappe.msgprint(frm.doc.id);
	// 	console.log(frm);
	// 	// console.log(frm.doc.id);
	// }

	// before_save: (frm) => {
	// 		for (const row of frm.doc.table) {
	// 			frappe.msgprint(`Enter : ${row.client_name} >> Index : ${row.idx}`);
	// 		}
	// }


	/**
	 * Custom Buttons
	 */


	refresh(frm){

		// Creating a custom button
		// frm.add_custom_button('Custom button',() => {
		// 	frappe.msgprint("Custom button gets clicked")
		// })

		// Creating a frop down of buttons

		frm.add_custom_button("Male",() => {
			frappe.msgprint("Male button gets clicked")
		},'Gender')

		frm.add_custom_button("Female",() => {
			frappe.msgprint("Female button gets clicked")
		},'Gender')
	}
	
	

	

});

/**
 * For accessing the row in the child table 
 */

frappe.ui.form.on('child doc',{
	// Cdt is the doc_name and cdn is the row in the table 
	// new_name(frm,cdt,cdn){
		
	// 		frappe.msgprint(`Printing the entered name: ${cdt} ${cdn}`)

	// }
}
);
