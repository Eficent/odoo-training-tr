# Copyright 2019 Patrick Wilson <patrickraymondwilson@gmail.com>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import models, fields


class ResPartner(models.Model):
    _inherit = 'res.partner'

    certification_status_id = fields.Many2one('partner.certification.status')
    certification_ids = fields.One2many(comodel_name='certification', inverse_name='entity_id')




