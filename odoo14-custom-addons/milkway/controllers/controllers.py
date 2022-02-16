# -*- coding: utf-8 -*-
# from odoo import http


# class Milkway(http.Controller):
#     @http.route('/milkway/milkway/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/milkway/milkway/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('milkway.listing', {
#             'root': '/milkway/milkway',
#             'objects': http.request.env['milkway.milkway'].search([]),
#         })

#     @http.route('/milkway/milkway/objects/<model("milkway.milkway"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('milkway.object', {
#             'object': obj
#         })
