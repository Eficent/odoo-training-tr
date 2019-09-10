# Copyright 2019 Eficent
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

{
    'name': 'Certification Alert',
    'summary': "Warning when you purchase a product without a certificate.",
    'author': "Eficent, Odoo Community Association (OCA)",
    'website': "https://github.com/<my_github_user>",
    'category': 'Certification Management',
    'version': '12.0.1.0.0',
    'license': 'AGPL-3',
    'depends': ['base', 'purchase', 'certification_v2', 'product'],
    'data': ['security/ir.model.access.csv',
             'views/product_template_views.xml'
             ],
    'development_status': 'Beta',
    'maintainers': ['ceeficent'],
}