# Copyright 2014-2015 Grupo ESOC <www.grupoesoc.es>
# Copyright 2017-Apertoso N.V. (<http://www.apertoso.be>)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
{
    "name": "Help Desk Tai",
    "summary": "Enterprise Help Desk Application",
    'version': '12.0.1.0.0',
    "category": "Customer Relationship Management",
    "website": "https://github.com/oca/partner-contact",
    "author": "Grupo ESOC, Tecnativa, Odoo Community Association (OCA)",
    "contributors": [
        'Bilal ASLAN <bilal.aslan@tai.com.tr>',
        'Nurbanu Işık Delibalta <nurbanu.isik@tai.com.tr>',
        'Rüveyda YASAK <ruveyda.yasak@tai.com.tr>',
        'Muhammed GENÇ <muhammed.genc@tai.com.tr>',

    ],
    "license": "AGPL-3",
    'application': True,
    'installable': True,
    'auto_install': False,
    "depends": [
        "base",
    ],
    "data": [
        "security/helpdesk_security.xml",
        "security/ir.model.access.csv",
        "views/incident.xml",
        "views/ticket.xml",

    ],

}
