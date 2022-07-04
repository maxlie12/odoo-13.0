from odoo import models, fields


class PartnerCRM(models.Model):
    _inherit = 'crm.lead'

    crm_description = fields.Char(String='crm Description')