import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()

    def test_luotu_kassapaate_on_olemassa(self):
        self.assertNotEqual(self.kassapaate, None)

    def test_kassapaatteen_rahamaara_on_oikein(self):
        rahaa = self.kassapaate.kassassa_rahaa
        self.assertEqual(rahaa, 100000)

    def test_myytyjen_edullisten_maara_on_oikein(self):
        edullisia = self.kassapaate.edulliset
        self.assertEqual(edullisia, 0)

    def test_myytyjen_maukkaiden_maara_on_oikein(self):
        maukkaita = self.kassapaate.maukkaat
        self.assertEqual(maukkaita, 0)

# Käteisostojen testaus:

    def test_rahamaara_kasvaa_oikein_edullisen_kateisostossa_tasaraha(self):
        self.kassapaate.syo_edullisesti_kateisella(240)
        rahaa = self.kassapaate.kassassa_rahaa
        self.assertEqual(rahaa, 100240)

    def test_rahamaara_kasvaa_oikein_maukkaan_kateisostossa_tasaraha(self):
        self.kassapaate.syo_maukkaasti_kateisella(400)
        rahaa = self.kassapaate.kassassa_rahaa
        self.assertEqual(rahaa, 100400)

    def test_rahamaara_kasvaa_oikein_edullisen_kateisostossa_ei_tasaraha(self):
        self.kassapaate.syo_edullisesti_kateisella(300)
        rahaa = self.kassapaate.kassassa_rahaa
        self.assertEqual(rahaa, 100240)

    def test_rahamaara_kasvaa_oikein_maukkaan_kateisostossa_ei_tasaraha(self):
        self.kassapaate.syo_maukkaasti_kateisella(500)
        rahaa = self.kassapaate.kassassa_rahaa
        self.assertEqual(rahaa, 100400)

    def test_vaihtoraha_on_oikein_edullisen_kateisostossa(self):
        vaihtoraha = self.kassapaate.syo_edullisesti_kateisella(300)
        self.assertEqual(vaihtoraha, 60)

    def test_vaihtoraha_on_oikein_maukkaan_kateisostossa(self):
        vaihtoraha = self.kassapaate.syo_maukkaasti_kateisella(500)
        self.assertEqual(vaihtoraha, 100)

    def test_myytyjen_edullisten_maara_on_oikein_kateisoston_jalkeen(self):
        self.kassapaate.syo_edullisesti_kateisella(240)
        edullisia = self.kassapaate.edulliset
        self.assertEqual(edullisia, 1)

    def test_myytyjen_maukkaiden_maara_on_oikein_kateisoston_jalkeen(self):
        self.kassapaate.syo_maukkaasti_kateisella(400)
        maukkaita = self.kassapaate.maukkaat
        self.assertEqual(maukkaita, 1)

    def test_rahamaara_ei_kasva_edullisen_puutteellisessa_kateisostossa(self):
        self.kassapaate.syo_edullisesti_kateisella(200)
        rahaa = self.kassapaate.kassassa_rahaa
        self.assertEqual(rahaa, 100000)

    def test_rahamaara_ei_kasva_maukkaiden_puutteellisessa_kateisostossa(self):
        self.kassapaate.syo_maukkaasti_kateisella(300)
        rahaa = self.kassapaate.kassassa_rahaa
        self.assertEqual(rahaa, 100000)

    def test_maksu_palautetaan_edullisen_puutteellisessa_kateisostossa(self):
        vaihtoraha = self.kassapaate.syo_edullisesti_kateisella(200)
        self.assertEqual(vaihtoraha, 200)

    def test_maksu_palautetaan_maukkaan_puutteellisessa_kateisostossa(self):
        vaihtoraha = self.kassapaate.syo_maukkaasti_kateisella(300)
        self.assertEqual(vaihtoraha, 300)

    def test_myytyjen_edullisten_maara_on_oikein_puutteellisen_kateisoston_jalkeen(self):
        self.kassapaate.syo_edullisesti_kateisella(200)
        edullisia = self.kassapaate.edulliset
        self.assertEqual(edullisia, 0)

    def test_myytyjen_maukkaiden_maara_on_oikein_puutteellisen_kateisoston_jalkeen(self):
        self.kassapaate.syo_maukkaasti_kateisella(300)
        maukkaita = self.kassapaate.maukkaat
        self.assertEqual(maukkaita, 0)

# Korttiostojen testaus:

    def test_edullisen_korttiosto_veloittaa_summan_kortilta(self):
        maksukortti = Maksukortti(300)
        self.kassapaate.syo_edullisesti_kortilla(maksukortti)
        self.assertEqual(str(maksukortti), "saldo: 0.6")

    def test_maukkaan_korttiosto_veloittaa_summan_kortilta(self):
        maksukortti = Maksukortti(500)
        self.kassapaate.syo_maukkaasti_kortilla(maksukortti)
        self.assertEqual(str(maksukortti), "saldo: 1.0")

    def test_onnistunut_edullisen_korttiosto_palauttaa_True(self):
        maksukortti = Maksukortti(300)
        onnistuiko = self.kassapaate.syo_edullisesti_kortilla(maksukortti)
        self.assertEqual(onnistuiko, True)

    def test_onnistunut_maukkaan_korttiosto_palauttaa_True(self):
        maksukortti = Maksukortti(500)
        onnistuiko = self.kassapaate.syo_edullisesti_kortilla(maksukortti)
        self.assertEqual(onnistuiko, True)

    def test_myytyjen_edullisten_maara_on_oikein_korttioston_jalkeen(self):
        maksukortti = Maksukortti(300)
        self.kassapaate.syo_edullisesti_kortilla(maksukortti)
        edullisia = self.kassapaate.edulliset
        self.assertEqual(edullisia, 1)

    def test_myytyjen_maukkaiden_maara_on_oikein_korttioston_jalkeen(self):
        maksukortti = Maksukortti(500)
        self.kassapaate.syo_maukkaasti_kortilla(maksukortti)
        maukkaita = self.kassapaate.maukkaat
        self.assertEqual(maukkaita, 1)

    def test_puutteellista_edullisen_korttiostoa_ei_veloiteta(self):
        maksukortti = Maksukortti(200)
        self.kassapaate.syo_edullisesti_kortilla(maksukortti)
        self.assertEqual(str(maksukortti), "saldo: 2.0")

    def test_puutteellista_maukkaan_korttiostoa_ei_veloiteta(self):
        maksukortti = Maksukortti(300)
        self.kassapaate.syo_maukkaasti_kortilla(maksukortti)
        self.assertEqual(str(maksukortti), "saldo: 3.0")

    def test_myytyjen_edullisten_maara_on_oikein_puutteellisen_korttioston_jalkeen(self):
        maksukortti = Maksukortti(200)
        self.kassapaate.syo_edullisesti_kortilla(maksukortti)
        edullisia = self.kassapaate.edulliset
        self.assertEqual(edullisia, 0)

    def test_myytyjen_maukkaiden_maara_on_oikein_puutteellisen_korttioston_jalkeen(self):
        maksukortti = Maksukortti(300)
        self.kassapaate.syo_maukkaasti_kortilla(maksukortti)
        maukkaita = self.kassapaate.maukkaat
        self.assertEqual(maukkaita, 0)

    def test_epaonnistunut_edullisen_korttiosto_palauttaa_False(self):
        maksukortti = Maksukortti(200)
        onnistuiko = self.kassapaate.syo_edullisesti_kortilla(maksukortti)
        self.assertEqual(onnistuiko, False)

    def test_epaonnistunut_maukkaan_korttiosto_palauttaa_False(self):
        maksukortti = Maksukortti(300)
        onnistuiko = self.kassapaate.syo_maukkaasti_kortilla(maksukortti)
        self.assertEqual(onnistuiko, False)

    def test_kassan_rahamaara_ei_muutu_edullisen_korttiostossa(self):
        maksukortti = Maksukortti(300)
        self.kassapaate.syo_edullisesti_kortilla(maksukortti)
        rahaa = self.kassapaate.kassassa_rahaa
        self.assertEqual(rahaa, 100000)

    def test_kassan_rahamaara_ei_muutu_maukkaan_korttiostossa(self):
        maksukortti = Maksukortti(500)
        self.kassapaate.syo_maukkaasti_kortilla(maksukortti)
        rahaa = self.kassapaate.kassassa_rahaa
        self.assertEqual(rahaa, 100000)

# Rahan latauksen testaus

    def test_rahan_lataus_kasvattaa_kortin_saldoa_oikein(self):
        maksukortti = Maksukortti(100)
        self.kassapaate.lataa_rahaa_kortille(maksukortti, 500)
        self.assertEqual(str(maksukortti), "saldo: 6.0")

    def test_rahan_lataus_kasvattaa_kassan_rahamaaraa_oikein(self):
        maksukortti = Maksukortti(100)
        self.kassapaate.lataa_rahaa_kortille(maksukortti, 500)
        rahaa = self.kassapaate.kassassa_rahaa
        self.assertEqual(rahaa, 100500)

    def test_negatiivinen_lataus_ei_vahenna_saldoa(self):
        maksukortti = Maksukortti(200)
        self.kassapaate.lataa_rahaa_kortille(maksukortti, -100)
        self.assertEqual(str(maksukortti), "saldo: 2.0")

    def test_negatiivinen_lataus_ei_vahenna_kassan_rahamaaraa(self):
        maksukortti = Maksukortti(200)
        self.kassapaate.lataa_rahaa_kortille(maksukortti, -100)
        rahaa = self.kassapaate.kassassa_rahaa
        self.assertEqual(rahaa, 100000)