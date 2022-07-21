import unittest

from pokemon_base import PokemonBase
from tester_base import TesterBase

from random import *

class TestTask1(TesterBase):

    def test_charmander_string(self):
        from pokemon import Charmander
        try:
            c = Charmander()
        except Exception as e:
            self.verificationErrors.append(f"Charmander could not be instantiated: {str(e)}.")
            return
        try:
            s = str(c)
            if s != "Charmander's HP = 7 and level = 1":
                self.verificationErrors.append(f"String method did not return correct string: {s}")
        except Exception as e:
            self.verificationErrors.append(f"String method failed. {e}")

    ### ADD TESTS HERE

    def test_bulbasaur_string(self):
        from pokemon import Bulbasaur
        try:
            c = Bulbasaur()
        except Exception as e:
            self.verificationErrors.append(f"Bulbasaur could not be instantiated: {str(e)}.")
            return
        try:
            s = str(c)
            if s != "Bulbasaur's HP = 9 and level = 1":
                self.verificationErrors.append(f"String method did not return correct string: {s}")
        except Exception as e:
            self.verificationErrors.append(f"String method failed. {e}")

    def test_squirtle_string(self):
        from pokemon import Squirtle
        try:
            c = Squirtle()
        except Exception as e:
            self.verificationErrors.append(f"Squirtle could not be instantiated: {str(e)}.")
            return
        try:
            s = str(c)
            if s != "Squirtle's HP = 8 and level = 1":
                self.verificationErrors.append(f"String method did not return correct string: {s}")
        except Exception as e:
            self.verificationErrors.append(f"String method failed. {e}")






    def test_calc_damage_assertion(self):
        from pokemon import Charmander,Bulbasaur,Squirtle
        """
        Objective: This method test calc_damage() pre condition
        
        # test cases
        test_value = "hello"    # invalid
        test_value = 10         # invalid
        test_value = 10.5       # invalid
        test_value = True       # invalid
        
        """

        # can use any of these
        test_value = Charmander()
        # test_value = Bulbasaur()
        # test_value = Squirtle()
        try:
            # instantiate
            c = Charmander()

            # test
            c.calc_dmg(test_value)
        except Exception as e:
            self.verificationErrors.append(
                "Charmander.calc_damage() has wrong parameter type:")



        try:
            # instantiate
            b = Bulbasaur()

            # test
            b.calc_dmg(test_value)
        except Exception as e:
            self.verificationErrors.append(
                "Bulbasaur.calc_damage() has wrong parameter type:")



        try:
            # instantiate
            s = Squirtle()

            # test
            s.calc_dmg(test_value)
        except Exception as e:
            self.verificationErrors.append(
                "Squirtle.calc_damage() has wrong parameter type:")



    def test_set_level_assertion(self):
        from pokemon import Charmander, Bulbasaur, Squirtle
        """
        Objective: This method test set_level() pre condition

        # test cases
        test_value = 20
        test_value = "hello"    # invalid
        test_value = 10.5       # invalid
        test_value = True       # invalid

        """

        test_value = 10
        try:
            # instantiate
            c = Charmander()

            # test
            c.set_level(test_value)
        except Exception as e:
            self.verificationErrors.append(
                "Charmander.set_level() has wrong parameter type:")

        try:
            # instantiate
            b = Bulbasaur()

            # test
            b.set_level(test_value)
        except Exception as e:
            self.verificationErrors.append(
                "Bulbasaur.set_level() has wrong parameter type:")

        try:
            # instantiate
            s = Squirtle()

            # test
            s.set_level(test_value)
        except Exception as e:
            self.verificationErrors.append(
                "Squirtle.set_level() has wrong parameter type:")





    def test_set_hp_assertion(self):
        from pokemon import Charmander, Bulbasaur, Squirtle
        """
        Objective: This method test set_hp() pre condition

        # test cases
        test_value = 20
        test_value = "hello"    # invalid
        test_value = 10.5       
        test_value = True       # invalid

        """

        test_value = 10
        try:
            # instantiate
            c = Charmander()

            # test
            c.set_hp(test_value)
        except Exception as e:
            self.verificationErrors.append(
                "Charmander.set_hp() has wrong parameter type:")

        try:
            # instantiate
            b = Bulbasaur()

            # test
            b.set_hp(test_value)
        except Exception as e:
            self.verificationErrors.append(
                "Bulbasaur.set_hp() has wrong parameter type:")

        try:
            # instantiate
            s = Squirtle()

            # test
            s.set_hp(test_value)
        except Exception as e:
            self.verificationErrors.append(
                "Squirtle.set_hp() has wrong parameter type:")





    def test_set_poke_type_assertion(self):
        from pokemon import Charmander, Bulbasaur, Squirtle
        """
        Objective: This method test set_poke_type() pre condition

        # test cases # 
        test_value = "Grass"
        test_value = "Water"
        test_value = "hello"    # invalid
        test_value = 10.5       # invalid
        test_value = True       # invalid

        """

        test_value = "Fire"

        try:
            # instantiate
            c = Charmander()

            # test
            c.set_poke_type(test_value)
        except Exception as e:
            self.verificationErrors.append(
                "Charmander.set_poke_type() has wrong parameter type:")

        try:
            # instantiate
            b = Bulbasaur()

            # test
            b.set_poke_type(test_value)
        except Exception as e:
            self.verificationErrors.append(
                "Bulbasaur.set_poke_type() has wrong parameter type:")

        try:
            # instantiate
            s = Squirtle()

            # test
            s.set_poke_type(test_value)
        except Exception as e:
            self.verificationErrors.append(
                "Squirtle.set_poke_type() has wrong parameter type:")



    def test_is_alive(self):
        from pokemon import Charmander, Bulbasaur, Squirtle
        """
        Objective: This method is to test is_alive() 

        # test cases #
        test_value = 0
        test_value = 1          
        test_value = "hello"    # invalid
        test_value = 10.5       # invalid 
        test_value = True       # invalid

        """

        test_value = 1
        try:
            # instantiate
            c = Charmander()

            # need to set the hp to test is_alive()
            try:
                c.set_hp(test_value)
            except Exception as e:
                raise ValueError("Charmander.set_hp() invalid paramater ")

            # test
            if test_value == 0 and c.is_alive() == True:
                raise Exception("Charmander.is_alive() returned the wrong is_alive()")
            elif test_value > 0 and c.is_alive() == False:
                raise Exception("Charmander.is_alive() returned the wrong is_alive()")

        # to handle set_hp() invalid
        except ValueError:
            self.verificationErrors.append(
                "Squirtle.set_hp() invalid paramater")

        # to handle is_alive() invalid
        except Exception as e:
            self.verificationErrors.append(
                "Charmander.is_alive() returned the wrong is_alive()")

        try:
            # instantiate
            b = Bulbasaur()

            # need to set the hp to test is_alive()
            try:
                b.set_hp(test_value)
            except Exception as e:
                raise ValueError("Bulbasaur.set_hp() invalid paramater ")

            # test
            if test_value == 0 and b.is_alive() == True:
                raise Exception("Bulbasaur.is_alive() returned the wrong is_alive()")
            elif test_value > 0 and b.is_alive() == False:
                raise Exception("Bulbasaur.is_alive() returned the wrong is_alive()")

        # to handle set_hp() invalid
        except ValueError:
            self.verificationErrors.append(
                "Squirtle.set_hp() invalid paramater")

        # to handle is_alive() invalid
        except Exception as e:
            self.verificationErrors.append(
                "Bulbasaur.is_alive() returned the wrong is_alive()")

        try:
            # instantiate
            s = Squirtle()

            # need to set the hp to test is_alive()
            try:
                s.set_hp(test_value)
            except Exception as e:
                raise ValueError("Squirtle.set_hp() invalid paramater ")

            # test
            if test_value == 0 and s.is_alive() == True:
                raise Exception("Squirtle.is_alive() returned the wrong is_alive()")
            elif test_value > 0 and s.is_alive() == False:
                raise Exception("Squirtle.is_alive() returned the wrong is_alive()")

        # to handle set_hp() invalid
        except ValueError:
            self.verificationErrors.append(
                "Squirtle.set_hp() invalid paramater")

        # to handle is_alive() invalid
        except Exception as e:
            self.verificationErrors.append(
                "Squirtle.is_alive() returned the wrong is_alive()")





    def test_get_attack(self):
        from pokemon import Charmander, Bulbasaur, Squirtle
        """
        Objective: This method is to test get_attack() 

        # test cases #
        test_value = 0
        test_value = 1          
        test_value = "hello"    # invalid
        test_value = 10.5       # invalid 
        test_value = True       # invalid

        """

        test_value = 1
        try:
            # instantiate
            c = Charmander()

            # can set the level to test get_attack()
            try:
                c.set_level(test_value)
            except Exception as e:
                raise ValueError("Charmander.set_level() invalid paramater ")

            # test
            if c.get_attack() != (6 + test_value):
                raise Exception("Charmander.get_attack() returned the wrong get_attack()")


        # to handle set_hp() invalid
        except ValueError:
            self.verificationErrors.append(
                "Squirtle.set_level() invalid paramater")

        # to handle is_alive() invalid
        except Exception as e:
            self.verificationErrors.append(
                "Charmander.get_attack() returned the wrong get_attack()")



        try:
            # instantiate
            b = Bulbasaur()

            # can set the level to test get_attack()
            try:
                b.set_level(test_value)
            except Exception as e:
                raise ValueError("Bulbasaur.set_level() invalid paramater ")

            # test
            if b.get_attack() != 5:
                raise Exception("Bulbasaur.get_attack() returned the wrong get_attack()")


        # to handle set_hp() invalid
        except ValueError:
            self.verificationErrors.append(
                "Squirtle.set_level() invalid paramater")

        # to handle is_alive() invalid
        except Exception as e:
            self.verificationErrors.append(
                "Bulbasaur.get_attack() returned the wrong get_attack()")



        try:
            # instantiate
            s = Squirtle()

            # can set the level to test get_attack()
            try:
                s.set_level(test_value)
            except Exception as e:
                raise ValueError("Squirtle.set_level() invalid paramater ")

            # test
            if s.get_attack() != (4 + (test_value // 2)):
                raise Exception("Squirtle.get_attack() returned the wrong get_attack()")


        # to handle set_hp() invalid
        except ValueError:
            self.verificationErrors.append(
                "Squirtle.set_level() invalid paramater")

        # to handle is_alive() invalid
        except Exception as e:
            self.verificationErrors.append(
                "Squirtle.get_attack() returned the wrong get_attack()")

            def test_get_attack(self):
                from pokemon import Charmander, Bulbasaur, Squirtle
                """
                Objective: This method is to test get_attack() 

                # test cases #
                test_value = 1          
                test_value = "hello"    # invalid
                test_value = 10.5       # invalid 
                test_value = True       # invalid

                """

                test_value = 1
                try:
                    # instantiate
                    c = Charmander()

                    # can set the level to test get_attack()
                    try:
                        c.set_level(test_value)
                    except Exception as e:
                        raise ValueError("Charmander.set_level() invalid paramater ")

                    # test
                    if c.get_attack() != (6 + test_value):
                        raise Exception("Charmander.get_attack() returned the wrong get_attack()")


                # to handle set_level() invalid
                except ValueError:
                    self.verificationErrors.append(
                        "Squirtle.set_level() invalid paramater")

                # to handle get_attack() invalid
                except Exception as e:
                    self.verificationErrors.append(
                        "Charmander.get_attack() returned the wrong get_attack()")

                try:
                    # instantiate
                    b = Bulbasaur()

                    # can set the level to test get_attack()
                    try:
                        b.set_level(test_value)
                    except Exception as e:
                        raise ValueError("Bulbasaur.set_level() invalid paramater ")

                    # test
                    if b.get_attack() != 5:
                        raise Exception("Bulbasaur.get_attack() returned the wrong get_attack()")


                # to handle set_level() invalid
                except ValueError:
                    self.verificationErrors.append(
                        "Squirtle.set_level() invalid paramater")

                # to handle get_attack() invalid
                except Exception as e:
                    self.verificationErrors.append(
                        "Bulbasaur.get_attack() returned the wrong get_attack()")

                try:
                    # instantiate
                    s = Squirtle()

                    # can set the level to test get_attack()
                    try:
                        s.set_level(test_value)
                    except Exception as e:
                        raise ValueError("Squirtle.set_level() invalid paramater ")

                    # test
                    if s.get_attack() != (4 + (test_value // 2)):
                        raise Exception("Squirtle.get_attack() returned the wrong get_attack()")


                # to handle set_level() invalid
                except ValueError:
                    self.verificationErrors.append(
                        "Squirtle.set_level() invalid paramater")

                # to handle get_attack() invalid
                except Exception as e:
                    self.verificationErrors.append(
                        "Squirtle.get_attack() returned the wrong get_attack()")




    def test_get_defence(self):
        from pokemon import Charmander, Bulbasaur, Squirtle
        """
        Objective: This method is to test get_defence() 

        # test cases #
        test_value = 1          
        test_value = "hello"    # invalid
        test_value = 10.5       # invalid 
        test_value = True       # invalid

        """

        test_value = 1
        try:
            # instantiate
            c = Charmander()

            # can set the level to test get_attack()
            try:
                c.set_level(test_value)
            except Exception as e:
                raise ValueError("Charmander.set_level() invalid paramater ")

            # test
            if c.get_defence() != 4:
                raise Exception("Charmander.get_defence() returned the wrong get_defence()")


        # to handle set_level() invalid
        except ValueError:
            self.verificationErrors.append(
                "Squirtle.set_level() invalid paramater")

        # to handle get_defence() invalid
        except Exception as e:
            self.verificationErrors.append(
                "Charmander.get_defence() returned the wrong get_defence()")



        try:
            # instantiate
            b = Bulbasaur()

            # can set the level to test get_attack()
            try:
                b.set_level(test_value)
            except Exception as e:
                raise ValueError("Bulbasaur.set_level() invalid paramater ")

            # test
            if b.get_defence() != 5:
                raise Exception("Bulbasaur.get_defence() returned the wrong get_defence()")


        # to handle set_level() invalid
        except ValueError:
            self.verificationErrors.append(
                "Squirtle.set_level() invalid paramater")

        # to handle get_defence() invalid
        except Exception as e:
            self.verificationErrors.append(
                "Bulbasaur.get_defence() returned the wrong get_defence()")



        try:
            # instantiate
            s = Squirtle()

            # can set the level to test get_attack()
            try:
                s.set_level(test_value)
            except Exception as e:
                raise ValueError("Squirtle.set_level() invalid paramater ")

            # test
            if s.get_defence() != (6 + test_value):
                raise Exception("Squirtle.get_defence() returned the wrong get_defence()")


        # to handle set_level() invalid
        except ValueError:
            self.verificationErrors.append(
                "Squirtle.set_level() invalid paramater")

        # to handle get_defence() invalid
        except Exception as e:
            self.verificationErrors.append(
                "Squirtle.get_defence() returned the wrong get_defence()")





    def test_get_speed(self):
        from pokemon import Charmander, Bulbasaur, Squirtle
        """
        Objective: This method is to test get_speed() 

        # test cases #
        test_value = 1          
        test_value = "hello"    # invalid
        test_value = 10.5       # invalid 
        test_value = True       # invalid

        """

        test_value = 1
        try:
            # instantiate
            c = Charmander()

            # can set the level to test get_speed()
            try:
                c.set_level(test_value)
            except Exception as e:
                raise ValueError("Charmander.set_level() invalid paramater ")

            # test
            if c.get_speed() != (7 + test_value):
                raise Exception("Charmander.get_speed() returned the wrong get_speed()")


        # to handle set_level() invalid
        except ValueError:
            self.verificationErrors.append(
                "Squirtle.set_level() invalid paramater")

        # to handle get_defence() invalid
        except Exception as e:
            self.verificationErrors.append(
                "Charmander.get_speed() returned the wrong get_speed()")



        try:
            # instantiate
            b = Bulbasaur()

            # can set the level to test get_speed()
            try:
                b.set_level(test_value)
            except Exception as e:
                raise ValueError("Bulbasaur.set_level() invalid paramater ")

            # test
            if b.get_speed() != (7 + (test_value//2)):
                raise Exception("Bulbasaur.get_speed() returned the wrong get_speed()")


        # to handle set_level() invalid
        except ValueError:
            self.verificationErrors.append(
                "Squirtle.set_level() invalid paramater")

        # to handle get_speed() invalid
        except Exception as e:
            self.verificationErrors.append(
                "Bulbasaur.get_speed() returned the wrong get_speed()")



        try:
            # instantiate
            s = Squirtle()

            # can set the level to test get_attack()
            try:
                s.set_level(test_value)
            except Exception as e:
                raise ValueError("Squirtle.set_level() invalid paramater ")

            # test
            if s.get_speed() != 7:
                raise Exception("Squirtle.get_speed() returned the wrong get_speed()")


        # to handle set_level() invalid
        except ValueError:
            self.verificationErrors.append(
                "Squirtle.set_level() invalid paramater")

        # to handle get_defence() invalid
        except Exception as e:
            self.verificationErrors.append(
                "Squirtle.get_speed() returned the wrong get_speed()")




    def test_abstract_class(self):
        from pokemon import Charmander, Bulbasaur, Squirtle
        """
        Objective:  to test wheter the methods from the abstract class
                    can be called or not 
                    as in to check the pre conditions of the abstract methods
        """
        c = Charmander()

        # test usage of abstract method get_attack()
        try:
            PokemonBase.get_attack(c)
        except Exception as e:
            self.verificationErrors.append(
                f"{str(e)}")

        # test usage of abstract method get_defence()
        try:
            PokemonBase.get_defence(c)
        except Exception as e:
            self.verificationErrors.append(
                f"{str(e)}")


        # test usage of abstract method get_speed()
        try:
            PokemonBase.get_speed(c)
        except Exception as e:
            self.verificationErrors.append(
                f"{str(e)}")


        # test usage of abstract method calc_dmg()
        b = Bulbasaur()
        try:
            PokemonBase.calc_dmg(c,b)
        except Exception as e:
            self.verificationErrors.append(
                f"{str(e)}")


    def test_consistency_all_method(self):
        """
        objective:  to test consistency of all methods created in pokemon class and pokemon_base which was
                    inherited.
        """
        from pokemon import Charmander, Bulbasaur, Squirtle
        # these are the list of pokemons
        pokemon_list_1 = []
        pokemon_list_2 = []

        # adding charmander to the lists of pokemons
        c1 = Charmander()
        pokemon_list_1.append(c1)

        c2 = Charmander()
        pokemon_list_2.append(c2)

        # adding bulbasaur to the lists of pokemons
        b1 = Bulbasaur()
        pokemon_list_1.append(b1)

        b2 = Bulbasaur()
        pokemon_list_2.append(b2)

        # addint squirtle to the list of pokemons
        s1 = Squirtle()
        pokemon_list_1.append(s1)

        s2 = Squirtle()
        pokemon_list_2.append(s2)


        # pokemon_list_1 = [c1,b1,s1]
        # pokemon_list_2 = [c2,b2,s2]

        # appending all the methods in the pokemons_base and pokemon file
        methods = []

        # pokemon_base class
        methods.append("get_level")
        methods.append("get_hp")
        methods.append("get_poke_type")

        # pokemon class
        methods.append("get_attack")
        methods.append("get_defence")
        methods.append("get_speed")
        methods.append("calc_dmg")

        # methods = ["get_level","get_hp","get_poke_type","get_attack","get_defence","get_speed","calc_dmg"]

        # to iterate over all methods
        for method_name in methods:

            # to iterate over all pokemons in pokemon_list_1
            for pokemon_1 in pokemon_list_1:

                # to iterate over all pokemons in pokemon_list_2
                for pokemon_2 in pokemon_list_2:

                    # to test the consistency of all methods by iterating a certain amount of times
                    for _ in range(10):

                        # to declare and initialize the variables which will be used to
                        # set the level
                        random_level_pokemon_1 = 1
                        random_level_pokemon_2 = 1

                        # to add a variety of testing by selecting different combinations of leveling
                        # 1 is for pokemon 1 to have a different level
                        # 2 is for pokemon 2 to have a different level
                        # 3 is for both pokemons to be of a certain level
                        random_level_picker = randint(1,3)

                        # used to decide the domain of the random int
                        level_from = 1
                        level_to = 6

                        if random_level_picker == 1:

                            # to set pokemon_1 to a certain level
                            random_level_pokemon_1 = randint(level_from, level_to)
                            pokemon_1.set_level(random_level_pokemon_1)

                        elif random_level_picker == 2:
                            # to set pokemon_1 to level 1
                            pokemon_1.set_level(random_level_pokemon_1)

                            # to set pokemon_2 to a certain level
                            random_level_pokemon_2 = randint(level_from, level_to)
                            pokemon_2.set_level(random_level_pokemon_2)

                        else:
                            # to set pokemon_1 to a certain level
                            random_level_pokemon_1 = randint(level_from, level_to)
                            pokemon_1.set_level(random_level_pokemon_1)

                            # to set pokemon_2 to a certain level
                            random_level_pokemon_2 = randint(level_from, level_to)
                            pokemon_2.set_level(random_level_pokemon_2)


                        # testing get_level()
                        if method_name == "get_level":
                            """
                            Objective: to test the get_level() and set_level() 
                            """

                            # if pokemon 1 is charmander
                            if isinstance(pokemon_1, Charmander):

                                # if level is not the set value
                                if pokemon_1.get_level() != random_level_pokemon_1:
                                    self.verificationErrors.append(
                                        f"charmander.get_level() method did not return correct get_level: {pokemon_1.get_level()}")


                            # if pokemon 1 is Bulbasaur
                            elif isinstance(pokemon_1, Bulbasaur):

                                # if level is not the set value
                                if pokemon_1.get_level() != random_level_pokemon_1:
                                    self.verificationErrors.append(
                                        f"bulbasaur.get_level() method did not return correct get_level: {pokemon_1.get_level()}")


                            # if pokemon 1 is Squirtle
                            elif isinstance(pokemon_1, Squirtle):

                                # if level is not the set value
                                if pokemon_1.get_level() != random_level_pokemon_1:
                                    self.verificationErrors.append(
                                        f"squirtle.get_level() method did not return correct get_level: {pokemon_1.get_level()}")



                        # testing get_hp()
                        elif method_name == "get_hp":
                            """
                            objective: testing get_hp() and set_hp()
                            """

                            # if pokemon 1 is charmander
                            if isinstance(pokemon_1, Charmander):

                                # if hp is not the same as default value
                                if pokemon_1.get_hp() != 7:
                                    self.verificationErrors.append(
                                        f"charmander.get_hp() method did not return correct get_hp: {pokemon_1.get_hp()}")

                                # testing set_hp()
                                random_hp_pokemon = randint(1, 10)
                                pokemon_1.set_hp(random_hp_pokemon)

                                # if hp is not the same as random_hp_pokemon
                                if pokemon_1.get_hp() != random_hp_pokemon:
                                    self.verificationErrors.append(
                                        f"charmander.get_hp() method did not return correct get_hp: {pokemon_1.get_hp()}")

                                # resetting the hp for future test
                                pokemon_1.set_hp(7)


                            # if pokemon 1 is Bulbasaur
                            elif isinstance(pokemon_1, Bulbasaur):

                                # if hp is not the same as the default value
                                if pokemon_1.get_hp() != 9:
                                    self.verificationErrors.append(
                                        f"bulbasaur.get_hp() method did not return correct get_hp: {pokemon_1.get_hp()}")

                                # testing set_hp()
                                random_hp_pokemon = randint(1, 10)
                                pokemon_1.set_hp(random_hp_pokemon)

                                # if hp is not the same as random_hp_pokemon
                                if pokemon_1.get_hp() != random_hp_pokemon:
                                    self.verificationErrors.append(
                                        f"bulbasaur.get_hp() method did not return correct get_hp: {pokemon_1.get_hp()}")

                                # resetting the hp for future test
                                pokemon_1.set_hp(9)


                            # if pokemon 1 is Squirtle
                            elif isinstance(pokemon_1, Squirtle):

                                # if hp is not the same as the default value
                                if pokemon_1.get_hp() != 8:
                                    self.verificationErrors.append(
                                        f"squirtle.get_hp() method did not return correct get_hp: {pokemon_1.get_hp()}")

                                # testing set_hp()
                                random_hp_pokemon = randint(1, 10)
                                pokemon_1.set_hp(random_hp_pokemon)

                                # if hp is not the given value
                                if pokemon_1.get_hp() != random_hp_pokemon:
                                    self.verificationErrors.append(
                                        f"squirtle.get_hp() method did not return correct get_hp: {pokemon_1.get_hp()}")

                                # resetting the hp for future test
                                pokemon_1.set_hp(8)



                        # testing get_poke_type()
                        elif method_name == "get_poke_type":
                            """
                            objective: to test the get_poke_type() and set_poke_type() 
                            """

                            # if pokemon 1 is charmander
                            if isinstance(pokemon_1, Charmander):

                                # if poke_type is not the one given in the specification
                                if pokemon_1.get_poke_type() != "Fire":
                                    self.verificationErrors.append(
                                        f"charmander.get_poke_type() method did not return correct get_poke_type: {pokemon_1.get_poke_type()}")

                                # testing set_poke_type()
                                test_value = "Water"
                                pokemon_1.set_poke_type(test_value)

                                # if poke_type is not the same as the test_value
                                if pokemon_1.get_poke_type() != test_value:
                                    self.verificationErrors.append(
                                        f"charmander.get_poke_type() method did not return correct get_poke_type: {pokemon_1.get_poke_type()}")

                                # to reset the poke_type for future test
                                pokemon_1.set_poke_type("Fire")


                            # if pokemon 1 is Bulbasaur
                            elif isinstance(pokemon_1, Bulbasaur):

                                # if poke_type is not the one given in the specification
                                if pokemon_1.get_poke_type() != "Grass":
                                    self.verificationErrors.append(
                                        f"bulbasaur.get_poke_type() method did not return correct get_poke_type: {pokemon_1.get_poke_type()}")

                                # testing set_poke_type()
                                test_value = "Fire"
                                pokemon_1.set_poke_type(test_value)

                                # if poke_type is not the same as the test_value
                                if pokemon_1.get_poke_type() != test_value:
                                    self.verificationErrors.append(
                                        f"bulbasaur.get_poke_type() method did not return correct get_poke_type: {pokemon_1.get_poke_type()}")

                                # to reset the poke_type for future test
                                pokemon_1.set_poke_type("Grass")


                            # if pokemon 1 is Squirtle
                            elif isinstance(pokemon_1, Squirtle):

                                # if poke_type is not the one given in the specification
                                if pokemon_1.get_poke_type() != "Water":
                                    self.verificationErrors.append(
                                        f"squirtle.get_poke_type() method did not return correct get_poke_type: {pokemon_1.get_poke_type()}")

                                # testing set_poke_type()
                                test_value = "Grass"
                                pokemon_1.set_poke_type(test_value)

                                # if poke_type is not the same as the test_value
                                if pokemon_1.get_poke_type() != test_value:
                                    self.verificationErrors.append(
                                        f"squirtle.get_poke_type() method did not return correct get_poke_type: {pokemon_1.get_poke_type()}")

                                # to reset the poke_type for future test
                                pokemon_1.set_poke_type("Water")



                        # testing get_attack()
                        elif method_name == "get_attack":
                            """
                            objective: to test get_attack()
                            """

                            # if pokemon 1 is Charmander
                            if isinstance(pokemon_1, Charmander):

                                # if attack is not the default value + random_level_pokemon_1
                                if pokemon_1.get_attack() != (6 + random_level_pokemon_1):
                                    self.verificationErrors.append(
                                        f"charmander.get_attack() method did not return correct get_attack: {pokemon_1.get_attack()}")

                            # if pokemon 1 is Bulbasaur
                            elif isinstance(pokemon_1, Bulbasaur):

                                # if attack is not the default value + random_level_pokemon_1
                                if pokemon_1.get_attack() != (5):
                                    self.verificationErrors.append(
                                        f"bulbasaur.get_attack() method did not return correct get_attack: {pokemon_1.get_attack()}")


                            # if pokemon 1 is Squirtle
                            elif isinstance(pokemon_1, Squirtle):

                                # if attack is not the default value + random_level_pokemon_1
                                if pokemon_1.get_attack()!= (4 + (random_level_pokemon_1 // 2)):
                                    self.verificationErrors.append(
                                        f"squirtle.get_attack() method did not return correct get_attack: {pokemon_1.get_attack()}")



                        # testing get_defence()
                        elif method_name == "get_defence":
                            """
                            objective: to test get_defence()
                            """

                            # if pokemon 1 is Charmander
                            if isinstance(pokemon_1, Charmander):

                                # if defence is not the default value
                                if pokemon_1.get_defence() != 4:
                                    self.verificationErrors.append(
                                        f"charmander.get_defence() method did not return correct get_defence: {pokemon_1.get_defence()}")

                            # if pokemon 1 is Bulbasaur
                            elif isinstance(pokemon_1, Bulbasaur):

                                # if defence is not the default value
                                if pokemon_1.get_defence() != 5:
                                    self.verificationErrors.append(
                                        f"bulbasaur.get_defence() method did not return correct get_defence: {pokemon_1.get_defence()}")

                            # if pokemon 1 is Squirtle
                            elif isinstance(pokemon_1, Squirtle):

                                # if defence is not the default value + random_level_pokemon_1
                                if pokemon_1.get_defence() != (6 + random_level_pokemon_1):
                                    self.verificationErrors.append(
                                        f"squirtle.get_defence() method did not return correct get_defence: {pokemon_1.get_defence()}")



                        # testing get_speed()
                        elif method_name == "get_speed":
                            """
                            objective: to test get_speed()
                            """

                            # if pokemon 1 is Charmander
                            if isinstance(pokemon_1, Charmander):

                                # if speed is not the default value + random_level_pokemon_1
                                if pokemon_1.get_speed() != (7 + random_level_pokemon_1):
                                    self.verificationErrors.append(
                                        f"charmander.get_speed() method did not return correct get_speed: {pokemon_1.get_speed()}")


                            # if pokemon 1 is Bulbasaur
                            elif isinstance(pokemon_1, Bulbasaur):

                                # if speed is not the default value + random_level_pokemon_1 // 2
                                if pokemon_1.get_speed() != (7 + (random_level_pokemon_1 // 2)):
                                    self.verificationErrors.append(
                                        f"bulbasaur.get_speed() method did not return correct get_speed: {pokemon_1.get_speed()}")


                            # if pokemon 1 is Squirtle
                            elif isinstance(pokemon_1, Squirtle):

                                # if speed is not the default value
                                if pokemon_1.get_speed()!= 7:
                                    self.verificationErrors.append(
                                        f"squirtle.get_speed() method did not return correct get_speed: {pokemon_1.get_speed()}")



                        # testing calc_dmg()
                        elif method_name == "calc_dmg":
                            """
                            objective: to test calc_dmg() which is the damage calculated after 
                            effective damage and then defence
                            # pokemon 2 attacks pokemon 1
                            # so calculate received damage for pokemon 1
                            """

                            # if its charmander being attacked
                            if isinstance(pokemon_1,Charmander):
                                damage_received = pokemon_1.calc_dmg(pokemon_2)

                                # if its bulbasaur attacking
                                if pokemon_2.get_poke_type() == "Grass":

                                    if (pokemon_2.get_attack() // 2) > pokemon_1.get_defence():

                                        # if the ( damage calculated after type effectiveness ) > defence
                                        if damage_received != (pokemon_2.get_attack() // 2):
                                            self.verificationErrors.append(
                                                f"> charmander.calc_damage(bulbasaur) method did not return correct received_damage: {damage_received}")

                                    else:

                                        # if the ( damage calculated after type effectiveness ) <= defence
                                         if damage_received != ((pokemon_2.get_attack() // 2) // 2):
                                            self.verificationErrors.append(
                                                f"<= charmander.calc_damage(bulbasaur) method did not return correct received_damage: {damage_received}")

                                # if its squirtle attacking
                                elif pokemon_2.get_poke_type() == "Water":

                                    if (pokemon_2.get_attack() * 2) > pokemon_1.get_defence():

                                        # if the ( damage calculated after type effectiveness ) > defence
                                        if damage_received != (pokemon_2.get_attack() * 2):
                                            self.verificationErrors.append(
                                                f"> charmander.calc_damage(squirtle) method did not return correct received_damage: {damage_received}")

                                    else:

                                        # if the ( damage calculated after type effectiveness ) <= defence
                                        if damage_received != ((pokemon_2.get_attack() * 2) // 2):
                                            self.verificationErrors.append(
                                                f"<= charmander.calc_damage(squirtle) method did not return correct received_damage: {damage_received}")

                                # if its charmander attacking
                                elif pokemon_2.get_poke_type() == "Fire":

                                    if (pokemon_2.get_attack()) > pokemon_1.get_defence():

                                        # if the ( damage calculated after type effectiveness ) > defence
                                        if damage_received != (pokemon_2.get_attack()):
                                            self.verificationErrors.append(
                                                f"> charmander.calc_damage(charmander) method did not return correct received_damage: {damage_received}")

                                    else:

                                        # if the ( damage calculated after type effectiveness ) <= defence
                                        if damage_received != ((pokemon_2.get_attack()) // 2):
                                            self.verificationErrors.append(
                                                f"<= charmander.calc_damage(charmander) method did not return correct received_damage: {damage_received}")



                            # if its bulbasaur being attacked
                            elif isinstance(pokemon_1,Bulbasaur):
                                damage_received = pokemon_1.calc_dmg(pokemon_2)

                                # if its bulbasaur attacking
                                if pokemon_2.get_poke_type() == "Grass":

                                    if pokemon_2.get_attack() > (pokemon_1.get_defence() + 5):

                                        # if the ( damage calculated after type effectiveness ) > defence + 5
                                        if damage_received != (pokemon_2.get_attack()):
                                            self.verificationErrors.append(
                                                f"> bulbasaur.calc_damage(bulbasaur) method did not return correct received_damage: {damage_received}")

                                    else:

                                        # if the ( damage calculated after type effectiveness ) <= defence + 5
                                        if damage_received != ((pokemon_2.get_attack()) // 2) :
                                            self.verificationErrors.append(
                                                f"<= bulbasaur.calc_damage(bulbasaur) method did not return correct received_damage: {damage_received}")

                                # if its squirtle attacking
                                elif pokemon_2.get_poke_type() == "Water":

                                    if (pokemon_2.get_attack() // 2) > (pokemon_1.get_defence() + 5):

                                        # if the ( damage calculated after type effectiveness ) > defence + 5
                                        if damage_received != (pokemon_2.get_attack() // 2):
                                            self.verificationErrors.append(
                                                f"> bulbasaur.calc_damage(squirtle) method did not return correct received_damage: {damage_received}")

                                    else:

                                        # if the ( damage calculated after type effectiveness ) <= defence + 5
                                        if damage_received != ((pokemon_2.get_attack() // 2) // 2):
                                            self.verificationErrors.append(
                                                f"<= bulbasaur.calc_damage(squirtle) method did not return correct received_damage: {damage_received}")


                                # if its charmander attacking
                                elif pokemon_2.get_poke_type() == "Fire":

                                    if (pokemon_2.get_attack() * 2) > (pokemon_1.get_defence() + 5):

                                        # if the ( damage calculated after type effectiveness ) > defence + 5
                                        if damage_received != (pokemon_2.get_attack() * 2):
                                            self.verificationErrors.append(
                                                f"> bulbasaur.calc_damage(charmander) method did not return correct received_damage: {damage_received}")

                                    else:

                                        # if the ( damage calculated after type effectiveness ) <= defence + 5
                                        if damage_received != ((pokemon_2.get_attack() * 2) // 2):
                                            self.verificationErrors.append(
                                                f"<= bulbasaur.calc_damage(charmander) method did not return correct received_damage: {damage_received}")



                            # if its squirtle being attacked
                            elif isinstance(pokemon_1, Squirtle):
                                damage_received = pokemon_1.calc_dmg(pokemon_2)


                                # if its bulbasaur attacking
                                if pokemon_2.get_poke_type() == "Grass":

                                    if (pokemon_2.get_attack() * 2) > (pokemon_1.get_defence() * 2):

                                        # if the ( damage calculated after type effectiveness ) > defence * 2
                                        if damage_received != (pokemon_2.get_attack() * 2):
                                            self.verificationErrors.append(
                                                f"> squirtle.calc_damage(bulbasaur) method did not return correct received_damage: {damage_received}")
                                    else:

                                        # if the ( damage calculated after type effectiveness ) <= defence * 2
                                        if damage_received != ((pokemon_2.get_attack() * 2) // 2):
                                            self.verificationErrors.append(
                                                f"<= squirtle.calc_damage(bulbasaur) method did not return correct received_damage: {damage_received}")

                                # if its squirtle attacking
                                elif pokemon_2.get_poke_type() == "Water":

                                    if (pokemon_2.get_attack()) > (pokemon_1.get_defence() * 2):

                                        # if the ( damage calculated after type effectiveness ) > defence * 2
                                        if damage_received != (pokemon_2.get_attack()):
                                            self.verificationErrors.append(
                                                f"> squirtle.calc_damage(squirtle) method did not return correct received_damage: {damage_received}")

                                    else:

                                        # if the ( damage calculated after type effectiveness ) <= defence * 2
                                        if damage_received != ((pokemon_2.get_attack()) // 2):
                                            self.verificationErrors.append(
                                                f"<= squirtle.calc_damage(squirtle) method did not return correct received_damage: {damage_received}")

                                # if its charmander attacking
                                elif pokemon_2.get_poke_type() == "Fire":

                                    if (pokemon_2.get_attack() // 2) > (pokemon_1.get_defence() * 2):

                                        # if the ( damage calculated after type effectiveness ) > defence * 2
                                        if damage_received != (pokemon_2.get_attack() // 2):
                                            self.verificationErrors.append(
                                                f"> squirtle.calc_damage(charmander) method did not return correct received_damage: {damage_received}")

                                    else:

                                        # if the ( damage calculated after type effectiveness ) <= defence * 2
                                        if damage_received != ((pokemon_2.get_attack() // 2) // 2):
                                            self.verificationErrors.append(
                                                f"<= squirtle.calc_damage(charmander) method did not return correct received_damage: {damage_received}")






if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestTask1)
    unittest.TextTestRunner(verbosity=0).run(suite)

