import frappe
from frappe import _

@frappe.whitelist()
def create_Suits(**kwargs):
    """Create a new Suit record"""
    try:
        data = frappe._dict(kwargs)

        required_fields = ["name1"]
        for field in required_fields:
            if not data.get(field):
                frappe.throw(_("{0} is required").format(field))

        suit = frappe.new_doc("Suits")
        suit.update({
            "name1": data.get("name1"),
            "scope_of_work": data.get("scope_of_work"),
            "entry_date": data.get("entry_date"),
            "client": data.get("client"),
            "client_role": data.get("client_role"),
            "internal_reference_number": data.get("internal_reference_number"),
            "priority": data.get("priority"),
            "opponent": data.get("opponent"),
            "opponent_role": data.get("opponent_role")
        })

        suit.insert(ignore_permissions=True)

        return {
            "name": suit.name,
            "message": _("Suit created successfully")
        }

    except Exception as e:
        frappe.log_error(frappe.get_traceback(), _("Failed to create Suit"))
        frappe.throw(_("Failed to create Suit. Error: {0}").format(str(e)))
