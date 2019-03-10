# Submitter: bssoohoo(Soo Hoo, Brandon)
# Partner  : lgazzola(Gazzola, Luca)
# We certify that we worked cooperatively on this programming
#   assignment, according to the rules for pair programming

import prompt
from goody       import safe_open
from math        import ceil
from collections import defaultdict


#d has 2 friends
#2 - something
#something = ceil(2 / 2) 


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
                print(line[0], line[1])
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
    ans = ""
    for key in sorted(list(graph)):
        ans += "  " + key + " -> ["
        sorted_list = sorted(list(graph[key]))
        try:
            for index in range(len(sorted_list)):
                if index == 0:
                    ans += "\'" + sorted_list[index] + "\'"
                else:
                    ans += ", \'" + sorted_list[index] + "\'"
        except TypeError:
            break
        ans += "]\n"    
    print(ans)
    return ans

def find_influencers(graph : {str:{str}}, trace : bool = False) -> {str}:
    infl_dict = {}
    for key in graph:
        infl_dict[key] = [(len(graph[key]) - ceil(len(graph[key]) / 2)) if len(graph[key]) > 0 else -1, len(graph[key]), key]
    while True:
        #print(infl_dict)
        #print (graph)
        cand_list = []
        for key in infl_dict:
            if infl_dict[key][0] >= 0:
                cand_list.append((infl_dict[key][0], infl_dict[key][1], infl_dict[key][2]))
        #print(infl_dict)
        if cand_list == []:
            return set(infl_dict.keys())
        cand_list.sort(key = lambda x : x[2])
        least = max(cand_list, key = lambda x : x[0])[0]
        letter_least_key = max(cand_list, key = lambda x : x[0])[2]
        least_friends = cand_list[0][1]
        for index in cand_list:
            if index[2] == letter_least_key:
                least_friends = index[1]
        for index in cand_list:
            if index[0] < least:
                least = index[0]
                letter_least_key = index[2]
                least_friends = index[1]
            elif index[0] == least:
                if least_friends > index[1]:
                    least = index[0]
                    letter_least_key = index[2]
                    least_friends = index[1]
        #print(letter_least_key)
        #print(letter_least_key)
        #print(infl_dict)
        
        if trace: #prints for if trace is True
            print("influencer dictionary\t=", infl_dict)
            print("removal candidates\t=", cand_list)
            print((infl_dict[letter_least_key][0], infl_dict[letter_least_key][1], infl_dict[letter_least_key][2]), "is the smallest candidate")
            print("Removing", letter_least_key, "as key from influencer dictionary; decrementing friend's values here", end = "\n\n")

        infl_dict.pop(letter_least_key)
        #graph.pop(letter_least_key)  #remove letter_least_key element in graph
        for key in infl_dict:  #remove letter_least_key from each element of graph
            if letter_least_key in graph[key]:
                infl_dict[key][0] -= 1
                infl_dict[key][1] -= 1
                    
    #print(cand_list)


def all_influenced(graph : {str:{str}}, influencers : {str}) -> {str}:
    ans = set(influencers)
    #print(ans)
    while True:
        add_to_ans = False
        for key in graph:
            count = 0
            for influenced in ans:
                if influenced in graph[key]:
                    count += 1
            if count >= ceil(len(graph[key]) / 2) and count > 0:
                if not key in ans:
                    ans.add(key)
                    add_to_ans = True
        if not add_to_ans:
            return ans
       
            
    
if __name__ == '__main__':
    # Write script here

    file = safe_open ("Enter a file storing a friendship graph", mode="r", error_message="That don't work homie", default="")
    fileGraph = read_graph (file)
    dupe = str (fileGraph)
    file.close ()
    originalFileLen = len (fileGraph)

    graph_as_str (fileGraph)

    influencers = find_influencers (eval (dupe), prompt.for_bool ("Trace the Algorithm", default=True, error_message="That don't work either homie"))
    print("influencers: ", influencers)
    
    while True:
        redflag = False
        userPrompt = str(prompt.for_string("Enter influencers set (or else quit)", default=influencers, error_message="Homie stop"))
        if userPrompt == "quit":
            break
        try:            
            if type (eval (userPrompt)) == type (set ()):
                for user_key in eval (userPrompt):
                    if user_key not in fileGraph.keys ():
                        print ("  Entry Error: ", userPrompt, ";", sep="")
                        print ("  Please enter a legal String\n")
                        redflag = True
                        break
            else:
                print ("That is not a valid entry. Please enter a valid entry\n")
                continue
            if redflag:
                continue
            if str(userPrompt) != "quit":
                if type(userPrompt) == str:
                    influenced = all_influenced(fileGraph, eval (userPrompt))
                    print (influenced)
                    print ("All Influenced ", "(", (len (influenced)/originalFileLen)*100, "%) = ", influenced, "\n", sep="")
            else:
                break
        except:
            print ("That is not a valid entry. Please enter a valid entry\n")
        

    # For running batch self-tests
    print()
    import driver
    driver.default_file_name = "bsc1.txt"
    #driver.default_show_traceback = True
    #driver.default_show_exception = True
    #driver.default_show_exception_message = True
    driver.driver()
