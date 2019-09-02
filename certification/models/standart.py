# Copyright 2014-2015 Grupo ESOC <www.grupoesoc.es>
# Copyright 2017-Apertoso N.V. (<http://www.apertoso.be>)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import models, fields, api


class CertificationStandard(models.Model):
    _name = 'certification.standard'
    _description = 'Certification Types'

    name = fields.Char()
    description = fields.Text()
