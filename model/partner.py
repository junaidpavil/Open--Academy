from odoo import models,api,fields

class ResPartner(models.Model):
    _inherit = "res.partner"

    instructor=fields.Boolean(string='Instructor')
    session_id=fields.Many2many('academy.session',string='Session')

