import frappe

def get_context(context):
    # Querying upcoming products (assuming you have a field named 'release_date' in your Item doctype)
    upcoming_products = frappe.db.sql("""
        SELECT item_code, item_name, description, valuation_rate, image
        FROM `tabItem` 
        WHERE creation > CURDATE() 
        ORDER BY creation ASC 
        LIMIT 8
    """, as_dict=True)

    context.upcoming_products = upcoming_products

    # Querying shoe brands
    shoe_brands = frappe.get_list("Brand", fields=["name", "description", "logo"])

    context.shoe_brands = shoe_brands
