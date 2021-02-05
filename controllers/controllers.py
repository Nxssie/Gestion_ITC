# -*- coding: utf-8 -*-
from odoo import http

# class GestionItc(http.Controller):
#     @http.route('/gestion_itc/gestion_itc/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/gestion_itc/gestion_itc/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('gestion_itc.listing', {
#             'root': '/gestion_itc/gestion_itc',
#             'objects': http.request.env['gestion_itc.gestion_itc'].search([]),
#         })

#     @http.route('/gestion_itc/gestion_itc/objects/<model("gestion_itc.gestion_itc"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('gestion_itc.object', {
#             'object': obj
#         })