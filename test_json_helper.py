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
        expected = [{'name': 'Mario', 'neutral_special': 'Fireball', 'side_special': 'Cape', 'up_special': 'Super Jump Punch', 'down_special': 'F.L.U.D.D.', 'final_smash': 'Mario Finale'}, {'name': 'Link', 'neutral_special': 'Bow and Arrows', 'side_special': ' Boomerang', 'up_special': ' Spin Attack', 'down_special': 'Remote Bomb', 'final_smash': 'Ancient Bow and Arrow'}]
        actual = 'data/super_smash_bros'
        self.assertEqual(expected, json_helper.read_all_json_files(actual))

    def test_pickle(self):
        test_case = [
            ('super_smash_characters.pickle', 'data/super_smash_bros'),
            ('atum_characters.pickle', 'data/atum')


        ]
        for (path, data) in test_case:
            with self.subTest(f'{path},{data}'):
                json_helper.write_pickle(path, json_helper.read_all_json_files(data))
                actual = json_helper.load_pickle(path)
                print(actual)
                self.assertEqual(actual, json_helper.read_all_json_files(data))
