from __future__ import division
from __future__ import absolute_import
import random
from node import Room
from io import open

new_dict = {}
mons, hole, gold, wall = 0, 0, 0, 0
listparam = [mons, hole, gold, wall]

main_dict = {}

# This is used for loading the maze
def generate_pre_dictonary_2(lst):
    for el in lst:
        main_dict.update({el: []})

# This is used for creating the maze
def generate_pre_dictonary(lst):
    for el in lst:
        new_dict.update({el: []})

def print_dict(dict):
    for el in dict:
        stri = el.toString() + u": { "
        tmplst = dict[el]
        for val in tmplst:
            if val != tmplst[0]:
                stri += u", "
            stri += u"\"" + u"Room " + unicode(val.id) + u"\""
        stri += u" }"
        print stri

def print_list(lst):
    stri = u"["
    for el in lst:
        stri += u" \"" + el.toString() + u"\" "
    stri += u"]"
    print stri

def has_duplicates(listObj):
    return len(listObj) != len(set(listObj))

#Check if graph can be constructed with the given number of nodes and edges
def check(N, K, p ,k):
    lst = []
    for i in xrange(N-K):
        lst.append(p)
    for i in xrange(K):
        lst.append(k)

    while(len(lst) > 0):
        lst.sort(reverse=True)
        x = lst[0]
        lst.remove(x)

        if x == 0:
            return True
        for i in xrange(x):
            lst[i] -= 1
        if -1 in lst:
            return False



def generate(N, K, p, k):
    lst = []
    explored = []
    ready = []

    normal = []
    border = []

    num_of_normal = N-K
    num_of_borders = K

    templist = range(1, N+1)

    # Fill list of normal nodes
    for i in xrange(N-K):
        x = random.choice(templist)
        templist.remove(x)
        nroom = Room(x)
        nroom.isNormal = True
        normal.append(nroom)

    # Fill list of border nodes
    for i in xrange(N-K, N):
        x = random.choice(templist)
        templist.remove(x)
        nroom = Room(x)
        nroom.isNormal = False
        border.append(nroom)
    lst = normal + border
    added = []
    cpy_mons = listparam[0]

    # Time to distribute monsters!!!
    while(cpy_mons > 0):
        tmp = random.choice(lst)
        if tmp in added:
            continue
        tmp.pres_monster = 1
        tmp.pres_smell = 1
        cpy_mons -= 1
        added.append(tmp)
    del added
    del cpy_mons

    # Time to distribute walls!
    added = []
    cpy_walls = listparam[3]
    while(cpy_walls > 0):
        tmp = random.choice(lst)
        if tmp in added:
            continue
        tmp.pres_wall = 1
        cpy_walls -= 1
        added.append(tmp)
    del added
    del cpy_walls

    #Time to distribute gold!
    added = []
    cpy_gold = listparam[2]
    while (cpy_gold > 0):
        tmp = random.choice(lst)
        if tmp in added:
            continue
        tmp.pres_gold = 1
        cpy_gold -= 1
        added.append(tmp)
    del added
    del cpy_gold

    # Time to distribute holes!
    added = []
    cpy_holes = listparam[1]
    while (cpy_holes > 0):
        tmp = random.choice(lst)
        if tmp in added:
            continue
        tmp.pres_hole = 1
        tmp.pres_wind = 1
        cpy_holes -= 1
        added.append(tmp)
    del added
    del cpy_holes

    #print(lst)
    generate_pre_dictonary(lst)
    copylist = lst[:]

    del copylist
    #create first step of graph
    while(True):

        if len(lst) == 0:
            break

        current_node = random.choice(lst)   #get random list element
        lst.remove(current_node)            # delete it from list

        if not explored:                    #check if explored is empty
            explored.append(current_node)
        else:
            while(True):
                rand_expl_node = random.choice(explored)        #Choosing random node from explored
                if rand_expl_node not in ready:
                    new_dict[current_node].append(rand_expl_node)          #Connect
                    new_dict[rand_expl_node].append(current_node)          #Connect

                    #Add nodes with maximum connections to 'ready'
                    if (rand_expl_node.isNormal == True) and (len(new_dict[rand_expl_node]) == p):
                        ready.append(rand_expl_node)
                        num_of_normal -= 1
                    if (rand_expl_node.isNormal == False) and (len(new_dict[rand_expl_node]) == k):
                        ready.append(rand_expl_node)
                        num_of_borders -= 1
                    break
                else:
                    continue
            explored.append(current_node)

    # Remove all nodes that are ready. No more need in them
    for el in ready:
        explored.remove(el)

    new_lst = explored      # New Main list to choose from
    rem_normal = []         # Remainning normal nodes
    rem_border = []         # Remaining border nodes
    #print_list(new_lst)

    for el in new_lst:
        if el.isNormal == True:
            rem_normal.append(el)
        else:
            rem_border.append(el)

    # Add the remaining connections
    while(True):

        # Termination condition
        if len(new_lst) == 0:
            break

        # Choose firt element to connect
        first = random.choice(new_lst)

        # This is done for 'first' and 'second' not to be the same
        # We cannot remove 'first directly from new_lst because, it may not be 'ready'
    #    copy_lst = new_lst[:]
        copy_lst = new_lst[:]
        copy_normal = rem_normal[:]
        copy_border = rem_border[:]

        copy_lst.remove(first)

        # This is to choose second from lists where no first element
        if first in copy_normal:
            copy_normal.remove(first)
        else:
            copy_border.remove(first)

        # Choose second that is normal
        if len(copy_normal) > 0:
            second = random.choice(copy_normal)
        elif len(copy_border) > 0:
            second = random.choice(copy_border)

        new_dict[first].append(second)  # Connect
        new_dict[second].append(first)  # Connect

        # Check if first has max number of connections
        if (first.isNormal == True) and (len(new_dict[first]) == p):
            ready.append(first)
            num_of_normal -= 1
            if len(rem_normal) > 0:
                rem_normal.remove(first)
            new_lst.remove(first)
        if (first.isNormal == False) and (len(new_dict[first]) == k):
            ready.append(first)
            num_of_borders -= 1
            if len(rem_border) > 0:
                rem_border.remove(first)
            new_lst.remove(first)

        # Check if second has max number of connections
        if (second.isNormal == True) and (len(new_dict[second]) == p):
            ready.append(second)
            num_of_normal -= 1
            if len(rem_normal) > 0:
                rem_normal.remove(second)
            if second in new_lst:
                new_lst.remove(second)
        if (second.isNormal == False) and (len(new_dict[second]) == k):
            ready.append(second)
            num_of_borders -= 1
            if len(rem_border) > 0:
                rem_border.remove(second)
            new_lst.remove(second)

def read_generator(file, teta, omega):
    f = open(file, u"r+")                # open file
    count = 0                           # count the number of lines ~ rooms
    room_list = []
    list_of_rooms_nbrs = []             # list of rooms neighbors is used to figure out what is maximum num of neighbors

    for line in f:
        id = int(line[0])
        ww = int(line[2])
        hh = int(line[4])
        mm = int(line[6])
        gg = int(line[8])
        neighbors_list = line.split(u" ")
        neighbors_list.remove(neighbors_list[0])        # list with ids of current room's neighbors

        room = Room(id)
        room.pres_monster = mm
        room.pres_gold = gg
        room.pres_wall = ww
        room.pres_hole = hh

        print(neighbors_list)

        # Convert all ids to int
        for i in xrange(len(neighbors_list)):
            if neighbors_list[i] != "\n":
                neighbors_list[i] = int(neighbors_list[i])


        room.neighbors = neighbors_list[:]          # copy neighbor list

        # appending to the lists of rooms and neighbors
        room_list.append(room)
        list_of_rooms_nbrs.append(room.neighbors)

        count += 1
    # Get max number of neighbors
    max = 0
    for el in list_of_rooms_nbrs:
        if len(el) > max:
            max = len(el)
    #print(max)

    # Figure out if room is normal or border
    for el in room_list:
        if len(el.neighbors) == max:
            el.isNormal = True
        else:
            el.isNormal = False

    for el in room_list:
        if el.pres_monster == 1:
            el.pres_smell = 1
        if el.pres_hole == 1:
            el.pres_wind = 1

    # Create new dictionary that represents the maze
    generate_pre_dictonary_2(room_list)


    for el in room_list:
        for nl in room_list:
            if nl.id in el.neighbors:
                main_dict[el].append(nl)


    #print_list(room_list)
    allocate_smell(main_dict, teta, omega)
    allocate_wind(main_dict, teta, omega)
    print_maze(main_dict)   

def allocate_wind(graph, teta, omega):
    # if teta = 0; wind does not spread
    if teta == 0 or omega <= 0:
        return
    # going through all graph elements
    for el in graph:
        if el.pres_wind == 0: #if no wind in current room, move to next room
            continue
        bfs_wind(graph, el, teta, omega)

def allocate_smell(graph, teta, omega):
    # if teta = 0; wind does not spread
    if teta == 0 or omega <= 0:
        return
    # going through all graph elements
    for el in graph:
        if el.pres_smell == 0: #if no wind in current room, move to next room
            continue
        bfs_smell(graph, el, teta, omega)

def final_generator(N, K, p, k):

    while(True):
        flag = 0
        generate(N, K, p, k)
        for el in new_dict:
            if has_duplicates(new_dict[el]):
                new_dict.clear()
                flag = 1
                break
        if flag == 0:
            break
        else:
            continue

def calculate_limit(teta, omega):
    res = 1
    for i in xrange(teta):
        res /= omega
    return res

#These function was implemented using https://stackoverflow.com/a/46383689/9901274
def bfs_wind(graph, start, theta, omega):

   # print("Start is : {}".format(start.id))
    # keep track of all visited nodes
    explored = []
    # keep track of nodes to be checked
    queue = [start]

    levels = {}         # this dict keeps track of levels
    levels[start]= 0    # depth of start node is 0
    limit = calculate_limit(theta, omega)

    visited= [start]     # to avoid inserting the same node twice into the queue
    new_wind = start.pres_wind
    # keep looping until there are nodes still to be checked
    while queue:
       # pop shallowest node (first node) from queue
        if new_wind < limit:
           return

        node = queue.pop(0)
        explored.append(node)
        neighbours = graph[node]
        new_wind = new_wind / omega
        # add neighbours of node to queue
        for neighbour in neighbours:
            if neighbour not in visited:
                #HERE!!!
                if new_wind < limit:
                    return

                if new_wind > neighbour.pres_wind:
                    neighbour.pres_wind = new_wind
                queue.append(neighbour)
                visited.append(neighbour)

                levels[neighbour]= levels[node]+1
                if levels[neighbour] > theta:              # Theta defines 'depth'
                    return
                # print(neighbour, ">>", levels[neighbour])
    return explored

#These function was implemented using https://stackoverflow.com/a/46383689/9901274
def bfs_smell(graph, start, theta, omega):

    #print("Start is : {}".format(start.id))
    # keep track of all visited nodes
    explored = []
    # keep track of nodes to be checked
    queue = [start]

    levels = {}         # this dict keeps track of levels
    levels[start]= 0    # depth of start node is 0
    limit = calculate_limit(theta, omega)

    visited= [start]     # to avoid inserting the same node twice into the queue
    new_smell = start.pres_smell
    # keep looping until there are nodes still to be checked
    while queue:
        if new_smell < limit:
            return

       # pop shallowest node (first node) from queue
        node = queue.pop(0)
        explored.append(node)
        neighbours = graph[node]
        new_smell = new_smell / omega
        # add neighbours of node to queue
        for neighbour in neighbours:
            if neighbour not in visited:
                #HERE!!!
                if new_smell < limit:
                    return

                if new_smell > neighbour.pres_smell:
                    neighbour.pres_smell = new_smell
                queue.append(neighbour)
                visited.append(neighbour)

                levels[neighbour]= levels[node]+1
                if levels[neighbour] > theta:              # Theta defines 'depth'
                    return
                # print(neighbour, ">>", levels[neighbour])

    return explored

def main_input():

    while(True):

        N, K, p, k = raw_input(u"Provide values for N, K, p, k\n N should be > K, p should be > k\n").split()
        N, K, p, k = int(N), int(K), int(p), int(k)

        if (N <= K) or (p <= k):
            print u"Invalid number of nodes of edges. N should be > K, p should be > k\n"
            continue
        if check(N, K, p, k) == True:
            break
        else:
            print u"A maze cannot be constructed with this input. Try again\n"
            continue

    while(True):
        mons, hole, gold, wall = raw_input(u"Enter number of Monsters, holes, gold, walls respectively\n"
                                   u"Note that they should be less than total number of nodes\n").split()
        listparam[0], listparam[1], listparam[2], listparam[3] = int(mons), int(hole), int(gold), int(wall)

        if (listparam[0] < N) and (listparam[1] < N) and (listparam[2] < N) and (listparam[3] < N):
            break

    while(True):
        teta, omega = raw_input(u"Provide values for spread and decay: \n").split()
        teta, omega = int(teta), int(omega)

        if (teta < 0) or (omega < 0):
            print u"Incorrect input \n"
            continue
        else:
            break

    final_generator(N, K, p, k)
    allocate_wind(new_dict, teta, omega)
    allocate_smell(new_dict, teta, omega)
    output()
    print_maze(new_dict)


def main_main_input():
	what_to_do = raw_input("Do you want to create a maze or load one?\n\
		To create, type 'c', To load type 'l' \n")

	if what_to_do == 'c':
		main_input()
	elif what_to_do == 'l':

		while(True):

			f, tt, om = raw_input("Enter filename, spread and decay\n").split()
			tt = int(tt)
			om = int(om)
			if tt < 0 or om < 0:
				print("Incorrect input\n")
				continue
			else:
				break

		read_generator(f, tt, om)

def print_maze(dict):
	
    # FOR PYTHON 2.7 CHANGE TO: for key, value in d.iteritems():
    print("\n\n===================================================================\n\n")
    for key, value in dict.items():
        stri = u""
        stri = unicode(key.id) + u":" + unicode(key.pres_wall) + u"," + unicode(key.pres_hole) + u"," + unicode(key.pres_monster) + u"," + \
               unicode(key.pres_gold) + u"," + unicode(key.pres_wind) + u"," + unicode(key.pres_smell) + u" "

        for el in value:
            stri += unicode(el.id) + u" "
        stri += u"\n"
        print(stri)

def output():
    file = open(u"output.txt", u"r+")
    file.truncate(0)
    # FOR PYTHON 2.7 CHANGE TO: for key, value in d.iteritems():
    for key, value in new_dict.items():
        stri = u""
        stri = unicode(key.id) + u":" + unicode(key.pres_wall) + u"," + unicode(key.pres_hole) + u"," + unicode(key.pres_monster) + u"," + \
               unicode(key.pres_gold) + u"," + unicode(key.pres_wind) + u"," + unicode(key.pres_smell) + u" "

        for el in value:
            stri += unicode(el.id) + u" "
        stri += u"\n"
        file.write(stri)


main_main_input()
#final_generator(10, 5, 5, 3)
#print_dict(new_dict)

#ans = bfs_connected_component(new_dict, next(iter(new_dict)))
#print_list(ans)
