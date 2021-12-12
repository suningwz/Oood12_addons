# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
#
# Copyright (c) 2017  - MLMConseil- www.mlmconseil.dz

{
    'name': 'bhlab disable overprocessed transfert',
    'version': '0.2',
    'category': 'stock',
    'description': """
disable overpocessed transfert
========================================================================

This module applies to companies based in Algeria.

**Email:** it.bhlab@bhinvest.net
""",
    'depends': ['stock'],
    'data': [
        'views/overprocessed_transfer.xml',

    ],

    'installable': True,
    'application': False,
    'auto_install': False,
}
