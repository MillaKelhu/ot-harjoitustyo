import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(10)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_kortin_saldo_oikein(self):
        self.assertEqual(str(self.maksukortti), "saldo: 0.1")

    def test_kortille_voi_ladata_rahaa(self):
        self.maksukortti.lataa_rahaa(10)
        self.assertEqual(str(self.maksukortti), "saldo: 0.2")

    def test_kortilta_voi_ottaa_rahaa(self):
        self.maksukortti.ota_rahaa(5)
        self.assertEqual(str(self.maksukortti), "saldo: 0.05")

    def test_kortilta_ei_voi_ottaa_liikaa_rahaa(self):
        self.maksukortti.ota_rahaa(20)
        self.assertEqual(str(self.maksukortti), "saldo: 0.1")

    def test_onnistunut_metodi_palauttaa_True(self):
        onnistuiko = self.maksukortti.ota_rahaa(5)
        self.assertEqual(onnistuiko, True)

    def test_epaonistunut_metodi_palauttaa_False(self):
        onnistuiko = self.maksukortti.ota_rahaa(20)
        self.assertEqual(onnistuiko, False)