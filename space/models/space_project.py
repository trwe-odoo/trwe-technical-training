# -*- coding: utf-8 -*-

from odoo import models, fields, api

class SpaceProject(models.Model):
    _inherit = 'project.task'

    mission_id = fields.Many2one(comodel_name='mission',
                                 string='Related Mission',
                                 ondelete='set null')
