frappe.pages['server-side-page'].on_page_load = function(wrapper) {
	var page = frappe.ui.make_app_page({
		parent: wrapper,
		title: 'Demo page',
		single_column: true
	});

	page.set_title('Koncrete.tech')

	let $btn = page.set_primary_action('Primary', () => frappe.msgprint("Primary action button clicked"))
	let $btnOne = page.set_secondary_action('Secondary',() => frappe.msgprint("Secondary action Button"))
	page.add_menu_item("Menu",() => frappe.msgprint("Menu item"))
	page.add_action_item("Action item",() => frappe.msgprint("Action Item"))

	// Adding a field to the page

	let field =page.add_field({
		label:'Gender',
		fieldtype:'Select',
		fieldName:'Name',
		options:["Male","Female"],
		onchange(){
			frappe.msgprint(field.get_value())
		}
	})

	// Renderin a custom css and html

	$(frappe.render_template('server_side_page',{
		data:"Print the passed in data"
	})).appendTo(page.body)

}	
