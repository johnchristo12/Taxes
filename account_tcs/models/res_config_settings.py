from odoo import api, fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    group_order_tcs = fields.Boolean(
        string="Allow TCS",
        implied_group='account_tcs.group_order_tcs',
        config_parameter='account.group_order_tcs',
        help="Allows TCS")
    account_tcs = fields.Many2one(
        string="Allow TCS Account",
        comodel_name='account.account',
        related="company_id.account_tcs",
        readonly=False,
        help="Allow TCS Account")

    def set_values(self):
        super(ResConfigSettings, self).set_values()
        IrConfigPrmtr = self.env['ir.config_parameter'].sudo()
        IrConfigPrmtr.set_param('account.group_order_tcs',
                                self.group_order_tcs)

    @api.model
    def get_values(self):
        res = super(ResConfigSettings, self).get_values()
        IrConfigPrmtr = self.env['ir.config_parameter'].sudo()
        group_order_tcs = IrConfigPrmtr.get_param(
            'account.group_order_tcs')
        res.update({
            'group_order_tcs': group_order_tcs,
        })
        return res
