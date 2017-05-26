# -*- coding: utf-8 -*-
from odoo import models, fields, api

class print2(models.Moldel):
    _inherit = "purchase.order"

    @api.multi
    def my_button(self):
        self.write({'state': "sent"})
        return self.env['report'].get_action(self, 'purchase.report_purchasequotation')