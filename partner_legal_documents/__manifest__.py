# Copyright 2019 Eficent
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

{
    'name': 'Legal documents',
    'summary': "Compiles legal documents of people involved in the corportation.",
    'author': "Eficent, Odoo Community Association (OCA)",
    'website': "https://github.com/<my_github_user>",
    'category': 'Human Resources Management',
    'version': '12.0.1.0.0',
    'license': 'AGPL-3',
    'depends': ['contacts'],
    'data': ["security/ir.model.access.csv",
             "views/partner_legal_documents_view.xml",
             "views/res_partner.xml"
             ],
    'development_status': 'Beta',
    'maintainers': ['ceeficent']}
