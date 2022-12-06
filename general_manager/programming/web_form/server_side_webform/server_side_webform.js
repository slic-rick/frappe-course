frappe.ready(function() {
	// bind events here

	console.log("FRAPPE.READY CALLED :::::::::::::::::::::::::::;");

	// frappe.web_form.after_load = () => {

	// 	frappe.msgprint("After load is working")

		// frappe.web_form.on('dob',(field,value) => {
		// 	if(field){
		// 		var date = new Date(value)
		// 		var today = new Date()

		// 		var age = Math.floor((today - date) * 365.25 * 24 * 60 * 60 * 60)
		// 		frappe.web_form.set_value('age',[age])
		// 	}
		// })
	//};

	frappe.web_form.on('dob',(field,value) => {
		// frappe.msgprint('Please fill all values carefully');
		if(field){
			var date = new Date(value)
			var today = new Date()

			var age = Math.floor((today - date) / (365.25 * 24 * 60 * 60 * 1000))
			frappe.web_form.set_value('age',[age])
		}
	})
	// })
	// Method for validating form

	frappe.web_form.validate = () => {

		var age = frappe.web_form.get_value('age');

		if(age < 10){
			frappe.msgprint("The age has to be more than 10")
			return false;
		}

		return true
	}

	// frappe.init_client_script = () => {
	// 	frappe.msgprint('Please fill all values carefully');
	// }

	// frappe.web_form.after_load = () => {
	// 	console.log("IN FRAPPE.WEB_FORM.AFTER_LOAD");
	// 	frappe.msgprint('Please fill all values carefully');
	// };
})