#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    ht = HashTable(length)
    route = [None] * length

    """
    YOUR CODE HERE
    """

    for index in range(length):
        if tickets[index].source == 'NONE':
            route[0] = tickets[index].destination 
        hash_table_insert(ht, tickets[index].source, tickets[index].destination)
        # print(ht,tickets[index].source, tickets[index].destination)

    for i in range(length):
        if route[i-1] is not None:
            # get next array value by sending the key (source) and getting back the value (destination)
            route[i] = hash_table_retrieve(ht, route[i-1])

    return route