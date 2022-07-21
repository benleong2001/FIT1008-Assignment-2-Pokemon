"""
    Array-based implementation of SortedList ADT.
    Items to store should be of time ListItem.
"""

from referential_array import ArrayR
from sorted_list import *

from pokemon_base import PokemonBase

__author__ = 'Maria Garcia de la Banda and Brendon Taylor. Modified by Alexey Ignatiev and Graeme Gange'
__docformat__ = 'reStructuredText'


class ArraySortedList(SortedList[T]):
    """ SortedList ADT implemented with arrays. """
    MIN_CAPACITY = 1

    def __init__(self, max_capacity: int) -> None:
        """ ArraySortedList object initialiser. """

        # first, calling the basic initialiser
        SortedList.__init__(self)

        # initialising the internal array
        size = max(self.MIN_CAPACITY, max_capacity)
        self.array = ArrayR(size)

    def __str__(self):
        """ Magic method constructing a string representation of the ArraySortedList.
        :return:        Returns the ArraySortedList object's string representation.
        :complexity:    BC & WC - O(IsIns * len(self))

        METHODS CALLED          |   COMPLEXITY  |   REMARKS
        ------------------------|---------------|------------------------------------------------------
        isinstance()            |   O(IsIns)    |
        str.join(List[])        |   O(n)        |   where n = len(List[]) (in this case, n = len(self))
        PokemonBase.__str__()   |   O(1)        |
        PokemonBase.is_alive()  |   O(1)        |
        """
        return ", ".join([str(x.value) if isinstance(x.value, PokemonBase) and x.value.is_alive() else str(x) for x in
                          self.array[len(self) - 1::-1]])

    def reset(self):
        """ Reset the list. """
        SortedList.__init__(self)

    def __getitem__(self, index: int) -> T:
        """ Magic method. Return the element at a given position. """
        return self.array[index]

    def __setitem__(self, index: int, item: ListItem) -> None:
        """ Magic method. Insert the item at a given position,
            if possible (!). Shift the following elements to the right.
        """
        if self.is_empty() or \
                (index == 0 and item.key <= self[index].key) or \
                (index == len(self) and self[index - 1].key <= item.key) or \
                (index > 0 and self[index - 1].key <= item.key <= self[index].key):

            if self.is_full():
                self._resize()

            self._shuffle_right(index)
            self.array[index] = item
        else:
            # the list isn't empty and the item's position is wrong wrt. its neighbourghs
            raise IndexError('Element should be inserted in sorted order')

    def __contains__(self, item: ListItem):
        """ Checks if value is in the list. """
        for i in range(len(self)):
            if self.array[i] == item:
                return True
        return False

    def _shuffle_right(self, index: int) -> None:
        """ Shuffle items to the right up to a given position. """
        for i in range(len(self), index, -1):
            self.array[i] = self.array[i - 1]

    def _shuffle_left(self, index: int) -> None:
        """ Shuffle items starting at a given position to the left. """
        for i in range(index, len(self)):
            self.array[i] = self.array[i + 1]

    def _resize(self) -> None:
        """ Resize the list. """
        # doubling the size of our list
        new_array = ArrayR(2 * len(self.array))

        # copying the contents
        for i in range(self.length):
            new_array[i] = self.array[i]

        # referring to the new array
        self.array = new_array

    def delete_at_index(self, index: int) -> ListItem:
        """ Delete item at a given position. """
        if index >= len(self):
            raise IndexError('No such index in the list')
        item = self.array[index]
        self.length -= 1
        self._shuffle_left(index)
        return item

    def index(self, item: ListItem) -> int:
        """ Find the position of a given item in the list. """
        pos = self._index_to_add(item)
        if pos < len(self) and self[pos] == item:
            return pos
        raise ValueError('item not in list')

    def is_full(self):
        """ Check if the list is full. """
        return len(self) >= len(self.array)

    def add(self, item: ListItem) -> None:
        """ Add new element to the list. """
        if self.is_full():
            self._resize()

        # find where to place it
        position = self._index_to_add(item)

        self[position] = item
        self.length += 1

    def _index_to_add(self, item: ListItem) -> int:
        """ Find the position where the new item should be placed. """
        low = 0
        high = len(self) - 1

        while low <= high:
            mid = (low + high) // 2
            if self[mid].key < item.key:
                low = mid + 1
            elif self[mid].key > item.key:
                high = mid - 1
            else:
                return mid

        return low

    # ADDED METHODS
    def _new_index_to_add(self, item: ListItem, ori_dict: dict[PokemonBase, int]) -> int:
        """ New method to find the position where the new item should be placed.
        :param item:        The returning item.
        :param ori_dict:    A dictionary with the Pokemons as keys and their original index as values.
        :return:            Returns the index to add the item in.
        :complexity:        BC - O(1), when the index is found immediately
                            WC - O(n), when the index is found after looping through the entire array.
                                       where n is len(self)
        :pre:               Input item must be a ListItem object.
        :raises ValueError: When input item is not a ListItem object.

        Note:
            This method does not use binary search because I would like to prioritise the stability of the algorithm
            instead of efficiency.
            (The arrays have small lengths anyways so the time complexity will not be that high using this algorithm)
        """
        # Checking pre condition(s)
        if not isinstance(item, ListItem):
            raise ValueError(f'Input item must be a ListItem! item = {item}')

        # Finding index by searching from low index to high index
        for _ in range(len(self)):
            # If there is tie between the keys of the items,
            #   the items will check their original indices in order to maintain their relative positions
            if self[_].key > item.key\
                    or ori_dict and self[_].key == item.key \
                    and ori_dict.get(self[_].value) > ori_dict.get(item.value):
                return _
        return len(self)

    def new_add(self, item: ListItem, ori_dict: dict[PokemonBase, int] = None) -> int:
        """ New method to add new element to the list.
        :param item:        The returning item.
        :param ori_dict:    (Optional) A dictionary with the Pokemons as keys and their original index as values.
        :return:            Returns the index to add the item in.
        :complexity:        BC - O(1), when the index is found immediately
                            WC - O(n), when the index is found after looping through the entire array
                                       where n is len(self)
        :pre:               Input item must be a ListItem object.
        :raises ValueError: When input item is not a ListItem object.

        Note:
            Pre condition is checked when _new_index_to_add() method is invoked.
            This is a copy of the previous add() method but using _new_index_to_add() instead of _index_to_add().
        """
        if self.is_full():
            self._resize()

        # find where to place it
        position = self._new_index_to_add(item, ori_dict)

        self[position] = item
        self.length += 1
        return position
