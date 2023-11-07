import unittest

from Formelkoll import *


class SyntaxTest(unittest.TestCase):

    def testKorrektMol(self):

        self.assertEqual(kollaMolekyl("Na"),
                         "Formeln är syntaktiskt korrekt")

        self.assertEqual(kollaMolekyl("H20"),
                         "Formeln är syntaktiskt korrekt")

        self.assertEqual(kollaMolekyl("Si(C3(COOH)2)4(H2O)7"),
                         "Formeln är syntaktiskt korrekt")

        self.assertEqual(kollaMolekyl("Na332"),
                         "Formeln är syntaktiskt korrekt")

    def testFelaktigMol(self):

        self.assertEqual(kollaMolekyl("C(Xx4)5"),
                         "Okänd atom vid radslutet 4)5")

        self.assertEqual(kollaMolekyl("C(OH4)C"),
                         "Saknad siffra vid radslutet C")

        self.assertEqual(kollaMolekyl("C(OH4C"),
                         "Saknad högerparentes vid radslutet")

        self.assertEqual(kollaMolekyl("H2O)Fe"),
                         "Felaktig gruppstart vid radslutet )Fe")

        self.assertEqual(kollaMolekyl("H0"),
                         "För litet tal vid radslutet ")

        self.assertEqual(kollaMolekyl("H1C"),
                         "För litet tal vid radslutet C")

        self.assertEqual(kollaMolekyl("H02C"),
                         "För litet tal vid radslutet 2C")

        self.assertEqual(kollaMolekyl("Nacl"),
                         "Saknad stor bokstav vid radslutet cl")

        self.assertEqual(kollaMolekyl("a"),
                         "Saknad stor bokstav vid radslutet a")

        self.assertEqual(kollaMolekyl("(Cl)2)3"),
                         "Felaktig gruppstart vid radslutet )3")

        self.assertEqual(kollaMolekyl(")"),
                         "Felaktig gruppstart vid radslutet )")

        self.assertEqual(kollaMolekyl("2"),
                         "Felaktig gruppstart vid radslutet 2")


if __name__ == '__main__':
    unittest.main()
