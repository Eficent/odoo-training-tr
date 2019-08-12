# Copyright 2019 Eficent
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import models, fields


class PartnerLegalDocuments(models.Model):
    _name = 'partner.legal.documents'
    _description = 'Partner Legal Documents'

    name = fields.Many2one('res.partner')
    type = fields.Selection([
        ('pass', 'Passport'),
        ('ID', 'ID'),
        ('driving', 'Driving License')
    ])
    date = fields.Date(string=' Date')
    number = fields.Char()
    letter = fields.Char()

