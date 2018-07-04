# -*- coding: utf-8 -*-

from odoo import models, fields, api


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    vendor_id = fields.Many2one('product.supplierinfo', 'Vendor')
    is_route = fields.Boolean('Is Route', defualt=False)
    product_tmpl_id = fields.Many2one(related='product_id.product_tmpl_id',
                                      string='Product Template',
                                      store=True)

    @api.multi
    @api.onchange('route_id')
    def _onchange_route_id(self):
        if self.route_id:
            self.is_route = True


class ProcurementOrder(models.Model):
    _inherit = 'procurement.order'

    def _make_po_select_supplier(self, suppliers):
        """ Method intended to be overridden by customized modules
        to implement any logic in the
            selection of supplier.
        """
        if self:
            so = self.env['sale.order.line'].browse(self.sale_line_id.id)
            supplier = so.vendor_id or suppliers[0]

            return supplier
        else:
            return super(ProcurementOrder, self)\
                ._make_po_select_supplier(suppliers)
