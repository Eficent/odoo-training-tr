# Copyright 2014-2015 Grupo ESOC <www.grupoesoc.es>
# Copyright 2017-Apertoso N.V. (<http://www.apertoso.be>)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import fields, models, api
from odoo.exceptions import ValidationError


class Identity(models.Model):
    _name = 'identity'
    _description = 'Identity'
    _rec_name = 'employee_name'

    employee_name = fields.Many2one("hr.employee", required=True)
    type = fields.Selection([('passport', 'Passport'),
                              ('id_card', 'ID Card'),
                              ('driving_license', 'Driving License')],
                             string="Type", default='to_translate',
                             help=" Employee Identity Detail ", required=True)

    id_number = fields.Char('ID Number', required=True)

