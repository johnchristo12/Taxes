# -*- coding: utf-8 -*-

from odoo import api, fields, models, _


class ResCompany(models.Model):
    _inherit = "res.company"

    account_tds = fields.Many2one(
        string="TDS Account",
        comodel_name='account.account',
        help="Account for Global discount on invoices.")
