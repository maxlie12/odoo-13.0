from odoo import models, fields


class CourseInfo(models.Model):
    _name = 'course.academy'
    _description = 'Course Academy'

    # def _default_name(self):
    #     return self.get_value()
    #
    # def call(self):
    #     return self.check("model")

    name = fields.Char(String='name_course', required=True)
    author = fields.Char(String='name_auther', required=True)
    description = fields.Text(string='description')
    image = fields.Binary(string='image', attachment=True)
    responsible_user = fields.Many2one('res.users', string='Responsible User', index=True)
    session_list = fields.One2many('session.academy', 'course_id', string='Session list')

