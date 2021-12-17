from odoo import fields, models


class TdsManagement(models.Model):
    _name = "tds.management"
    _description = "Tds Management"

    name = fields.Char(string='Name')
    tds_type = fields.Selection([('with_pan', 'With PAN'), ('without_pan', 'Without PAN')], string="TDS Type")
    tds_percentage = fields.Float(string="TDS %")
    tds_account = fields.Many2one('account.account', string="TDS Account")

