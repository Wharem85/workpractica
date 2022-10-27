# -*- coding: utf-8 -*-
{
    'name': "vehiculos",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'sequence': '-100',
    'aplication': 'true',
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'account', 'product'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/account_reports.xml',
        'views/account_invoices_views.xml',
        'views/vehiculo_view.xml',
        'views/marca_view.xml',
        'wizard/catalogo_excel_wizard_view.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'test/static/src/css/account.css'
        ]
    },
    'aplication': 'True',
    'license': 'LGPL-3',
}
