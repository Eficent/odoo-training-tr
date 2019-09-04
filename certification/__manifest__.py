# Copyright 2014-2015 Grupo ESOC <www.grupoesoc.es>
# Copyright 2017-Apertoso N.V. (<http://www.apertoso.be>)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
{
    "name": "Certification",
    "summary": "Track partner certifications",
    'version': '12.0.1.0.0',
    "category": "Customer Relationship Management",
    "website": "https://github.com/oca/partner-contact",
    "author": "Grupo ESOC, Tecnativa, Odoo Community Association (OCA)",
    "contributors": [
        'Jairo Llopis <j.llopis@grupoesoc.es>',
        'Richard deMeester <richard@willowit.com.au>',
    ],
    "license": "AGPL-3",
    'application': False,
    'installable': True,
    'auto_install': False,
    "depends": [
        "base",
    ],
    "data": [
        "views/certification.xml",
        "views/standart.xml",
        'security/ir.model.access.csv',
        'security/certification_security.xml',
        "views/res_partner.xml",
        "reports/certification_view.xml",
    ],
    'demo': ['demo/certification_data.xml'],

}
