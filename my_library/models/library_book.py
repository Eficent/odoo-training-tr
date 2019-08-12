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
    _order = 'date_release, name'
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
                            'State', default='draft')

    # Define a method to change the state of a selection of books

    #  Check whether a state transition is allowed - creation of is_allowed_transition
    @api.model
    def is_allowed_transition(self, old_state, new_state):
        allowed = [('draft', 'available'),
                   ('available', 'borrowed'),
                   ('borrowed', 'available'),
                   ('available', 'lost'),
                   ('borrowed', 'lost'),
                   ('lost', 'available')]
        return (old_state, new_state) in allowed

    #  Method to change the state of some books to a new state passed as an argument
    @api.multi
    def change_state(self, new_state):
        for book in self:
            if book.is_allowed_transition(book.state, new_state):
                book.state = new_state
            else:
                continue
    # Method to change the book state by calling the change_State
    @api.model
    def make_available(self):
        self.change_state('available')

    @api.model
    def make_borrowed(self):
        self.change_state('borrowed')

    @api.model
    def make_lost(self):
        self.change_state('lost')

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
    publisher_city = fields.Char('Publisher City', related='publisher_id.city', readonly=True)

    # @api.depends('date_release')
    # Add the method withe the value computation logic
    # def _compute_age(self):
    #     today = fields.Date.today()
    #     for book in self.filtered('date_release'):
    #         delta = today - book.date_release
    #         book.age_days = delta.days
    #
    #  Add the method and implement the logic to write on the computed field
    # def _inverse_age(self):
    #     today = fields.Date.today()
    #     for book in self.filtered('date_release'):
    #         d = today - timedelta(days=book.age_days)
    #         book.date_release = d
    # Implement the logic to search in the computed field
    # def _search_age(self, operator, value):
    #   today = fields.Date.today()
    #   value_days = timedelta(days=value)
    #   value_date = today - value_days
    #   # convert the operator:
    #   # book with age > value have a date < value_date
    #   operator_map = {
    #       '>': '<', '>=': '<=',
    #       '<': '>', '<=': '>=',
    #   }
    # new_op = operator_map.get(operator, operator)
    # return [('date_release', new_op, value_date)]

    class ResPartner(models.Model):
        _inherit = 'res.partner'
        _order = 'name'
        authored_book_ids = fields.Many2many('library.book', string='Authored Books')
        count_books = fields.Integer('Number of Authored Books', compute='_compute_count_books')

        @api.depends('authored_book_ids')
        def _compute_count_books(self):
            for r in self:
                r.count_books = len(r.authored_book_ids)

    class LibraryMember(models.Model):
        _name = 'library.member'
        _inherits = {'res.partner': 'partner_id'}

        partner_id = fields.Many2one('res.partner', ondelete='cascade')
        date_start = fields.Date('Member Since')
        date_end = fields.Date('Termination Date')
        member_number = fields.Char()
        date_of_birth = fields.Date('Date of birth')
