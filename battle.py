""" Battle
Group:      T05G04
Members:    Lee Sing Yuan
            Benjamin Leong Tjen Ho
            Lim Jing Kai
            Loh Zhun Guan

Description:
    # BATTLE #
    - This file only has one class, Battle.
        Battle class has 3 different possible battle modes:
            - set_mode_battle
            - rotating_mode_battle
            - optimised_mode_battle
    - The first two battles are very similar. Hence, they both call a common function, modularised_battle.
        This is reduce the number of lines of code in the file.
    - There are also a bunch of things which occur in battles that are quite repetitive.
        Hence, we created external helper methods so that the battle methods can call them when needed.
        The external methods are:
        - single_round_fight
        - det_winner
        - Accessor and Mutator methods for battle_mode.

    # PRINTING #
    - We have also included a bunch of methods which are *not* required in this assignment.
        The main purpose of these additional methods are for printing.
        These additional methods are:
        - access
        - return_to_team
        - pretty_printing
    - The main bulk of printing functionality and logic is in pretty printing. It is called at the start of every battle.
    - pretty_printing prints out the teams in their short-form format and creates a list of these short-forms
        - These short-forms are then used *during* battle rounds to show what occurred on that round.
"""

from array_sorted_list import ArraySortedList
from poke_team import PokeTeam
from pokemon import Charmander, Bulbasaur, Squirtle, MissingNo
from pokemon_base import PokemonBase
from queue_adt import CircularQueue
from sorted_list import ListItem
from stack_adt import ArrayStack

from random import randint
from typing import Dict, Generic, Final, List, Tuple, TypeVar

T = TypeVar('T')
ADT_Type = (ArrayStack, CircularQueue, ArraySortedList)
Numeric = (int, float)
NoneType = type(None)


class Battle:
    """ A battle between two trainers, who has a team each.

    Attribute(s):
            team1 (PokeTeam):               The first team in the battle
            team2 (PokeTeam):               The second team in the battle
            battle_mode (int, NoneType):    The battle mode of the battle

    Class Variable(s):
            poke_print_index (List):    A list of indices of Pokemons to print (Only used for optimised_mode_battle).
    """
    # Class Variable(s)
    poke_print_index: List[int] = [0, 0]

    def __init__(self, trainer_one_name: str, trainer_two_name: str) -> None:
        """ Basic Battle object initialiser.
        :param trainer_one_name:    The name of the first trainer in the Battle.
        :param trainer_two_name:    The name of the second trainer in the Battle.
        :return:                    None
        :complexity:                BC & WC - O(IsIns)
        :pre:                       Pre conditions are checked when calling constructor of PokeTeam.

        ---------------------------------------------------------------------
        METHODS CALLED       |  COMPLEXITY    | REMARKS
        ---------------------|----------------|------------------------------
        self.set_team1()     |  O(IsIns)      | IsIns: refer to method called
        self.set_team2()     |  O(IsIns)      | IsIns: refer to method called
        ---------------------|----------------|------------------------------
        ---------------------------------------------------------------------
        """
        self.set_team1(PokeTeam(trainer_one_name))
        self.set_team2(PokeTeam(trainer_two_name))

    # Mutator Methods
    def set_team1(self, team1: PokeTeam) -> None:
        """ Mutator for team1 attribute of a Battle.
        :param team1:       New Battle team1 value.
        :return:            None
        :complexity:        BC & WC - O(IsIns)
        :pre:               Input team1 must be PokeTeam object.
        :raises TypeError:  When input team1 is not a PokeTeam object.

        ---------------------------------------------------------------------
        METHODS CALLED       |  COMPLEXITY  |   REMARKS
        ---------------------|--------------|--------------------------------
        isinstance()         |  O(IsIns)    |
        ---------------------|--------------|--------------------------------
        ---------------------------------------------------------------------
        """
        # Checking pre condition(s)
        if not isinstance(team1, PokeTeam):
            raise TypeError("".join(["Invalid team1 type! team1 type = ", str(type(team1))]))

        # Initialising Battle's attribute, team1
        self.team1 = team1

    def set_team2(self, team2: PokeTeam) -> None:
        """ Mutator for team2 attribute of a Battle.
        :param team2:   New Battle team2 value.
        :return:        None
        :complexity:    BC & WC - O(IsIns)
        :pre:               Input team1 must be PokeTeam object.
        :raises TypeError:  When input team1 is not a PokeTeam object.

        ---------------------------------------------------------------------
        METHODS CALLED       |  COMPLEXITY  |   REMARKS
        ---------------------|--------------|--------------------------------
        isinstance()         |  O(IsIns)    |
        ---------------------|--------------|--------------------------------
        ---------------------------------------------------------------------
        """
        # Checking pre condition(s)
        if not isinstance(team2, PokeTeam):
            raise TypeError("".join(["Invalid team1 type! team1 type = ", str(type(team2))]))

        # Initialising Battle's attribute, team2
        self.team2 = team2


    def set_battle_mode(self, battle_mode: int) -> None:
        """ Mutator for battle_mode attribute of a Battle.
        :param battle_mode: New Battle battle_mode value.
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
            raise ValueError("".join(["Invalid battle_mode input!", str(battle_mode)]))

        # Initialising the Battle's attribute, battle_mode
        self.battle_mode = battle_mode

    # Accessor Methods
    def get_team1(self) -> PokeTeam:
        """ Accessor method for Battle's attribute, team1.
        :return:        Returns the Battle's attribute, team1.
        :complexity:    BC & WC - O(1)
        """
        return self.team1

    def get_team2(self) -> PokeTeam:
        """ Accessor method for Battle's attribute, team2.
        :return:        Returns the Battle's attribute, team2.
        :complexity:    BC & WC - O(1)
        """
        return self.team2

    def get_battle_mode(self) -> int:
        """ Accessor method for Battle's attribute, battle_mode.
        :return:        Returns the Battle's attribute, battle_mode.
        :complexity:    BC & WC - O(1)
        """
        return self.battle_mode

    # Helper methods
    def access(self, team_adt: ADT_Type, _: int = 0) -> PokemonBase:
        """ This method acts as a generalised method to access an item in an ADT
        :param team_adt:    An ADT which holds a team's Pokemons
        :param _:           (Optional) Index for ArraySortedList ADTs (Only used for optimised_mode_battle).
        :return:            Returns the most "outer" Pokemon in team_adt.
        :complexity:        BC & WC - O(1)
        :pre:               Input team_adt is not empty.
        :pre:               Input _ must satisfy 0 <= _ < len(team_adt).
        :raises ValueError: When input team_adt is empty.
        :raises IndexError: When _ is not a valid index in team_adt.

        ----------------------------------------------------------
        METHODS CALLED                | COMPLEXITY  |   REMARKS
        ------------------------------|-------------|-------------
        ArrayStack.pop()              | O(1)        |
        CircularQueue.serve()         | O(1)        |
        ArraySortedList.__getitem__() | O(1)        |
        self.get_battle_mode()        | O(1)        |
        ------------------------------|-------------|-------------
        ----------------------------------------------------------
        """
        # Checking pre condition(s)
        if len(team_adt) == 0:
            raise ValueError("team_adt input is empty!")
        if not 0 <= _ < len(team_adt):
            raise IndexError("".join(["Input index value, ", str(_), ", is out of bounds!"]))

        # Getting Pokemon from ADT with the respective ADT methods
        if self.get_battle_mode() == 0:
            return team_adt.pop()
        elif self.get_battle_mode() == 1:
            return team_adt.serve()
        elif self.get_battle_mode() == 2:
            temp_list_item = team_adt[_]
            return temp_list_item.value

        # Battle object has an invalid battle_mode value
        else:
            raise ValueError("Invalid battle_mode value!")

    def return_to_team(self, team_adt: ADT_Type, returning_item: PokemonBase) -> None:
        """ This method acts as a generalised method to return an item to an ADT.
        :param team_adt:        The ADT which the Pokemon will be returning to.
        :param returning_item:  A Pokemon to return to its team ADT.
        :return:                None
        :complexity:            BC & WC - O(IsIns)
        :pre:                   Input team_adt is not full.
        :pre:                   Input returning_item must be a Pokemon.
        :raises ValueError:     When input team_adt is full.
        :raises ValueError:     When input returning_item is not a Pokemon.

        -----------------------------------------------------
        METHODS CALLED           |  COMPLEXITY   |  REMARKS
        -------------------------|---------------|-----------
        isinstance()             |  O(IsIns)     |
        ArrayStack.push()        |  O(1)         |
        CircularQueue.append()   |  O(1)         |
        self.get_battle_mode()   |  O(1)         |
        team_adt.us_full()       |  O(1)         |
        -------------------------|---------------|-----------
        -----------------------------------------------------

        Note:
            - Method not used for optimised_mode_battle because ArraySortedList holds ListItems instead of Pokemons
        """
        # Checking pre condition(s)
        if team_adt.is_full():
            raise ValueError("Input team_adt is full!")
        if not isinstance(returning_item, PokemonBase):
            raise ValueError("".join(["Input returning_item, ", str(returning_item), "is not a valid Pokemon!"]))

        # Returning the Pokemon to its team ADT using the respective ADT method
        if self.get_battle_mode() == 0:
            team_adt.push(returning_item)
        elif self.get_battle_mode() == 1:
            team_adt.append(returning_item)
        elif self.get_battle_mode() == 2:
            raise ValueError("".join(
                ["optimised_mode_battle does not use this method! battle_mode = ", str(self.get_battle_mode())]))

        # Battle object has an invalid battle_mode value
        else:
            raise ValueError("".join(["Invalid battle_mode value! battle_mode = ", str(self.get_battle_mode())]))

    def pretty_printing(self, team_adt_1: ADT_Type, team_adt_2: ADT_Type) -> List[List[str]]:
        """ Method to print out statements to give a clearer illustration of what the battle looks like.
        :param team_adt_1:  An ADT which holds the Pokemon instances in team 1.
        :param team_adt_2:  An ADT which holds the Pokemon instances in team 2.
        :return:            Returns a nested list with the short forms of the Pokemon instances from team_adt_1 and team_adt_2.
                                It should end up as something like [[C1, C2, S1...], [B1, B2, S1...]].
        :complexity:        BC & WC - O(IsIns)
        :pre:               Input team_adt_1 must have 1 to 6 (inclusive) Pokemon instances.
        :pre:               Input team_adt_2 must have 1 to 6 (inclusive) Pokemon instances.
        :raises Exception:  When either team_adt_1 or team_adt_2 has less than 1 or more than 6 Pokemon instances.

        ------------------------------------------------------------------------------------------------------------
        METHODS CALLED          |   COMPLEXITY    |     REMARKS
        ------------------------|-----------------|-----------------------------------------------------------------
        self.return_to_team()   |   O(IsIns)      |     IsIns: refer to method called
        isinstance()            |   O(IsIns)      |
        __str__(input)          |   O(d)          |     where d is the number of chars of input. Here, d = 1 -> O(1)
        str.join(List[])        |   O(n)          |     where n = len(List[]). Here, n = 2 or 4 -> O(1)
        ArrayStack.__init__()   |   O(1)          |
        ArrayStack.pop()        |   O(1)          |
        ArrayStack.push()       |   O(1)          |
        List.append()           |   O(1)          |
        self.access()           |   O(1)          |
        self.get_battle_mode()  |   O(1)          |
        ------------------------|-----------------|-----------------------------------------------------------------
        ------------------------------------------------------------------------------------------------------------
        """
        # Type hinting
        bulb_counter: int
        charm_counter: int
        chosen_criterion: str
        item: PokemonBase
        n: int
        short_form_lst: List[List[str]]
        squir_counter: int
        team_counter: int
        team_to_print: ADT_Type
        temp_stack: ArrayStack

        # Checking pre condition(s)
        if len(team_adt_1) > 6 or len(team_adt_1) == 0:
            raise ValueError("Team 1 must have 1 to 6 Pokemons!")

        if len(team_adt_2) > 6 or len(team_adt_2) == 0:
            raise ValueError("Team 2 must have 1 to 6 Pokemons!")

        ### PRINTING STARTS HERE ###
        short_form_lst = [[], []]  # This is the list which will contain all of the short forms of the Pokemons

        # This counter is so that the loop knows which team to refer to
        for team_counter in range(2):  # Complexity - O(1)
            charm_counter, bulb_counter, squir_counter = 1, 1, 1

            # A temporary stack to be used to hold the Pokemons
            # This is needed since when initially pushing back, the order of Pokemons will be reversed
            team_to_print = team_adt_2 if team_counter else team_adt_1
            n = len(team_to_print)
            temp_stack = ArrayStack(n)

            # We loop backwards because in ArraySortedList, the Pokemon who fights first is at the last index
            # Complexity - O(n). Here, n = 6 -> O(1)
            for _ in range(n - 1, -1, -1):
                item = self.access(team_to_print, _)

                # Checking what Pokemon is item to determine the short form for this Pokemon
                # For each Pokemon (except MissingNo), their respective counter increases by 1 after pkm gets initialised
                # This is so that the next short form will have appropriate next number
                if isinstance(item, Charmander):
                    short_form_lst[team_counter].append("".join(["C", str(charm_counter)]))
                    charm_counter += 1

                elif isinstance(item, Bulbasaur):
                    short_form_lst[team_counter].append("".join(["B", str(bulb_counter)]))
                    bulb_counter += 1

                elif isinstance(item, Squirtle):
                    short_form_lst[team_counter].append("".join(["S", str(squir_counter)]))
                    squir_counter += 1

                elif isinstance(item, MissingNo):
                    short_form_lst[team_counter].append("M1")

                # Invalid Pokemon detected in the ADT
                else:
                    raise ValueError("Invalid Pokemon in the ADT!")

                # Returning Pokemon to the ADT
                if self.get_battle_mode() == 0:
                    # The Pokemon is first stored in temp_stack
                    self.return_to_team(temp_stack, item)

                elif self.get_battle_mode() == 1:
                    self.return_to_team(team_to_print, item)

            # Popping from temp_stack then pushing into original ADT
            if temp_stack:
                while temp_stack:
                    team_to_print.push(temp_stack.pop())

            if self.get_battle_mode() == 2:
                chosen_criterion = [self.team1.get_criterion(), self.team2.get_criterion()][team_counter]
                print("".join(["Team ", str(team_counter + 1), ": Chosen Attribute: ", chosen_criterion]))
            print("".join(["Team ", str(team_counter + 1), ": ", " ".join(short_form_lst[team_counter])]))

        print()
        return short_form_lst

    def det_winner(self, first_poke: PokemonBase, second_poke: PokemonBase, poke_lists: List[List[str]],
                   second_call: bool = False) -> (NoneType, PokemonBase, str):
        """ Method to determine a winner based on the aliveness of the input Pokemon instances.
        :param first_poke:  A Pokemon currently in the battlefield
        :param second_poke: A Pokemon currently in the battlefield
        :param poke_lists:  A nested list of the two team's Pokemon instances' short forms
        :param second_call: A boolean which states if this is the second call to this method
        :return:            Scenario 1 - Both are not alive!
                            --> Returns None
                            Scenario 2 - Only one is alive
                            --> Returns the Pokemon still alive
                            Scenario 3 - Both are alive
                            --> Returns "Draw"
        :complexity:        BC & WC - O(IsIns)
        :pre:               Input first_poke must be a valid Pokemon
        :pre:               Input second_poke must be a valid Pokemon
        :raises Exception:  When either first_poke or second_poke is not a valid Pokemon

        -------------------------------------------------------------------------------------------------------
        METHODS CALLED           |  COMPLEXITY   |  REMARKS
        -------------------------|---------------|-------------------------------------------------------------
        PokemonBase.set_hp()     |  O(IsIns)     |  IsIns: refer to method called
        PokemonBase.set_level()  |  O(IsIns)     |  IsIns: refer to method called
        isinstance()             |  O(IsIns)     |
        __str__(input)           |  O(str)       |  where str = number of chars of input. Here, str = 2 -> O(1)
        del List[]               |  O(del)       |  where del = len(List[]). Here, 0 < del <= 6 -> O(1)
        str.join(List[])         |  O(join)      |  where join = len(List[]). Here, join = 2, 4 or 5
        PokemonBase.get_hp()     |  O(1)         |
        PokemonBase.get_level()  |  O(1)         |
        PokemonBase.is_alive()   |  O(1)         |
        -------------------------|---------------|-------------------------------------------------------------
        -------------------------------------------------------------------------------------------------------
        """
        # Checking pre condition(s)
        if not isinstance(first_poke, PokemonBase):
            raise ValueError("".join(["first_poke is not a valid Pokemon! first_poke = ", str(first_poke)]))
        elif not isinstance(second_poke, PokemonBase):
            raise ValueError("".join(["second_poke is not a valid Pokemon! second_poke = ", str(second_poke)]))

        # Determining which Pokemon won (if any, else Draw or None)
        ind_1, ind_2 = Battle.poke_print_index
        if not first_poke.is_alive() and not second_poke.is_alive():
            print("".join(["Team's 1 ", str(poke_lists[0][ind_1]), " fights Team 2's ", str(poke_lists[1][ind_2]),
                           " and both fainted!"]))
            del poke_lists[0][ind_1]
            del poke_lists[1][ind_2]
            return None

        elif not second_poke.is_alive():
            first_poke.set_level(first_poke.get_level() + 1)
            print("".join(["Team's 1 ", str(poke_lists[0][ind_1]), " faints Team 2's ", str(poke_lists[1][ind_2])]))
            del poke_lists[1][ind_2]
            return first_poke

        elif not first_poke.is_alive():
            second_poke.set_level(second_poke.get_level() + 1)
            print("".join(
                ["Team's 1 ", str(poke_lists[0][ind_1]), " is fainted by Team 2's ", str(poke_lists[1][ind_2])]))
            del poke_lists[0][ind_1]
            return second_poke

        else:
            if not second_call:
                first_poke.set_hp(first_poke.get_hp() - 1)
                second_poke.set_hp(second_poke.get_hp() - 1)
                return self.det_winner(first_poke, second_poke, poke_lists, True)
            else:
                print("".join(["Team's 1 ", str(poke_lists[0][ind_1]), " fights Team 2's ", str(poke_lists[1][ind_2]),
                               " and both live!"]))
                return "Draw"

    def single_round_fight(self, first_poke: PokemonBase, second_poke: PokemonBase, poke_lists: List[List[str]]) -> \
            (PokemonBase, str, NoneType):
        """ Method to simulate a single round fight between two Pokemons during a battle
        :param first_poke:  A Pokemon currently in the battlefield.
        :param second_poke: A Pokemon currently in the battlefield.
        :param poke_lists:  A nested list of the two team's Pokemons short forms.
        :complexity:        BC & WC - O(IsIns), which is the complexity of isinstance()
        :return:            Returns the Pokemon who wins in the round (if any).
        :pre:               Input first_poke must be a valid Pokemon.
        :pre:               Input second_poke must be a valid Pokemon.
        :raises Exception:  When either first_poke or second_poke is not a valid Pokemon.

        -------------------------------------------------------------------------
        METHODS CALLED          |   COMPLEXITY  |   REMARKS
        ------------------------|---------------|--------------------------------
        det_winner()            |   O(IsIns)    |   IsIns: refer to method called
        do_superpower()         |   O(IsIns)    |   IsIns: refer to method called
        isinstance()            |   O(IsIns)    |
        PokemonBase.calc_dmg()  |   O(IsIns)    |   IsIns: refer to method called
        PokemonBase.set_hp()    |   O(IsIns)    |   IsIns: refer to method called
        PokemonBase.get_hp()    |   O(1)        |
        PokemonBase.get_speed() |   O(1)        |
        ------------------------|---------------|--------------------------------
        -------------------------------------------------------------------------

        Note:
            - The method calls det_winner() to determine the winner of the round (if any, else it returns a draw).
        """
        # Type hinting
        fast_dmg_slow: Numeric
        faster: PokemonBase
        same_speed: bool
        slow_dmg_fast: Numeric
        slower: PokemonBase

        def do_superpower(miss: MissingNo, attacker: PokemonBase) -> None:
            """ Method to simulate what occurs when a MissingNo is being attacked
            :param miss:        MissingNo Pokemon being attacked
            :param attacker:    The Pokemon attacking the MissingNo Pokemon
            :complexity:        BC & WC - O(IsIns)
            :pre:               Input miss must be a MissingNo
            :raises ValueError: When miss is not a MissingNo

            -----------------------------------------------------------------------------
            METHODS CALLED          |   COMPLEXITY    |     REMARKS
            ------------------------|-----------------|----------------------------------
            MissingNo.superpower()  |   O(IsIns)      |     IsIns: refer to method called
            PokemonBase.calc_dmg()  |   O(IsIns)      |     IsIns: refer to method called
            PokemonBase.set_hp()    |   O(IsIns)      |     IsIns: refer to method called
            isinstance()            |   O(IsIns)      |
            PokemonBase.get_hp()    |   O(1)          |
            random.randint(0, N)    |   O(log N)      |     Here, N = 2 -> O(1)
            ------------------------|-----------------|----------------------------------
            -----------------------------------------------------------------------------


            Note:
                - Whether or not miss performs Superpower is dependant on a random integer assigned using randint()
            """
            # Type hinting
            receive_dmg: int

            # Checking pre condition(s)
            if not isinstance(miss, MissingNo):
                raise ValueError("".join(["miss is not a MissingNo: miss = ", str(miss)]))

            # Choosing to do superpower or to receive damage
            receive_dmg = randint(0, 3)
            if not receive_dmg:
                miss.superpower()
            else:
                miss.set_hp(miss.get_hp() - miss.calc_dmg(attacker))

        # Checking pre condition(s)
        if not (isinstance(first_poke, PokemonBase) and isinstance(second_poke, PokemonBase)):
            raise Exception("Both inputs must be valid Pokemons!")

        # Determining which Pokemon is faster (if any)
        # Same speed
        if same_speed := first_poke.get_speed() == second_poke.get_speed():
            faster, slower, same_speed = first_poke, second_poke, True

        # First pokemon is faster
        elif first_poke.get_speed() > second_poke.get_speed():
            faster, slower = first_poke, second_poke

        # Second pokemon is faster
        elif first_poke.get_speed() < second_poke.get_speed():
            faster, slower = second_poke, first_poke

        # Calculating damage from one Pokemon to another
        fast_dmg_slow = slower.calc_dmg(faster)
        slow_dmg_fast = faster.calc_dmg(slower)

        # If the Pokemons have the same speed
        if same_speed:
            # Both Pokemon instances attack each other simultaneously
            if isinstance(slower, MissingNo):
                do_superpower(slower, faster)
            else:
                slower.set_hp(slower.get_hp() - fast_dmg_slow)

            if isinstance(faster, MissingNo):
                do_superpower(faster, slower)
            else:
                faster.set_hp(faster.get_hp() - slow_dmg_fast)

        # If the Pokemons have different speeds
        elif not same_speed:
            # Faster attacks Slower
            if isinstance(slower, MissingNo):
                do_superpower(slower, faster)
            else:
                slower.set_hp(slower.get_hp() - fast_dmg_slow)

            # If slower is still alive,
            #   Slower attacks Faster
            if slower.is_alive():
                if isinstance(faster, MissingNo):
                    do_superpower(faster, slower)
                else:
                    faster.set_hp(faster.get_hp() - slow_dmg_fast)

        return self.det_winner(first_poke, second_poke, poke_lists)

    def set_mode_battle(self) -> str:
        """ Battle when battle_mode = 0
        :return:        Returns the winning trainer's name (if any, else Draw)
        :complexity:    O(IsIns)

        Note:
            Since set_mode_battle and rotating_mode_battle are so similar, they both call the same function.
            The only difference is the parameter input into modularised_battle().
                i.e., their respective battle_mode values (0 or 1).

        ---------------------------------------------------------------------
        METHODS CALLED       |  COMPLEXITY  |   REMARKS
        ---------------------|--------------|--------------------------------
        modularised_battle() |  O(IsIns)    |   IsIns: refer to method called
        ---------------------|--------------|--------------------------------
        ---------------------------------------------------------------------
        """

        return self.modularised_battle(0)

    def rotating_mode_battle(self) -> str:
        """ Battle when battle_mode = 1
        :return:        Returns the winning trainer's name (if any, else Draw)
        :complexity:    O(IsIns)

        ---------------------------------------------------------------------
        METHODS CALLED       |  COMPLEXITY  |   REMARKS
        ---------------------|--------------|--------------------------------
        modularised_battle() |  O(IsIns)    |   IsIns: refer to method called
        ---------------------|--------------|--------------------------------
        ---------------------------------------------------------------------
        """

        return self.modularised_battle(1)

    def optimised_mode_battle(self, criterion_team1: str, criterion_team2: str) -> str:
        """ Battle when battle_mode = 2
        :param criterion_team1: The criterion chosen by team1
        :param criterion_team2: The criterion chosen by team2
        :return:                Returns the winning trainer's name (if any, else Draw)
        :complexity:            O(IsIns)

        ---------------------------------------------------------------------------------------------
        METHODS CALLED                    | COMPLEXITY      |  REMARKS
        ----------------------------------|-----------------|----------------------------------------
        PokeTeam.choose_team()            | O(IsIns + Inp)  |   IsIns and Inp: refer to method called
        isinstance()                      | O(IsIns)        |
        key_finder()                      | O(IsIns)        |   IsIns: refer to method called
        pretty_printing()                 | O(IsIns)        |   IsIns: refer to method called
        set_battle_mode()                 | O(IsIns)        |   IsIns: refer to method called
        single_round_fight()              | O(IsIns)        |   IsIns: refer to method called
        ArraySortedList.delete_at_index() | O(dax)          |   where dax = len(ArraySortedList).
                                          |                 |         Here, 0 < dax <= 6 -> O(1)
        ArraySortedList.new_add()         | O(new)          |   where new = len(ArraySortedList).
                                          |                 |         Here, 0 < new <= 6 -> O(1)
        dictionary comprehension          | O(dic_comp)     |   where dic_comp = len(dict created).
                                          |                 |         Here, 0 < dic_comp <= 6 -> O(1)
        PokeTeam.get_trainer_name()       | O(1)            |
        append()                          | O(1)            |
        ----------------------------------|-----------------|----------------------------------------
        ---------------------------------------------------------------------------------------------

        Note:
            This method is just like the previous 2 battle methods but with some additions.
            Additions include:
                - Extra function to determine the key value when returning ListItems to the ADT
                - Creating dictionaries for each team to help in re-sorting Pokemons after they have battled.
                - Checking if other Pokemons have battled if the next Pokemon is a MissingNo
                    - Only if there exists a MissingNo in either of the teams
                    - This will be referred to as "The Condition" in the comments.
                - Finding the key to create ListItems when returning Pokemons to their teams
        """
        # Type hinting
        ORIGINAL_TEAM_1_SIZE: Final[int]
        ORIGINAL_TEAM_2_SIZE: Final[int]
        team_criterion: str
        do_check: bool
        i: int
        last_ind: int
        nested_poke_list: List[List[str]]
        return_poke: PokemonBase
        poke_1: PokemonBase
        poke_2: PokemonBase
        poke_dict_1: Dict[PokemonBase, int]
        poke_dict_2: Dict[PokemonBase, int]
        poke_key: int
        poke_team: PokeTeam
        pokemon: PokemonBase
        pokes_battled_1: List[(NoneType, str)]
        pokes_battled_2: List[(NoneType, str)]
        res: (PokemonBase, str)
        return_item: ListItem
        return_to_team: List[(NoneType, Tuple[PokemonBase, int])]
        round_counter: int
        short_form: str
        team_key: int

        def key_finder(poke: PokemonBase, criterion: str) -> int:
            """ Helper method to find the key value for ListItem when returning Pokemon to their team.
            :param poke:        A Pokemon returning into it's team's ArraySortedList
            :param criterion:   The criterion chosen by the Pokemon's trainer
            :return:            Returns the Pokemon's key to create a ListItem object
            :complexity:        BC & WC - O(IsIns)
            :pre:               Input poke is a valid Pokemon
            :raises ValueError: When input poke is an invalid Pokemon
            :raises ValueError: When input criterion is an invalid Pokemon
                                - This is raised after going through all conditional statements
                                - Hence, it is not a pre condition

            --------------------------------------------------------------
            METHODS CALLED            |  COMPLEXITY    |     REMARKS
            --------------------------|----------------|------------------
            isinstance()              |  O(IsIns)      |
            PokemonBase.get_attack()  |  O(1)          |
            PokemonBase.get_defence() |  O(1)          |
            PokemonBase.get_hp()      |  O(1)          |
            PokemonBase.get_level     |  O(1)          |
            PokemonBase.get_speed()   |  O(1)          |
            --------------------------|----------------|------------------
            --------------------------------------------------------------
            """
            # Checking pre condition(s)
            if not isinstance(poke, PokemonBase):
                raise ValueError("".join(["'Invalid input poke! poke = ", str(poke)]))

            # Finding appropriate key based on input criterion
            if criterion == "Level":
                return poke.get_level()
            elif criterion == "HP":
                return poke.get_hp()
            elif criterion == "Attack":
                return poke.get_attack()
            elif criterion == "Defence":
                return poke.get_defence()
            elif criterion == "Speed":
                return poke.get_speed()

            # Invalid input criterion
            else:
                raise AssertionError("".join(["Invalid criterion value! criterion = ", str(criterion)]))

        # Initialising battle_mode attribute using mutator method
        self.set_battle_mode(2)

        # Assigning teams to both trainers
        print("Trainer 1 chooses their team!")
        self.team1.choose_team(self.battle_mode, criterion_team1)
        print("Trainer 2 chooses their team!")
        self.team2.choose_team(self.battle_mode, criterion_team2)

        # Dictionaries are used to keep track of the Pokemons original indices
        # This is used so when sorting returning Pokemons, their relative positions are maintained
        #   so that the sorting algorithm is stable
        poke_dict_1 = {self.team1.team[ind].value: ind for ind in range(len(self.team1.team))}
        poke_dict_2 = {self.team2.team[ind].value: ind for ind in range(len(self.team2.team))}

        # Some fancy printing stuff
        nested_poke_list = self.pretty_printing(self.team1.team, self.team2.team)
        round_counter = 1

        # If either of the teams have a MissingNo in their team, do_check is set to True
        #   so that the code will check The Condition
        if do_check := "M1" in nested_poke_list[0] or "M1" in nested_poke_list[1]:
            ORIGINAL_TEAM_1_SIZE = len(self.team1.team)
            ORIGINAL_TEAM_2_SIZE = len(self.team2.team)
            pokes_battled_1, pokes_battled_2 = [None], [None]  # None is a placeholder to represent MissingNo in Team

        while len(self.team1.team) and len(self.team2.team):
            print("".join(["Round ", str(round_counter), ": "]), end="")
            round_counter += 1

            # Getting Pokemon from teams
            if do_check:
                # This loop checks if the Pokemon is a MissingNo
                # If it is then, it will need to check if the other Pokemons in its team have battled already or not.
                for team_index in range(2):
                    poke_team = self.team2.team if team_index else self.team1.team
                    last_ind = len(poke_team) - 1
                    i = 0

                    # If the next pokemon is a MissingNo
                    # Then check if all other Pokemons in its team have battled already
                    if isinstance(poke_team[last_ind].value, MissingNo) \
                            and (not team_index and len(pokes_battled_1) < ORIGINAL_TEAM_1_SIZE
                                 or team_index and len(pokes_battled_2) < ORIGINAL_TEAM_2_SIZE):
                        i = 1
                    Battle.poke_print_index[team_index] = i
                    pokemon = poke_team.delete_at_index(last_ind - i).value

                    # team1's Pokemon
                    if not team_index:
                        poke_1 = pokemon
                        if pokemon not in pokes_battled_1:
                            pokes_battled_1.append(pokemon)

                    # team2's Pokemon
                    elif team_index:
                        poke_2 = pokemon
                        if pokemon not in pokes_battled_2:
                            pokes_battled_2.append(pokemon)

                    # Invalid team_index value
                    else:
                        raise AssertionError("".join(["Invalid team_index value! team_index = ", str(team_index)]))

                # To prevent unnecessary checking of The Condition
                do_check = len(pokes_battled_1) >= ORIGINAL_TEAM_1_SIZE and len(pokes_battled_2) >= ORIGINAL_TEAM_2_SIZE

            # No need to check The Condition
            else:
                poke_1 = self.team1.team.delete_at_index(len(self.team1.team) - 1).value
                poke_2 = self.team2.team.delete_at_index(len(self.team2.team) - 1).value

            res = self.single_round_fight(poke_1, poke_2, nested_poke_list)

            # Still None fainted
            if res == "Draw":
                return_to_team = [(poke_1, 0), (poke_2, 1)]

            # poke2 fainted
            elif res == poke_1:
                return_to_team = [(poke_1, 0)]

            # poke1 fainted
            elif res == poke_2:
                return_to_team = [(poke_2, 1)]

            # Both poke faint during last battle
            elif res is None:
                return_to_team = []

            else:
                raise AssertionError("".join(["Invalid res value! res = ", str(res)]))

            # Returning Pokemons that did not faint
            for return_poke, team_key in return_to_team:
                team_criterion = self.get_team2().get_criterion() if team_key else self.get_team1().get_criterion()  # Getting criterion
                poke_key = key_finder(return_poke, team_criterion)  # Getting key for Pokemon
                return_item = ListItem(return_poke, poke_key)  # Creating returning ListItem

                short_form = nested_poke_list[team_key].pop(
                    Battle.poke_print_index[team_key])  # Getting short_form from list
                last_ind = self.team2.team.new_add(return_item, poke_dict_2) if team_key \
                    else self.team1.team.new_add(return_item, poke_dict_1)  # Getting new index of Pokemon

                i = len(nested_poke_list[team_key]) - last_ind  # Getting new index in list
                nested_poke_list[team_key].insert(i, short_form)  # Putting back short form in list

            Battle.poke_print_index = [0, 0]

        # Determining which trainer won (if any, else Draw)
        if len(self.team1.team) or len(self.team2.team):
            return self.team1.get_trainer_name() if len(self.team1.team) else self.team2.get_trainer_name()
        else:
            return "Draw"

    def modularised_battle(self, battle_mode: int):
        """ A modularised version of set_mode_battle and rotating_mode_battle
        :param:             The current battle_mode value.
        :return:            The trainer who won the battle (if any, else Draw).
        :complexity:        O(R + IsIns)
        :pre:               Input battle_value must be 0 or 1.
        :raises ValueError: When input battle_mode is not 0 or 1.

        ---------------------------------------------------------------------------------------------
        METHODS CALLED                  COMPLEXITY      REMARKS
        ----------------------------|---------------|------------------------------------------------
        self.pretty_printing()      |   O(IsIns)    |   IsIns: refer to method called
        self.set_battle_mode()      |   O(IsIns)    |   IsIns: refer to method called
        self.return_to_team()       |   O(IsIns)    |   IsIns: refer to method called
        self.single_round_fight()   |   O(IsIns)    |   IsIns: refer to method called
        str.__eq__(string)          |   O(eq)       |   where eq = len(string). Here, eq = 4 -> O(1)
        str.join(List[])            |   O(join)     |   where join = len(List[]). Here, join = 2
        PokeTeam.get_trainer_name() |   O(1)        |
        self.access()               |   O(1)        |
        self.get_battle_mode()      |   O(1)        |
        ----------------------------|---------------|------------------------------------------------
        ---------------------------------------------------------------------------------------------

        Note:
            - During checking of pre condition, the function does use the in keyword.
                But since the list only 2 items, the complexity is simply O(1).
            - This method uses List slicing and combining. However, since the lists have a maximum length of 6,
                the complexity reduces to O(1) only for List slicing and combining.
            - The two teams fight until either one of them run out of Pokemons.
                This means the main while loop will run R times.
                    where R is the total number of rounds which the battle lasts for.
        """
        # Type hinting
        nested_poke_list: List[List[str]]
        poke_1: PokemonBase
        poke_2: PokemonBase
        res: (PokemonBase, str)
        round_counter: int

        # Checking pre condition(s)
        if battle_mode not in [0, 1]:
            raise ValueError("".join(["Invalid battle_mode value for modularised_battle! battle = ", str(battle_mode)]))

        # Initialising battle_mode
        self.set_battle_mode(battle_mode)

        # Assigning teams to both trainers
        print("Trainer 1 chooses their team!")
        self.team1.choose_team(self.get_battle_mode())
        print("Trainer 2 chooses their team!")
        self.team2.choose_team(self.get_battle_mode())

        # Some fancy printing stuff
        nested_poke_list = self.pretty_printing(self.team1.team, self.team2.team)
        round_counter = 1

        # Main battle loop until at least 1 team runs out of Pokemons
        while len(self.team1.team) and len(self.team2.team):
            print("".join(["Round ", str(round_counter), ": "]), end="")  ##
            round_counter += 1

            # Getting Pokemons from each team
            poke_1 = self.access(self.team1.team)
            poke_2 = self.access(self.team2.team)

            # They fight!
            res = self.single_round_fight(poke_1, poke_2, nested_poke_list)

            # poke2 fainted
            if res == poke_1:
                self.return_to_team(self.team1.team, poke_1)

                if self.get_battle_mode() == 1 and len(nested_poke_list[0]) > 1:
                    nested_poke_list[0] = nested_poke_list[0][1:] + [nested_poke_list[0][0]]

            # poke1 fainted
            elif res == poke_2:
                self.return_to_team(self.team2.team, poke_2)

                if self.get_battle_mode() == 1 and len(nested_poke_list[1]) > 1:
                    nested_poke_list[1] = nested_poke_list[1][1:] + [nested_poke_list[1][0]]

            # None fainted
            elif res == "Draw":
                self.return_to_team(self.team1.team, poke_1)
                self.return_to_team(self.team2.team, poke_2)

                if self.get_battle_mode() == 1:
                    if len(nested_poke_list[0]) > 1:
                        nested_poke_list[0] = nested_poke_list[0][1:] + [nested_poke_list[0][0]]
                    if len(nested_poke_list[1]) > 1:
                        nested_poke_list[1] = nested_poke_list[1][1:] + [nested_poke_list[1][0]]

        # Determining which trainer won (if any, else Draw)
        if not len(self.team1.team) and not len(self.team2.team):
            return "Draw"
        else:
            return self.team1.get_trainer_name() if len(self.team1.team) else self.team2.get_trainer_name()