# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Book(models.Model):
    _name = 'Book'
    _description = 'Book information'
    
    name = fields.Char('Title', required=True)
    authors = fields.Char('Authors')
    editors = fields.Char('Editors')
    isbn = fields.Integer('ISBN')
    genre = fields.Char('Genre')