from odoo import models, fields, api


class CreateAttedees(models.TransientModel):
    _name = 'create.attendees.wizard'
    _description = "Wizard Test: Quick register of attendees to Session"

    def _default_session(self):
        return self.env('openacademy.session').browse(self._context.get('active_id'))

    session_id = fields.Many2one('session.academy', string='Session', required=True, default=_default_session)
    attendees_id = fields.Many2many('attendees.academy', string='Attendees')



