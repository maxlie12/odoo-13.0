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
        'security/ir.model.access.csv',
        'views/customise.xml',
        'views/menu.xml',
        'views/view_session.xml',
    ],
    'description': """Open academy""",
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
