""" Pokemons - Charmander, Bulbasaur, Squirtle, GlitchMon, MissingNo
Group:      T05G04
Members:    Lee Sing Yuan
            Benjamin Leong Tjen Ho
            Lim Jing Kai
            Loh Zhun Guan

Description:
    This file has the basic implementations of the Pokemons (and GlitchMons).
    It consists of 5 classes:
        - Charmander
        - Bulbasaur
        - Squirtle
        - GlitchMon (Abstract Class)
        - MissingNo
    Each of the non abstract classes implement the abstract methods from PokemonBase.
    The abstract class (GlitchMon) introduces 2 new methods which MissingNo inherits:
        - up_hp()
        - superpower()
"""

from pokemon_base import PokemonBase

from abc import ABC
from random import randint
from typing import Final

NoneType = type(None)


class Charmander(PokemonBase):
    """ Implementation of PokemonBase to represent the Pokemon Charmander.

    Attribute(s):
            level (int):            The current level of the Charmander.
            hp (int):               The amount of hp which the Charmander currently has.
            poke_type (str):        The poke_type of the Charmander.

    Class Variable(s):
            BASE_POKE_TYPE (str):   The poke_type of every Charmander.
            BASE_HP (int):          The hp which every Charmander starts with.
            BASE_ATTACK (int):      The attack stat every Charmander starts with (not considering level).
            BASE_DEFENCE (int):     The defence stat every Charmander starts with.
            BASE_SPEED (int):       The speed stat every Charmander starts with (not considering level).
    """
    # Class Variable(s)
    BASE_POKE_TYPE: Final[str] = "Fire"
    BASE_HP: Final[int] = 7
    BASE_ATTACK: Final[int] = 6
    BASE_DEFENCE: Final[int] = 4
    BASE_SPEED: Final[int] = 7

    def __init__(self, hp: int = BASE_HP, poke_type: str = BASE_POKE_TYPE) -> None:
        """ Basic Charmander object initialiser.
        :param hp:          (Optional) Input value to be used as initial hp (default value = BASE_HP = 7).
        :param poke_type:   (Optional) Input value to be used as initial poke_type (default value = BASE_POKE_TYPE = "Fire").
        :return:            None
        :complexity:        BC & WC - O(IsIns)

        ------------------------------------------------------------------------
        METHODS CALLED          |  COMPLEXITY    | REMARKS
        ------------------------|----------------|------------------------------
        PokemonBase.__init__()  |  O(IsIns)      | IsIns: refer to method called
        ------------------------|----------------|------------------------------
        ------------------------------------------------------------------------
        """
        PokemonBase.__init__(self, hp, poke_type)

    # Overriding Accessor Methods
    def get_attack(self) -> int:
        """ Overriding Accessor method for attack stat.
        :return:        Returns the Charmander attack stat value.
        :complexity:    BC & WC - O(1)

        --------------------------------------------------
        METHODS CALLED      |  COMPLEXITY  |   REMARKS
        --------------------|--------------|--------------
        self.get_level()    |  O(1)        |
        --------------------|--------------|--------------
        --------------------------------------------------
        """
        return Charmander.BASE_ATTACK + self.get_level()

    def get_defence(self) -> int:
        """ Overriding Accessor method for defence stat.
        :return:        Returns the Charmander defence stat value.
        :complexity:    BC & WC - O(1)
        """
        return Charmander.BASE_DEFENCE

    def get_speed(self) -> int:
        """ Overriding Accessor method for speed stat.
        :return:        Returns the Charmander speed stat value.
        :complexity:    BC & WC - O(1)

        -------------------------------------------------
        METHODS CALLED      |  COMPLEXITY  |   REMARKS
        --------------------|--------------|-------------
        self.get_level()    |  O(1)        |
        --------------------|--------------|-------------
        -------------------------------------------------
        """
        return Charmander.BASE_SPEED + self.get_level()

    # Other Method(s)
    def calc_dmg(self, attacker: PokemonBase) -> int:
        """ Method to calculate damage taken by an attacking Pokemon, attacker.
        :param attacker:    An attacking Pokemon.
        :return:            Returns the amount of effective damage the Charmander would receive from attacker.
        :complexity:        BC & WC - O(IsIns)
        :pre:               Input attacker must be a valid Pokemon.
        :raises Exception:  When input attacker is not a valid Pokemon.

        ----------------------------------------------------------------------------------
        METHODS CALLED          |  COMPLEXITY  |    REMARKS
        ------------------------|--------------|----------------------------------------------
        PokemonBase.calc_dmg()  |  O(IsIns)    |    IsIns: refer to method called
        str.__eq__(string)      |  O(eq)       |    where eq = len(string). Here, eq = 5 -> O(1)
        self.get_attack()       |  O(1)        |
        self.get_defence()      |  O(1)        |
        ------------------------|--------------|----------------------------------------------
        ----------------------------------------------------------------------------------
        """
        # Type hinting
        effective_dmg: int

        # Calling Parent's version of the method
        PokemonBase.calc_dmg(self, attacker)

        # Calculating effective damage
        if attacker.poke_type == "Grass":
            effective_dmg = attacker.get_attack() * 0.5
        elif attacker.poke_type == "Water":
            effective_dmg = attacker.get_attack() * 2
        else:
            effective_dmg = attacker.get_attack()

        return effective_dmg if effective_dmg > self.get_defence() else effective_dmg // 2


class Bulbasaur(PokemonBase):
    """ Implementation of PokemonBase to represent the Pokemon Bulbasaur.

    Attribute(s):
         level (int):               The current level of the Bulbasaur.
         hp (int):                  The amount of hp which the Bulbasaur currently has.
         poke_type (str):           The poke_type of the Bulbasaur.

    Class Variable(s):
         BASE_POKE_TYPE (str):      The poke_type of every Bulbasaur.
         BASE_HP (int):             The hp which every Bulbasaur starts with.
         BASE_ATTACK (int):         The attack stat every Bulbasaur starts with.
         BASE_DEFENCE (int):        The defence stat every Bulbasaur starts with.
         BASE_SPEED (int):          The speed stat every Bulbasaur starts with (not considering level).
    """
    # Class Variable(s)
    BASE_POKE_TYPE: Final[str] = "Grass"
    BASE_HP: Final[int] = 9
    BASE_ATTACK: Final[int] = 5
    BASE_DEFENCE: Final[int] = 5
    BASE_SPEED: Final[int] = 7

    def __init__(self, hp: int = BASE_HP, poke_type: str = BASE_POKE_TYPE) -> None:
        """ Basic Bulbasaur object initialiser.
        :param hp:          (Optional) Input value to be used as initial hp (default value = BASE_HP = 9).
        :param poke_type:   (Optional) Input value to be used as initial poke_type (default value = BASE_POKE_TYPE = "Grass").
        :return:            None
        :complexity:        BC & WC - O(IsIns)

        ------------------------------------------------------------------------
        METHODS CALLED          |  COMPLEXITY    | REMARKS
        ------------------------|----------------|------------------------------
        PokemonBase.__init__()  |  O(IsIns)      | IsIns: refer to method called
        ------------------------|----------------|------------------------------
        ------------------------------------------------------------------------
        """
        PokemonBase.__init__(self, hp, poke_type)

    # Overriding Accessor Methods
    def get_attack(self) -> int:
        """ Overriding Accessor method for attack stat.
        :return:        Returns the Bulbasaur attack stat value.
        :complexity:    BC & WC - O(1)
        """
        return Bulbasaur.BASE_ATTACK

    def get_defence(self) -> int:
        """ Overriding Accessor method for attack stat.
        :return:        Returns the Bulbasaur defence stat value.
        :complexity:    BC & WC - O(1)
        """
        return Bulbasaur.BASE_DEFENCE

    def get_speed(self) -> int:
        """ Overriding Accessor method for attack stat.
        :return:        Returns the Bulbasaur speed stat value.
        :complexity:    BC & WC - O(1)

        --------------------------------------------------
        METHODS CALLED      |  COMPLEXITY  |   REMARKS
        --------------------|--------------|--------------
        self.get_level()    |  O(1)        |
        --------------------|--------------|--------------
        --------------------------------------------------
        """
        return Bulbasaur.BASE_SPEED + self.get_level() // 2

    # Other Method(s)
    def calc_dmg(self, attacker: PokemonBase) -> int:
        """ Method to calculate damage taken by an attacking Pokemon, attacker.
        :param attacker:    An attacking Pokemon.
        :return:            Returns the amount of effective damage the Bulbasaur would receive from attacker.
        :complexity:        BC & WC - O(IsIns)
        :pre:               Input attacker must be a valid Pokemon.
        :raises Exception:  When input attacker is not a valid Pokemon.

        ----------------------------------------------------------------------------------------
        METHODS CALLED          |  COMPLEXITY  |    REMARKS
        ------------------------|--------------|------------------------------------------------
        PokemonBase.calc_dmg()  |  O(IsIns)    |    IsIns: refer to method called
        str.__eq__(string)      |  O(eq)       |    where eq = len(string). Here, eq = 5 -> O(1)
        self.get_attack()       |  O(1)        |
        self.get_defence()      |  O(1)        |
        ------------------------|--------------|------------------------------------------------
        ----------------------------------------------------------------------------------------
        """
        # Type hinting
        effective_dmg: int

        # Calling Parent's version of the method
        PokemonBase.calc_dmg(self, attacker)

        # Calculating effective damage
        if attacker.poke_type == "Water":
            effective_dmg = attacker.get_attack() * 0.5
        elif attacker.poke_type == "Fire":
            effective_dmg = attacker.get_attack() * 2
        else:
            effective_dmg = attacker.get_attack()

        return effective_dmg if effective_dmg > self.get_defence() + 5 else effective_dmg // 2


class Squirtle(PokemonBase):
    """ Implementation of PokemonBase to represent the Pokemon Squirtle.

    Attribute(s):
         level (int):           The current level of the Squirtle.
         hp (int):              The amount of hp which the Squirtle currently has.
         poke_type (str):       The poke_type of the Squirtle.

    Class Variable(s):
         BASE_POKE_TYPE (str):  The poke_type of every Squirtle.
         BASE_HP (int):         The hp which every Squirtle starts with.
         BASE_ATTACK (int):     The attack stat every Squirtle starts with (not considering level).
         BASE_DEFENCE (int):    The defence stat every Squirtle starts with (not considering level).
         BASE_SPEED (int):      The speed stat every Squirtle starts with.
    """
    BASE_POKE_TYPE: Final[str] = "Water"
    BASE_HP: Final[int] = 8
    BASE_ATTACK: Final[int] = 4
    BASE_DEFENCE: Final[int] = 6
    BASE_SPEED: Final[int] = 7

    def __init__(self, hp: int = BASE_HP, poke_type: str = BASE_POKE_TYPE) -> None:
        """ Basic Squirtle object initialiser.
        :param hp:          (Optional) Input value to be used as initial hp (default value = BASE_HP = 8).
        :param poke_type:   (Optional) Input value to be used as initial poke_type (default value = BASE_POKE_TYPE = "Water").
        :return:            None
        :complexity:        BC & WC - O(IsIns)

        -------------------------------------------------------------------------
        METHODS CALLED          |  COMPLEXITY    | REMARKS
        ------------------------|----------------|-------------------------------
        PokemonBase.__init__()  |  O(IsIns)      | IsIns: refer to method called
        ------------------------|----------------|-------------------------------
        -------------------------------------------------------------------------
        """
        PokemonBase.__init__(self, hp, poke_type)

    # Overriding Accessor Methods
    def get_attack(self) -> int:
        """ Overriding Accessor method for attack stat.
        :return:        Returns the Squirtle object's attack stat value.
        :complexity:    BC & WC - O(1)

        --------------------------------------------------
        METHODS CALLED      |  COMPLEXITY  |   REMARKS
        --------------------|--------------|--------------
        self.get_level()    |  O(1)        |
        --------------------|--------------|--------------
        --------------------------------------------------
        """
        return Squirtle.BASE_ATTACK + self.level // 2

    def get_defence(self) -> int:
        """ Overriding Accessor method for attack stat.
        :return:        Returns the Squirtle object's defence stat value.
        :complexity:    BC & WC - O(1)

        --------------------------------------------------
        METHODS CALLED      |  COMPLEXITY  |   REMARKS
        --------------------|--------------|--------------
        self.get_level()    |  O(1)        |
        --------------------|--------------|--------------
        --------------------------------------------------
        """
        return Squirtle.BASE_DEFENCE + self.level

    def get_speed(self) -> int:
        """ Overriding Accessor method for attack stat.
        :return:        Returns the Squirtle object's speed stat value.
        :complexity:    BC & WC - O(1)
        """
        return Squirtle.BASE_SPEED

    # Other Method(s)
    def calc_dmg(self, attacker: PokemonBase) -> int:
        """ Method to calculate damage taken by an attacking Pokemon, attacker.
        :param attacker:    An attacking Pokemon.
        :return:            Returns the amount of effective damage the Squirtle would receive from attacker.
        :complexity:        BC & WC - O(IsIns)
        :pre:               Input attacker must be a valid Pokemon.
        :raises Exception:  When input attacker is not a valid Pokemon.

        ----------------------------------------------------------------------------------------
        METHODS CALLED          |  COMPLEXITY  |    REMARKS
        ------------------------|--------------|------------------------------------------------
        PokemonBase.calc_dmg()  |  O(IsIns)    |    IsIns: refer to method called
        str.__eq__(string)      |  O(eq)       |    where eq = len(string). Here, eq = 5 -> O(1)
        self.get_attack()       |  O(1)        |
        self.get_defence()      |  O(1)        |
        ------------------------|--------------|------------------------------------------------
        ----------------------------------------------------------------------------------------
        """
        # Type hinting
        effective_dmg: int

        # Calling Parent's version of the method
        PokemonBase.calc_dmg(self, attacker)

        # Calculating effective damage
        if attacker.poke_type == "Fire":
            effective_dmg = attacker.get_attack() * 0.5
        elif attacker.poke_type == "Grass":
            effective_dmg = attacker.get_attack() * 2
        else:
            effective_dmg = attacker.get_attack()

        return effective_dmg if effective_dmg > self.get_defence() * 2 else effective_dmg // 2


class GlitchMon(PokemonBase, ABC):
    """ Abstract class for Glitched Pokemons.

    Attribute(s):
         level (int):       The current level of the GlitchMon.
         hp (int):          The amount of hp which the GlitchMon currently has.
         poke_type (str):   The poke_type of the GlitchMon.

    Class Variable(s):
         None
    """

    def __init__(self, hp: int, poke_type: str) -> None:
        """ Basic GlitchMon object initialiser.
        :param hp:          Input value to be used as initial hp.
        :param poke_type:   Input value to be used as initial poke_type.
        :return:            None
        :complexity:        BC & WC - O(IsIns)

        ------------------------------------------------------------------------
        METHODS CALLED          |  COMPLEXITY    | REMARKS
        ------------------------|----------------|------------------------------
        PokemonBase.__init__()  |  O(IsIns)      | IsIns: refer to method called
        ------------------------|----------------|------------------------------
        ------------------------------------------------------------------------
        """
        PokemonBase.__init__(self, hp, poke_type)

    # Extra Methods
    def up_hp(self) -> None:
        """ Extra Method to increase the GlitchMon object's hp by 1.
        :return:            None
        :complexity:        BC & WC - O(IsIns)
        :pre:               The GlitchMon needs to be alive.
        :raises Exception:  When the GlitchMon has already fainted.

        -----------------------------------------------------------------
        METHODS CALLED   |  COMPLEXITY   |  REMARKS
        -----------------|---------------|-------------------------------
        self.set_hp()    |  O(IsIns)     |  IsIns: refer to method called
        self.get_hp()    |  O(1)         |
        self.is_alive()  |  O(1)         |
        -----------------|---------------|-------------------------------
        -----------------------------------------------------------------
        """
        # Checking pre condition(s)
        if not self.is_alive():
            raise AssertionError("GlitchMon is not alive!")

        # Increasing hp value by 1
        self.set_hp(self.get_hp() + 1)

    def superpower(self) -> None:
        """ Extra Method that may be called when the GlitchMon has to defend.
        :return:            None
        :complexity:        BC & WC - O(IsIns)
        :pre:               The GlitchMon needs to be alive.
        :raises Exception:  When the GlitchMon has already fainted.

        -----------------------------------------------------------------------------------
        METHODS CALLED        | COMPLEXITY    | REMARKS
        ----------------------|---------------|--------------------------------------------
        self.up_hp()          | O(IsIns)      | IsIns: refer to method called (PokemonBase)
        self.set_level()      | O(IsIns)      | IsIns: refer to method called (PokemonBase)
        self.get_level()      | O(1)          |
        self.is_alive()       | O(1)          |
        random.randint(0, N)  | O(log N)      | Here, N = 2
        ----------------------|---------------|--------------------------------------------
        -----------------------------------------------------------------------------------
        """
        # Type hinting
        rand_int: int

        # Checking pre condition(s)
        if not self.is_alive():
            raise AssertionError("GlitchMon is not alive!")

        # Choosing a random integer from 0, 1 or 2
        rand_int = randint(0, 2)

        # Performing the superpower action depending on which integer was chosen
        if rand_int == 0:
            self.up_hp()
        elif rand_int == 1:
            self.set_level(self.get_level() + 1)
        elif rand_int == 2:
            self.up_hp()
            self.set_level(self.get_level() + 1)


class MissingNo(GlitchMon):
    """ Implementation of PokemonBase to represent the Pokemon MissingNo.
        Attribute(s):
         level (int):               The current level of the MissingNo.
         hp (int):                  The amount of hp which the MissingNo currently has.
         poke_type (str):           The poke_type of the MissingNo.

    Class Variable(s):
         BASE_POKE_TYPE (NoneType): The poke_type of every MissingNo.
         BASE_HP (int):             The hp which every MissingNo starts with.
         BASE_ATTACK (float):       The attack stat every MissingNo starts with (not considering level).
         BASE_DEFENCE (float):      The defence stat every MissingNo starts with (not considering level).
         BASE_SPEED (float):        The speed stat every MissingNo starts with (not considering level).

    """
    BASE_POKE_TYPE: Final[NoneType] = None
    BASE_HP: Final[int] = 8
    BASE_ATTACK: Final[float] = 13 / 3
    BASE_DEFENCE: Final[float] = 13 / 3
    BASE_SPEED: Final[float] = 19 / 3

    def __init__(self, hp: int = BASE_HP, poke_type: str = BASE_POKE_TYPE) -> None:
        """ Basic MissingNo object initialiser.
        :param hp:          (Optional) Input value to be used as initial hp (default value = BASE_HP = 8).
        :param poke_type:   (Optional) Input value to be used as initial poke_type (default value = BASE_POKE_TYPE = None).
        :return:            None
        :complexity:        BC & WC - O(IsIns)

        ---------------------------------------------------------------------
        METHODS CALLED       |  COMPLEXITY    | REMARKS
        ---------------------|----------------|------------------------------
        GlitchMon.__init__() |  O(IsIns)      | IsIns: refer to method called
        ---------------------|----------------|------------------------------
        ---------------------------------------------------------------------
        """
        GlitchMon.__init__(self, hp, poke_type)

    # Overriding Accessor Methods
    def get_attack(self) -> int:
        """ Overriding Accessor method for attack stat.
        :return:        Returns the MissingNo object's attack stat value.
        :complexity:    BC & WC - O(1)

        ------------------------------------------------
        METHODS CALLED      |  COMPLEXITY  |  REMARKS
        --------------------|--------------|------------
        self.get_level()    |  O(1)        |
        --------------------|--------------|------------
        ------------------------------------------------
        """
        return MissingNo.BASE_ATTACK + self.get_level()

    def get_defence(self) -> int:
        """ Overriding Accessor method for attack stat.
        :return:        Returns the MissingNo object's defence stat value.
        :complexity:    BC & WC - O(1)

        ------------------------------------------------
        METHODS CALLED      |  COMPLEXITY  |  REMARKS
        --------------------|--------------|------------
        self.get_level()    |  O(1)        |
        --------------------|--------------|------------
        ------------------------------------------------
        """
        return MissingNo.BASE_DEFENCE + self.get_level()

    def get_speed(self) -> int:
        """ Overriding Accessor method for attack stat.
        :return:        Returns the MissingNo object's speed stat value.
        :complexity:    BC & WC - O(1)

        -------------------------------------------------
        METHODS CALLED      |  COMPLEXITY  |  REMARKS
        --------------------|--------------|-------------
        self.get_level()    |  O(1)        |
        --------------------|--------------|-------------
        -------------------------------------------------
        """
        return MissingNo.BASE_SPEED + self.get_level()

    # Overriding Mutator Method
    def set_level(self, level: int) -> None:
        """ Overriding Mutator method for level stat.
        :param level:   Input value to set MissingNo's level as.
        :return:        None
        :complexity:    BC & WC - O(IsIns)
        :pre:           Input level must be a positive integer.
        :raises         Exception: When level is not an integer or is non-negative.

        -------------------------------------------------------------------------
        METHODS CALLED        | COMPLEXITY     |    REMARKS
        ----------------------|----------------|---------------------------------
        GlitchMon.set_level() | O(IsIns)       |    IsIns: refer to method called
        isinstance()          | O(IsIns)       |
        self.set_hp()         | O(IsIns)       |    IsIns: refer to method called
        self.get_level()      | O(1)           |
        self.get_hp()         | O(1)           |
        ----------------------|----------------|---------------------------------
        -------------------------------------------------------------------------

        """
        # Type hinting
        level_inc: int

        # Checking pre condition(s)
        if not isinstance(level, int) or level <= 0 or isinstance(level, bool):
            raise ValueError("".join(["Invalid level value! level = ", str(level)]))

        # If MissingNo is levelling up, its hp should increase too
        if level == 1:
            self.set_hp(MissingNo.BASE_HP)
        if level > 1:
            level_inc = level - self.get_level()
            self.set_hp(self.get_hp() + level_inc)
        GlitchMon.set_level(self, level)

    # Other Method(s)
    def calc_dmg(self, attacker: PokemonBase) -> int:
        """ Method to calculate damage taken by an attacking Pokemon, attacker.
        :param attacker:    An attacking Pokemon.
        :return:            Returns the amount of effective damage the MissingNo would receive from attacker.
        :complexity:        BC & WC - O(IsIns)
        :pre:               Input attacker must be a valid Pokemon.
        :raises Exception:  When input attacker is not a valid Pokemon.

        -----------------------------------------------------------------------
        METHODS CALLED          |  COMPLEXITY  |  REMARKS
        ------------------------|--------------|-------------------------------
        PokemonBase.calc_dmg()  |  O(IsIns)    |  IsIns: refer to method called
        self.get_attack()       |  O(1)        |
        self.get_defence()      |  O(1)        |
        random.randint(0,N)     |  O(log N)    |  Here, N = 2 -> O(1)
        ------------------------|--------------|-------------------------------
        -----------------------------------------------------------------------
        """
        # Type hinting
        defence: int
        rand_int: int

        # Calling Parent's version of the method
        PokemonBase.calc_dmg(self, attacker)

        # Choosing defence value
        rand_int = randint(0, 2)
        defence = [self.get_defence(), self.get_defence() + 5, self.get_defence() * 2][rand_int]

        return attacker.get_attack() if attacker.get_attack() > defence else attacker.get_attack() // 2