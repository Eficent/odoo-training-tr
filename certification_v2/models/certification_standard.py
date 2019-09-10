from odoo import models,fields


class CertificationStandard(models.Model):
    _name = 'certification.standard'
    _description = 'Certification Standard'

    name = fields.Char()
