# -*- coding: utf-8 -*-
{
    'name': 'Vendor Selection',
    'summary': 'Customer will select vendor as per his choice.',
    'website': 'http://www.aktivsoftware.com',
    'description': 'Customer will select vendor as per his choice in sale order \
        when customer choose drop shipping scenario.',
    'license': 'AGPL-3',
    'author': 'Aktiv Software',
    'category': 'Sales',
    'version': '12.0.1.0.0',
    'depends': ['sale_management', 'purchase', 'stock'],
    'data': [
        'views/sale_order.xml',
    ],
    'images': ['static/description/banner.jpg'],
    'auto_install': False,
    'installable': True,
    'application': False
}
