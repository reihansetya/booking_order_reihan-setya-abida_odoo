# -*- coding: utf-8 -*-
from odoo import http

# class BookingOrderReihansetyaabida10(http.Controller):
#     @http.route('/booking_order_reihansetyaabida_10/booking_order_reihansetyaabida_10/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/booking_order_reihansetyaabida_10/booking_order_reihansetyaabida_10/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('booking_order_reihansetyaabida_10.listing', {
#             'root': '/booking_order_reihansetyaabida_10/booking_order_reihansetyaabida_10',
#             'objects': http.request.env['booking_order_reihansetyaabida_10.booking_order_reihansetyaabida_10'].search([]),
#         })

#     @http.route('/booking_order_reihansetyaabida_10/booking_order_reihansetyaabida_10/objects/<model("booking_order_reihansetyaabida_10.booking_order_reihansetyaabida_10"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('booking_order_reihansetyaabida_10.object', {
#             'object': obj
#         })