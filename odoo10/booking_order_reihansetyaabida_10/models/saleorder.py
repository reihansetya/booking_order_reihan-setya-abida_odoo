from email.policy import default
from odoo import api, fields, models


class Saleorder(models.Model):
    _inherit = 'sale.order'

    is_booking_order = fields.Boolean(
        string='is booking order',
        default=True)
    team_id = fields.Many2one(
        comodel_name='booking.service_team',
        string='Team')
    team_leader = fields.Many2one(
        comodel_name='res.users',
        string='Team Leader')
    team_member = fields.Many2many(
        comodel_name='res.users',
        string='Team Member')
    booking_start = fields.Datetime(string='Booking Start')
    booking_end = fields.Datetime(string='Booking End')
