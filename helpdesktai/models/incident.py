# Copyright 2014-2015 Grupo ESOC <www.grupoesoc.es>
# Copyright 2017-Apertoso N.V. (<http://www.apertoso.be>)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
from datetime import timedelta
from odoo import fields, models, api
from odoo.exceptions import ValidationError


class Incident(models.Model):
    _name = 'incident'
    _description = 'Incident'


    name = fields.Char(string='Incident Name', required=True)
    sla_day = fields.Integer(string='SLA Day', required=True)
    responsible_department = fields.Many2one('hr.department', string='Responsible Department', required=True)
