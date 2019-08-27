
from odoo import models,fields,api
from odoo.exceptions import ValidationError


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    certification_ids = fields.Many2many('certification.standard')
