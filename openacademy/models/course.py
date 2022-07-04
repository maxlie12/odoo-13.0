from odoo import models, fields


class CourseInfo(models.Model):
    _name = 'course.academy'
    _description = 'Course Academy'

    name = fields.Char(String='name_course', required=True)
    author = fields.Char(String='name_auther', required=True)
    description = fields.Text(string='description')
    image = fields.Binary(string='image')