# Copyright 2014-2015 Grupo ESOC <www.grupoesoc.es>
# Copyright 2017-Apertoso N.V. (<http://www.apertoso.be>)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
from datetime import timedelta
from odoo import fields, models, api
from odoo.exceptions import ValidationError


class Ticket(models.Model):
    _name = 'ticket'
    _description = 'Ticket'
    _rec_name = 'ticket_no'

    ticket_no = fields.Char(string='Ticket Number',required=True)
    subject = fields.Text(string='Ticket Subject')
    incident_id = fields.Many2one('incident', string='Incident Area', required=True)
    priority = fields.Selection([('high_priority', 'High Priority'),
                              ('low_priority', 'Low Priority'),
                              ('medium_priority', 'Medium Priority')],
                             string="Priority", default='low_priority',
                             help=" Ticket Priority Type ", required=True)
