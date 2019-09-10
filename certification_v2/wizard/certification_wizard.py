# Copyright 2019 Eficent
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from datetime import timedelta

from odoo import models, fields, api
from odoo.exceptions import ValidationError


class CertificationWizard(models.TransientModel):
    _name = "certification.wizard"
    _description = 'Certification Search'

    date = fields.Date(string='Expiration Date')
    entity_id = fields.Many2one('res.partner', string="Certification Entity")
    is_certification_body = fields.Boolean(string="Is Valid Entity", readonly=True)
    certification_count=fields.Integer(string="# Certifications", readonly=True)

    @api.onchange('entity_id')
    def onchange_entity_id(self):
       self.is_certification_body = self.entity_id.is_certification_body

    @api.multi
    def certification_entity_date_valid(self):
        self.ensure_one()  # Recordset must contain only 1 record
        action = self.env.ref('certification_v2.certification')  # act windows defined in views
        result = action.read()[0]  # After reference an action we always do
        if not result.get('domain', False):  # if domain key doesn’t exist
           result['domain'] = []  # We create them
        if self.entity_id:  # If we have marked a Certification entity
           result['domain'] = [('entity_id', '=', self.entity_id.id)]  # Filter by that entity
        if self.date:  # If we have select a date
           result['domain'] += [('date', '>=', self.date)]  # Date bigger than selected
        return result

    @api.onchange('entity_id', 'date')
    def onchange_entity_date(self):
        if self.entity_id:
            domain = [('entity_id', '=', self.entity_id.id)]
            if self.date:
               domain += [('date', '>=', self.date)]
            certification_ids = self.env['certification'].search(domain)
            self.certification_count = len(certification_ids)
        else:
            self.certification_count = 0





