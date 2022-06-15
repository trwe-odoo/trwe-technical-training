# -*- coding: utf-8 -*-

{
    'name': 'Odoo Space Mission',
    'summary': """Keep track of spaceships""",
    'description': """
        Keep track of spaceships
    """,
    'author': 'Odoo',
    'website': 'https://www.odoo.com',
    'category': 'Training',
    'version': '0.1',
    'depends': ['base'],
    'data': [
        'security/space_security.xml',
        'security/ir.model.access.csv',
        'views/space_menuitems.xml',
        'views/space_views.xml',
        'views/mission_views.xml',
    ],
    'demo': [
        'demo/spaceship_demo.xml',
    ],
}