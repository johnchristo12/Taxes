from odoo import fields, models, api


class ResPartnerInherit(models.Model):
    _inherit = 'res.partner'

    applicable_tds = fields.Boolean(string="TDS Applicable", default=False)
    tds_section = fields.Many2one('tds.management', string="TDS Section")
    tds_type = fields.Selection([('with_pan', 'With PAN'), ('without_pan', 'Without PAN')], string="TDS Type")
    tds_percentage = fields.Float(string="TDS %")
    tds_account = fields.Many2one('account.account', string="TDS Account")

    @api.onchange('tds_section')
    def onchange_tds_section(self):
        if self.tds_section:
            if self.tds_section.tds_type:
                self.tds_type = self.tds_section.tds_type
            if self.tds_section.tds_percentage:
                self.tds_percentage = self.tds_section.tds_percentage
            if self.tds_section.tds_account:
                self.tds_account = self.tds_section.tds_account
