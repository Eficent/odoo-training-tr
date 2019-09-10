
from odoo import models,fields,api


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    certification_ids = fields.Many2many('certification.standard')
