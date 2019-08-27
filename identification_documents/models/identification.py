from odoo.exceptions import UserError
from odoo import fields,models,api


class IdentificationDocument (models.Model):
    _name = "identification"

    employee_id = fields.Many2one('res.partner')
    number = fields.Char()
    type = fields.Selection([
        ('passport', 'Passport'),
        ('card', 'ID Card'),
        ('driving', 'Driving License')
    ])
    date = fields.Date()

    ref_doc_id = fields.Reference(
        selection='_referencable_models',
        string='Reference Document')

    @api.constrains('number')
    def check_number(self):
        if self.number == ' ':
            msg = 'Empty field'
            raise UserError(msg)


