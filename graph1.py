from random import randint


class Vertex:
    def __init__(self, graph, sign, index):
        self.graph = graph
        self.sign = sign
        self.index = index
        self.degree = []
        self.edges = []
        self.color = ''

        self.ex = {}
        self.visited = []
        self.not_visited = self.degree
        self.connection_count = 1
        self.connection = {}
        self.prev = 0

        self.connection_path = []


        self.path_values = []

        self.gam_path = []

class Edge:
    def __init__(self, graph, vertex1, vertex2, type, sign):
        self.graph = graph
        self.sign = sign
        self.vertex1 = vertex1
        self.vertex2 = vertex2
        self.type = type
        self.color = ''



class Graph:
    def __init__(self):
        self.name = ''
        self.v_list = []
        self.e_list = []
        self.matrix = []
        self.name = ''

        self.ex = {}


        self.v_amount = 0
        self.e_amount = 0

        self.gam_cycles = []

        self.visited = []
        self.not_visited = []

    # set graph NAME
    def set_name(self, name):
        self.name = name

    def print_matrix(self):
        for list in self.matrix:
            print(list)

    def return_v_amount(self):
        return len(self.v_list)
    def return_e_amount(self):
        return len(self.e_list)

    def return_degrees(self):
        for v in self.v_list:
            print(v.sign,': ',len(v.edges))
    def return_v_degree(self, vertex):
        for v in self.v_list:
            if v.sign == vertex:
                print(v.sign,': ',len(v.edges))




    # -------------- CONNECTION -----------------
    # return True if it is
    # False if it is not
    def is_connected(self):
        count = 0
        for v in self.v_list:
            path = []
            kol, path = self.dfs_connected(v, v, path)
            v.connection_path = path
            print(v.sign, 'kolvo',kol, 'path-', path)
            if kol == len(self.v_list):
                count += 1
        if count == len(self.v_list) or count == len(self.v_list) - 1:
            return True
        else:
            return False

    def dfs_connected(self, v0, vertex, path):
        all_vis = 1
        path.append(vertex.sign)
        for v in vertex.degree:
            if v.sign not in path:
                all_vis1, path = self.dfs_connected(v0, v, path)
                all_vis += all_vis1

        return all_vis, path

    # make graph the connected one
    def make_connected(self):

        for vertex in self.v_list:
            # check if our graph is really not connected
            if len(vertex.connection_path) != len(self.v_list):
                # make a list of all vertexes signs
                vertexes_sign_list = []
                for v in self.v_list:
                    vertexes_sign_list.append(v.sign)

                # create a list of not vertexes that we can connect with our not connected one
                # to make graph connected
                candidates_to_connect_with = list(filter(lambda s: s in vertex.connection_path, vertexes_sign_list))
                # a list of not connected vertexes
                not_connected_vertexes = list(filter(lambda s: s not in vertex.connection_path, vertexes_sign_list))

                if len(not_connected_vertexes) != 0:
                    for v in self.v_list:
                        for v1 in not_connected_vertexes:
                            if v.sign == v1:
                                self.add_e_oriented(vertex.sign, v.sign)
                                print(vertex.sign,'->', v.sign)
                                if self.is_connected():
                                    return True
            return False

    # -------------------------------------------


    def DFSUtil(self, v, visited):

        # Mark the current node as visited and print it
        visited[v] = True
        print(v)
        # Recur for all the vertices adjacent to
        # this vertex
        for i in self.v_list[v]:
            if visited[i] == False:
                self.DFSUtil(i, visited)
    # The function to do DFS traversal. It uses
    # recursive DFSUtil()
    def DFS(self):
        V = len(self.v_list)  # total vertices

        # Mark all the vertices as not visited
        visited = [False] * (V)

        # Call the recursive helper function to print
        # DFS traversal starting from all vertices one
        # by one
        for i in range(V):
            if visited[i] == False:
                self.DFSUtil(i, visited)


    # -------------- GAMILTON -----------------
    # find GAMILTON CYCLES
    def dfs_gamilton(self, v0, vertex, visited, not_visited_edges):
        flag = False

        if flag == False:
            if v0 == vertex and len(visited) == len(self.v_list):
                v0.gam_path.append(vertex.sign)
                flag = True
            if vertex.sign not in visited:
                visited.append(vertex.sign)
                v0.gam_path.append(vertex.sign)
                print('not visited edges for', vertex.sign)

                for e in not_visited_edges:
                    if e.type == 1:
                        if e.vertex1 == vertex:
                            v = e.vertex2
                            print(vertex.sign,'->',v.sign)
                            not_visited_edges.remove(e)
                            edges = []
                            for edge in v.edges:
                                if e != edge:
                                    edges.append(edge)
                            flag = self.dfs_gamilton(v0, v, visited,edges)

                            if not flag:
                                if e.type == 1:
                                    #self.add_e_oriented(vertex.sign, v.sign)
                                    not_visited_edges.append(e)
                                    # visited.remove(v.sign)
                                    # v0.gam_path.remove(v.sign)
                                elif e.type == 2:
                                    #self.add_e_not_oriented(vertex.sign, v.sign)
                                    not_visited_edges.append(e)
                                    # visited.remove(v.sign)
                                    # v0.gam_path.remove(v.sign)
                    elif e.type == 2:
                        if e.vertex1 == vertex:
                            v = e.vertex2
                            print(vertex.sign,'->',v.sign)
                            not_visited_edges.remove(e)
                            edges = []
                            for edge in v.edges:
                                if e != edge:
                                    edges.append(edge)
                            flag = self.dfs_gamilton(v0, v, visited, edges)
                            if flag:
                                return True
                            else:
                                if e.type == 1:
                                    #self.add_e_oriented(vertex.sign, v.sign)
                                    not_visited_edges.append(e)
                                elif e.type == 2:
                                    #self.add_e_not_oriented(vertex.sign, v.sign)
                                    not_visited_edges.append(e)
                        elif e.vertex1 != vertex:
                            v = e.vertex1
                            print(vertex.sign, '->', v.sign)
                            not_visited_edges.remove(e)
                            edges = []
                            for edge in v.edges:
                                if e != edge:
                                    edges.append(edge)
                            flag = self.dfs_gamilton(v0, v, visited,edges)
                            if flag:
                                return True
                            else:
                                if e.type == 1:
                                   # self.add_e_oriented(vertex.sign, v.sign)
                                    not_visited_edges.append(e)
                                    # visited.remove(v.sign)
                                    # v0.gam_path.remove(v.sign)
                                elif e.type == 2:
                                    #self.add_e_not_oriented(vertex.sign, v.sign)
                                    not_visited_edges.append(e)
                                    # visited.remove(v.sign)
                                    # v0.gam_path.remove(v.sign)


        return flag

    def is_gamilton(self):
        for v in self.v_list:
            not_visited_edges = []
            for e in v.edges:
                not_visited_edges.append(e)
                print(e.type,':',e.vertex1.sign, '->', e.vertex2.sign)
            print('-------vertex',v.sign)
            f = self.dfs_gamilton(v, v, [], not_visited_edges)
            if f:
                self.gam_cycles.append(v.gam_path)
        print(self.gam_cycles)
        return f


        # for v in self.v_list:
        #     path = []
        #     count = 0
        #     visited = []
        #     count = 1
        #     self.dfs_gamilton(v, v, visited, count)
        #     print(v.sign, 'path-', visited)
    # -----------------------------------------


    def dfs(self, v0, vertex, path, visited, count):
        flag = False
        if flag == False:
            if self.matrix[vertex.index][count-1] == 1:
                if count == len(self.v_list) and v0 == vertex:
                    flag = True
                else:
                    if vertex not in visited:
                        visited.append(vertex)
                        path[count] = vertex.sign


                        for v in self.v_list:
                            if v.index == count - 1:
                             flag = self.dfs(v0, v, path, visited, count+1)
                             if flag == False:
                                 visited.remove(v)

        return flag







    def check_dfs(self):
        for v in self.v_list:
            path = []
            for i in range(len(self.v_list)):
                path.append(0)
            #path = []
            visited = []
            count = 0
            path[count] = v.sign
            print(v.sign)
            flag = self.dfs(v,v,path, visited, count + 1)
            print(path)


    # центр - множество вершин
    def center(self):
        min = 0
        min_v = 0
        for v in self.v_list:
            if len(v.degree) <= min:
                min = len(v.degree)
                min_v = v.sign
        return min_v


    # add VERTEX
    def add_v(self, vertex):
        self.v_amount += 1
        v = Vertex(self, vertex, self.v_amount-1)
        self.v_list.append(v)

        if len(self.matrix) == 0:
            self.matrix.append([0])
        else:
            count = 0
            for list in self.matrix:
                list.append(0)
                count += 1
            # add new vertex to the matrix
            new_list = []
            for i in range(0, count+1):
                new_list.append(0)
            print(self.v_amount)
            self.matrix.append(new_list)

    def remove_v(self, vertex):
        del_v = None
        for v in self.v_list:
            if v.sign == vertex:
                del_v = v
                # remove all EDGES
                for other_v in v.degree:
                    other_v.degree.remove(v)
                    e = self.search_e(v, other_v)
                    if e != None:
                        other_v.edges.remove(e)

        for count, list in enumerate(self.matrix):
            list.pop(del_v.index)

        # low the vertexes indexes
        for i in range(del_v.index, len(self.v_list)):
            self.v_list[i].index -= 1

        self.matrix.pop(del_v.index)
        self.v_list.remove(del_v)
        self.v_amount -= 1

    def set_v_color(self, vertex, color):
        for v in self.v_list:
            if v.sign == vertex:
                v.color = color


    def find_vertex(self, vertex):
        for v in self.v_list:
            if v.sign == vertex:
                return v



    def add_e_oriented(self, vertex1, vertex2):
        self.e_amount += 1
        sign = 'e' + str(self.e_amount)

        #NOT SURE if we shoul add new vertexes
        #v1, v2 = None, None
        v1 = self.find_vertex(vertex1)
        v2 = self.find_vertex(vertex2)


        e = Edge(self, v1, v2, 1, sign)
        self.e_list.append(e)

        v1.degree.append(v2)
        v1.edges.append(e)
        #v2.degree.append(v1)

        # add EDGE to the matrix
        for count, list in enumerate(self.matrix):
            if v1.index == count:
                for i in range(0, len(list)):
                    if i == v2.index:
                        list[i] = 1
                        break


    def add_e_not_oriented(self, vertex1, vertex2):
        self.e_amount += 1
        sign = 'e' + str(self.e_amount)
        for v in self.v_list:
            if v.sign == vertex1:
                v1 = v
            elif v.sign == vertex2:
                v2 = v
        e = Edge(self, v1, v2, 2, sign)
        print(e.vertex1.sign,'->',e.vertex2.sign)
        self.e_list.append(e)

        v1.degree.append(v2)
        v2.degree.append(v1)
        v1.edges.append(e)
        v2.edges.append(e)

        # add EDGE to the matrix
        for count, list in enumerate(self.matrix):
            if v1.index == count:
                for i in range(0, len(list)):
                    if i == v2.index:
                        list[i] = 1
                        break
            if v2.index == count:
                for i in range(0, len(list)):
                    if i == v1.index:
                        list[i] = 1
                        break

    # remove EDGE
    def remove_e(self, edge):
        for e in self.e_list:
            if e.sign == edge:

                v1 = e.vertex1
                v2 = e.vertex2
                if e.type == 2:
                    for count, list in enumerate(self.matrix):
                        if v1.index == count:
                            for i in range(0, len(list)):
                                if i == v2.index:
                                    list[i] = 2
                                    v1.edges.remove(e)
                                    v1.degree.remove(v2)

                        if v2.index == count:
                            for i in range(0, len(list)):
                                if i == v1.index:
                                    list[i] = 2
                                    v2.edges.remove(e)
                                    v2.degree.remove(v1)
                    self.e_list.remove(e)

                elif e.type == 1:
                    for count, list in enumerate(self.matrix):
                        if v1.index == count:
                            for i in range(0, len(list)):
                                if i == v2.index:
                                    list[i] = 2
                                    v1.edges.remove(e)
                                    v2.edges.remove(e)
                                    v1.degree.remove(v2)
                                    v2.degree.remove(v1)
                    self.e_list.remove(e)
        self.e_amount -= 1


    def set_e_color(self, edge, color):
        for e in self.e_list:
            if e.sign == edge:
                e.color = color

    def search_e(self, v1, v2):
        for e in self.e_list:
            if (e.vertex1 == v1 and e.vertex2 == v2) or (e.vertex1 == v2 and e.vertex2 == v1):
                return e
        return None

    def add_multiple_e(self, vertex1, vertex2):
        self.e_amount += 2


        # NOT SURE if we shoul add new vertexes
        # v1, v2 = None, None
        v1 = self.find_vertex(vertex1)
        v2 = self.find_vertex(vertex2)

        sign1 = 'e' + str(self.e_amount)
        e1 = Edge(self, v1, v2, 3, sign1)
        self.e_list.append(e1)

        sign2 = 'e' + str(self.e_amount)
        e2 = Edge(self, v1, v2, 3, sign2)
        self.e_list.append(e2)

        # add EDGE to the matrix
        for count, list in enumerate(self.matrix):
            if v1.index == count:
                for i in range(0, len(list)):
                    if i == v2.index:
                        list[i] += 1
                        v1.degree.append(v2)
                        v1.edges.append(e1)
                        v2.degree.append(v1)
                        v2.edges.append(e1)

        for count, list in enumerate(self.matrix):
            if v1.index == count:
                for i in range(0, len(list)):
                    if i == v2.index:
                        list[i] += 1
                        v1.edges.append(e2)
                        v2.edges.append(e2)

    def find_min_path_matrix(self, v0, vertex, min_path_matrix):
        for i, value in enumerate(self.matrix[vertex.index]):

            #print(value)
            if value == 0:
                index = vertex.index - 1
                if i != vertex.index:
                    while index >= 0:

                        if min_path_matrix[index][i] != 0:
                            min_path_matrix[vertex.index][i] = min_path_matrix[index][i] + 1
                        index -= 1

            elif value >= 1:
                # if v0.index != 0:
                #     if i != v0.index:
                #         print(v0.sign,min_path_matrix[v0.index])
                #         if min_path_matrix[v0.index-1][i] == 0:
                #             min_path_matrix[v0.index-1][i] = (vertex.index + 1)
                index = vertex.index - 1
                #if min_path_matrix[index][i] == 0:


                count = 2
                print(vertex.sign, value, i, vertex.index)
                if i != vertex.index:
                    # нужно ведь и самаго него изменить
                    # можео проверить, что он последний в графе

                    # нужно проверять направление дуг?
                    while index >= 0:
                        if index != i:
                            # не корректно
                            # потребуется еще доп проверка
                            if min_path_matrix[index][i] > count or min_path_matrix[index][i] == 0:
                                min_path_matrix[index][i] = count
                                index -= 1
                                count += 1
                            else:
                                index -= 1
                        else:
                            index -= 1
                        # if min_path_matrix[index][i] > count:
                        #     min_path_matrix[index][i] = count
                        #     index -= 1
                        #     count += 1
                        # else:
                        #     index -= 1
                        #     count += 1

            # для корректного отображения остальных [], но не ткущего, нужна езе проверка
            if vertex.index == len(self.v_list) - 1:
                for i in range(0, len(self.v_list)-1):
                    print('vert',self.v_list[i].sign)
                    self.find_min_path_matrix(self.v_list[i], self.v_list[i], min_path_matrix)


        #
    def check_last_vertex(self, vertex, min_path_matrix):
        last = []
        index = 0
        for i in min_path_matrix[vertex.index]:
            last.append(i)


        for i, value in enumerate(min_path_matrix[vertex.index]):
            if value == 1:
                index = i
            if value == 0:
                if i != vertex.index:
                    if min_path_matrix[index][i] != 0:
                        min_path_matrix[vertex.index][i] = min_path_matrix[index][i] + 1





    def min_path_matrix(self):
        min_path_matrix = []

        for list in self.matrix:
            min_path_matrix.append(list)

        for vertex in self.v_list:
            #(vertex.sign, vertex.index)
            self.find_min_path_matrix(vertex, vertex, min_path_matrix)
            if vertex.index == len(self.v_list) - 1:
                self.check_last_vertex(vertex, min_path_matrix)
        for list in min_path_matrix:
            print(list)