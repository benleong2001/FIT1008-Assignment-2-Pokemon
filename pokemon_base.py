""" PokemonBase
Group:      T05G04
Members:    Lee Sing Yuan
            Benjamin Leong Tjen Ho
            Lim Jing Kai
            Loh Zhun Guan

Description:
    This file consists of one abstract class only, PokemonBase.
    It is an abstract class which contains methods and attribute that all Pokemons have.
    The only methods implemented in this class are methods which generally function the same for all Pokemons.
        (They can still be overridden to add additional functionalities to the method(s).)

    Pre conditions are not checked in __init__ as they will be checked in the respective attribute mutators.

    There are two extra methods which are not required in this Assignment:
        _get_name(): To get the name of the class (or Pokemon).     (@classmethod)
        is_alive():  To check if a Pokemon is still alive.

Side note:
    The format for docstring documentation:
        For methods:                                 |  For classes:
            :param:                                  |      Short Description
            :return:                                 |      Attribute(s):
            :complexity: BC - Best Case Complexity   |          Attribute 1
                         WC - Worst Case Complexity  |          Attribute 2
            :pre:                                    |          ...
            :raises Exception:                       |
                                                     |      Class Variable(s):
            Note:                                    |          Class Variable 1
                 *Note here*                         |          Class Variable 2
                                                     |          ...
            (This format applies for all files)

    Classes and Methods also start of with type hints to indicate what are the types of variables in the Class/Method
        (if applicable)
"""

from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Final

Numeric = (int, float)


class PokemonBase(ABC):
    """ Abstract class for Pokemons.

    Attribute(s):
            level (int):           The current level of the Pokemon.
            hp (int):              The amount of hp which the Pokemon currently has.
            poke_type (str):       The poke_type of the Pokemon.

    Class Variable(s):
            BASE_LEVEL (int) = 1:  The level which every Pokemon starts with.
    """
    # Class Variable(s)
    BASE_LEVEL: Final[int] = 1

    def __init__(self, hp: int, poke_type: str) -> None:
        """ Basic PokemonBase object initialiser.
        :param hp:          Input value to be used as initial hp value.
        :param poke_type:   Input value to be used as initial value of poke_type.
        :return:            None
        :complexity:        BC & WC - O(IsIns)

        -------------------------------------------------------------------------------
        METHODS CALLED       |  COMPLEXITY      |   REMARKS
        ---------------------|------------------|--------------------------------------
        self.set_hp()        |  O(IsIns)        |   IsIns: refer to method called
        self.set_level()     |  O(IsIns)        |   IsIns: refer to method called
        self.set_poke_type() |  O(1)            |
        ---------------------|------------------|--------------------------------------
        -------------------------------------------------------------------------------
        """
        # Initialising the Pokemon's instance variables
        self.set_level(PokemonBase.BASE_LEVEL)
        self.set_hp(hp)
        self.set_poke_type(poke_type)

    def __str__(self) -> str:
        """ Magic method constructing a string representation of the Pokemon.
        :return:        Returns the Pokemon object's string representation.
        :complexity:    BC & WC - O(1)

        ------------------------------------------------------------------------------------------------------
        METHODS CALLED      |  COMPLEXITY  |   REMARKS
        --------------------|--------------|------------------------------------------------------------------
        int.__str__()       |  O(i_str)    |   where i_str = number of digits of int. Here, n = 1 -> O(1)
        float.__str__()     |  O(f_str)    |   where f_str = number of digits of float. Here, n <= 2 -> O(1)
        str.join(List[])    |  O(join)     |   where join = len(List[]). Here, n = 5 -> O(1)
        --------------------|--------------|------------------------------------------------------------------
        ------------------------------------------------------------------------------------------------------
        """
        h = str(int(self.get_hp())) if self.get_hp() == int(self.get_hp()) else str(int(self.get_hp() * 10) / 10)
        return "".join([self._get_name(), "'s HP = ", h, " and level = ", str(self.get_level())])

    @classmethod
    def _get_name(cls) -> str:
        """ Class method to get the name of the class (i.e., the name of the Pokemon).
        :return:        Returns the Pokemon object's name
        :complexity:    BC & WC - O(1)
        """
        return cls.__name__

    def set_level(self, level: int) -> None:
        """ Mutator for level attribute of a Pokemon.
        :param level:       Input value to set the Pokemon's level as.
        :return:            None
        :complexity:        BC & WC - O(IsIns)
        :pre:               Input level must be a positive integer value.
        :raises Exception:  When input level is not an integer or has a non-negative value.

        -----------------------------------------------------------------------------------
        METHODS CALLED       |  COMPLEXITY  |   REMARKS
        ---------------------|--------------|----------------------------------------------
        isinstance()         |  O(IsIns)    |
        ---------------------|--------------|----------------------------------------------
        -----------------------------------------------------------------------------------
        """
        # Checking for pre-condition(s)
        if isinstance(level, bool) or not isinstance(level, int) or level <= 0:
            raise ValueError("".join(["Invalid level value! level = ", str(level)]))

        # Initialising Pokemon's attribute, level
        self.level = level

    def set_hp(self, hp: int) -> None:
        """ Mutator for hp attribute of a Pokemon.
        :param hp:          Input value to set the Pokemon's hp as.
        :return:            None
        :complexity:        BC & WC - O(IsIns)
        :pre:               Input hp must be a positive integer value.
        :raises Exception:  When input hp value is invalid.

        -----------------------------------------------------------------------------------
        METHODS CALLED       |  COMPLEXITY  |   REMARKS
        ---------------------|--------------|----------------------------------------------
        isinstance()         |  O(IsIns)    |
        ---------------------|--------------|----------------------------------------------
        -----------------------------------------------------------------------------------
        """
        # Checking for pre-condition(s)
        if isinstance(hp, bool) or not isinstance(hp, Numeric):
            raise ValueError("".join(["Invalid hp value! hp = ", str(hp)]))

        # Initialising Pokemon's attribute, hp
        self.hp = hp

    def set_poke_type(self, poke_type: str) -> None:
        """ Mutator for poke_type attribute of a Pokemon.
        :param poke_type:   Input value to set the Pokemon's poke_type as.
        :return:            None
        :complexity:        BC & WC - O(1)
        :pre:               Input poke_type must be one of "Fire", "Grass", "Water", None.
        :raises Exception:  When input poke_type value is invalid.

        Note:
            During checking of pre condition, the function does use the 'in' keyword.
            But since the list only has 4 items, the complexity is simply O(1).
        """
        # Checking for pre-condition(s)
        poke_types = ["Fire", "Grass", "Water", None]
        if poke_type not in poke_types:
            raise ValueError("".join(["Invalid poke_type value! poke_type = ", str(poke_type)]))

        # Initialising Pokemon's attribute, poke_type
        self.poke_type = poke_type

    def get_level(self) -> int:
        """ Accessor for level attribute of a Pokemon.
        :return:        Returns the level of the Pokemon.
        :complexity:    BC & WC - O(1)
        """
        return self.level

    def get_hp(self) -> int:
        """ Accessor for hp attribute of a Pokemon.
        :return:        Returns the hp of the Pokemon.
        :complexity:    BC & WC - O(1)
        """
        return self.hp

    def get_poke_type(self) -> str:
        """ Accessor for poke_type attribute of a Pokemon.
        :return:        Returns the poke_type of the Pokemon.
        :complexity:    BC & WC - O(1)
        """
        return self.poke_type

    @abstractmethod
    def get_attack(self) -> int:
        """ Accessor for attack stat of a Pokemon """
        raise NotImplementedError("Abstract method is not implemented!")

    @abstractmethod
    def get_defence(self) -> int:
        """ Accessor for defence stat of a Pokemon """
        raise NotImplementedError("Abstract method is not implemented!")

    @abstractmethod
    def get_speed(self) -> int:
        """ Accessor for speed stat of a Pokemon """
        raise NotImplementedError("Abstract method is not implemented!")

    @abstractmethod
    def calc_dmg(self, attacker: PokemonBase) -> int:
        """ Method to calculate damage taken by an attacking Pokemon, attacker
        :param attacker:    An attacking Pokemon.
        :pre:               Input attacker must be a valid Pokemon.
        :raises Exception:  When input attacker is not a valid Pokemon.

        ------------------------------------------------
        METHODS CALLED      |  COMPLEXITY  |  REMARKS
        --------------------|--------------|------------
        isinstance()        |  O(IsIns)    |
        --------------------|--------------|------------
        ------------------------------------------------

        Note:
            Since this is just an abstract method, it is only used to check for pre condition(s).
        """
        # Checking pre condition(s)
        if not isinstance(attacker, PokemonBase):
            raise ValueError("".join(["Invalid attacking Pokemon! attacker = ", str(attacker)]))

    # Extra Method
    def is_alive(self) -> bool:
        """ Method to check if the Pokemon is alive or not.
        :return:        Returns a boolean which states if the Pokemon is alive or not.
                        (True -> Alive, False -> Fainted)
        :complexity:    BC & WC - O(1)

        -----------------------------------------------
        METHODS CALLED  |   COMPLEXITY  |   REMARKS
        ----------------|---------------|--------------
        self.get_hp()   |     O(1)      |
        ----------------|---------------|--------------
        -----------------------------------------------

        Note:
            It uses the hp of the Pokemon to determine if the Pokemon is alive or not
        """
        return self.get_hp() > 0
