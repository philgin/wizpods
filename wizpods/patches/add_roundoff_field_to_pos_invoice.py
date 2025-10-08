import frappe

def execute():
    """Ensure the field use_company_roundoff_cost_center exists on POS Invoice"""
    fieldname = "use_company_roundoff_cost_center"
    doctype = "POS Invoice"

    if not frappe.db.exists("Custom Field", {"dt": doctype, "fieldname": fieldname}):
        frappe.get_doc({
            "doctype": "Custom Field",
            "dt": doctype,
            "fieldname": fieldname,
            "label": "Use Company Roundoff Cost Center",
            "fieldtype": "Check",
            "default": 0,
            "insert_after": "rounding_adjustment",
        }).insert(ignore_permissions=True)
        frappe.db.commit()
        frappe.logger().info(f"✅ Added missing field: {fieldname} on {doctype}")
    else:
        frappe.logger().info(f"ℹ️ Field already exists: {fieldname} on {doctype}")