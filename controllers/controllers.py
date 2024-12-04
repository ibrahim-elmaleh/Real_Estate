# -*- coding: utf-8 -*-
# from odoo import http


# class MyAddons(http.Controller):
#     @http.route('/my_addons/my_addons', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/my_addons/my_addons/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('my_addons.listing', {
#             'root': '/my_addons/my_addons',
#             'objects': http.request.env['my_addons.my_addons'].search([]),
#         })

#     @http.route('/my_addons/my_addons/objects/<model("my_addons.my_addons"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('my_addons.object', {
#             'object': obj
#         })

