# Copyright 2014-2015 Grupo ESOC <www.grupoesoc.es>
# Copyright 2017-Apertoso N.V. (<http://www.apertoso.be>)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import fields, models, api
from odoo.exceptions import ValidationError


class BookCategory(models.Model):
    _name = 'library.book.category'
    name = fields.Char('Category')
    parent_id = fields.Many2one('library.book.category',
                                string='Parent Category',
                                ondelete='restrict',
                                index=True)
    child_ids = fields.One2many('library.book.category', 'parent_id', string='Child Categories')

    # @api.constrains('date_release')
    #     def _check_release_date(self):
    #     for record in self:
    #         if record.date_release and record.date_release > fields.Date.today():
    #             raise models.ValidationError('Release date must be in the past')
    #
    # _sql_constraints = [('name_uniq','UNIQUE (name)','Book title must be unique.')]
