from odoo import fields, models


class TcsManagement(models.Model):
    _name = "tcs.management"
    _description = "Tcs Management"

    name = fields.Char(string='Name')
    tcs_type = fields.Selection([('with_pan', 'With PAN'), ('without_pan', 'Without PAN')], string="TCS Type")
    tcs_percentage = fields.Float(string="TCS %")
    tcs_account = fields.Many2one('account.account', string="TCS Account")
