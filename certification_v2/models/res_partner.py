
from odoo import models,fields


class ResPartner(models.Model):
    _inherit = 'res.partner'

    is_certification_body = fields.Boolean(string="Certification Entity", default=False)
    certification_ids = fields.One2many(comodel_name='certification', inverse_name='owner_id')


