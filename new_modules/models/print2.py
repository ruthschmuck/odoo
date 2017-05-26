# -*- coding: utf-8 -*-
from odoo import models, fields, api

class print2(models.Model):
    _inherit = "sale.order"

    @api.multi
    def my_button(self):
        self.write({'state': "sent"})
        return self.env['report'].get_action(self, 'my_module.antoni_report_saleorder')