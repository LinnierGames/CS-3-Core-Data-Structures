import os
import sys

# from hashtable import HashTable
from binarytree import BinarySearchTree

file_of_numbers = "data/phone-numbers-10000.txt"
file_of_costs = "data/route-costs-100.txt"


def _path_for(relative_path):
    script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
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
    with open(_path_for(file_of_costs)) as f_costs:
        arr_routes = f_costs.read().split('\n')
        arr_routes = filter(lambda item: item != '', arr_routes)

        tree_costs = BinarySearchTree()

        print 'create tree'
        for a_route in arr_routes:
            a_route_split = a_route.split(',')
            a_route_key = a_route_split[0]
            a_route_cost = a_route_split[1]

            node_cost = CostNode(a_route_key, a_route_cost)
            tree_costs.insert(node_cost)

    print 'return tree'
    return tree_costs


def cost_of_number(number):

    longest_match_key = None

    for a_route in routes_costs_keys:
        if number.startswith(a_route.prefix):
            if longest_match_key is None:
                longest_match_key = a_route.prefix
            else:
                if len(a_route.prefix) > len(longest_match_key):
                    longest_match_key = a_route.prefix

    if longest_match_key is not None:
        return routes_costs.search(CostNode(longest_match_key, None)).cost
    else:
        return 0


if __name__ == "__main__":

    # store the route costs into key-value pairs (prefix, cost)
    routes_costs = _map_route_costs()
    routes_costs_keys = routes_costs.items_in_order()

    # print cost_of_number("+8163975")

    # create a list of the numbers to check the cost of
    with open(_path_for(file_of_numbers)) as f_numbers_to_call:
        phone_numbers_to_call = [line.rstrip('\n') for line in f_numbers_to_call]

    for a_number in phone_numbers_to_call:
        cost_value = cost_of_number(a_number)
        print("{},{}".format(a_number, cost_value))
