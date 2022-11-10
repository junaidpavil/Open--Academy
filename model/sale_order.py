from odoo import api, fields, models


class SaleOrder(models.Model):
    _inherit = "sale.order"

    check = fields.Selection(
        [('done', 'Done'), ('cancel', 'Cancel'), ('draft', 'Draft'), ('waiting', 'Waiting'), ('ready', 'Ready')],
          string='Status',compute='change_state')





    def change_state(self):
        list=[]
        for rec in self:
            if not rec.picking_ids:
                rec.check=None
            else:
                for line in rec.picking_ids:
                    list.append(line.state)

                if 'done' and 'cancel' and 'confirmed' in list:
                    rec.check='waiting'
                elif 'done' and 'cancel' in list:
                    rec.check='done'
                elif 'done' in list:
                    rec.check='done'
                else:
                    rec.check=None




    # def change_state(self):
    #     first_line = None
    #     for rec in self:
    #         if not rec.picking_ids:
    #             rec.check=None
    #         for line in rec.picking_ids:
    #
    #             if first_line == None:
    #                 first_line = line.state
    #             if (first_line=='done' and line.state=='confirmed') or (first_line=='confirmed' and line.state=='done'):
    #                 rec.check='waiting'
    #             elif (first_line=='done' and line.state=='cancel') or (first_line=='cancel' and line.state=='done'):
    #                 rec.check='done'
    #             elif first_line=='done' and line.state=='done':
    #                 rec.check='done'
    #
    #             else:
    #                 rec.check=None



    # def change_state(self):
    #     for rec in self:
    #       if  rec.picking_ids.state=='draft':
    #           rec.check='draft'
    #       elif rec.picking_ids.state=='done':
    #           rec.check='done'
    #       elif rec.picking_ids.state=='confirmed':
    #           rec.check='waiting'
    #       elif rec.picking_ids.state=='assigned':
    #           rec.check='ready'
    #       else:
    #           rec.check='cancel'
