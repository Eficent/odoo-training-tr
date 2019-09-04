# Copyright 2019 Eficent
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

{
    'name': 'Purchase Validation Certificate',
    'summary': "Indicates if the supplier owns the corresponding certificates attached "
               "to the products needed to be purchased",
    'author': "Eficent, Odoo Community Association (OCA)",
    'website': "https://github.com/<my_github_user>",
    'category': 'Purchase',
    'version': '12.0.1.0.0',
    'license': 'AGPL-3',
    'depends': ['product', 'certification', 'base', 'purchase'],
    'data': ['security/ir.model.access.csv',
             'views/product_template_view.xml'],
    'development_status': 'Beta',
    'maintainers': ['ceeficent']
}