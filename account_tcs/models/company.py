# -*- coding: utf-8 -*-

from odoo import api, fields, models, _


class ResCompany(models.Model):
    _inherit = "res.company"

    account_tcs = fields.Many2one(
        string="TCS Account",
        comodel_name='account.account',
        help="Account for Global discount on invoices.")
