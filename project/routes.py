import os
import sys

from hashtable import HashTable

file_of_numbers = "data/phone-numbers-100.txt"
file_of_costs = "data/route-costs-100.txt"


def _path_for(relative_path):
    script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
    abs_file_path = os.path.join(script_dir, relative_path)

    return abs_file_path


def _map_route_costs():
    with open(_path_for(file_of_costs)) as f_costs:
        arr_routes = f_costs.read().split('\n')
        arr_routes = filter(lambda item: item != '', arr_routes)

        hash_cost = HashTable()

        print 'create hash'
        for a_route in arr_routes:
            a_route_split = a_route.split(',')
            a_route_key = a_route_split[0]
            a_route_cost = a_route_split[1]

            hash_cost.set(a_route_key, a_route_cost)

    print 'return hash'
    return hash_cost


routes_costs = _map_route_costs()

print 'get keys of hash'
routes_costs_keys = routes_costs.keys()


def cost_of_number(number):

    longest_match_key = None

    for a_route in routes_costs_keys:
        if number.startswith(a_route):
            if longest_match_key is None:
                longest_match_key = a_route
            else:
                if len(a_route) > len(longest_match_key):
                    longest_match_key = a_route

    return routes_costs.get(longest_match_key) if longest_match_key is not None else 0


with open(_path_for(file_of_numbers)) as f_numbers_to_call:
    phone_numbers_to_call = [line.rstrip('\n') for line in f_numbers_to_call]

for a_number in phone_numbers_to_call:
    cost = cost_of_number(a_number)
    if cost != 0:
        print(cost)
