# -*- coding: utf-8 -*-
{
    'name': "Vendor Selection For Dropshipping",

    'summary': """
        Customer will select vendor as per his choice.""",

    'description': """
       Customer will select vendor as per his choice in sale order when customer choose drop shipping scenario.
    """,

    'author': "Aktiv software ",
    'website': "http://www.aktivsoftware.com/",

    
    'category': 'Sales',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['sale_management', 'purchase'],

    # always loaded
    'data': [
        'views/sale_order.xml',
    ],
    

   'images':  ['static/description/banner.jpg'],
    'application': True,
}
