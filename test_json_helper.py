from unittest import TestCase

import json_helper


class Test(TestCase):
    def test_read_json(self):
        test_case = [({'name': 'Anxiety', 'neutral_special': 'Pie Toss', 'side_special': 'Slip', 'up_special': 'Laugh',
         'down_special': 'Cry', 'final_smash': 'Crowned Clown'}, 'data/atum/anxiety.json'),
        ({"name": "Despair", "neutral_special": "Mana Blades", "side_special": "Slash Dance", "up_special": "Death "
           "Blink", "down_special": "Blade Tango", "final_smash": "Death Waltz"}, 'data/atum/despair.json'),
                     ]
        for (expected, actual) in test_case:
            with self.subTest(f'{expected}, {actual}'):
                self.assertEqual(expected, json_helper.read_json(actual))

    def test_read_all_json_files(self):
        self.fail()

    def test_write_pickle(self):
        self.fail()

    def test_load_pickle(self):
        self.fail()
