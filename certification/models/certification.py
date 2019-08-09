# Copyright 2019 Eficent
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import models, fields


class Certification(models.Model):
    _name = 'certification'
    _description = 'Certification'

    name = fields.Char()
    date = fields.Date(string='Validation Date')
    description = fields.Text(string='Validation Details')
    type = fields.Selection([
        ('eucer', 'EU Certification'),
        ('noneucer', 'Non-Eu Certification')
    ])
    entity_id = fields.Many2one('res.partner')
