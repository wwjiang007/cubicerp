# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE_LGPL file for full copyright and licensing details.

from odoo import models, fields
from odoo.tools.translate import _


class BarcodeRule(models.Model):
    _inherit = 'barcode.rule'

    type = fields.Selection(selection_add=[
            ('weight', _('Weighted Product')),
            ('price', _('Priced Product')),
            ('discount', _('Discounted Product')),
            ('client', _('Client')),
            ('cashier', _('Cashier'))
        ])
