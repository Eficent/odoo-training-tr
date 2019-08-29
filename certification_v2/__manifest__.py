# Copyright 2019 Eficent
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

{
    'name': 'Certification V2',
    'summary': "Defines certifaction for different purposes.",
    'author': "Eficent, Odoo Community Association (OCA)",
    'website': "https://github.com/<my_github_user>",
    'category': 'Certification Management',
    'version': '12.0.1.0.0',
    'license': 'AGPL-3',
    'depends': ['base', 'contacts'],
    'data': ['security/ir.model.access.csv',
             'views/certification_view.xml',
             'views/res_partner_view.xml',
             'views/standard_view.xml',
             'wizard/certification_wizard.xml',
             'security/certification_security.xml',
             'reports/certification_report.xml',
             'reports/certification_template.xml'
             ],
    'demo':
        ['demo/certification_data.xml',
         ],
    'development_status': 'Beta',
    'maintainers': ['ceeficent'],
}