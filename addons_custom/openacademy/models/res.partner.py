from odoo import models, fields


class Instructor_user(models.Model):
    _inherit = 'res.partner'

    instructor = fields.Boolean(String="Instructor")

