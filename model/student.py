from odoo import models,fields

class Students(models.Model):
    _name = 'academy.student'
    _description = 'Academy Students'


    name=fields.Char(string='Name')
    age=fields.Integer(string='Age')