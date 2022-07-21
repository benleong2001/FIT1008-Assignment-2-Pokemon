import unittest

from pokemon import Charmander, Bulbasaur
from pokemon_base import PokemonBase
from tester_base import TesterBase


class TestPokemonBase(TesterBase):
    """ Tester class for PokemonBase class
    Since PokemonBase is an abstract class, we cannot create any objects from it.
    Therefore we need to create an object of it's child class
        and use this object to invoke the methods from the parent class.
    """
    # My precious little char_char will be the tester Pokemon for the method in PokemonBase class.
    char_char = Charmander()

    def test_pokemon_base_string(self):
        """
        Test case for __init__() and __str__() methods.
        Test 1: Test if the constructor functions as intended.
            Not tested with invalid values as that will be done under tester for Mutator Methods.
        Test 2: Test if __str__() method can be invoked properly.
        Test 2: Test if the string method returns the expected string representation of PokemonBase object.
        """
        # Test 1
        # Instantiating an object
        c = Charmander()
        hp = 5
        poke_type = "Water"
        try:
            PokemonBase.__init__(c, hp, poke_type)
        except Exception as e:
            self.verificationErrors.append(f'PokemonBase object not properly instantiated: {str(e)}.')
            return

        # Test 2
        try:
            poke_string = str(c)
        except Exception as e:
            self.verificationErrors.append(f'Method could not be invoked properly: {str(e)}')
            return

        # Test 3
        try:
            self.assertEqual(poke_string, "Charmander's HP = 5 and level = 1",
                             f'String method did not return correct string: expected "Charmander\'s HP = 5 and level = 1", got {poke_string}')
        except AssertionError as e:
            self.verificationErrors.append(str(e))

    def test__get_name(self):
        """
        Test case for _get_name() method.
        Test 1: Test if the method can be invoked properly.
        Test 2: Test if the return value is the class name.
        """
        # Test 1
        try:
            name = PokemonBase._get_name()
        except Exception as e:
            self.verificationErrors.append(f'Class name could not be retrieved: {str(e)}')
            return

        # Test 2
        try:
            self.assertEqual(name, "PokemonBase",
                             f'Failed to return the correct class name: expected "PokemonBase", got {name}.')
        except AssertionError as e:
            self.verificationErrors.append(str(e))

    # Testing Mutator Methods
    def test_set_level(self):
        """
        Test case for set_level() method.
        Test 1: Test set_level() pre condition.
        Test 2: Test if level can be set using set_level().
        Test 3: Test if level assigned is set properly.
        """
        # Test 1
        invalid_level_value = "one"
        try:
            self.assertRaises(ValueError, TestPokemonBase.char_char.set_level, invalid_level_value)
        except AssertionError:
            self.verificationErrors.append("set_level() method does not handle invalid input properly.")
            return

        # Test 2
        valid_level_value = 10
        try:
            TestPokemonBase.char_char.set_level(valid_level_value)
        except Exception as e:
            self.verificationErrors.append(f'Pokemon level could not be set: {str(e)}')
            return

        # Test 3
        try:
            self.assertEqual(TestPokemonBase.char_char.level, valid_level_value,
                             f'Pokemon level not properly set: expected {valid_level_value}, got {TestPokemonBase.char_char.level}')
        except AssertionError as e:
            self.verificationErrors.append(str(e))

    def test_set_hp(self):
        from pokemon import Charmander, Bulbasaur, Squirtle
        """
        Test case for set_hp() method.
        Test 1: Test set_hp() pre condition.
        Test 2: Test if hp can be set using set_hp().
        Test 3: Test if hp assigned is set properly.
        """
        # Test 1
        invalid_hp_value = True
        try:
            self.assertRaises(ValueError, TestPokemonBase.char_char.set_hp, invalid_hp_value)
        except AssertionError:
            self.verificationErrors.append("set_hp() method does not handle invalid input properly.")
            return

        # Test 2
        valid_hp_value = 10
        try:
            TestPokemonBase.char_char.set_hp(valid_hp_value)
        except Exception as e:
            self.verificationErrors.append(f'Pokemon hp could not be set: {str(e)}')
            return

        try:
            self.assertEqual(TestPokemonBase.char_char.hp, valid_hp_value,
                             f'Pokemon hp not properly set: expected {valid_hp_value}, got {TestPokemonBase.char_char.hp}')
        except AssertionError as e:
            self.verificationErrors.append(str(e))

    def test_set_poke_type(self):
        """
        Test case for set_poke_type() method.
        Test 1: Test set_poke_type() pre condition.
        Test 2: Test if poke_type can be set using set_poke_type().
        Test 3: Test if poke_type assigned is set properly.
        """
        # Test 1
        invalid_poke_type_value = True
        try:
            self.assertRaises(ValueError, TestPokemonBase.char_char.set_poke_type, invalid_poke_type_value)
        except AssertionError:
            self.verificationErrors.append("set_poke_type() method does not handle invalid input properly.")
            return

        # Test 2
        valid_poke_type_value = "Water"
        try:
            TestPokemonBase.char_char.set_poke_type(valid_poke_type_value)
        except Exception as e:
            self.verificationErrors.append(f'Pokemon poke_type could not be set: {str(e)}')
            return

        # Test 3
        try:
            self.assertEqual(TestPokemonBase.char_char.poke_type, valid_poke_type_value,
                             f'Pokemon poke_type not properly set: expected {valid_poke_type_value} got {TestPokemonBase.char_char.poke_type}')
        except AssertionError as e:
            self.verificationErrors.append(str(e))

    # Testing Accessor Methods
    def test_get_level(self):
        """
        Test case for method get_level().
        Test 1: Test if the method can be invoked.
        Test 2: Test if the returned level is the expected level value
        """
        expected_level = 10
        TestPokemonBase.char_char.level = expected_level

        # Test 1
        try:
            res_level = TestPokemonBase.char_char.get_level()
        except Exception as e:
            self.verificationErrors.append(f'Level attribute could not be retrieved: {str(e)}')
            return

        # Test 2
        try:
            self.assertEqual(res_level, expected_level,
                             f'Pokemon level accessed incorrectly: expected {expected_level}, got {res_level}')
        except AssertionError as e:
            self.verificationErrors.append(str(e))

    def test_get_hp(self):
        """
        Test case for method get_hp().
        Test 1: Test if the method can be invoked properly.
        Test 2: Test if the returned hp is the expected hp value
        """
        expected_hp = 420
        TestPokemonBase.char_char.hp = expected_hp

        # Test 1
        try:
            res_hp = TestPokemonBase.char_char.get_hp()
        except Exception as e:
            self.verificationErrors.append(f'HP attribute could not be retrieved: {str(e)}')
            return

        # Test 2
        try:
            self.assertEqual(res_hp, expected_hp,
                             f'Pokemon level accessed incorrectly: expected {expected_hp}, got {res_hp}')
        except AssertionError as e:
            self.verificationErrors.append(str(e))

    def test_get_poke_type(self):
        """
        Test case for method get_hp().
        Test 1: Test if the method can be invoked properly.
        Test 2: Test if the returned hp is the expected hp value
        """
        expected_poke_type = "Water"
        TestPokemonBase.char_char.poke_type = expected_poke_type

        # Test 1
        try:
            res_poke_type = TestPokemonBase.char_char.get_poke_type()
        except Exception as e:
            self.verificationErrors.append(f'Poke Type attribute could not be retrieved: {str(e)}')
            return

        # Test 2
        try:
            self.assertEqual(res_poke_type, expected_poke_type,
                             f'Pokemon poke_type accessed incorrectly: expected {expected_poke_type}, got {res_poke_type}')
        except AssertionError as e:
            self.verificationErrors.append(str(e))

    # Testing Abstract Methods
    def test_get_attack(self):
        """ Test case for method get_attack().
        Test if NotImplementedError is raised when calling method.
        """
        try:
            self.assertRaises(NotImplementedError, PokemonBase.get_attack, TestPokemonBase.char_char)
        except AssertionError:
            self.verificationErrors.append("NotImplementedError not raised.")

    def test_get_defence(self):
        """ Test case for method get_defence().
        Test if NotImplementedError is raised when calling method.
        """
        try:
            self.assertRaises(NotImplementedError, PokemonBase.get_defence, TestPokemonBase.char_char)
        except AssertionError:
            self.verificationErrors.append("NotImplementedError not raised.")

    def test_get_speed(self):
        """ Test case for method get_speed().
        Test if NotImplementedError is raised when calling method.
        """
        try:
            self.assertRaises(NotImplementedError, PokemonBase.get_speed, TestPokemonBase.char_char)
        except AssertionError:
            self.verificationErrors.append("NotImplementedError not raised.")

    def test_calc_dmg(self):
        """ Test case for calc_dmg() method
        Test 1: Test if ValueError is raised when invalid input is used.
        Test 2: Test if nothing happens when valid input is used.
        """
        # Test 1
        invalid_attacker_input = "Bad input"
        try:
            self.assertRaises(ValueError, TestPokemonBase.char_char.calc_dmg, invalid_attacker_input)
        except AssertionError:
            self.verificationErrors.append("calc_dmg() method does not handle invalid input properly.")
            return

        # Test 2
        valid_attacker_input = Bulbasaur()
        try:
            PokemonBase.calc_dmg(TestPokemonBase.char_char, valid_attacker_input)
        except Exception as e:
            self.verificationErrors.append(f'Method could not be invoked properly: {str(e)}')

    # Testing Extra methods
    def test_is_alive(self):
        """ Test case for is_alive() method.
        Test 1: Test if method can be invoked properly.
            Test 1.1: Once for positive HP value.
            Test 1.2: Once for non-positive HP value.
        Test 2: Test if method returns True when Pokemon's HP is a positive integer.
        Test 3: Test if method returns False when Pokemon's HP is a non-positive integer.
        """
        # Test 1
        # Test 1.1
        positive_hp_value = 1
        TestPokemonBase.char_char.hp = positive_hp_value
        try:
            alive_bool = TestPokemonBase.char_char.is_alive()
        except Exception as e:
            self.verificationErrors.append(f'Method could not be invoked properly: {str(e)}')
            return

        # Test 1.2
        non_positive_hp_value = -1
        TestPokemonBase.char_char.hp = non_positive_hp_value
        try:
            not_alive_bool = TestPokemonBase.char_char.is_alive()
        except Exception as e:
            self.verificationErrors.append(f'Method could not be invoked properly: {str(e)}')
            return

        # Test 2
        try:
            self.assertTrue(alive_bool,
                             f'Method does not return the appropriate boolean value: expected "True", got {TestPokemonBase.char_char.is_alive()}')
        except AssertionError as e:
            self.verificationErrors.append(str(e))
            return

        # Test 3
        try:
            self.assertFalse(not_alive_bool,
                             f'Method does not return the appropriate boolean value: expected "False", got {TestPokemonBase.char_char.is_alive()}')
        except AssertionError as e:
            self.verificationErrors.append(str(e))


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestPokemonBase)
    unittest.TextTestRunner(verbosity=0).run(suite)
