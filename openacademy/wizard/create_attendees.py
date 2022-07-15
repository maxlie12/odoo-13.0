from odoo import models, fields, api


class CreateAttedees(models.TransientModel):
    _name = 'create.attendees'
    _description = "Wizard Test: Quick register of attendees to Session"

    # def _default_session(self):
    #     return self.env('openacademy.session').browse(self._context.get('active_id'))

    session_id = fields.Many2one('session.academy', string='Session', required=True,)
    attendees_id = fields.Many2many('attendees.academy', string='Attendees')
    description = fields.Char(String="description")

    # def create_attendees(self):
    #     ids = self.env.context('active_ids')
    #     sessions = self.env['session.academy'].browse(ids)
    #     new_data = []
    #
    #     if self.attendees_id:
    #         new_data["attendees_id"] = self.attendees_id
    #
    #     sessions.write(new_data)

