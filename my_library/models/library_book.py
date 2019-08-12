# Copyright 2014-2015 Grupo ESOC <www.grupoesoc.es>
# Copyright 2017-Apertoso N.V. (<http://www.apertoso.be>)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import fields, models, api
from odoo.addons.decimal_precision import get_precision
from datetime import timedelta


class LibraryBook(models.Model):
    _name = 'library.book'
    _description = 'Library Book'
    # To sort records from newer to older and by title
    # _order = 'data_release, name'
    # To add in the form view
    _rec_name = 'short_name'

    name = fields.Char('Title', required=True)
    author_ids = fields.Many2many('res.partner', string='Authors')
    cost_price = fields.Float('Book Cost', get_precision('Book Price'))
    short_name = fields.Char('Short Title')
    notes = fields.Text('Internal Notes')
    state = fields.Selection([('draft', 'Not Available'),
                            ('available', 'Available'),
                            ('lost', 'Lost')],
                            'State')
    description = fields.Html('Description')
    cover = fields.Binary('Book Cover')
    out_of_print = fields.Boolean('Out of Print?')
    date_release = fields.Date('Release Date')
    date_updated = fields.Datetime('Last Updated')
    pages = fields.Integer('Number of Pages')
    reader_rating = fields.Float('Reader Average Rating', digits=(14, 4))
    currency_id = fields.Many2one('res.currency', string='Currency')
    retail_price = fields.Monetary('Retail Price')
    publisher_id = fields.Many2one('res.partner', string='Publisher')
    published_book_id = fields.One2many('library.book', 'publisher_id', string='Published Books')
    age_days = fields.Float(string='Days Since Release', compute='_compute_age', inverse='_inverse_age',
                            search='_search_age', store='False', compute_sudo='False')

    # @api.depends('date_release')
    # def _compute_age(self):
    #     today = fields.Date.today()
    #     for book in self.filtered('date_release'):
    #         delta = today - book.date_release
    #         book.age_days = delta.days
    #
    # def _inverse_age(self):
    #     today = fields.Date.today()
    #     for book in self.filtered('date_release'):
    #         d = today - timedelta(days=book.age_days)
    #         book.date_release = d
    #