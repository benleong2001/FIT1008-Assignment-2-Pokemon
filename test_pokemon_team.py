import unittest

from tester_base import TesterBase, captured_output


class TestTask2(TesterBase):

    def test_limit(self):
        from poke_team import PokeTeam
        try:
            team = PokeTeam("Ash")
        except Exception as e:
            self.verificationErrors.append(f"Ash's team could not be instantiated: {str(e)}.")
            return
        try:
            with captured_output("4 4 1\n1 1 1") as (inp, out, err):
                # 4 4 1 should fail, since it is too many pokemon.
                # So 1 1 1 should be the correct team.
                team.choose_team(0, None)
        except Exception as e:
            self.verificationErrors.append(f"Ash's team could not be chosen: {str(e)}.")
            return
        output = out.getvalue().strip()

        # Check the prompt is being printed.
        try:
            assert "is the number of Charmanders" in output
            assert "is the number of Bulbasaurs" in output
            assert "is the number of Squirtles" in output
        except AssertionError:
            self.verificationErrors.append(f"PokeTeam does not print prompt correctly.")
        try:
            assert str(
                team) == "Charmander's HP = 7 and level = 1, Bulbasaur's HP = 9 and level = 1, Squirtle's HP = 8 and level = 1"
        except AssertionError:
            self.verificationErrors.append(f"PokeTeam does not handle limit correctly. {str(team)}")

    def test_set_trainer_name(self):
        """ Objective: To test the pre condition in set_trainer_name()

        test cases
        test_value = "Red"
        test_value = 1      # invalid
        test_value = True   # invalid
        test_value = 1.3    # invalid
        """
        from poke_team import PokeTeam
        # Instantiate object PokeTeam
        poke_team_object = PokeTeam("lee")

        # VALID TRAINER_NAME INPUT
        valid_test_value = "Ash"
        try:
            poke_team_object.set_trainer_name(valid_test_value)
        except Exception as e:
            self.verificationErrors.append(f"PokeTeam trainer_name could not be set: {str(e)}")

        # INVALID TRAINER_NAME INPUT
        invalid_test_value = 0
        try:
            self.assertRaises(TypeError, poke_team_object.set_trainer_name, invalid_test_value)
        except AssertionError:
            self.verificationErrors.append("set_trainer_name() method does not handle invalid input properly.")

    def test_set_battle_mode(self):
        """
        Objective: To test the pre condition in set_battle_mode()

        # test cases
        test_value = 0
        test_value = 1
        test_value = 2
        test_value = 1.5    # invalid
        test_value = True   # invalid
        test_value = "one"  # invalid

        """
        from poke_team import PokeTeam
        # instantiate object PokeTeam
        poke_team_object = PokeTeam("Lee")

        # VALID BATTLE_MODE VALUE
        for valid_test_value in [0, 1, 2]:
            try:
                poke_team_object.set_battle_mode(valid_test_value)
            except Exception as e:
                self.verificationErrors.append(f"PokeTeam battle_mode could not be set: {str(e)}.")

        # VALID BATTLE_MODE VALUE
        invalid_test_value = "one"
        try:
            self.assertRaises(TypeError, poke_team_object.set_trainer_name, invalid_test_value,
                              "set_battle_mode() method does not handle invalid input properly.")
        except AssertionError as e:
            self.verificationErrors.append(str(e))

    def test_set_criterion(self):
        """ Objective: To test the pre condition in set_criterion()

        # test cases
        valid_criterion_values = ["level", "lvl", "attack", "att", "att dmg", "attack damage", "health points", "speed", "defence"]

        test_value = 1.5    # invalid
        test_value = True   # invalid
        test_value = "one"  # invalid

        """
        from poke_team import PokeTeam
        # instantiate object PokeTeam
        poke_team_object = PokeTeam("Lee")

        # must first set battle mode to 2 to test
        poke_team_object.set_battle_mode(2)

        # VALID CRITERION VALUE
        valid_test_value = "hp"
        try:
            poke_team_object.set_criterion(valid_test_value)
        except Exception as e:
            self.verificationErrors.append(f"PokeTeam criterion could not be set: {str(e)}")

        # INVALID CRITERION VALUE
        invalid_test_value = True
        try:
            self.assertRaises(ValueError, poke_team_object.set_criterion, invalid_test_value)
        except AssertionError:
            self.verificationErrors.append("set_criterion() method does not handle invalid input properly.")

    def test_choose_team(self):
        from poke_team import PokeTeam
        from queue_adt import CircularQueue
        from stack_adt import ArrayStack
        from array_sorted_list import ArraySortedList
        """ Objective: To test the choose_team() method 
        Testing choose_team() request for input validity
        Test 1: Test if (c+b+s+m) can be < 1 or > 6
        Test 2: Test if the input can be other then int
        Test 3: Test the mode
        
        Test cases for c b s m 
            Description: c b s m acts as a sample input from the user in the terminal when the input() method is called.
            Format: c b s m     total = (c + b + s + m)

            # INVALID TEST CASES
            Reason: total > 6
                c b s m     total = (c + b + s + m)
                2 2 3 0       7

            Reason: total < 1
                c b s m     total = (c + b + s + m)
                0 0 0 0       0

            Reason: m > 1  
                c b s m     total = (c + b + s + m)
                0 0 0 2       2

            # VALID TEST CASE 
            Reason: 1 <= total <= 6 and 0 <= m <= 2
                c b s m     total = (c + b + s + m)
                2 2 1 1       6
            
            ** Since the actual code asks for user input, we can assume that c, b, s and m are in str format.
            ** Note: Also tested missing no
        """
        name1 = "Lee"

        # Instantiating PokeTeam object
        try:
            poke_team_object = PokeTeam(name1)
        except Exception as e:
            self.verificationErrors.append(f"PokeTeam object could not be instantiated: {str(e)}.")
            return

        """ Test cases for mode
        valid_modes = [0, 1, 2]
        invalid_modes = [3, -1, 2.0, "cool", True]
        """
        modes = [0, 1, 2]
        for mode in modes:
            valid_cbsm_input = "1 2 3 0"

            # if mode == 2 because mode 2 which is list, needs criteria
            if mode == 2:
                criteria = "hp"

                # Testing validity of input which is the limit of pokemons
                try:
                    with captured_output(valid_cbsm_input) as (inp, out, err):
                        poke_team_object.choose_team(mode, criteria)
                except Exception as e:
                    self.verificationErrors.append(f'input for mode {mode} was invalid: {str(e)}.')
                    return

            else:
                try:
                    with captured_output(valid_cbsm_input) as (inp, out, err):
                        poke_team_object.choose_team(mode)
                # if got Error
                except Exception as e:
                    self.verificationErrors.append(f'input for mode {mode} was invalid: {str(e)}.')
                    return

    def test_assign_team(self):
        from poke_team import PokeTeam
        from queue_adt import CircularQueue
        from stack_adt import ArrayStack
        from array_sorted_list import ArraySortedList

        name1 = "lee"

        # Instantiating PokeTeam object
        try:
            poke_team_object = PokeTeam(name1)
        except Exception as e:
            self.verificationErrors.append(f"PokeTeam object could not be instantiated: {str(e)}.")
            return

        # testing the input of assign_team()
        # Objective 1 : to test the criterion and mode
        for mode in [0, 1, 2]:
            try:
                # for assign team the battle mode must be set first
                # or its default value will be 0
                poke_team_object.set_battle_mode(mode)
                criteria = "hp"

                if poke_team_object.get_battle_mode() == 2:
                    poke_team_object.set_criterion(criteria)

                # testing assign_team() pre condtion
                try:
                    """ Test cases for c b s m 
                    Description: c b s m acts as a sample input from the user in the terminal when the input() method is called.
                    Format: c b s m     total = (c + b + s + m)
        
                    # INVALID TEST CASES
                    Reason: total > 6
                        c b s m     total = (c + b + s + m)
                        2 2 3 0       7
        
                    Reason: total < 1
                        c b s m     total = (c + b + s + m)
                        0 0 0 0       0
        
                    Reason: m > 1  
                        c b s m     total = (c + b + s + m)
                        0 0 0 2       2
        
                    # VALID TEST CASE 
                    Reason: 1 <= total <= 6 and 0 <= m <= 2
                        c b s m     total = (c + b + s + m)
                        2 2 1 1       6
                    
                    ** Unlike choose_team(), c, b, s and m are integer parameters, so they are not strings
                    ** Note: Also tested missing no
                    """
                    c, b, s, m = 1, 2, 3, 0
                    poke_team_object.assign_team(c, b, s, m)

                except Exception as e:
                    self.verificationErrors.append(f"Failed to assign PokeTeam team: {str(e)}.")
                    return

            # if there was an error
            except Exception as e:
                self.verificationErrors.append(f"PokeTeam assign_team() test failed: {str(e)}.")
                return

        # to test if mode = 0, it must be ArrayStack
        if poke_team_object.get_battle_mode() == 0:
            try:
                self.assertTrue(isinstance(poke_team_object.team, ArrayStack), "mode 0 did not instantiate ArrayStack for PokeTeam.team")
            except AssertionError as e:
                self.verificationErrors.append(str(e))
                return

        # to test if I select mode 1 ,it must be CircularQueue
        elif poke_team_object.get_battle_mode() == 1:
            try:
                self.assertTrue(isinstance(poke_team_object.team, CircularQueue), "mode 1 did not instantiate CircularQueue for PokeTeam.team")
            except AssertionError as e:
                self.verificationErrors.append(str(e))
                return


        # to test if I select mode 2 ,it must be ArraySortedList
        elif poke_team_object.get_battle_mode() == 2:
            try:
                self.assertTrue(isinstance(poke_team_object.team, ArraySortedList), "mode 2 did not instantiate ArraySortedList for PokeTeam.team")
            except AssertionError as e:
                self.verificationErrors.append(str(e))
                return


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestTask2)
    unittest.TextTestRunner(verbosity=0).run(suite)
