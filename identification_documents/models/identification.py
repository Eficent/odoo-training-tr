
from odoo import fields,models


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

    @api.constrains('number')
    def check_number(self):
        if self.number == ' ':
            raise ValidationError('Missing field')



