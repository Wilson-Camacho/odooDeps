# -*- coding: utf-8 -*-
# from odoo import http


# class Ejemplo02-scaffold(http.Controller):
#     @http.route('/ejemplo02-scaffold/ejemplo02-scaffold/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/ejemplo02-scaffold/ejemplo02-scaffold/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('ejemplo02-scaffold.listing', {
#             'root': '/ejemplo02-scaffold/ejemplo02-scaffold',
#             'objects': http.request.env['ejemplo02-scaffold.ejemplo02-scaffold'].search([]),
#         })

#     @http.route('/ejemplo02-scaffold/ejemplo02-scaffold/objects/<model("ejemplo02-scaffold.ejemplo02-scaffold"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('ejemplo02-scaffold.object', {
#             'object': obj
#         })
