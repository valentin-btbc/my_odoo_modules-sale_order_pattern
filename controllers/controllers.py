# -*- coding: utf-8 -*-
from odoo import http

# class SaleOrderPattern(http.Controller):
#     @http.route('/sale_order_pattern/sale_order_pattern/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sale_order_pattern/sale_order_pattern/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('sale_order_pattern.listing', {
#             'root': '/sale_order_pattern/sale_order_pattern',
#             'objects': http.request.env['sale_order_pattern.sale_order_pattern'].search([]),
#         })

#     @http.route('/sale_order_pattern/sale_order_pattern/objects/<model("sale_order_pattern.sale_order_pattern"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sale_order_pattern.object', {
#             'object': obj
#         })