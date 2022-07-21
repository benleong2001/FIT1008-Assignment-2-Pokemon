import unittest
from pokemon import Charmander, Bulbasaur, Squirtle, MissingNo
from pokemon_base import PokemonBase
from random import randint, seed
from tester_base import TesterBase


class TestPokemon(TesterBase):

    # Testing Constructors and String Methods
    def test_charmander_string(self):
        """ Test case for __init__() and __str__() method in Charmander class.
        Test 1: Test if Charmander object can be instantiated.
        Test 2: Test if __str__() method can be invoked properly.
        Test 3: Test if the string returned is as expected.
        """
        # Test 1
        try:
            c = Charmander()
        except Exception as e:
            self.verificationErrors.append(f'Charmander could not be instantiated: {str(e)}.')
            return

        # Test 2
        try:
            c_string = str(c)
        except Exception as e:
            self.verificationErrors.append(f'String method failed. {str(e)}')
            return

        # Test 3
        try:
            self.assertEqual(c_string, "Charmander's HP = 7 and level = 1",
                             f'String method did not return correct string: expected Charmander\'s HP = 7 and level = 1, got {c_string}')
        except AssertionError as e:
            self.verificationErrors.append(str(e))

    def test_bulbasaur_string(self):
        """ Test case for __init__() and __str__() method in Bulbasaur class.
        Test 1: Test if Bulbasaur object can be instantiated.
        Test 2: Test if __str__() method can be invoked properly.
        Test 3: Test if the string returned is as expected.
        """
        # Test 1
        try:
            b = Bulbasaur()
        except Exception as e:
            self.verificationErrors.append(f'Bulbasaur could not be instantiated: {str(e)}.')
            return

        # Test 2
        try:
            b_string = str(b)
        except Exception as e:
            self.verificationErrors.append(f'String method failed. {str(e)}')
            return

        # Test 3
        try:
            self.assertEqual(b_string, "Bulbasaur's HP = 9 and level = 1",
                             f'String method did not return correct string: expected Bulbasaur\'s HP = 9 and level = 1, got {b_string}')
        except AssertionError as e:
            self.verificationErrors.append(str(e))

    def test_squirtle_string(self):
        """ Test case for __init__() and __str__() method in Squirtle class.
        Test 1: Test if Squirtle object can be instantiated.
        Test 2: Test if __str__() method can be invoked properly.
        Test 3: Test if the string returned is as expected.
        """
        # Test 1
        try:
            s = Squirtle()
        except Exception as e:
            self.verificationErrors.append(f'Squirtle could not be instantiated: {str(e)}.')
            return

        # Test 2
        try:
            s_string = str(s)
        except Exception as e:
            self.verificationErrors.append(f'String method failed. {e}')
            return

        # Test 3
        try:
            self.assertEqual(s_string, "Squirtle's HP = 8 and level = 1",
                             f'String method did not return correct string: expected Squirtle\'s HP = 8 and level = 1, got {s_string}')
        except AssertionError as e:
            self.verificationErrors.append(str(e))

    def test_missing_no_string(self):
        """ Test case for __init__() and __str__() method in MissingNo class.
        Test 1: Test if MissingNo object can be instantiated.
        Test 2: Test if __str__() method can be invoked properly.
        Test 3: Test if the string returned is as expected.
        """
        # Test 1
        try:
            m = MissingNo()
        except Exception as e:
            self.verificationErrors.append(f'MissingNo could not be instantiated: {str(e)}.')
            return

        # Test 2
        try:
            m_string = str(m)
        except Exception as e:
            self.verificationErrors.append(f'String method failed. {e}')
            return

        # Test 3
        try:
            self.assertEqual(m_string, "MissingNo's HP = 8 and level = 1",
                             f'String method did not return correct string: expected MissingNo\'s HP = 8 and level = 1, got {m_string}')
        except AssertionError as e:
            self.verificationErrors.append(str(e))

    def test_calc_dmg(self):
        """ Test case for calc_dmg() method.
        TEST CASES
            Squirtle attack Charmander - 2x multiplier
            Squirtle attack Bulbasaur - 0.5x multiplier
            MissingNo attack Squirtle - 1x multiplier
            MissingNo attack MissingNo - Testing MissingNo getting attacked
        Test 1: Test if calc_dmg() can be invoked properly.
        Test 2: Test if calc_dmg() returns the correct expected value.
        
                  A  T  T  A  C  K
          D     |  c  |  b  |  s  |   m   |
          E ----|-----|-----|-----|-------|
          F   c |  7  |  1  |  8  |  16/3 |
          E   b | 14  |  2  |  1  |   2   |
          N   s |  1  |  5  |  2  |   2   |
          D   m |  7  |  2  |  2  |   2   |
            Table of damage values at base level.
        
        Note:
            For MissingNo, we are forcing it to choose Charmander's defence comparison formula 
            (i.e., if damage > defence: ...)
                This is done by using random.seed()
        """
        c, b, s, m = Charmander(), Bulbasaur(), Squirtle(), MissingNo()

        # Test Case 1 - Squirtle attack Charmander
        try:
            dmg = c.calc_dmg(s)
        except Exception as e:
            self.verificationErrors.append(f'calc_dmg() method not invoked properly for Charmander: {str(e)}')
            return

        try:
            self.assertEqual(dmg, 8,
                             f'Failed to retrieve expected damage for Charmander from Squirtle: expected 8, got {dmg}')
        except AssertionError as e:
            self.verificationErrors.append(str(e))

        # Test Case 2 - Squirtle attack Bulbasaur
        try:
            dmg = b.calc_dmg(s)
        except Exception as e:
            self.verificationErrors.append(f'calc_dmg() method not invoked properly for Bulbasaur: {str(e)}')
            return

        try:
            self.assertEqual(dmg, 1, f'Failed to retrieve expected damage for Bulbasaur: expected 1, got {dmg}')
        except AssertionError as e:
            self.verificationErrors.append(str(e))

        # Test Case 3 - MissingNo attack Squirtle
        try:
            dmg = s.calc_dmg(m)
        except Exception as e:
            self.verificationErrors.append(f'calc_dmg() method not invoked properly for Squirtle: {str(e)}')
            return

        try:
            self.assertEqual(dmg, 2, f'Failed to retrieve expected damage for Squirtle: expected 2, got {dmg}')
        except AssertionError as e:
            self.verificationErrors.append(str(e))

        # Test Case 4 - MissingNo attack MissingNo
        try:
            seed_int = 0
            while True:
                seed(seed_int)
                i = randint(0, 2)
                if i == 0:
                    break
                seed_int += 1
            seed(seed_int)
            dmg = m.calc_dmg(m)
        except Exception as e:
            self.verificationErrors.append(f'calc_dmg() method not invoked properly for MissingNo: {str(e)}')
            return

        try:
            self.assertEqual(dmg, 2, f'Failed to retrieve expected damage for MissingNo: expected 2, got {dmg}')
        except AssertionError as e:
            self.verificationErrors.append(str(e))

    def test_get_attack(self):
        """ Test case for get_attack() method.
        Test 1: Test if get_attack() can be invoked properly.
        Test 2: Test if get_attack() returns the correct expected value.

        Note:
            Tests are done for all 4 Pokemons where their level is set at 2
        """
        fixed_level = 2
        c, b, s, m = Charmander(), Bulbasaur(), Squirtle(), MissingNo()
        c.level, b.level, s.level, m.level = [fixed_level] * 4

        # Test for Charmander
        try:  # Test 1
            c_att = c.get_attack()
        except Exception as e:
            self.verificationErrors.append(f'get_attack() method was not invoked properly for Charmander: {str(e)}')
            return

        try:  # Test 2
            self.assertEqual(c_att, 6 + fixed_level,
                             f'Failed to retrieve expected attack for Charmander: expected {6 + fixed_level}, got {c_att}')
        except AssertionError as e:
            self.verificationErrors.append(str(e))

        # Test for Bulbasaur
        try:  # Test 1
            b_att = b.get_attack()
        except Exception as e:
            self.verificationErrors.append(f'get_attack() method was not invoked properly for Bulbasaur: {str(e)}')
            return

        try:  # Test 2
            self.assertEqual(b_att, 5, f'Failed to retrieve expected attack for Bulbasaur: expected 5, got {b_att}')
        except AssertionError:
            self.verificationErrors.append()

        # Test for Squirtle
        try:  # Test 1
            s_att = s.get_attack()
        except Exception as e:
            self.verificationErrors.append(f'get_attack() method was not invoked properly for Squirtle: {str(e)}')
            return

        try:  # Test 2
            self.assertEqual(s_att, 4 + fixed_level // 2,
                             f'Failed to retrieve expected attack for Squirtle: expected {4 + fixed_level // 2}, got {s_att}')
        except AssertionError as e:
            self.verificationErrors.append(str(e))

        # Test for MissingNo
        try:  # Test 1
            m_att = m.get_attack()
        except Exception as e:
            self.verificationErrors.append(f'get_attack() method was not invoked properly for MissingNo: {str(e)}')
            return

        try:  # Test 2
            self.assertEqual(m_att, 13 / 3 + fixed_level,
                             f'Failed to retrieve expected attack for MissingNo: expected {16 / 3 + fixed_level}, got {m_att}')
        except AssertionError as e:
            self.verificationErrors.append(str(e))

    def test_get_defence(self):
        """ Test case for get_defence() method.
        Test 1: Test if get_defence() can be invoked properly.
        Test 2: Test if get_defence() returns the correct expected value.

        Note:
            Tests are done for all 4 Pokemons where their level is set at 2
        """
        fixed_level = 2
        c, b, s, m = Charmander(), Bulbasaur(), Squirtle(), MissingNo()
        c.level, b.level, s.level, m.level = [fixed_level] * 4

        # Test for Charmander
        try:  # Test 1
            c_def = c.get_defence()
        except Exception as e:
            self.verificationErrors.append(f'get_defence() method was not invoked properly for Charmander: {str(e)}')
            return

        try:  # Test 2
            self.assertEqual(c_def, 4, f'Failed to retrieve expected defence for Charmander: expected 4, got {c_def}')
        except AssertionError as e:
            self.verificationErrors.append(str(e))

        # Test for Bulbasaur
        try:  # Test 1
            b_def = b.get_defence()
        except Exception as e:
            self.verificationErrors.append(f'get_defence() method was not invoked properly for Bulbasaur: {str(e)}')
            return

        try:  # Test 2
            self.assertEqual(b_def, 5, f'Failed to retrieve expected defence for Bulbasaur: expected 5, got {b_def}')
        except AssertionError as e:
            self.verificationErrors.append(str(e))

        # Test for Squirtle
        try:  # Test 1
            s_def = s.get_defence()
        except Exception as e:
            self.verificationErrors.append(f'get_defence() method was not invoked properly for Squirtle: {str(e)}')
            return

        try:  # Test 2
            self.assertEqual(s_def, 6 + fixed_level,
                             f'Failed to retrieve expected defence for Squirtle: expected {6 + fixed_level}, got {s_def}')
        except AssertionError as e:
            self.verificationErrors.append(str(e))

        # Test for MissingNo
        try:  # Test 1
            m_def = m.get_defence()
        except Exception as e:
            self.verificationErrors.append(f'get_defence() method was not invoked properly for MissingNo: {str(e)}')
            return

        try:  # Test 2
            self.assertEqual(m_def, 13 / 3 + fixed_level,
                             f'Failed to retrieve expected damage for MissingNo: expected {16 / 3 + fixed_level}, got {m_def}')
        except AssertionError as e:
            self.verificationErrors.append(str(e))

    def test_get_speed(self):
        """ Test case for get_defence() method.
        Test 1: Test if get_defence() can be invoked properly.
        Test 2: Test if get_defence() returns the correct expected value.

        Note:
            Tests are done for all 4 Pokemons where their level is set at 2
        """
        fixed_level = 2
        c, b, s, m = Charmander(), Bulbasaur(), Squirtle(), MissingNo()
        c.level, b.level, s.level, m.level = [fixed_level] * 4

        # Test for Charmander
        try:  # Test 1
            c_spd = c.get_speed()
        except Exception as e:
            self.verificationErrors.append(f'get_defence() method was not invoked properly for Charmander: {str(e)}')
            return

        try:  # Test 2
            self.assertEqual(c_spd, 7 + fixed_level,
                             f'Failed to retrieve expected defence for Charmander: expected {7 + fixed_level}, got {c_spd}')
        except AssertionError as e:
            self.verificationErrors.append(str(e))

        # Test for Bulbasaur
        try:  # Test 1
            b_spd = b.get_speed()
        except Exception as e:
            self.verificationErrors.append(f'get_defence() method was not invoked properly for Bulbasaur: {str(e)}')
            return

        try:  # Test 2
            self.assertEqual(b_spd, 7 + fixed_level // 2,
                             f'Failed to retrieve expected defence for Bulbasaur: expected {7 + fixed_level // 2}, got {b_spd}')
        except AssertionError as e:
            self.verificationErrors.append(str(e))

        # Test for Squirtle
        try:  # Test 1
            s_spd = s.get_speed()
        except Exception as e:
            self.verificationErrors.append(f'get_defence() method was not invoked properly for Squirtle: {str(e)}')
            return

        try:  # Test 2
            self.assertEqual(s_spd, 7, f'Failed to retrieve expected defence for Squirtle: expected 7, got {s_spd}')
        except AssertionError as e:
            self.verificationErrors.append(str(e))

        # Test for MissingNo
        try:  # Test 1
            m_spd = m.get_speed()
        except Exception as e:
            self.verificationErrors.append(f'get_defence() method was not invoked properly for MissingNo: {str(e)}')
            return

        try:  # Test 2
            self.assertEqual(m_spd, 19 / 3 + fixed_level,
                             f'Failed to retrieve expected damage for MissingNo: expected {22 / 3 + fixed_level}, got {m_spd}')
        except AssertionError as e:
            self.verificationErrors.append(str(e))

    def base_attribute_values_verification(self):
        """ Objective: To verify that the Base Attribute Values are as intended according to the Assignment specifications.
        The code compares the Base Values of each of the classes with their intended values.
        """

        for classes in [Charmander, Bulbasaur, Squirtle, MissingNo]:
            if classes == Charmander:
                if classes.BASE_POKE_TYPE != "Fire":
                    self.verificationErrors.append(
                        f'Incorrect BASE_POKE_TYPE value for Charmander: expected Fire, got {classes.BASE_POKE_TYPE}')
                if classes.BASE_HP != 7:
                    self.verificationErrors.append(
                        f'Incorrect BASE_HP value for Charmander: expected 7, got {classes.BASE_HP}')
                if classes.BASE_ATTACK != 6:
                    self.verificationErrors.append(
                        f'Incorrect BASE_ATTACK value for Charmander: expected 6, got {classes.BASE_ATTACK}')
                if classes.BASE_DEFENCE != 4:
                    self.verificationErrors.append(
                        f'Incorrect BASE_DEFENCE value for Charmander: expected 4, got {classes.BASE_DEFENCE}')
                if classes.BASE_SPEED != 7:
                    self.verificationErrors.append(
                        f'Incorrect BASE_SPEED value for Charmander: expected 7, got {classes.BASE_SPEED}')
            elif classes == Bulbasaur:
                if classes.BASE_POKE_TYPE != "Grass":
                    self.verificationErrors.append(
                        f'Incorrect BASE_POKE_TYPE value for Bulbasaur: expected Grass, got {classes.BASE_POKE_TYPE}')
                if classes.BASE_HP != 9:
                    self.verificationErrors.append(
                        f'Incorrect BASE_HP value for Bulbasaur: expected 9, got {classes.BASE_HP}')
                if classes.BASE_ATTACK != 5:
                    self.verificationErrors.append(
                        f'Incorrect BASE_ATTACK value for Bulbasaur: expected 5, got {classes.BASE_ATTACK}')
                if classes.BASE_DEFENCE != 5:
                    self.verificationErrors.append(
                        f'Incorrect BASE_DEFENCE value for Bulbasaur: expected 5, got {classes.BASE_DEFENCE}')
                if classes.BASE_SPEED != 7:
                    self.verificationErrors.append(
                        f'Incorrect BASE_SPEED value for Bulbasaur: expected 7, got {classes.BASE_SPEED}')
            elif classes == Squirtle:
                if classes.BASE_POKE_TYPE != "Water":
                    self.verificationErrors.append(
                        f'Incorrect BASE_POKE_TYPE value for Squirtle: expected Water, got {classes.BASE_POKE_TYPE}')
                if classes.BASE_HP != 8:
                    self.verificationErrors.append(
                        f'Incorrect BASE_HP value for Squirtle: expected 8, got {classes.BASE_HP}')
                if classes.BASE_ATTACK != 4:
                    self.verificationErrors.append(
                        f'Incorrect BASE_ATTACK value for Squirtle: expected 4, got {classes.BASE_ATTACK}')
                if classes.BASE_DEFENCE != 6:
                    self.verificationErrors.append(
                        f'Incorrect BASE_DEFENCE value for Squirtle: expected 6, got {classes.BASE_DEFENCE}')
                if classes.BASE_SPEED != 7:
                    self.verificationErrors.append(
                        f'Incorrect BASE_SPEED value for Squirtle: expected 7, got {classes.BASE_SPEED}')
            elif classes == MissingNo:
                if classes.BASE_POKE_TYPE is not None:
                    self.verificationErrors.append(
                        f'Incorrect BASE_POKE_TYPE value for Squirtle: expected None, got {classes.BASE_POKE_TYPE}')
                if classes.BASE_HP != 8:
                    self.verificationErrors.append(
                        f'Incorrect BASE_HP value for Squirtle: expected 8, got {classes.BASE_HP}')
                if classes.BASE_ATTACK != 13 / 3:
                    self.verificationErrors.append(
                        f'Incorrect BASE_ATTACK value for Squirtle: expected 4, got {classes.BASE_ATTACK}')
                if classes.BASE_DEFENCE != 13 / 3:
                    self.verificationErrors.append(
                        f'Incorrect BASE_DEFENCE value for Squirtle: expected 6, got {classes.BASE_DEFENCE}')
                if classes.BASE_SPEED != 19 / 3:
                    self.verificationErrors.append(
                        f'Incorrect BASE_SPEED value for Squirtle: expected 7, got {classes.BASE_SPEED}')

    def test_consistency_all_method(self):
        """ Objective:  To test the consistency of all methods in pokemon and pokemon_base classes (inherited). """
        # List of Pokemons
        pokemon_list_1 = []
        pokemon_list_2 = []

        # Adding Charmander to the lists of Pokemons
        c1, c2 = Charmander(), Charmander()

        pokemon_list_1.append(c1)
        pokemon_list_2.append(c2)

        # Adding Bulbasaur to the lists of Pokemons
        b1, b2 = Bulbasaur(), Bulbasaur()

        pokemon_list_1.append(b1)
        pokemon_list_2.append(b2)

        # Adding Squirtle to the list of Pokemons
        s1, s2 = Squirtle(), Squirtle()

        pokemon_list_1.append(s1)
        pokemon_list_2.append(s2)

        # Adding MissingNo to the list of pokemons
        m1, m2 = MissingNo(), MissingNo()

        pokemon_list_1.append(m1)
        pokemon_list_2.append(m2)

        # pokemon_list_1 = [c1,b1,s1,m1]
        # pokemon_list_2 = [c2,b2,s2,m2]

        # Making a list of all the methods in the pokemon_base.py and pokemon.py files
        # pokemon_base class
        pokemon_base_methods = ["get_level", "get_hp", "get_poke_type"]

        # pokemon class
        pokemon_methods = ["get_attack", "get_defence", "get_speed", "calc_dmg"]

        methods = pokemon_base_methods + pokemon_methods

        # methods = ["get_level", "get_hp", "get_poke_type",
        #            "get_attack", "get_defence", "get_speed","calc_dmg"]

        # Iterating over all methods
        for method in methods:

            # Iterating over all pokemons in pokemon_list_1
            for pokemon_1 in pokemon_list_1:

                # Iterating over all pokemons in pokemon_list_2
                for pokemon_2 in pokemon_list_2:

                    # to test the consistency of all methods by iterating a certain amount of times
                    for _ in range(10):

                        # to add a variety of testing by selecting different combinations of leveling
                        # 1 - pokemon_1 has a different level, pokemon_2 has level 1
                        # 2 - pokemon_2 has a different level, pokemon_1 has level 1
                        # 3 - both pokemons has different levels
                        random_level_picker = randint(1, 3)

                        # Used to decide the domain of the random int
                        level_from, level_to = 1, 6

                        # Declaring and initialising variables which is used to set the level
                        random_level_pokemon_1 = 1 if random_level_picker == 2 else randint(level_from, level_to)
                        random_level_pokemon_2 = 1 if random_level_picker == 1 else randint(level_from, level_to)

                        pokemon_1.set_level(random_level_pokemon_1)
                        pokemon_2.set_level(random_level_pokemon_2)

                        pokemon_class_1 = type(pokemon_1)
                        pokemon_class_2 = type(pokemon_2)

                        # Testing get_level() and set_level()
                        if method == "get_level":
                            """ Objective: To test consistency of get_level() and set_level() methods. """
                            # If level is not the same as random_level_pokemon_1
                            if pokemon_1.get_level() != random_level_pokemon_1:
                                self.verificationErrors.append(
                                    f'get_level() method did not return correct level value for {pokemon_class_1.__name__}: '
                                    f'expected {random_level_pokemon_1}, got {pokemon_1.get_level()}')

                        # Testing get_hp() and set_hp()
                        elif method == "get_hp":
                            """ Objective: To test consistency of get_hp() and set_hp() methods. """

                            # Determining offset (if any)
                            adder = random_level_pokemon_1 - 1 if pokemon_class_1 == MissingNo else 0

                            # If hp is not the same as expected value.
                            if pokemon_1.get_hp() != pokemon_class_1.BASE_HP + adder:
                                self.verificationErrors.append(
                                    f'get_hp() method did not return correct default hp value for {pokemon_class_1.__name__}: '
                                    f'expected {pokemon_class_1.BASE_HP + adder}, got {pokemon_1.get_hp()}')

                            # Testing set_hp()
                            pokemon_1.set_hp(random_hp_pokemon := randint(1, 10))

                            # If hp is not the same as random_hp_pokemon
                            if pokemon_1.get_hp() != random_hp_pokemon:
                                self.verificationErrors.append(
                                    f'get_hp() method did not return correct hp value for {pokemon_class_1.__name__}: '
                                    f'expected {random_hp_pokemon}, got {pokemon_1.get_hp()}')

                            # Resetting hp value for remaining tests
                            pokemon_1.set_hp(pokemon_class_1.BASE_HP + adder)

                        # Testing get_poke_type() and set_poke_type()
                        elif method == "get_poke_type":
                            """ Objective: To test consistency of get_poke_type() and set_poke_type() methods. """

                            # If poke_type if not the same as the default value
                            if pokemon_1.get_poke_type() != pokemon_class_1.BASE_POKE_TYPE:
                                self.verificationErrors.append(
                                    f'get_poke_type() method did not return correct default poke_type value for {pokemon_class_1.__name__}: '
                                    f'expected {pokemon_class_1.BASE_POKE_TYPE}, got {pokemon_1.get_poke_type()}')

                            # Testing set_poke_type() with all poke_type values
                            for types in ["Fire", "Grass", "Water"]:
                                pokemon_1.set_poke_type(types)

                                # If poke_type is not the same as types
                                if pokemon_1.get_poke_type() != types:
                                    self.verificationErrors.append(
                                        f'get_poke_type() method did not return correct poke_type value for {pokemon_class_1.__name__}: '
                                        f'expected {types}, got {pokemon_1.get_poke_type()}')

                            # Resetting poke_type value for remaining tests
                            pokemon_1.set_poke_type(pokemon_class_1.BASE_POKE_TYPE)

                        # Testing get_attack()
                        elif method == "get_attack":
                            """ Objective: To test consistency of get_attack() method. """

                            # Determining offset (if any)
                            if pokemon_class_1 == Bulbasaur:
                                adder = 0
                            elif pokemon_class_1 == Squirtle:
                                adder = random_level_pokemon_1 // 2
                            else:
                                adder = random_level_pokemon_1

                            # If attack is not the expected value
                            if pokemon_1.get_attack() != pokemon_class_1.BASE_ATTACK + adder:
                                self.verificationErrors.append(
                                    f'get_attack() method did not return correct default attack value for {pokemon_class_1.__name__}: '
                                    f'expected {pokemon_class_1.BASE_ATTACK + adder}, got {pokemon_1.get_attack()}')

                        # Testing get_defence()
                        elif method == "get_defence":
                            """ Objective: To test consistency of get_defence() method. """

                            # Determining offset (if any)
                            adder = random_level_pokemon_1 if pokemon_class_1 == Squirtle or pokemon_class_1 == MissingNo else 0

                            # If defence is not the expected value
                            if pokemon_1.get_defence() != pokemon_class_1.BASE_DEFENCE + adder:
                                self.verificationErrors.append(
                                    f'get_defence() method did not return correct default defence value for {pokemon_class_1.__name__}: '
                                    f'expected {pokemon_class_1.BASE_DEFENCE + adder}, got {pokemon_1.get_defence()}')

                        # Testing get_speed()
                        elif method == "get_speed":
                            """ Objective: To test consistency of get_speed() method. """

                            # Determining offset (if any)
                            if pokemon_class_1 == Squirtle:
                                adder = 0
                            elif pokemon_class_1 == Bulbasaur:
                                adder = random_level_pokemon_1 // 2
                            else:
                                adder = random_level_pokemon_1

                            # If speed is not the expected value
                            if pokemon_1.get_speed() != pokemon_class_1.BASE_SPEED + adder:
                                self.verificationErrors.append(
                                    f'get_speed() method did not return correct default speed value for {pokemon_class_1.__name__}: '
                                    f'expected {pokemon_class_1.BASE_SPEED + adder}, got {pokemon_1.get_speed()}')

                        # Testing calc_dmg()
                        elif method == "calc_dmg":
                            """ Objective: To test consistency of calc_dmg() method.
                            Note:
                                - damage returned = damage stat * type multiplier and then compared with defence
                                - pokemon_2 attacks pokemon_1
                                    - received damage for pokemon_1 is calculated
                            """
                            poke_type_1 = pokemon_class_1.BASE_POKE_TYPE if pokemon_class_1.BASE_POKE_TYPE else ""
                            poke_type_2 = pokemon_class_2.BASE_POKE_TYPE if pokemon_class_2.BASE_POKE_TYPE else ""
                            combined_type = poke_type_2 + poke_type_1

                            # Finding damage after type multiplier
                            if combined_type in ["GrassFire", "FireWater", "WaterGrass"]:
                                effective_dmg = pokemon_2.get_attack() * 0.5
                            elif combined_type in ["FireGrass", "WaterFire", "GrassWater"]:
                                effective_dmg = pokemon_2.get_attack() * 2
                            else:
                                effective_dmg = pokemon_2.get_attack()

                            # Finding defence value for pokemon_1
                            if pokemon_class_1 == Bulbasaur:
                                defence = pokemon_1.get_defence() + 5
                            elif pokemon_class_1 == Squirtle:
                                defence = pokemon_1.get_defence() * 2
                            else:
                                defence = pokemon_1.get_defence()

                            # Finding expected damage taken after comparing with defence
                            expected_dmg = effective_dmg if effective_dmg > defence else effective_dmg // 2

                            # Fixing defence for MissingNo
                            seed_int = 0
                            while True:
                                seed(seed_int)
                                i = randint(0, 2)
                                if not i:
                                    break
                                seed_int += 1
                            seed(seed_int)

                            # Testing calc_dmg() method
                            damage_received = pokemon_1.calc_dmg(pokemon_2)

                            # If value received is not the same as expected
                            if damage_received != expected_dmg:
                                self.verificationErrors.append(
                                    f'calc_damage({pokemon_class_2.__name__}) method did not return correct damage '
                                    f'received for {pokemon_class_1.__name__}: expected {expected_dmg}, got {damage_received}')


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestPokemon)
    unittest.TextTestRunner(verbosity=0).run(suite)
