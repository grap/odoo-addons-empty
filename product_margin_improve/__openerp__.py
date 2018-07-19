# -*- encoding: utf-8 -*-
##############################################################################
#
#    Product - Margin Improve Module for Odoo
#    Copyright (C) 2013-Today GRAP (http://www.grap.coop)
#    @author Julien WESTE
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    'name': 'TO DELETE - product_margin_improve',
    'version': '0.2',
    'category': 'Product',
    'description': """
This module brings modifications to the product_margin module
=============================================================
    * include pos_orders in the margin calculation
    * include inventory losses in the margin calculation
    * take the UoM into account
    * ...

Copyright, Author and Licence :
-------------------------------
    * Copyright : 2014, Groupement Régional Alimentaire de Proximité;
    * Author :
        * Julien WESTE;
    * Licence : AGPL-3 (http://www.gnu.org/licenses/)
    """,
    'author': 'GRAP',
    'website': 'http://www.grap.coop',
    'license': 'AGPL-3',
    'depends': [
        'product_margin',
        'point_of_sale',
    ],
    'data': [
        'wizard/product_margin_view.xml',
        'view/product_margin_view.xml',
        'view/action.xml',
        'view/menu.xml',
    ],
}
