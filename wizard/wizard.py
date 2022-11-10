from odoo import api, fields, models,tools


class AcademyWizards(models.TransientModel):
    _name = 'academy.transient'
    _description = 'Academy Transient'

    # def default_get(self, fields):
    #     result = super(AcademyWizards, self).default_get('relation_sid')
    #     result['relation_sid'] = self._context.get('name')
    #     return result

    # @tools.ormcache()
    # def _get_default_relation_sid(self):
    #     # Deletion forbidden (at least through unlink)
    #     return self.env.ref('open_academy.relation_sid')

    # @api.model
    # def _default_name(self):
    #     return self.env['academy.session'].search([])

    # @api.model
    # def _default_name(self):
    #     return self.env['academy.transient'].browse(self._context.get('relation_sid.name'))



    relation_sid = fields.Many2one('academy.session', string='Relatio_session')

    relation_cid = fields.Many2many('res.partner', string='relation_Partner',
                                    default=lambda self: self.env['res.partner'].search([],limit=1))


    def action_save(self):
        self.relation_sid.attendees_id = self.relation_sid.attendees_id+self.relation_cid



