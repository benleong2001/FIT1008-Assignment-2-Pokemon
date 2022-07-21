import unittest
from array_sorted_list import ArraySortedList
from doctest import Example
from poke_team import PokeTeam
from pokemon import Bulbasaur, Charmander, MissingNo, Squirtle
from queue_adt import CircularQueue
from sorted_list import ListItem
from stack_adt import ArrayStack
from tester_base import TesterBase, captured_output
from xml.dom.minidom import CharacterData


class TestBattle(TesterBase):
    from battle import Battle
    b = Battle("Bernard", "Ben")

    def test_set_team1(self):
        """ Test case for set_team1() method.
        Test 1: Test if TypeError is raised when invalid input is given.
        Test 2: Test if team1 can be set with the method.
        """
        # Test 1
        invalid_team1_input = "Bad PokeTeam1 input"
        try:
            self.assertRaises(TypeError, TestBattle.b.set_team1, invalid_team1_input)
        except AssertionError:
            self.verificationErrors.append("TypeError is not raised for invalid input")
            return

        # Test 2
        valid_team1_input = PokeTeam("Ash")
        try:
            TestBattle.b.set_team1(valid_team1_input)
        except TypeError as e:
            self.verificationErrors.append(f"team1 could not be set: {str(e)}.")

    def test_set_team2(self):
        """ Test case for set_team2() method.
        Test 1: Test if TypeError is raised when invalid input is given.
        Test 2: Test if team1 can be set with the method.
        """
        # Test 1
        invalid_team2_input = "Bad PokeTeam2 input"
        try:
            self.assertRaises(TypeError, TestBattle.b.set_team1, invalid_team2_input)
        except AssertionError:
            self.verificationErrors.append("TypeError is not raised for invalid input")
            return

        # Test 2
        valid_team2_input = PokeTeam("Misty")
        try:
            TestBattle.b.set_team2(valid_team2_input)
        except TypeError as e:
            self.verificationErrors.append(f"team2 could not be set: {str(e)}.")

    def test_set_battle_mode(self):
        """ Test case for set_battle_mode() method.
        Test if ValueError is raised when invalid input is given.
        """
        # INVALID TEST CASES
        bad_examples = [-1, 3, 100]
        for bad_example in bad_examples:
            try:
                self.assertRaises(ValueError, TestBattle.b.set_battle_mode, bad_example)
            except AssertionError:
                self.verificationErrors.append("set_battle_mode() method does not handle invalid input properly.")

        # VALID TEST CASES
        good_examples = [0, 1, 2]
        for good_example in good_examples:
            try:
                TestBattle.b.set_battle_mode(good_example)
            except Exception as e:
                self.verificationErrors.append(f"Failed to invoke battle_mode properly: {e}")

    def test_get_team1(self):
        """ Test case for get_team1() method.
        Test if team1 is retrieved correctly with the intended value
        """
        expected = [PokeTeam(""), PokeTeam("Ash"), PokeTeam("Misty")]
        for value in expected:
            TestBattle.b.team1 = value
            try:
                self.assertEqual(TestBattle.b.get_team1(), value,
                                 f'team1 accessed incorrectly: expected {str(value)}, got {str(TestBattle.b.get_team1())}.')
            except AssertionError as e:
                self.verificationErrors.append(str(e))

    def test_get_team2(self):
        """ Test case for get_team2() method.
        Test if team2 is retrieved correctly with the intended value
        """
        expected = [PokeTeam(""), PokeTeam("Ben"), PokeTeam("Staff")]
        for value in expected:
            TestBattle.b.team2 = value
            try:
                self.assertEqual(TestBattle.b.get_team2(), value,
                                 f'team1 accessed incorrectly: expected {str(value)}, got {str(TestBattle.b.get_team2())}.')
            except AssertionError as e:
                self.verificationErrors.append(str(e))

    def test_get_battle_mode(self):
        """ Test case for get_battle_mode() method.
        Test if battle mode is retrieved correctly with the intended value
        """
        expected = [0, 1, 2]
        for value in expected:
            TestBattle.b.set_battle_mode(value)
            try:
                assert TestBattle.b.get_battle_mode() == value
            except AssertionError:
                self.verificationErrors.append(f"Battle mode accessed incorrectly: {str(value)}.")

    def test_access(self):
        """ Test case for access() method.
        Test 1: Test if Value Error is raised when index that wanted to access is out of range
        Test 2: Test if correct Pokemon is retrieved when battle mode is 0
        Test 3: Test if correct Pokemon is retrieved when battle mode is 1
        Test 4: Test if correct Pokemon is retrieved when battle mode is 2
        Test 5: Test if Exception is raised when battle mode is in valid
        Test 6: Invalid Battle Mode
        """
        team_sample = TestBattle.b
        team_sample.team1 = CircularQueue(6)

        """ Test 1
        Test if Value Error is raised when index that wanted to access is out of range
        """
        # Empty ADT
        try:
            self.assertRaises(ValueError, TestBattle.b.access, team_sample.team1)
        except AssertionError:
            self.verificationErrors.append("ValueError is not raised when index out of range")
            return

        # Index out of range
        for _ in range(6):
            TestBattle.b.team1.append(Charmander())
        # Index too high
        try:
            self.assertRaises(IndexError, TestBattle.b.access, team_sample.team1, 7)
        except AssertionError:
            self.verificationErrors.append("ValueError is not raised when index out of range")
            return
        # Index too low
        try:
            self.assertRaises(IndexError, TestBattle.b.access, team_sample.team1, -1)
        except AssertionError:
            self.verificationErrors.append("ValueError is not raised when index out of range")
            return

        """ Test 2
        Test if correct Pokemon is retrieved when battle mode is 0
        """
        team_sample.team1 = ArrayStack(6)
        team_sample.team1.push(Charmander())
        team_sample.team1.push(Bulbasaur())
        team_sample.team1.push(Squirtle())
        TestBattle.b.set_battle_mode(0)
        try:
            self.assertTrue(isinstance(team_sample.access(team_sample.team1), Squirtle),
                            f'Incorrect Pokemon retrieved, expected Squirtle, got: {str(team_sample.access(team_sample.team1))}.')
        except AssertionError as e:
            self.verificationErrors.append(str(e))

        """ Test 3 
        Test if correct Pokemon is retrieved when battle mode is 1
        """
        team_sample.team1 = CircularQueue(6)
        team_sample.set_battle_mode(1)
        team_sample.team1.append(Charmander())
        team_sample.team1.append(Bulbasaur())
        team_sample.team1.append(Squirtle())
        try:
            self.assertTrue(isinstance(team_sample.access(team_sample.team1), Charmander),
                            f'Incorrect Pokemon retrieved, expected Charmander, got: {str(team_sample.access(team_sample.team1))}.')
        except AssertionError as e:
            self.verificationErrors.append(str(e))

        """ Test 4
        Test if correct Pokemon is retrieved when battle mode is 2
        """
        team_sample.set_battle_mode(2)
        team_sample.team1 = ArraySortedList(6)
        char_key, bulb_key, squir_key = Charmander().get_hp(), Bulbasaur().get_hp(), Squirtle().get_hp()
        team_sample.team1.new_add(ListItem(Squirtle(), squir_key))
        team_sample.team1.new_add(ListItem(Bulbasaur(), bulb_key))
        team_sample.team1.new_add(ListItem(Charmander(), char_key))
        try:
            self.assertTrue(isinstance(team_sample.access(team_sample.team1, 0), Charmander),
                            f'Incorrect Pokemon retrieved, expected Charmander, got: {str(team_sample.access(team_sample.team1)._get_name)}.')
        except AssertionError as e:
            self.verificationErrors.append(str(e))

        """ Test 5 
        Test if Exception is raised when battle mode is invalid
        """
        team_sample.team1.battle_mode = 7  # invalid battle mode
        team_sample.team1 = ArraySortedList(6)
        try:
            self.assertRaises(Exception, team_sample.access, team_sample.team1)
        except AssertionError:
            self.verificationErrors.append("access() method does not handle invalid battle_mode properly.")

    def test_return_to_team(self):
        """ Test case for return_to_team() method.
        Test 1: Test if ValueError is raised when ArrayADT if full
        Test 2: Test if ValueError is raised when returning item is not a valid Pokemon
        Test 3: Test if Pokemon is correctly returned to team in battle mode 0
        Test 4: Test if Pokemon is correctly returned to team in battle mode 1
        Test 5: Test if ValueError is raised when battle mode 2 is selected (Invalid battle_mode value)
        Test 6: Test if ValueError is raised when battle mode is invalid (Invalid battle_mode value, other than 2)
        """
        team_sample = TestBattle.b

        """ Test 1 
        Test if ValueError is raised when ArrayADT if full
        """
        team_sample.team1 = ArrayStack(3)
        # Array with size of 3 with 3 elements inside, so the array is full
        team_sample.team1.push(Charmander())
        team_sample.team1.push(Bulbasaur())
        team_sample.team1.push(Squirtle())
        try:
            self.assertRaises(ValueError, team_sample.return_to_team, team_sample.team1, Charmander())
        except AssertionError:
            self.verificationErrors.append("ValueError is not raised when ArrayADT if full")

        """ Test 2
        Test if ValueError is raised when returning item is not a valid Pokemon
        """
        team_sample.team1 = ArrayStack(4)
        # Array with size of 4 with 3 elements inside, so the array is not full
        team_sample.team1.push(Charmander())
        team_sample.team1.push(Bulbasaur())
        team_sample.team1.push(Squirtle())

        try:
            # Charmander here is String type instead of PokemonBase type
            self.assertRaises(ValueError, team_sample.return_to_team, team_sample.team1, "Charmander")
        except AssertionError:
            self.verificationErrors.append("ValueError is not raised when returning item is not a valid Pokemon")

        """ Test 3
        Test if Pokemon is correctly returned to team in battle mode 0
        """
        team_sample.battle_mode = 0
        # battle mode 0 selected
        team_sample.team1 = ArrayStack(6)
        team_sample.team1.push(Bulbasaur())
        team_sample.team1.push(Squirtle())
        team_sample.return_to_team(team_sample.team1, Charmander())
        try:
            self.assertEqual(str(
                team_sample.team1),
                "Charmander's HP = 7 and level = 1, Squirtle's HP = 8 and level = 1, Bulbasaur's HP = 9 and level = 1",
                "Pokemon did not return to team correctly")
        except AssertionError as e:
            self.verificationErrors.append(str(e))

        """ Test 4
        Test if Pokemon is correctly returned to team in battle mode 1
        """
        team_sample.team1 = CircularQueue(6)
        team_sample.set_battle_mode(1)
        # battle mode 1 selected
        team_sample.team1.append(Bulbasaur())
        team_sample.team1.append(Squirtle())
        team_sample.return_to_team(team_sample.team1, Charmander())

        try:
            self.assertEqual(str(
                team_sample.team1),
                "Bulbasaur's HP = 9 and level = 1, Squirtle's HP = 8 and level = 1, Charmander's HP = 7 and level = 1",
                "Pokemon did not return to team correctly")
        except AssertionError as e:
            self.verificationErrors.append(str(e))

        """ Test 5
        Test if ValueError is raised when battle mode 2 is selected
        """
        team_sample.set_battle_mode(2)
        # battle mode 2 selected
        team_sample.team1 = CircularQueue(6)
        team_sample.team1.append(Bulbasaur())
        team_sample.team1.append(Squirtle())
        try:
            self.assertRaises(ValueError, team_sample.return_to_team, team_sample.team1, Charmander)
        except AssertionError:
            self.verificationErrors.append("ValueError is not raised when battle mode 2 is selected")

        """ Test 6
        Test if ValueError is raised when battle mode is invalid
        """
        team_sample.battle_mode = 7
        # 7 is invalid battle mode
        team_sample.team1 = CircularQueue(6)
        team_sample.team1.append(Bulbasaur())
        team_sample.team1.append(Squirtle())
        try:
            self.assertRaises(ValueError, team_sample.return_to_team, team_sample.team1, Charmander)
        except AssertionError:
            self.verificationErrors.append("ValueError is not raised when battle mode is invalid")
            return

    def test_det_winner(self):
        """ Test Case for det_winner() method.
        Test 1: Test if Exception is raised when first param is invalid
        Test 2: Test if Exception is raised when second param is invalid
        Test 3: None is returned as both pokemon are not alive
        Test 4: The pokemon that is still alive is returned
        Test 5: Draw is returned as both pokemon are alive
        """

        """ Test 1
        Test if Exception is raised when first Pokemon parameter is invalid
        """
        b = TestBattle.Battle("John", "Wong")
        poke_lst = [['C1'], ['C1']]
        try:
            self.assertRaises(ValueError, b.det_winner, "Charmander", Charmander(), poke_lst, False)
        except AssertionError:
            self.verificationErrors.append("Exception is not raised when first Pokemon parameter is invalid")
            return

        """ Test 2
        Test if Exception is raised when second Pokemon parameter is invalid
        """
        try:
            self.assertRaises(Exception, b.det_winner, Charmander(), "Charmander", poke_lst, False)
        except AssertionError:
            self.verificationErrors.append("Exception is not raised when second Pokemon parameter is invalid")
            return

        """ Test 3
        None is returned as both pokemon are not alive
        """
        team = TestBattle.b
        # Test Case 1
        bu1, bu2 = Bulbasaur(), Bulbasaur()
        bu1.set_hp(1)
        bu2.set_hp(1)

        # team 1
        team.team1 = CircularQueue(1)
        team.team1.append(bu1)

        # team 2
        team.team2 = CircularQueue(1)
        team.team2.append(bu2)

        poke_lst = [['B1'], ['B1']]
        func_winner = team.det_winner(bu1, bu2, poke_lst)
        expected_winner = None

        try:
            self.assertEqual(func_winner, expected_winner, "Both Pokemons should have fainted.")
        except AssertionError as e:
            self.verificationErrors.append(str(e))

        """ Test 4 
        The pokemon that is still alive is returned
        """
        ch, bu = Charmander(), Bulbasaur()
        bu.set_hp(1)

        # team 1
        team.team1 = CircularQueue(1)
        team.team1.append(ch)

        # team 2
        team.team2 = CircularQueue(1)
        team.team2.append(bu)

        poke_lst = [['C1'], ['B1']]
        func_winner = team.det_winner(ch, bu, poke_lst)
        expected_winner = ch
        try:
            self.assertEqual(func_winner, expected_winner, "Bulbasaur should not be alive")
        except AssertionError as e:
            self.verificationErrors.append(str(e))

        """ Test 5 
        Draw is returned as both pokemon are alive
        """
        ch1 = Charmander()
        ch2 = Charmander()

        # team 1
        team.team1 = CircularQueue(1)
        team.team1.append(ch1)

        # team 2
        team.team2 = CircularQueue(1)
        team.team2.append(ch2)

        poke_lst = [['C1'], ['C1']]
        func_winner = team.det_winner(ch, ch, poke_lst)
        expected_winner = "Draw"
        try:
            self.assertEqual(func_winner, expected_winner, "Both Pokemon should be alive")
        except AssertionError as e:
            self.verificationErrors.append(str(e))

    def test_single_round_fight(self):
        """ Test Case for single_round_fight() method
        Test Case 1: Pokemon 1 is faster
        Test Case 2: Pokemon 2 is faster
        Test Case 3: Both Pokemon are equally fast
        Test Case 4: Invalid Pokemons
        """
        team = TestBattle.b

        """ Test Case 1
        Pokemon 1 is faster, Charmander should attack first
        """
        ch, bu = Charmander(), Bulbasaur()

        # team 1
        team.team1 = CircularQueue(1)
        ch.set_level(9)
        team.team1.append(ch)

        # team 2
        team.team2 = CircularQueue(1)
        team.team2.append(bu)

        poke_lst = [['C1'], ['B1']]
        team.single_round_fight(ch, bu, poke_lst)
        try:
            self.assertTrue(ch.hp == 7 and bu.hp == -21, "Charmander should attack first")
            # expected value of both Pokemon after battle
        except AssertionError as e:
            self.verificationErrors.append(str(e))

        """ Test Case 2
        Pokemon 2 is faster, Charmander should attack first
        """
        ch, bu = Charmander(), Bulbasaur()

        # team 1
        team.team1 = CircularQueue(1)
        team.team1.append(bu)

        # team 2
        ch.set_level(9)  # set higher level to get higher speed, so Charmander wil have greater speed the Bulbasaur
        team.team2 = CircularQueue(1)
        team.team2.append(ch)

        poke_lst = [['B1'], ['C1']]
        team.single_round_fight(bu, ch, poke_lst)
        try:
            self.assertTrue(ch.hp == 7 and bu.hp == -21, "Charmander should attack first")
            # expected value of both Pokemon after battle
        except AssertionError as e:
            self.verificationErrors.append(str(e))

        """ Test Case 3
        Both Pokemons have same speed
        """
        bu1, bu2 = Bulbasaur(), Bulbasaur()

        # team 1
        team.team1 = CircularQueue(2)
        team.team1.append(bu1)

        # team 2
        team.team2 = CircularQueue(2)
        team.team1.append(bu2)

        poke_lst = [['B1'], ['B1']]
        team.single_round_fight(bu1, bu2, poke_lst)

        try:
            self.assertTrue(bu1.hp == 6 and bu2.hp == 6, "Both Bulbasaur should attack together")
            # expected hp value of both Pokemon after battle
        except AssertionError as e:
            self.verificationErrors.append(str(e))

    def test_set_mode_battle(self):
        """ Test case for set_mode_battle() method.
        Test 1: Ash vs. Misty - Misty wins!
        Test 2: Ash vs. Misty - Ash wins!
        Test 3: Ash vs. Misty - Draw!
        Test 4: Ash vs. Misty - Ash wins! -- Battle with MissingNo!
        """
        from battle import Battle

        """ Test 1
        Ash vs. Misty - Misty wins!
        """
        # Instantiating Battle
        try:
            b = Battle("Ash", "Misty")
        except Exception as e:
            self.verificationErrors.append(f"Battle could not be instantiated: {str(e)}.")
            return

        # Executing battle
        try:
            with captured_output("0 1 0\n1 0 0") as (inp, out, err):
                # Here, Ash gets a Bulbasaur, and Misty gets a Charmander.
                result = b.set_mode_battle()
        except Exception as e:
            self.verificationErrors.append(f"Battle failed to execute: {str(e)}.")
            return

        # Comparing results
        try:
            self.assertEqual(result, "Misty", f'Misty should win: {result}.')
        except AssertionError as e:
            self.verificationErrors.append(str(e))

        """ Test 2
        Ash vs. Misty - Ash wins!
        """
        # Instantiating Battle
        try:
            b = Battle("Ash", "Misty")
        except Exception as e:
            self.verificationErrors.append(f"Battle could not be instantiated: {str(e)}.")
            return

        # Executing battle
        try:
            with captured_output("2 2 1\n0 2 1") as (inp, out, err):
                # Team 1: [C1, C2, B1, B2, S1]
                # Team 2: [B1, B2, S1]
                result = b.set_mode_battle()
        except Exception as e:
            self.verificationErrors.append(f"Battle failed to execute: {str(e)}.")
            return

        # Comparing results
        try:
            self.assertEqual(result, "Ash", f'Ash should win: {result}.')
        except AssertionError as e:
            self.verificationErrors.append(str(e))

        """ Test 3
        Ash vs. Misty - Draw!
        """
        # Instantiating Battle
        try:
            b = Battle("Ash", "Misty")
        except Exception as e:
            self.verificationErrors.append(f"Battle could not be instantiated: {str(e)}.")
            return

        # Executing battle
        try:
            with captured_output("1 1 1\n1 1 1") as (inp, out, err):
                # Team 1: [C1, B1, S1]
                # Team 2: [C1, B1, S1]
                result = b.set_mode_battle()
        except Exception as e:
            self.verificationErrors.append(f"Battle failed to execute: {str(e)}.")
            return

        # Comparing results
        try:
            self.assertEqual(result, "Draw", f'Battle should be a draw: {result}.')
        except AssertionError as e:
            self.verificationErrors.append(str(e))

        """ Test 4
        Battle with MissingNo!
        Ash vs. Misty - Ash wins!
        """
        # Instantiating Battle
        try:
            b = Battle("Ash", "Misty")
        except Exception as e:
            self.verificationErrors.append(f"Battle could not be instantiated: {str(e)}.")
            return

        # Executing Battle
        try:
            with captured_output("1 1 1 1\n1 1 1") as (inp, out, err):
                # Team 1: [C1, B1, S1, M1]
                # Team 2: [C1, B1, S1]
                result = b.set_mode_battle()
        except Exception as e:
            self.verificationErrors.append(f"Battle failed to execute: {str(e)}.")
            return

        # Comparing results
        try:
            self.assertEqual(result, "Ash", f'Ash should win: {result}.')
        except AssertionError as e:
            self.verificationErrors.append(str(e))

        # Comparing team after battle
        try:
            self.assertEqual(str(b.team1), "MissingNo's HP = 8 and level = 1", f"Team 1 is not correct after battle: {str(b.team1)}")
        except AssertionError as e:
            self.verificationErrors.append(str(e))

    def test_rotating_mode_battle(self):
        """ Test case for rotating_mode_battle() method.
        Test 1: Test case if Brock win
        Test 2: Test case if Gary win
        Test 3: Test case if Draw
        """
        from battle import Battle

        """ Test 1
        Test case if Brock win
        """
        # Instantiating Battle
        try:
            b = Battle("Brock", "Gary")
        except Exception as e:
            self.verificationErrors.append(f"Battle could not be instantiated: {str(e)}.")
            return

        # Executing Battle
        try:
            with captured_output("2 2 1\n0 2 1") as (inp, out, err):
                result = b.rotating_mode_battle()
        except Exception as e:
            self.verificationErrors.append(f"Battle failed to execute: {str(e)}.")
            return

        # Comparing results
        try:
            self.assertEqual(result, "Brock", f"Brock should win: {result}.")
        except AssertionError as e:
            self.verificationErrors.append(str(e))

        # Comparing team after battle
        try:
            self.assertEqual(str(
                b.team1),
                "Squirtle's HP = 8 and level = 1, Charmander's HP = 7 and level = 2, Charmander's HP = 7 and level = 2, Bulbasaur's HP = 7 and level = 1, Bulbasaur's HP = 8 and level = 2",
                f"Team 1 is not correct after battle: {str(b.team1)}")
        except AssertionError as e:
            self.verificationErrors.append(str(e))

        """ Test 2
        Test case if Gary win
        """
        # Executing Battle
        try:
            with captured_output("1 1 1\n2 2 2") as (inp, out, err):
                result = b.rotating_mode_battle()
        except Exception as e:
            self.verificationErrors.append(f"Battle failed to execute: {str(e)}.")
            return

        # Comparing results
        try:
            self.assertEqual(result, "Gary", f"Misty should win: {result}.")
        except AssertionError as e:
            self.verificationErrors.append(str(e))

        # Comparing team after battle
        try:
            self.assertEqual(str(
                b.team2),
                "Squirtle's HP = 8 and level = 1, Squirtle's HP = 8 and level = 1, Charmander's HP = 7 and level = 2, Bulbasaur's HP = 7 and level = 1, Bulbasaur's HP = 8 and level = 2",
                f"Team 2 is not correct after battle: {str(b.team2)}")
        except AssertionError as e:
            self.verificationErrors.append(str(e))

        """ Test 3
        Test case if Draw
        """
        # Executing Battle
        try:
            with captured_output("1 1 1\n1 1 1") as (inp, out, err):
                result = b.rotating_mode_battle()
        except Exception as e:
            self.verificationErrors.append(f"Battle failed to execute: {str(e)}.")
            return

        # Comparing results
        try:
            self.assertEqual(result, "Draw", f"Battle should be draw: {result}.")
        except AssertionError as e:
            self.verificationErrors.append(str(e))

        # Comparing team after battle
        try:
            self.assertTrue(b.team1.team.is_empty() and b.team2.team.is_empty(),
                            "Team 1 and Team 2 is not correct after battle.")
        except AssertionError as e:
            self.verificationErrors.append(str(e))

        """ Test 4
        Test if ValueError is Raised when invalid criterion input
        """
        try:
            self.assertRaises(ValueError, b.optimised_mode_battle, "invalid", "input")
        except AssertionError:
            self.verificationErrors.append("ValueError is not Raised when invalid criterion input")

    def test_optimised_mode_battle(self):
        """ Test case for optimised_mode_battle() method.
        Test 1: Test case if Ash win
        Test 2: Test case if Misty win
        Test 3: Test case if Draw
        Test 4: Test if ValueError is Raised when invalid criterion input
        """
        from battle import Battle

        """ Test 1
        Test case if Ash win
        """
        # Instantiating Battle
        try:
            b = Battle("Ash", "Misty")
        except Exception as e:
            self.verificationErrors.append(f"Battle could not be instantiated: {str(e)}.")
            return

        # Executing battle
        try:
            with captured_output("2 2 1\n0 2 1") as (inp, out, err):
                result = b.optimised_mode_battle("hp", "lvl")
        except Exception as e:
            self.verificationErrors.append(f"Battle failed to execute: {str(e)}.")
            return

        # Comparing results
        try:
            self.assertEqual(result, "Ash", f"Ash should win: {result}.")
        except AssertionError as e:
            self.verificationErrors.append(str(e))

        # Comparing team after battle
        try:
            self.assertEqual(str(
                b.team1),
                "Bulbasaur's HP = 6 and level = 1, Bulbasaur's HP = 5 and level = 2, Squirtle's HP = 2 and level = 1",
                f"Team 1 is not correct after battle: {str(b.team1)}")
        except AssertionError as e:
            self.verificationErrors.append(str(e))

        """ Test 2
        Test case if Misty win
        """
        # Executing battle
        try:
            with captured_output("1 1 1\n2 2 2") as (inp, out, err):
                result = b.optimised_mode_battle("hp", "lvl")
        except Exception as e:
            self.verificationErrors.append(f"Battle failed to execute: {str(e)}.")
            return

        # Comparing results
        try:
            self.assertEqual(result, "Misty", f"Misty should win: {result}.")
        except AssertionError as e:
            self.verificationErrors.append(str(e))

        # Comparing team after battle
        try:
            self.assertEqual(str(
                b.team2),
                "Bulbasaur's HP = 7 and level = 2, Bulbasaur's HP = 9 and level = 1, Squirtle's HP = 8 and level = 1, Squirtle's HP = 8 and level = 1",
                f"Team 2 is not correct after battle: {str(b.team2)}")
        except AssertionError as e:
            self.verificationErrors.append(str(e))

        """ Test 3
        Test case if Draw
        """
        # Executing battle
        try:
            with captured_output("0 0 1\n0 0 1") as (inp, out, err):
                result = b.optimised_mode_battle("hp", "lvl")
        except Exception as e:
            self.verificationErrors.append(f"Battle failed to execute: {str(e)}.")
            return

        # Comparing results
        try:
            self.assertEqual(result, "Draw", f"Battle should be draw: {result}.")
        except AssertionError as e:
            self.verificationErrors.append(str(e))

        # Comparing team after battle
        try:
            self.assertTrue(b.team1.team.is_empty() and b.team2.team.is_empty(),
                            "Team 1 and Team 2 is not correct after battle.")
        except AssertionError as e:
            self.verificationErrors.append(str(e))

        """ Test 4
        Test if ValueError is Raised when invalid criterion input
        """
        try:
            self.assertRaises(ValueError, b.optimised_mode_battle, "invalid", "input")
        except AssertionError:
            self.verificationErrors.append("ValueError is not Raised when invalid criterion input")


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestBattle)
    unittest.TextTestRunner(verbosity=0).run(suite)
