// Copyright (c) 2022, koncrete.tech and contributors
// For license information, please see license.txt

frappe.ui.form.on('server side scripting', {
	// refresh: function(frm) {

	// }

	// Using frappe.call to access any python file in the module

	server_name:(frm) => {
		frappe.call({
	
			method:'general_manager.programming.doctype.client_scripting.client_scripting.frappe_call',
			args:{
				msg:"Message from client side .js file"
			},
			freeze:true,
			freeze_message:__("The slow programmer"),
			callback: (r) =>{
				frappe.msgprint(r.message)

			}
		})
	}
});
