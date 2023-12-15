import frappe

no_cache = 1


def get_context(context):
	context.categories = get_categories()

	return context

def get_categories():
	return frappe.get_all("Help Category", fields="*", order_by='custom_prio ASC')
