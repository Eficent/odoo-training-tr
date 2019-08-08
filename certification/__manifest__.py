# Copyright 2019 Eficent
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

{
    'name': 'Certification',
    'summary': "Defines certifaction for different purposes.",
    'author': "Eficent, Odoo Community Association (OCA)",
    'website': "https://github.com/<my_github_user>",
    'category': 'Certification Management',
    'version': '12.0.1.0.0',
    'license': 'AGPL-3',
    'depends': ['base'],
    'data': ['security/ir.model.access.csv',
             'views/certification_view.xml'
             ],
    'development_status': 'Beta',
    'maintainers': ['ceeficent'],
}