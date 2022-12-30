# -*- coding: utf-8 -*-
# from odoo import http


# class KhkNetToGross(http.Controller):
#     @http.route('/khk_net_to_gross/khk_net_to_gross/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/khk_net_to_gross/khk_net_to_gross/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('khk_net_to_gross.listing', {
#             'root': '/khk_net_to_gross/khk_net_to_gross',
#             'objects': http.request.env['khk_net_to_gross.khk_net_to_gross'].search([]),
#         })

#     @http.route('/khk_net_to_gross/khk_net_to_gross/objects/<model("khk_net_to_gross.khk_net_to_gross"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('khk_net_to_gross.object', {
#             'object': obj
#         })
