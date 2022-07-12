import random
from odoo import models, fields, api, exceptions


class SessionInfo(models.Model):
    _name = 'session.academy'
    _description = 'Session academy'

    name = fields.Char(String='Name', required=True)
    start_date = fields.Datetime(String='Datetime', default=fields.Date.today)
    duration = fields.Float(String='Date', digits=(6, 2), help="Duration in days")
    number_of_seat = fields.Integer(String='number of seat')
    active = fields.Boolean(default=True)
    # Taken seat
    taken_seats = fields.Float(string='taken seats', computer='_taken_seats')
    seats = fields.Integer(string='seats', computer='seats')
    # connect many 2 one(Many2one)
    instructor = fields.Many2one('attendees.academy', string='Instructor',
                                 domain=[('instructor', '=', True)])
    teacher1 = fields.Many2one('attendees.academy', string='Teacher1',
                               domain=[('teacher1', '=', True)])
    teacher2 = fields.Many2one('attendees.academy', string='Teacher2',
                               domain=[('teacher2', '=', True)])
    course_id = fields.Many2one('course.academy', string='Course id')
    # (Many2many)
    attendees_id = fields.Many2many('attendees.academy', string="attendees")

    @api.depends('seats', 'attendees_id')
    def _taken_seats(self):
        for r in self:
            if not r.seats:
                r.taken_seats = 0.0
            else:
                r.taken_seats = 100.0 * len(r.attendees_id) / r.seats

    @api.onchange('seats', 'attendees')
    def _verify_valid_seats(self):
        if self.seats < 0:
            return {
                'warning': {
                    'title': "Incorrect 'seats' value",
                    'message': "The number of available 'seats' may not be negative"
                }
            }
        if self.seats < len(self.attendees_id):
            return {
                'warning': "To many attendees",
                'message': "Increase seats or remove excess attendees"
            }

    @api.constrains('instructor', 'attendees_id')
    def check_instructor_not_attendees(self):
        for r in self:
            if r.instructor and r.instructor in r.attendees_id:
                raise exceptions.ValidationError("A session instructor can't be an attendees")
