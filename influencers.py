# Author: Tri Nguyen
# Version: Spring 19

import prompt
from goody       import safe_open
from math        import ceil 
from collections import defaultdict

def read_graph(open_file : open) -> {str:{str}}:
    friend_graph = {};
    while True:
        line = open_file.readline()
        line = line.strip("\n")
        if line == "":
            break;
        line = line.split(";")
        key = friend_graph.keys()
        if len(line) > 1:
            if (line[0] in key):
                friend_graph[line[0]].add(line[1])
            else:
                friend_graph[line[0]] = set()
                friend_graph[line[0]].add(line[1])
            if (line[1] in key):
                friend_graph[line[1]].add(line[0])
            else:
                friend_graph[line[1]] = set()
                friend_graph[line[1]].add(line[0])
        elif len(line) == 1:
            if (not line[0] in key):
                friend_graph[line[0]] = set()
    return friend_graph

def graph_as_str(graph : {str:{str}}) -> str:
    pass


def find_influencers(graph : {str:{str}}, trace : bool = False) -> {str}:
    pass


def all_influenced(graph : {str:{str}}, influencers : {str}) -> {str}:
    pass

if __name__ == '__main__':
    # Write script here
              
    # For running batch self-tests
    print()
    import driver
    driver.default_file_name = "bsc1.txt"
#     driver.default_show_traceback = True
#     driver.default_show_exception = True
#     driver.default_show_exception_message = True
    driver.driver()
