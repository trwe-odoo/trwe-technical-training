# -*- coding: utf-8 -*-
from odoo import models, fields, api


class ProjectWizard(models.TransientModel):
    _name = 'space.project.wizard'
    _description = 'Wizard: Create Project for a Mission'

    def _default_mission(self):
        return self.env['mission'].browse(self._context.get('active_id'))

    mission_id = fields.Many2one(comodel_name='mission',
                                 string='Mission',
                                 required=True,
                                 default=_default_mission)

    def create_space_project(self):
        if self.mission_id:
            project_id = self.env['project.task'].create({
                'mission_id': self.mission_id,
            })