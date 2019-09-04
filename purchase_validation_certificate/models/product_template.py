# Copyright 2019 Eficent
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import models, fields, api
from odoo.exceptions import ValidationError
from datetime import timedelta


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    certification_ids = fields.Many2many('certification.standard')

