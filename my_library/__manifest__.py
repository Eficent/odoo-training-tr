# Copyright 2014-2015 Grupo ESOC <www.grupoesoc.es>
# Copyright 2017-Apertoso N.V. (<http://www.apertoso.be>)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
{
    "name": "Library Book",
    "summary": "My library book",
    'version': '12.0.1.0.0',
    "category": "Customer Relationship Management",
    "website": "https://github.com/ceeficent",
    "author": "Grupo ESOC, Tecnativa, Odoo Community Association (OCA)",
    "contributors": ['Clara Escriva <clara.escriva@eficent.com'],
    "license": "AGPL-3",
    'application': False,
    'installable': True,
    'auto_install': False,
    "depends": ["base", 'decimal_precision'],
    "data": [
        "security/groups.xml",
        "security/ir.model.access.csv",
        "views/library_book.xml",
    ],
}
