# -*- coding: utf-8 -*-

{
    'name': 'Payment Acquirer',
    'category': 'Accounting',
    'summary': 'Payment Acquirer Base Module',
    'version': '1.0',
    'description': """Payment Acquirer Base Module""",
    'depends': ['account', 'resource'],
    'data': [
        'data/account_data.xml',
        'data/payment_icon_data.xml',
        'data/payment_acquirer_data.xml',
        'data/payment_sequence.xml',
        'views/payment_views.xml',
        'views/account_payment_views.xml',
        'views/payment_templates.xml',
        'views/payment_portal_templates.xml',
        'views/assets.xml',
        'views/res_partner_views.xml',
        'security/ir.model.access.csv',
        'security/payment_security.xml',
    ],
    'installable': True,
    'auto_install': True,
}
