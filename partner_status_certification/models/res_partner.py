# Copyright 2019 Patrick Wilson <patrickraymondwilson@gmail.com>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import models, fields


class ResPartner(models.Model):
    _inherit = 'res.partner'

    status = fields.Selection([('approved', 'Approved'),
         ('progress', 'In progress'),
        ('nonapproved', 'Non-approved')])

