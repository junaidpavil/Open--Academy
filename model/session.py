from odoo import fields,models,api
from odoo.exceptions import ValidationError
import datetime

class Sessions(models.Model):
    _name = 'academy.session'
    _description = 'Academy Session'


    name=fields.Char(string='Name')
    date=fields.Date(string='Start Date', default=fields.Date.context_today)
    end_date=fields.Date(string='End Date')
    seat=fields.Integer(string='Seats')
    duration=fields.Char(string='Duration')
    instructor_id=fields.Many2one('res.partner',string='Instructors')
    course_id=fields.Many2one('academy.course','Course')
    attendees_id=fields.Many2many('res.partner',string='Attendees')
    percentage=fields.Float(string='Percentage of taken seats',compute='_compute_perc')
    student_id=fields.Many2many('academy.student',string='Students')
    active=fields.Boolean(string='Boolean')
    count_attendees=fields.Integer(string='Count',compute='_count_attendees',store=True)

    def _count_attendees(self):
        for rec in self:
            if rec.seat:
                count=len(rec.attendees_id)
                rec.count_attendees=count
            else:
                rec.count_attendees=0

    def _compute_perc(self):
        for rec in self:
            if rec.seat:
                length = len(rec.attendees_id)
                perc = (length / rec.seat) * 100
                rec.percentage = perc
            else:
                rec.seat=0


    @api.onchange('attendees_id')
    def onchange_attendes(self):
        if len( self.attendees_id ) > self.seat:
            return {
                'warning':{
                    'title':'something bad happened',
                    'message':'No more seats available !!!!'
                }
            }

    @api.constrains('attendees_id')
    def _check_same(self):
        if self.instructor_id == self.attendees_id:
            raise ValidationError('the instructor should  not be include the attendees ')


    def wizard(self):
        wiz= self.env.ref('open_academy.action_wizard_transient').read()[0]
        wiz['context']={'default_relation_sid':self.id}

        return wiz
