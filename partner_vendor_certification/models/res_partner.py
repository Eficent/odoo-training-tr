from odoo import models, fields


class ResPartner(models.Model):
    _inherit = 'res.partner'

    status_certification_id = fields.Many2one('partner.certification.status')
    certification_ids = fields.One2many(comodel_name='certification', inverse_name='entity_id')
