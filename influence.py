import prompt
from goody       import safe_open
from math        import ceil 
from collections import defaultdict


def read_graph(open_file : open) -> {str:{str}}:
    pass


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

