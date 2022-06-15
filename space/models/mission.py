from encodings import utf_8


# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Mission(models.Model):
    _name = 'mission'
    _descriptoin = 'Odoo space mission'

    name = fields.Char(string='Mission Name')

    spaceships = fields.Many2many(comodel_name='spaceship', string='Spaceships')

    crew_members = fields.Many2many(comodel_name='res.partner', string='Crew Members')

    launch_date = fields.Date(string='Launch Date')

    return_date = fields.Date(string='Return Date')
