[![Runbot Status](https://runbot.odoo-community.org/runbot/badge/flat/167/10.0.svg)](https://runbot.odoo-community.org/runbot/repo/github-com-oca-sale-workflow-167)
[![Build Status](https://travis-ci.org/OCA/sale-workflow.svg?branch=10.0)](https://travis-ci.org/OCA/sale-workflow)
[![codecov](https://codecov.io/gh/OCA/sale-workflow/branch/10.0/graph/badge.svg)](https://codecov.io/gh/OCA/sale-workflow)

Odoo Sales, Workflow and Organization
======================================

This project aim to deal with modules related to manage sale and their related workflow. You'll find modules that:

 - Allow to group discounts / advances / fees separately
 - Add a condition on sales that is pushed on related invoices
 - Compute shipped rate differently
 - Easy the cancellation of SO
 - ...

[//]: # (addons)

Available addons
----------------
addon | version | summary
--- | --- | ---
[sale_exception](sale_exception/) | 10.0.2.0.0 | Custom exceptions on sale order
[sale_order_lot_selection](sale_order_lot_selection/) | 10.0.1.0.0 | Sale Order Lot Selection
[sale_product_set](sale_product_set/) | 10.0.1.0.0 | Sale product set
[sale_product_set_layout](sale_product_set_layout/) | 10.0.1.0.0 | Sale product set layout


Unported addons
---------------
addon | version | summary
--- | --- | ---
[account_invoice_reorder_lines](account_invoice_reorder_lines/) | 0.1 (unported) | Invoice lines with sequence number
[mail_quotation](mail_quotation/) | 0.1 (unported) | Mail quotation
[partner_prepayment](partner_prepayment/) | 8.0.1.0.0 (unported) | Option on partner to set prepayment policy
[partner_prospect](partner_prospect/) | 8.0.1.0.0 (unported) | Partner Prospect
[pricelist_share_companies](pricelist_share_companies/) | 1.0 (unported) | Share pricelist between compagnies, not product
[product_customer_code_sale](product_customer_code_sale/) | 1.0 (unported) | Product Customer code on sale
[product_special_type](product_special_type/) | 1.0 (unported) | Product Special Types
[product_special_type_invoice](product_special_type_invoice/) | 1.0 (unported) | Product Special Type on Invoice
[product_special_type_sale](product_special_type_sale/) | 1.0 (unported) | Product Special Type on Sale
[sale_automatic_workflow](sale_automatic_workflow/) | 9.0.1.0.0 (unported) | Sale Automatic Workflow
[sale_automatic_workflow_payment_mode](sale_automatic_workflow_payment_mode/) | 9.0.2.0.0 (unported) | Sale Automatic Workflow - Payment Mode
[sale_cancel_reason](sale_cancel_reason/) | 8.0.1.1 (unported) | Sale Cancel Reason
[sale_condition_text](sale_condition_text/) | 1.3 (unported) | Sale/invoice condition
[sale_delivery_term](sale_delivery_term/) | 0.1 (unported) | Delivery term for sale orders
[sale_dropshipping](sale_dropshipping/) | 1.1.1 (unported) | Sale Dropshipping
[sale_exception_nostock](sale_exception_nostock/) | 8.0.1.2.0 (unported) | Sale stock exception
[sale_fiscal_position_update](sale_fiscal_position_update/) | 1.0 (unported) | Changing the fiscal position of a sale order will auto-update sale order lines
[sale_jit_on_services](sale_jit_on_services/) | 1.0 (unported) | Sale Service Just In Time
[sale_last_price_info](sale_last_price_info/) | 8.0.1.0.0 (unported) | Product Last Price Info - Sale
[sale_multi_picking](sale_multi_picking/) | 0.1 (unported) | Multi Pickings from Sale Orders
[sale_order_add_variants](sale_order_add_variants/) | 8.0.0.1.0 (unported) | Add variants from template into sale order
[sale_order_force_number](sale_order_force_number/) | 0.1 (unported) | Force sale orders numeration
[sale_order_line_description](sale_order_line_description/) | 8.0.1.0.0 (unported) | Sale order line description
[sale_order_price_recalculation](sale_order_price_recalculation/) | 8.0.1.0.0 (unported) | Price recalculation in sales orders
[sale_order_revision](sale_order_revision/) | 8.0.0.1.0 (unported) | Sale order revisions
[sale_order_type](sale_order_type/) | 8.0.1.0.1 (unported) | Sale Order Types
[sale_owner_stock_sourcing](sale_owner_stock_sourcing/) | 8.0.0.1.0 (unported) | Manage stock ownership on sale order lines
[sale_packaging_price](sale_packaging_price/) | 9.0.1.0.0 (unported) | Sale Packaging Price
[sale_partner_order_policy](sale_partner_order_policy/) | 8.0.1.0.0 (unported) | Adds customer create invoice method on partner form
[sale_payment_term_interest](sale_payment_term_interest/) | 8.0.1.0.0 (unported) | Sales Payment Term Interests
[sale_procurement_group_by_line](sale_procurement_group_by_line/) | 8.0.1.0.0 (unported) | Base module for multiple procurement group by Sale order
[sale_quotation_number](sale_quotation_number/) | 8.0.1.1.0 (unported) | Different sequence for sale quotations
[sale_quotation_sourcing](sale_quotation_sourcing/) | 8.0.0.3.1 (unported) | manual sourcing of sale quotations
[sale_quotation_sourcing_stock_route_transit](sale_quotation_sourcing_stock_route_transit/) | 8.0.0.1.0 (unported) | Link module for sale_quotation_sourcing + stock_route_transit
[sale_reason_to_export](sale_reason_to_export/) | 8.0.0.1.0 (unported) | Reason to export in Sales Order
[sale_rental](sale_rental/) | 8.0.0.1.0 (unported) | Manage Rental of Products
[sale_sourced_by_line](sale_sourced_by_line/) | 8.0.1.1.0 (unported) | Multiple warehouse source locations for Sale order
[sale_sourced_by_line_sale_transport_multi_address](sale_sourced_by_line_sale_transport_multi_address/) | 8.0.1.0.0 (unported) | Make sale_sourced_by_line and sale_transport_multi_addresswork together
[sale_start_end_dates](sale_start_end_dates/) | 8.0.0.1.0 (unported) | Adds start date and end date on sale order lines
[sale_stock_global_delivery_lead_time](sale_stock_global_delivery_lead_time/) | 0.1 (unported) | Sale global delivery lead time
[sale_validity](sale_validity/) | 8.0.7.0.0 (unported) | Sales Quotation Validity Date

[//]: # (end addons)

Translation Status
------------------
[![Transifex Status](https://www.transifex.com/projects/p/OCA-sale-workflow-10-0/chart/image_png)](https://www.transifex.com/projects/p/OCA-sale-workflow-10-0)
