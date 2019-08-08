# Copyright 2019 Eficent
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

import odoo.tests.common as common

class TestPartnerStatusCertification(common.TransactionCase):

    def setUp(self):
        super(TestPartnerStatusCertification, self).setUp()

        self.res_partner = self.env['res.partner']
        self.partner = self.res_partner.create({
            'name': "test1",
            'email': "test@test.com"})

    def test_status(self):
        partner_status_certification = self.env['partner.status.certification']
        status_certification = partner_status_certification.create({
            'name': 'Super high',
            'description': 'This is super high status certification'})

        self.partner.status_certification_id = status_certification
        self.assertEqual(self.partner.status_certification_id, status_certification)
