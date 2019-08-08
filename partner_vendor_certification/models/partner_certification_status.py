# Copyright 2019 Eficent <patrickraymondwilson@gmail.com>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import models,fields


class PartnerCertificationStatus(models.Model):
    _name = 'partner.certification.status'
    _description = 'Partner Certification Status'

    name = fields.Char(string="Status", required=True)
    description = fields.Text(required=True)


    organisation_ids = fields.Many2many(comodel_name='res.partner',relation='certification_organisation_rel',
                                        column1='cert_id',column2='org_id')