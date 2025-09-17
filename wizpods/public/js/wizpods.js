frappe.ready(() => {
    // Remove "Documentation" link
    // $('.dropdown-help a[href*="docs"]').parent().remove();

    // Remove "Report an Issue" link
    // $('.dropdown-help a:contains("Report an Issue")').parent().remove();

    // If you just want the dropdown gone entirely:
    $('.dropdown-help').remove();
});