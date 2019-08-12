
from odoo import models, fields


class ResPartner(models.Model):
    _inherit = 'res.partner'

    legal_documents_id = fields.One2many(comodel_name='partner.legal.documents', inverse_name='name')

