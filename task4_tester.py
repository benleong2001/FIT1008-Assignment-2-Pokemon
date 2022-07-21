import unittest

from tester_base import TesterBase, captured_output

class TestTask4(TesterBase):

    def test_battle_example(self):
        from battle import Battle

        try:
            b = Battle("Brock", "Gary")
        except Exception as e:
            self.verificationErrors.append(f"Battle could not be instantiated: {str(e)}.")
            return
        try:
            with captured_output("2 2 1\n0 2 1") as (inp, out, err):
                result = b.rotating_mode_battle()
        except Exception as e:
            self.verificationErrors.append(f"Battle failed to execute: {str(e)}.")
            return
        try:
            assert result == "Brock"
        except AssertionError:
            self.verificationErrors.append(f"Brock should win: {result}.")
        try:
            assert str(b.team1) == "Squirtle's HP = 8 and level = 1, Charmander's HP = 7 and level = 2, Charmander's HP = 7 and level = 2, Bulbasaur's HP = 7 and level = 1, Bulbasaur's HP = 8 and level = 2"
        except AssertionError:
            self.verificationErrors.append(f"Team 1 is not correct after battle: {str(b.team1)}")
    
    
    # Test case to check if AssertionError for pre-condition is raised correctly and if Pokemon is assigned correctly according to the input.
    def test_assign_team(self):
        from poke_team import PokeTeam
        
        b=PokeTeam("Ash")
        b.battle_mode=1
        
        charm=7  #put a large number to test if AssertionError is raised correctly
        bulb=2
        squir=1
        miss =1
        try:
            #check if pre condition is raised correctly
            self.assertRaises(AssertionError,b.assign_team,charm,bulb,squir,miss)
        except AssertionError:  
            self.verificationErrors.append(f"Invalid pre-condition for total number of Pokemon is not raised, number of Pokemon :{str(charm+bulb+squir+miss)}.")
        charm=2
        bulb=2
        squir=1
        miss =1
        b.assign_team(charm,bulb,squir,miss) 
        try:      
            #check if pokemon is assigned correctly according to their numbers

            assert str(b.team)=="Charmander's HP = 7 and level = 1, Charmander's HP = 7 and level = 1, Bulbasaur's HP = 9 and level = 1, Bulbasaur's HP = 9 and level = 1, Squirtle's HP = 8 and level = 1, MissingNo's HP = 8 and level = 1"
        except AssertionError:
            self.verificationErrors.append(f"Team is not correctly instantiated :{str(b.team)}.")


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestTask4)
    unittest.TextTestRunner(verbosity=0).run(suite)
