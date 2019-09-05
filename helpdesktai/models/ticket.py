# Copyright 2014-2015 Grupo ESOC <www.grupoesoc.es>
# Copyright 2017-Apertoso N.V. (<http://www.apertoso.be>)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
from datetime import timedelta,date, datetime
from odoo import fields, models, api
from odoo.exceptions import ValidationError



class Ticket(models.Model):
    _name = 'ticket'
    _description = 'Ticket'
    _rec_name = 'id'

    status = fields.Selection([('open', 'Open'),
                               ('in_progress', 'In Progress'),
                               ('cancel', 'Cancel'),
                               ('done', 'Done')],
                              string="Status", default='open', required=True)
    subject = fields.Text(string='Ticket Subject')
    incident_id = fields.Many2one('incident', string='Incident Area', required=True)
    priority = fields.Selection([('high_priority', 'High Priority'),
                                 ('low_priority', 'Low Priority'),
                                 ('medium_priority', 'Medium Priority')],
                                string="Priority", default='low_priority',
                                help=" Ticket Priority Type ", required=True)
    responsible_department = fields.Many2one(related='incident_id.responsible_department')

    sla_status = fields.Selection([('suitable', 'Suitable'),
                                   ('alert', 'Alert')],
                                  string="SLA Status", required=True, compute='_compute_sla_status')

    deadline_day = fields.Char('Deadline',compute='_compute_sla_status')

    @api.multi
    def open_ticket(self):
        self.status = "open"

    @api.multi
    def in_progress_ticket(self):
        self.status = "in_progress"

    @api.multi
    def done_ticket(self):
        self.status = "done"

    @api.multi
    def cancel_ticket(self):
        self.status = "cancel"


    @api.multi
    def _compute_sla_status(self):

        for record in self:
            date_diff = (record.create_date.date() - datetime.now().date()).days
            if record.incident_id.sla_day > date_diff:
                record.sla_status = "suitable"
                record.deadline_day = record.incident_id.sla_day - date_diff
            else:
                record.sla_status = "alert"





