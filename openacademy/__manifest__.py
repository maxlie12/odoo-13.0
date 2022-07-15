# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'Open academy',
    'catetory' : 'Extra Tools',
    'version' : '1.1',
    'summary': 'open academy',
    'sequence': 15,
    'depends' : ['crm'],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/customise.xml',
        'views/view_session.xml',
        'views/view_attendees.xml',
        'report/session_report.xml',
    ],
    'description': """Open academy""",
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
