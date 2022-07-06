from odoo import models, fields


class SessionInfo(models.Model):
    _name = 'session.academy'
    _description = 'Session academy'

    name = fields.Char(String='Name', required=True)
    start_date = fields.Datetime(String='Datetime', default=fields.Date.today)
    duration = fields.Float(String='Date',digits=(6,2), help="Duration in days" )
    number_of_seat = fields.Integer(String='number of seat')
    instructor = fields.Many2one('res.partner', string='Instructor')
    course_id = fields.Many2one('course.academy', string='Course id')


class AttendeesInfo(models.Model):
    _name = 'attendees.academy'
    _description = 'Attendees academy'

