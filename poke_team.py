""" PokeTeam
Group:      T05G04
Members:    Lee Sing Yuan
            Benjamin Leong Tjen Ho
            Lim Jing Kai
            Loh Zhun Guan

Description:
    - This file only has one class, PokeTeam.
        The class is a blueprint of a Team, that can be in a battle, against another Team.
    - The main purpose of the methods in this class is to create a team of Pokemons.
        The data type of the team is dependant on the Team's battle_mode attribute.
    - The criterion attribute is only use when battle_mode = 2.
        It is used to find the key to create ListItems when adding Pokemons to an ADT
            (when creating a team)
    - To decrease the number of lines of assign_team (as there are a lot of repeating steps),
        we created 2 helper methods:
        - add_to_team()
        - key_finder()
"""

from array_sorted_list import ArraySortedList
from pokemon import Squirtle, Charmander, Bulbasaur, MissingNo
from pokemon_base import PokemonBase
from queue_adt import CircularQueue
from sorted_list import ListItem
from stack_adt import ArrayStack

from typing import Callable, Final, List

ADT_Type = (ArrayStack, CircularQueue, ArraySortedList)
NoneType = type(None)


class PokeTeam:
    """ A team which each trainer has during a battle.

    Attribute(s):
            trainer_name (str): The name of the trainer in the PokeTeam.
            battle_mode (int):  The battle mode of the battle the PokeTeam is in.
            criterion (str):    The criterion chosen by this team (if the battle is optimised_mode_battle).
            team (ADT_Type):    An ADT which holds the Pokemons in a PokeTeam.

    Class Variable(s):
            LIMIT (int):        The limit to the number of Pokemons a team can have.
            LEVEL (List):       A list of possible criterion values for level (lowercase).
            HP (List):          A list of possible criterion values for hp (lowercase).
            ATTACK (List):      A list of possible criterion values for attack (lowercase).
            DEFENCE (List):     A list of possible criterion values for defence (lowercase).
            SPEED (List):       A list of possible criterion values for speed (lowercase).
    """

    LIMIT: Final[int] = 6
    LEVEL: Final[List[str]] = ["level", "lvl"]
    HP: Final[List[str]] = ["health points", "hp"]
    ATTACK: Final[List[str]] = ["att", "att dmg", "attack", "attack damage"]
    DEFENCE: Final[List[str]] = ["defence"]
    SPEED: Final[List[str]] = ["speed"]

    def __init__(self, trainer_name: str) -> None:
        """ Basic PokeTeam object initialiser.
        :param trainer_name:    Input value to be used as the PokeTeam's trainer_name.
        :return:                None
        :complexity:            BC & WC - O(IsIns)
        :pre:                   Pre conditions are checked in methods called.

        -------------------------------------------------------------------------
        METHODS CALLED           |  COMPLEXITY   |  REMARKS
        -------------------------|---------------|-------------------------------
        self.set_trainer_name()  |  O(IsIns)     |  IsIns: refer to method called
        -------------------------|---------------|-------------------------------
        -------------------------------------------------------------------------
        """
        self.set_trainer_name(trainer_name)
        self.battle_mode = None
        self.criterion = None
        self.team = None

    def __str__(self) -> str:
        """ Magic method constructing a string representation of the PokeTeam.
        :return:        Returns the PokeTeam's string representation.
        :complexity:    BC & WC - O(IsIns * len(self.team))

        -----------------------------------------------------------------------------------
        METHODS CALLED       |  COMPLEXITY                 |  REMARKS
        ---------------------|-----------------------------|-------------------------------
        self.team.__str__()  |  O(IsIns * len(self.team))  |  IsIns: refer to method called
        ---------------------|-----------------------------|-------------------------------
        -----------------------------------------------------------------------------------
        """
        return str(self.team)

    # Static Helper Methods
    @staticmethod
    def add_to_team(battle_mode: int, team_adt: ADT_Type, adding_item: Callable, criterion_key: int = None) -> None:
        """ This method acts as a generalised method to adding Pokemons into ADTs.
        :param battle_mode:     The team's battle_mode value.
        :param team_adt:        The ADT which the Pokemon will be returning to.
        :param adding_item:     A Pokemon to return to its team ADT.
        :param criterion_key:   The key value which is used to create a ListItem (only used for battle_mode = 2).
        :return:                None
        :complexity:            BC & WC - O(IsIns)
        :pre:                   Input team_adt is not full.
        :pre:                   Input returning_item must be a Pokemon.
        :raises ValueError:     When input team_adt is full.
        :raises ValueError:     When input returning_item is not a Pokemon.

        ------------------------------------------------------
        METHODS CALLED           |  COMPLEXITY   |  REMARKS
        -------------------------|---------------|------------
        isinstance()             |  O(IsIns)     |
        ArrayStack.push()        |  O(1)         |
        CircularQueue.append()   |  O(1)         |
        self.get_battle_mode()   |  O(1)         |
        team_adt.us_full()       |  O(1)         |
        -------------------------|---------------|------------
        ------------------------------------------------------
        """

        # Checking pre condition(s)
        if team_adt.is_full():
            raise ValueError("Input team_adt is full!")
        if adding_item not in [Charmander, Bulbasaur, Squirtle, MissingNo]:
            raise ValueError("".join(["Invalid adding_item! adding_item =", str(adding_item)]))

        # Returning the Pokemon to its team ADT using the respective ADT method
        if battle_mode == 0:
            team_adt.push(adding_item())
        elif battle_mode == 1:
            team_adt.append(adding_item())
        elif battle_mode == 2:
            team_adt.new_add(ListItem(adding_item(), criterion_key))

        # Invalid battle_mode value
        else:
            ValueError("".join(["Invalid battle_mode value! battle_mode = ", str(battle_mode)]))

    @staticmethod
    def key_finder(pokemon: PokemonBase, criterion: str) -> (int, NoneType):
        """ Helper method to find the key value for ListItem when returning Pokemon to their team.
        :param pokemon:     A Pokemon returning into it's team's ArraySortedList.
        :param criterion:   The criterion chosen by the Pokemon's trainer.
        :return:            Returns the Pokemon's key to create a ListItem object.
        :complexity:        BC & WC - O(IsIns)
        :pre:               Input poke is a valid Pokemon.
        :raises ValueError: When input poke is an invalid Pokemon.
        :raises ValueError: When input criterion is an invalid Pokemon.
                            - This is raised after going through all conditional statements
                            - Hence, it is not a pre condition

        -------------------------------------------------------------
        METHODS CALLED           |  COMPLEXITY    |     REMARKS
        -------------------------|----------------|------------------
        isinstance()             |  O(IsIns)      |
        PokemonBase.get_attack() |  O(1)          |
        PokemonBase.get_defence()|  O(1)          |
        PokemonBase.get_hp()     |  O(1)          |
        PokemonBase.get_level    |  O(1)          |
        PokemonBase.get_speed()  |  O(1)          |
        -------------------------|----------------|------------------
        -------------------------------------------------------------
        """
        # Checking pre condition(s)
        if not isinstance(pokemon, PokemonBase):
            raise TypeError("".join(["Invalid input poke! poke = ", str(poke)]))

        # Finding appropriate key based on input criterion
        if criterion is None:
            return
        elif criterion == "Level":
            return pokemon.get_level()
        elif criterion == "HP":
            return pokemon.get_hp()
        elif criterion == "Attack":
            return pokemon.get_attack()
        elif criterion == "Defence":
            return pokemon.get_defence()
        elif criterion == "Speed":
            return pokemon.get_speed()

        # Invalid criterion value
        else:
            raise ValueError("".join(["Invalid criterion value! criterion = ", str(criterion)]))

    # Mutator Methods
    def set_trainer_name(self, trainer_name: str) -> None:
        """ Mutator for battle_mode attribute of a PokeTeam.
        :param trainer_name:    New PokeTeam trainer_name value.
        :return:                None
        :complexity:            BC & WC - O(IsIns)
        :pre:                   Input trainer_name is a string.
        :raises TypeError:     When trainer_name is not a string.

        --------------------------------------------------
        METHODS CALLED       |  COMPLEXITY  |   REMARKS
        ---------------------|--------------|-------------
        isinstance()         |  O(IsIns)    |
        ---------------------|--------------|-------------
        --------------------------------------------------
        """
        # Checking pre condition(s)
        if not isinstance(trainer_name, str):
            raise TypeError("".join(["Invalid trainer_name value! trainer_name = ", str(trainer_name)]))

        # Initialising PokeTeam's attribute, trainer_name
        self.trainer_name = trainer_name

    def set_battle_mode(self, battle_mode: int) -> None:
        """ Mutator for battle_mode attribute of a PokeTeam. (Not to be confused with set_mode_battle)
        :param battle_mode: New PokeTeam battle_mode value.
        :return:            None
        :complexity:        BC & WC - O(IsIns)

        :pre:               Input battle_mode must be 0, 1 or 2 only.
        :raises Exception:  When input level is not 0, 1 or 2.

        --------------------------------------------------
        METHODS CALLED       |  COMPLEXITY  |   REMARKS
        ---------------------|--------------|-------------
        isinstance()         |  O(IsIns)    |
        ---------------------|--------------|-------------
        --------------------------------------------------

        Note:
            During checking of pre condition, the function does use the in keyword.
            But since the list only 3 items, the complexity is simply O(1).
        """
        # Checking pre condition(s)
        if isinstance(battle_mode, bool) or battle_mode not in [0, 1, 2]:
            raise ValueError("".join(["Invalid battle_mode input! battle_mode = ", str(battle_mode)]))

        # Initialising the PokeTeam's attribute, battle_mode
        self.battle_mode = battle_mode

    def set_criterion(self, criterion: str) -> None:
        """ Mutator for criterion attribute of a PokeTeam.
        :param criterion:   New PokeTeam battle_mode value.
        :return:            None
        :complexity:        BC & WC - O(1)
        :pre:               self.battle_mode must be 2
        :pre:               Input criterion is in either one of the static class variables (except LIMIT).
        :raises :
        :raises ValueError:  When input criterion is not in either one of the static class variables (except LIMIT).

        -----------------------------------------------------
        METHODS CALLED          |  COMPLEXITY  |   REMARKS
        ------------------------|--------------|-------------
        self.get_battle_mode()  |  O(1)        |
        ------------------------|--------------|-------------
        -----------------------------------------------------

        Note:
            During checking of pre condition, the function does use the in keyword.
            But since the list only has at most 4 items, the complexity is simply O(1).
        """
        # Checking pre condition(s)
        if self.get_battle_mode() != 2:
            raise ValueError(
                "".join(["battle_mode must be 2 to set criterion value! battle_mode = ", str(self.get_battle_mode())]))
        elif not (criterion in PokeTeam.LEVEL or
                  criterion in PokeTeam.HP or
                  criterion in PokeTeam.ATTACK or
                  criterion in PokeTeam.DEFENCE or
                  criterion in PokeTeam.SPEED):
            raise ValueError("".join(["Invalid criterion input! criterion = ", str(criterion)]))

        # Initialising the PokeTeam's attribute, criterion
        cri = criterion.lower()
        if cri in PokeTeam.LEVEL:
            self.criterion = "Level"
        elif cri in PokeTeam.HP:
            self.criterion = "HP"
        elif cri in PokeTeam.ATTACK:
            self.criterion = "Attack"
        elif cri in PokeTeam.DEFENCE:
            self.criterion = "Defence"
        elif cri in PokeTeam.SPEED:
            self.criterion = "Speed"
        else:
            raise ValueError("".join(["Invalid criterion input! criterion = ", str(criterion)]))

    # Accessor Methods
    def get_trainer_name(self) -> str:
        """ Accessor method for trainer_name attribute.
        :return:        Returns the PokeTeam's trainer_name attribute.
        :complexity:    BC & WC - O(1)
        """
        return self.trainer_name

    def get_battle_mode(self) -> int:
        """ Accessor method for battle_mode attribute.
        :return:        Returns the PokeTeam's battle_mode attribute.
        :complexity:    BC & WC - O(1)
        """
        return self.battle_mode

    def get_criterion(self) -> str:
        """ Accessor method for criterion attribute.
        :return:        Returns the PokeTeam's criterion attribute.
        :complexity:    BC & WC - O(1)
        """
        return self.criterion

    # Team Assignment Methods
    def choose_team(self, battle_mode: int = 0, criterion: str = None) -> None:
        """ Method to determine the structure of the PokeTeam.
        :param battle_mode: The current battle mode.
        :param criterion:   The criterion chosen by the team (for optimised_mode_battle).
        :return:            None
        :complexity:        BC & WC - O(IsIns + Inp)

        -----------------------------------------------------------------------------------------------------
        METHODS CALLED           |  COMPLEXITY     |    REMARKS
        -------------------------|-----------------|---------------------------------------------------------
        self.assign_team()       |  O(IsIns)       |    IsIns: refer to method called
        self.set_battle_mode()   |  O(IsIns)       |    IsIns: refer to method called
        input()                  |  O(Inp)         |
        List comprehension       |  O(L)           |    where L = len(list created). Here, L = 3 or 4 -> O(1)
        sum(List[])              |  O(s)           |    where s = len(List[]). Here, s = 3 or 4 -> O(1)
        print()                  |  O(1)           |
        self.set_criterion()     |  O(1)           |
        self.get_battle_mode()   |  O(1)           |
        -------------------------|-----------------|---------------------------------------------------------
        -----------------------------------------------------------------------------------------------------
        """
        # Type hinting
        bulb: int
        charm: int
        input_num: str
        miss: int
        num_lst: List[int]
        num_of_pokes: int
        squir: int

        # Initialising the PokeTeam's attributes
        self.set_battle_mode(battle_mode)
        if self.get_battle_mode() == 2:
            self.set_criterion(criterion)

        # User inputs until a valid input is received
        while True:
            # Input prompt
            input_num = input("Howdy Trainer! Choose your team as C B S M\n"
                              "where C is the number of Charmanders\n      B is the number of Bulbasaurs\n      "
                              "S is the number of Squirtles\n      M is the number of MissingNos (Maximum of 1 only!)\n")

            # Checking validity of user input
            try:
                num_lst = [int(s) for s in input_num.strip().split()]
                num_of_pokes = len(num_lst)
            except ValueError:
                print("Invalid input. Please try again.\n")
                num_lst = None

            # Invalid input
            if num_lst is None:
                pass
            elif any([x < 0 for x in num_lst]):
                print("Negative numbers are not accepted. Please try again.\n")
            elif sum(num_lst) < 1:
                print("Please select a minimum of 1 Pokemon!\n")
            elif sum(num_lst) > 6:
                print("Please select a maximum of 6 Pokemons!\n")
            elif num_of_pokes == 4 and not 0 <= num_lst[num_of_pokes - 1] <= 1:
                print("A team can only have 0 or 1 MissingNos in their team!\n")

            # Valid input
            else:
                charm, bulb, squir, miss = num_lst if num_of_pokes == 4 else num_lst + [0]
                break

        self.assign_team(charm, bulb, squir, miss)

    def assign_team(self, charm: int, bulb: int, squir: int, miss: int) -> None:
        """ Method to fill the team ADTs with the Pokemons chosen (via user input)
        :param charm:       The number of Charmanders chosen.
        :param bulb:        The number of Bulbasaurs chosen.
        :param squir:       The number of Squirtles chosen.
        :param miss:        The number of MissingNos chosen.
        :return:            None
        :complexity:        BC & WC - O(IsIns)
        :pre:               0 < charm + bulb + squir + miss <= 6 and they must be integers
        :raises Exception:  When the total number of Pokemons chosen is non-positive or exceeds 6

        -------------------------------------------------------------------------------------------------------
        METHODS CALLED              |   COMPLEXITY     |    REMARKS
        ----------------------------|------------------|-------------------------------------------------------
        isinstance()                |   O(IsIns)       |
        ArrayStack.__init__()       |   O(length)      |    Here, length == 6 -> O(1)
        CircularQueue.__init__()    |   O(length)      |    Here, length == 6 -> O(1)
        ArraySortedList.__init__()  |   O(length)      |    Here, length == 6 -> O(1)
        ArraySortedList.new_add()   |   O(n)           |    where n = len(self.team). Here, 0 <= n <= 6 -> O(1)
        ArrayStack.push()           |   O(1)           |
        CircularQueue.append()      |   O(1)           |
        PokemonBase.get_attack()    |   O(1)           |
        PokemonBase.get_defence()   |   O(1)           |
        PokemonBase.get_hp()        |   O(1)           |
        PokemonBase.get_level()     |   O(1)           |
        PokemonBase.get_speed()     |   O(1)           |
        self.get_battle_mode()      |   O(1)           |
        self.get_criterion()        |   O(1)           |
        ----------------------------|------------------|-------------------------------------------------------
        -------------------------------------------------------------------------------------------------------
        """
        # Type hinting
        bat_mod: int
        bulb_key: int
        char_key: int
        miss_key: int
        squir_key: int

        # Checking pre condition(s)
        if isinstance(charm, bool) or isinstance(bulb, bool) \
                or isinstance(squir, bool) or isinstance(miss, bool):
            raise TypeError("Input charm, bulb, squir and miss must be integers!")
        elif not 0 < charm + bulb + squir + miss <= 6:
            raise AssertionError(
                "".join(["A team must have 1 to 6 Pokemons! team size = ", str(charm + bulb + squir + miss)]))
        elif miss not in [0, 1]:
            raise ValueError("".join(["Invalid MissingNo amount! MissingNo amount = ", str(miss)]))

        char_key = PokeTeam.key_finder(Charmander(), self.get_criterion())
        bulb_key = PokeTeam.key_finder(Bulbasaur(), self.get_criterion())
        squir_key = PokeTeam.key_finder(Squirtle(), self.get_criterion())
        miss_key = PokeTeam.key_finder(MissingNo(), self.get_criterion())

        # set_mode_battle
        if (bat_mod := self.get_battle_mode()) == 0:
            # Team is an Array Stack ADT
            self.team = ArrayStack(self.LIMIT)

        # rotating_mode_battle
        elif bat_mod == 1:
            # Team is a Circular Queue ADT
            self.team = CircularQueue(self.LIMIT)

        # optimised_mode_battle
        elif bat_mod == 2:
            # Team is an Array Sorted List ADT
            self.team = ArraySortedList(self.LIMIT)

        first, second, third, fourth = [charm, bulb, squir, miss] if bat_mod == 1 else [miss, squir, bulb, charm]

        for _ in range(first):
            poke = Charmander if bat_mod == 1 else MissingNo
            key = char_key if bat_mod == 1 else miss_key
            self.add_to_team(bat_mod, self.team, poke, key)
        for _ in range(second):
            poke = Bulbasaur if bat_mod == 1 else Squirtle
            key = bulb_key if bat_mod == 1 else squir_key
            self.add_to_team(bat_mod, self.team, poke, key)
        for _ in range(third):
            poke = Squirtle if bat_mod == 1 else Bulbasaur
            key = squir_key if bat_mod == 1 else bulb_key
            self.add_to_team(bat_mod, self.team, poke, key)
        for _ in range(fourth):
            poke = MissingNo if bat_mod == 1 else Charmander
            key = miss_key if bat_mod == 1 else char_key
            self.add_to_team(bat_mod, self.team, poke, key)