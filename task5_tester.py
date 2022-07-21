import unittest

from tester_base import TesterBase, captured_output

class TestTask4(TesterBase):

    def test_battle_example(self):
        from battle import Battle

        try:
            b = Battle("Cynthia", "Steven")
        except Exception as e:
            self.verificationErrors.append(f"Battle could not be instantiated: {str(e)}.")
            return
        try:
            with captured_output("2 2 1\n0 2 1") as (inp, out, err):
                result = b.optimised_mode_battle("hp", "lvl")
        except Exception as e:
            self.verificationErrors.append(f"Battle failed to execute: {str(e)}.")
            return
        try:
            # Gen IV supremacy >:D
            assert result == "Cynthia"
        except AssertionError:
            self.verificationErrors.append(f"Cynthia should win: {result}.")
        try:
            assert str(b.team1) == "Bulbasaur's HP = 6 and level = 1, Bulbasaur's HP = 5 and level = 2, Squirtle's HP = 2 and level = 1"
        except AssertionError:
            self.verificationErrors.append(f"Team 1 is not correct after battle: {str(b.team1)}")
    
    # Test Case to test if Pre-condition of criterion is raised correctly in task 5 for method assign_team
    def test_assign_team(self):
        from poke_team import PokeTeam
        
        b=PokeTeam("Ash")
        b.battle_mode=2
        b.criterion="helloworld" # purposely put string not included in criterion to test if Exception is raised
        
        charm=2
        bulb=2
        squir=1
        miss =1
        try:
            #check if invalid pre-condition is raised correctly
            self.assertRaises(ValueError,b.assign_team,charm,bulb,squir,miss)
        except ValueError:  
            self.verificationErrors.append(f"Invalid criterion not raised correctly :{str(b.criterion)}.")

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestTask4)
    unittest.TextTestRunner(verbosity=0).run(suite)
