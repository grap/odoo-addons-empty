# coding: utf-8
# Copyright (C) 2015 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    'name': 'TO DELETE - product_standard_price_vat_incl',
    'summary': "Brings a standard Price with VAT Included on Products",
    'version': '8.0.1.0.0',
    'category': 'Product',
    'author': 'GRAP',
    'website': 'http://www.grap.coop',
    'license': 'AGPL-3',
    'depends': [
        'account',
    ],
    'data': [
        'data/product_price_type.xml',
        'views/view_product_template.xml',
    ],
    'demo': [
        'demo/res_groups.xml',
        'demo/product_pricelist.xml',
        'demo/account_tax.xml',
        'demo/product_template.xml',
    ],
    'images': [
        'static/description/pricelist_version_form.png',
        'static/description/product_form.png',
    ],
    'installable': True,
}
