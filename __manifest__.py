# -*- coding: utf-8 -*-
{
    'name': "gestionITC",

    'summary': """
        Módulo de gestión para el ITC""",

    'description': """
        Gestión aplicada a proyectos, aplicaciones y todo lo que rodea la logística del ITC.
    """,

    'author': "Joel & Carlos S.",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'views/views.xml',
        'views/templates.xml',
        'security/security.xml',
        'security/ir.model.access.csv',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application': 'True',
}