from odoo import models, fields


class Attendees(models.Model):
    _name = 'attendees.academy'

    name = fields.Char(String='Name attendees', required=True)
    session_id = fields.Many2many('session.academy', string='Session', readonly=True)


class AttendeesInfo(models.Model):
    _name = 'attendees.academy'
    _inherit = 'attendees.academy'

    instructor = fields.Boolean(string='Instructor', default=False)
    teacher1 = fields.Boolean(string='teacher1', default=False)
    teacher2 = fields.Boolean(string='teacher2', default=False)


