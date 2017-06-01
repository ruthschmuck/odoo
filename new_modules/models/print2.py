# -*- coding: utf-8 -*-
from odoo import models, fields, api

class print2(models.TransientModel):
    _name = "sale.wizard"
    _inherit = "sale.order"

    wiz = fields.Char(string="New Wizard")

    @api.multi
    def my_button(self):
        self.write({'state': "sent"})
        return {
            'name': 'New Wizard',
            'type': 'ir.actions.act_window',
            'res_model': 'sale.wizard',
            'view_type': 'form',
            'view_mode': 'form',
            'target': 'new',
        }
