# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Spaceship(models.Model):
    _name = 'spaceship'
    _description = 'Odoo space mission exercise'
    
    name = fields.Char(string='Name', required=True)
    ship_dimensions = fields.Char(string='Ship Dimensions')
    fuel_type = fields.Char(string='Fuel Type')
    ship_type = fields.Char(string='Ship Type')
    num_passengers = fields.Integer(string='Number of Passengers')
    active = fields.Boolean(string='Active', default=True)