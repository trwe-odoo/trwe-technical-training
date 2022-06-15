# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError

class Spaceship(models.Model):
    _name = 'spaceship'
    _description = 'Odoo space mission exercise'
    
    name = fields.Char(string='Name', required=True)
    ship_width = fields.Integer(string='Ship Width')
    ship_length = fields.Integer(string='Ship Length')
    fuel_type = fields.Char(string='Fuel Type')
    ship_type = fields.Char(string='Ship Type')
    num_passengers = fields.Integer(string='Number of Passengers')
    active = fields.Boolean(string='Active', default=True)

    @api.constrains('ship_width', 'ship_length')
    def _check_dimensions(self):
        for record in self:
            if record.ship_width > record.ship_length:
                raise UserError('Ship width can not be greater than ship length')
