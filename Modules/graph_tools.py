from Modules.elliptic_curve_tools import same_size


# [[1,2],[1,3],[2,3],[3,4]]
class Graph:
    def __init__(self, set_of_edges):
        self.vertices = [*range(1, find_max_vert(set_of_edges) + 1)]
        self.edges = set_of_edges
        self.degrees = find_degrees(find_max_vert(set_of_edges), set_of_edges)
        self.max_degree = find_max_degree(self.degrees)


def find_max_vert(set_of_edges):
    max = 1
    for edge in set_of_edges:
        if edge[0] > max:
            max = edge[0]
        elif edge[1] > max:
            max = edge[1]
    # print(max)
    return max


def find_degree(vert, set_of_edges):
    degree = 0
    for edge in set_of_edges:
        if edge[0] == vert or edge[1] == vert:
            degree += 1
    # print([vert, degree])
    return [vert, degree]


def find_degrees(max_vert, set_of_edges):
    list_of_degrees = []
    for vert in range(1, max_vert + 1):
        list_of_degrees.append(find_degree(vert, set_of_edges))
    # print(list_of_degrees)
    return list_of_degrees


def find_max_degree(list_of_degrees):
    max_degree = 1
    for degree in list_of_degrees:
        if degree[1] > max_degree:
            max_degree = degree[1]
    return max_degree


def find_all_connection(vert, graph):
    connection = []
    for edge in graph.edges:
        if edge[0] == vert:
            connection.append(edge[1])
        elif edge[1] == vert:
            connection.append(edge[0])
    # print(connection)
    return connection


def find_degree_of_con(connections, graph):
    number_of_degrees = []
    for i in range(0, 6):
        number_of_degrees.append(0)
    for connection in connections:
        degree = find_degree(connection, graph.edges)
        number_of_degrees[degree[1]] = number_of_degrees[degree[1]] + 1
    return number_of_degrees


def copy_list(list):
    new_list = []
    if list is []:
        return new_list
    for con in list:
        new_list.append(con)
    return new_list


def double_copy_list(list):
    new_list = []
    if list == []:
        return new_list
    for con in list:
        new_list.append([con[0], con[1]])
    return new_list


def find_graph(list_of_graphs, graph_so_far, verts_to_find, rest_of_vert, graph1, graph2):
    vert = verts_to_find.pop(0)
    degree_of_vert = find_degree(vert, graph1.edges)[1]
    degree_of_connections = find_degree_of_con(find_all_connection(vert, graph1), graph1)
    for try_vert in rest_of_vert:
        degree_of_try_vert = find_degree(try_vert, graph2.edges)[1]
        if degree_of_try_vert == degree_of_vert:
            degree_of_try_vert_connections = find_degree_of_con(find_all_connection(try_vert, graph2), graph2)
            ##print("Compere real "+str(degree_of_connections)+", try "+str(degree_of_try_vert_connections))
            if degree_of_connections == degree_of_try_vert_connections:
                if verts_to_find is []:
                    graph_so_far.append([vert, try_vert])
                    print(graph_so_far)
                    print("hello")
                    return graph_so_far

                new_graph_so_far = double_copy_list(graph_so_far)
                new_graph_so_far.append([vert, try_vert])
                if verts_to_find == []:
                    # print(new_graph_so_far)
                    list_of_graphs.append(new_graph_so_far)
                    return new_graph_so_far
                # print(new_graph_so_far)
                new_verts_to_find = copy_list(verts_to_find)
                # print(verts_to_find)
                new_rest_of_vert = copy_list(rest_of_vert)
                index_to_pop = new_rest_of_vert.index(try_vert)
                new_rest_of_vert.pop(index_to_pop)
                find_graph(list_of_graphs, new_graph_so_far, new_verts_to_find, new_rest_of_vert, graph1, graph2)


def check_graph(list_of_graphs, graph1, graph2):
    for translate in list_of_graphs:
        control_list = double_copy_list(graph2.edges)
        # translate
        # print(translate)
        translation = double_copy_list(graph1.edges)
        for line in translate:

            for i in range(0, len(graph1.edges)):
                # print(translation[i])
                if graph1.edges[i][0] == line[0]:
                    translation[i][0] = line[1]
                elif graph1.edges[i][1] == line[0]:
                    translation[i][1] = line[1]

        # print(translation)

        # checking
        for i in range(0, len(graph2.edges)):
            for j in range(0, len(graph2.edges)):
                # print("Translate: "+str(translation[i])+", Control: "+str(graph2.edges[i]))
                if (translation[i][0] == graph2.edges[j][0] and translation[i][1] == graph2.edges[j][1]) or (
                        translation[i][1] == graph2.edges[j][0] and translation[i][0] == graph2.edges[j][1]):
                    control_list.pop(0)
        # print(len(control_list))
        if len(control_list) == 0:
            #print(translate)
            return translate
    return False
    # print("No result")


def is_two_graphs_isomorphic(connections_1, connections_2):
    graph_1 = Graph(connections_1)
    graph_2 = Graph(connections_2)
    print("Isomorphic")
    print("G1 = " + str(graph_1.vertices) + ", " + str(connections_1))
    print("G2 = " + str(graph_2.vertices) + ", " + str(connections_2))
    print(" "+37*"_"+"\n"+"|"+same_size("Graph", 15) + same_size("G1", 10) + same_size("G2", 10))
    error_1 = ""
    if len(graph_1.vertices) != len(graph_2.vertices):
        error_1 = " Error!"
    print(
        "|"+same_size("# Vertices", 15) + same_size(str(len(graph_1.vertices)), 10) + same_size(str(len(graph_2.vertices)),
                                                                                            10) + error_1)
    error_2 = ""
    if len(graph_1.edges) != len(graph_2.edges):
        error_2 = " Error!"
    print("|"+same_size("# Edges", 15) + same_size(str(len(graph_1.edges)), 10) + same_size(str(len(graph_2.edges)),
                                                                                        10) + error_2)
    error_3 = ""
    if graph_1.max_degree != graph_2.max_degree:
        error_3 = " Error!"
    print("|"+same_size("Degree", 15) + same_size(str(graph_1.max_degree), 10) + same_size(str(graph_2.max_degree),
                                                                                         10) + error_3)
    if error_1 == "" and error_2 == "" or error_3 == "":
        list_of_graphs = []
        find_graph(list_of_graphs, [], [*range(1, len(graph_1.vertices)+1)], [*range(1,len(graph_1.vertices)+1)], graph_1,
                   graph_2)
        translete = check_graph(list_of_graphs, graph_1, graph_2)
        if translete is False:
            print("|"+same_size("Connections", 15) + same_size("False", 10) + same_size("False", 10) + " Error!")
        else:
            print("|"+same_size("Connections", 15) + same_size("Ok", 10) + same_size("Ok", 10))
        print("|"+15*"_"+"|"+10*"_"+"|"++10*"_"+"|")

        if translete:
            print("Graphs are Isomorphic!\n")
            line_1=""
            line_2=""
            for i in range(0,len(translete)):
                if i != len(translete)-1:
                    line_1=line_1+str(translete[i][0])+", "
                    line_2=line_2+str(translete[i][1])+", "
                else:
                    line_1 = line_1 + str(translete[i][0])
                    line_2 = line_2 + str(translete[i][1])
            print("Permutation\nπ = / "+line_1+" \\"+
                "\n    \\ "+line_2+" /")
        else:
            print("Graphs are NOT Isomorphic!")
a = [[1, 2], [2, 3], [3, 4]]
b = [[1, 4], [4, 2], [2, 3]]

# find_max_vert(a)
# find_degree(2,a)
# find_degrees(4, a)
graph_1 = Graph(a)
graph_2 = Graph(b)
my_list = []
find_graph(my_list, [], [1, 2, 3, 4], [1, 2, 3, 4], graph_1, graph_2)
# print(my_list)
check_graph(my_list, graph_1, graph_2)

# c = [[1, 3], [1, 4], [1, 5], [2, 3], [3, 4]]
# d = [[1, 4], [2, 5], [3, 4], [3, 5], [4, 5]]
# graph3 = Graph(c)
# graph4 = Graph(d)
# my_new_list = []
# find_graph(my_new_list, [], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5], graph3, graph4)
# print(my_new_list)
# check_graph(my_new_list, graph3, graph4)
is_two_graphs_isomorphic(a, b)
