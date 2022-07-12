from odoo import http
import logging
import json
_logger = logging.getLogger(__name__)


class CourseController(http.Controller):
    @http.route('/api', auth='public', website=False, csrf=False, type='json', methods=['get', 'POST'])
    def hello(self, **kw):
        # add information in database to API postman
        contacts = http.request.env['course.academy'].search([])
        contact_list = []
        for contact in contacts:
            contact_list.append({
                'name': contact.name,
                'author': contact.author,
                'description': contact.description,
            })
        return contact_list
    @http.route('/api/insert', auth='public', website=False, csrf=False, type='json', methods=['get', 'POST'])
    def add(self, **kw):
        insert = http.request.env['course.academy'].sudo().create({
            'name': kw.get('name'),
            'author': kw.get('author'),
            'description': kw.get('description')
        }).id
        return json.dumps(insert)