# Copyright 2019 Eficent
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

{
    'name': 'Partner Status Certification',
    'summary': "Adds status certification to partners in order to evaluate .",
    'author': "Eficent, Odoo Community Association (OCA)",
    'website': "https://github.com/OCA/partner-contact",
    'category': 'Customer Relationship Management',
    'version': '12.0.1.0.0',
    'license': 'AGPL-3',
    'depends': ['contacts'],
    'data': ["security/ir.model.access.csv",
             "views/partner_status_certification.xml",
             "views/res_partner.xml"
             ],
    'development_status': 'Beta',
    'maintainers': ['ceeficent'],
}
