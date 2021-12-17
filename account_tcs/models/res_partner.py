from odoo import fields, models, api


class ResPartnerInherit(models.Model):
    _inherit = 'res.partner'

    applicable_tcs = fields.Boolean(string="TCS Applicable", default=False)
    tcs_section = fields.Many2one('tcs.management', string="TCS Section")
    tcs_type = fields.Selection([('with_pan', 'With PAN'), ('without_pan', 'Without PAN')], string="TCS Type")
    tcs_percentage = fields.Float(string="TCS %")
    tcs_account = fields.Many2one('account.account', string="TCS Account")

    @api.onchange('tcs_section')
    def onchange_tcs_section(self):
        if self.tcs_section:
            if self.tcs_section.tcs_type:
                self.tcs_type = self.tcs_section.tcs_type
            if self.tcs_section.tcs_percentage:
                self.tcs_percentage = self.tcs_section.tcs_percentage
            if self.tcs_section.tcs_account:
                self.tcs_account = self.tcs_section.tcs_account
