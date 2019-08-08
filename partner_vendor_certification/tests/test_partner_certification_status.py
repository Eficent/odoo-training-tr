# Copyright 2015 ACSONE SA/NV (<http://acsone.eu>).
# Copyright 2016 Tecnativa - Vicent Cubells
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

import odoo.tests.common as common


class TestPartnerCertification(common.TransactionCase):

    def setUp(self):
        super(TestPartnerCertification, self).setUp()
        self.res_partner = self.env['res.partner']
        self.partner = self.res_partner.create({
            'name': "test1",
            'email': "test@test.com"})

    def test_certification_status (self):
        certification_status = self.env['partner.certification.status'].create({
            'name': 'AAA',
            'description': 'High quality product'})

        self.partner.certification_status_id=certification_status
        self.assertEqual(self.partner.certification_status_id,certification_status)
