# -*- coding: utf-8 -*-
{
    'name': "Open Academy",

    'summary': """Manage trainigns:""",

    'description': """
        Open academy module for managing trainings:
        - training courses
        - training sessions
        - attendees registration
    """,

    'author': "Ceviche",
    'website': "http://www.benandfrank.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Test',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'board'],

    # always loaded
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/openacademy.xml',
        'views/partner.xml',
        'views/session_board.xml',
        'reports/reports.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}