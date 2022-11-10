from odoo import fields,models


class Course(models.Model):
    _name = 'academy.course'
    _rec_name = 'title'
    _description = 'Academy Courses'

    title=fields.Char(string='Title')
    description=fields.Text(string='Description')


    user_id=fields.Many2one('res.users',string='User')
    relation_ids=fields.One2many('academy.session','course_id',string='Relation_id')

    _sql_constraints = [
        ('unique_name', 'unique(title)','Same Course not allowed'),
        ('unique_description','CHECK(title!=description)','description should be different')

    ]
