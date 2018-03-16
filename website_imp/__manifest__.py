# -*- coding: utf-8 -*-
{
    'name': 'Web Improvment for css',
    'category': 'Hidden',
    'version': '1.0',
    'description':
        """
Odoo Web css improvments module.
================================

This module provides some css change in the core of the Odoo Web Client.
        """,
    'depends': ['website','project','crm'],
    'auto_install': True,
    'data': [
        'views/webclient_templates.xml',
    ],
    'qweb': [ ],
    'bootstrap': True,  # load translations for login screen
}
