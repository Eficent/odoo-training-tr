from psycopg2.extensions import AsIs

from odoo import tools
from odoo import api, fields, models


class CertificationReport(models.Model):
    _name = "certification.report"
    _description = "Certification Report"
    _auto = False

    entity_id = fields.Many2one('res.partner', readonly=True)
    certification_count = fields.Integer(readonly=True)
    standard_id = fields.Many2one('standard')
    expiry_status = fields.Selection([
        ('expired', "Expired"),
        ('available', "Available")
    ], readonly=True)

    def _select(self):
        select_str = """
           SELECT
                   rp.id as id,
                   rp.id as entity_id,
                   rp.id as standard_id,
                   c.expiry_status as expiry_status,
                   count(c.id) as certification_count
       """
        return select_str
    def _from(self):
        from_str = """
        res_partner rp
           left join certification c on c.entity_id = rp.id
           """
        return from_str

    def _where(self):
       where_str = """rp.entity is True"""
       return where_str

    def _group_by(self):
        group_by_str = """
           GROUP BY
           rp.id,
           rp.id,
           c.expiry_status
       """
        return group_by_str

    @api.model_cr
    def init(self):
        tools.drop_view_if_exists(self.env.cr, self._table)
        self.env.cr.execute(
            """
            CREATE or REPLACE VIEW %s as (%s
            FROM ( %s ) WHERE ( %s )
            %s)""",
            (AsIs(self._table), AsIs(self._select()),
             AsIs(self._from()), AsIs(self._where()),
             AsIs(self._group_by())),
        )
