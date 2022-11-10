# -*- coding: utf-8 -*-


{
    'name': 'Open Academy',
    'version': '1.0.0',
    'category': 'Academy',
    'author':'odox',
    'summary': 'Open Academy System',
    'description': """Open Academy System""",
    'sequence':-102,
    'depends': ['base','sale','board'],
    'data': [
        'security/ir.model.access.csv',
        'security/security.xml',
        'wizard/wizard_view.xml',
        'data/demo.xml',
        'views/course.xml',
        'views/session.xml',
        'views/student.xml',
        'views/partner.xml',
        'views/dashboard.xml',
        'views/sale_view.xml',
        'reports/report.xml',
        'reports/session_card.xml',
    ],
    'demo': [],
    'application':True,
    'auto_install': False,
    'assets': {},
}
