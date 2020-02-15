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
        hash_table_insert(ht, tickets[index].source, tickets[index].destination)
        # print(ht,tickets[index].source, tickets[index].destination)
        route[0] = hash_table_retrieve(ht, 'NONE')

    for j in range(1, length-1):
            route[j] = hash_table_retrieve(ht, route[j-1])

    route.pop()
    return route