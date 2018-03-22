import os
import sys

# from hashtable import HashTable
from binarytree import BinarySearchTree

file_of_numbers = "data/phone-numbers-1000.txt"
file_of_costs = "data/route-costs-106000.txt"


def _path_for(relative_path):
    """return the absolute path from the script path and appending the relative_path"""

    script_dir = os.path.dirname(__file__)
    abs_file_path = os.path.join(script_dir, relative_path)

    return abs_file_path


class CostNode(object):

    def __init__(self, prefix, cost):
        self.prefix = prefix
        self.cost = cost

    def __eq__(self, other):
        return self.prefix == other.prefix

    def __lt__(self, other):
        return self.prefix < other.prefix

    def __gt__(self, other):
        return self.prefix > other.prefix

    def __str__(self):
        return "[{}, {}]".format(self.prefix, self.cost)

    def __repr__(self):
        return "[{}, {}]".format(self.prefix, self.cost)


def _map_route_costs():
    """create a tree to store the prefix and cost of the routes cost"""
    with open(_path_for(file_of_costs)) as f_costs:

        # list of "+123456,0.02"
        arr_routes = f_costs.read().splitlines()

        tree_costs = BinarySearchTree()
        for a_route in arr_routes:

            # create a node with prefix, cost key-value pair
            a_route_key, a_route_cost = a_route.split(',')
            node_cost = CostNode(a_route_key, a_route_cost)

            tree_costs.insert(node_cost)

    return tree_costs


def cost_of_number(number):
    """Find the longest match of the number given by searching the tree and
    stopping where a match is found
    """
    longest_match_key = None
    cost = 0

    # TODO: search by trimming the number one by one until a match is found
    for a_route in routes_costs_keys:
        if number.startswith(a_route.prefix):
            if longest_match_key is None:
                longest_match_key = a_route.prefix
                cost = a_route.cost
            else:
                if len(a_route.prefix) > len(longest_match_key):
                    longest_match_key = a_route.prefix
                    cost = a_route.cost
        else:
            print 'bad:', repr(number), repr(a_route.prefix)
    #

    return cost


if __name__ == "__main__":

    os.remove(_path_for("data/routes-costs-output.txt"))

    import time

    start = time.time()

    # store the route costs into key-value pairs (prefix, cost)
    routes_costs = _map_route_costs()
    routes_costs_keys = routes_costs.items_in_order()

    # print cost_of_number("+8163975")

    # create a list of the numbers to check the cost of
    with open(_path_for(file_of_numbers)) as f_numbers_to_call:
        phone_numbers_to_call = f_numbers_to_call.read().splitlines()

    zero = 0
    costs = 0
    for a_number in phone_numbers_to_call:
        cost_value = cost_of_number(a_number)

        with open(_path_for("data/routes-costs-output.txt"), 'a') as f:
            f.write(a_number + ',' + str(cost_value) + '\n')

        if cost_value == 0:
            zero += 1
        else:
            costs += 1

    print routes_costs_keys

    end = time.time()

    print (end - start)

    # 9460 - 1340
    print zero, "-", costs
        # print("{},{}".format(a_number, cost_value))
