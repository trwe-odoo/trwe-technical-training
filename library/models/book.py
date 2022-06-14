# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Book(models.Model):
    _name = 'book'
    _description = 'Book information'
    
    name = fields.Char(string='Title', required=True)
    authors = fields.Char(string='Authors')
    editors = fields.Char(string='Editors')
    isbn = fields.Integer(string='ISBN')
    genre = fields.Char(string='Genre')