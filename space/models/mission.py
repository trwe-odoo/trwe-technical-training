from encodings import utf_8


# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Mission(models.Model):
    _name = 'mission'
    _description = 'Odoo space mission'

    name = fields.Char(string='Mission Name')

    spaceships = fields.Many2many(comodel_name='spaceship', string='Spaceships')

    crew_members = fields.Many2many(comodel_name='res.partner', string='Crew Members')

    launch_date = fields.Date(string='Launch Date')

    return_date = fields.Date(string='Return Date')

    fuel_amount = fields.Integer(string='Amount of Fuel Needed')

    num_engines = fields.Integer(string='Number of Engines Required')

    risk_level = fields.Selection(string='Risk Level', selection=[('low', 'Low'), ('medium', 'Medium'), ('high', 'High')])
