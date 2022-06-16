#!/usr/bin/env python

# Diego Fernando
# "Pico y Placa" test
# 14/06/2022

import unittest
from PicoYPlacaService import PicoYPlacaService


class TestPicoYPlaca(unittest.TestCase):
    # def setup(self):
    #     self.pico_y_placa = PicoYPlacaService('LBD2800', '2022-06-15', '17:20')

    def test_service(self):
        self.assertEqual(PicoYPlacaService.be_on_road(
            'LBD2806', '2022-06-15', '17:20'), "Your car can't be on road")


if __name__ == "__main__":
    unittest.main()
