from odoo import api, fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    group_order_tds = fields.Boolean(
        string="Allow TDS",
        implied_group='account_tds.group_order_tds',
        config_parameter='account.group_order_tds',
        help="Allows TDS", default=False)
    account_tds = fields.Many2one(
        string="Allow TDS Account",
        comodel_name='account.account',
        related="company_id.account_tds",
        readonly=False,
        help="Allow TDS Account")

    def set_values(self):
        super(ResConfigSettings, self).set_values()
        IrConfigPrmtr = self.env['ir.config_parameter'].sudo()
        IrConfigPrmtr.set_param('account.group_order_tds',
                                self.group_order_tds)

    @api.model
    def get_values(self):
        res = super(ResConfigSettings, self).get_values()
        IrConfigPrmtr = self.env['ir.config_parameter'].sudo()
        group_order_tds = IrConfigPrmtr.get_param(
            'account.group_order_tds')
        res.update({
            'group_order_tds': group_order_tds,
        })
        return res
