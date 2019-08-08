# Copyright 2019 Eficent
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import models, fields


class PartnerStatusCertification(models.Model):
    _name = 'partner.status.certification'
    _description = 'Partner Status Certification'

    name = fields.Char(string="Status", required=True)
    description = fields.Text(required=True)

    organisation_ids = fields.Many2many(comodel_name='res.partner',relation='certification_organisation_rel',
                                        column1= 'cert_id', column2='org_id')
