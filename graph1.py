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

        self.gam_path = []
        self.gam_visited = []
        self.gam_not_visited = []

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






    def gamilton(self, v0):
        find = False
        if v0 not in self.gam_path:
            self.gam_path.append(v0)
            if len(self.gam_path) == len(self.v_list):
                return True
            for v in self.gam_not_visited:
                if v not in self.gam_visited:
                    self.gam_visited.append(v)
                    self.gam_path.append(v)
                    find = self.gamilton(v)
                    if not find:
                        self.gam_visited.remove(v)
        return find

    def dfs_connected(self, v0, vertex, path):
        all_vis = 1
        path.append(vertex.sign)
        for v in vertex.degree:
            if v.sign not in path:
                all_vis1, path = self.dfs_connected(v0, v, path)
                all_vis += all_vis1

        return all_vis, path

        # if v0 != vertex:
        #     if vertex not in path:
        #         path.append(vertex.sign)
        #
        #         if vertex.sign in v0.connection:
        #             v0.connection[vertex.sign] += 1
        #         elif vertex.sign not in v0.connection:
        #             if len(v0.connection) == 0:
        #                 v0.connection[vertex.sign] = v0.connection_count
        #             else:
        #                 if vertex in vertex.prev.degree:
        #                     v0.connection_count += 1
        #                     v0.connection[vertex.sign] = v0.connection_count
        #                 elif vertex not in vertex.prev.degree:
        #                     v0.connection[vertex.sign] = v0.connection_count - 1
        #
        #         print(vertex.sign)
        #         print(v0.connection)
        # elif v0 == vertex:
        #     v0.connection_count = 1
        # all_vis = 1
        # for v in vertex.degree:
        #     if v.sign not in path:
        #         v.prev = vertex
        #         all_vis1, path = self.dfs_connected(v0, v, path)
        #         all_vis += all_vis1
        #     else:
        #         pass



        # for e in vertex.edges:
        #     if e.vertex1 == vertex :
        #         v = e.vertex2
        #         if v.sign not in path:
        #             all_vis1, path = self.dfs(v0, v, path)
        #             all_vis += all_vis1



    def dfs_gamilton(self, v0, vertex, path):
        all_vis = 1
        path.append(vertex.sign)
        for e in vertex.edges:
            if e.vertex1 == vertex :
                v = e.vertex2
                if v.sign not in path:
                    all_vis1, path = self.dfs_gamilton(v0, v, path)
                    all_vis += all_vis1

        return all_vis, path
        # flag = False
        # if len(vertex.not_visited) != 0:
        #     for e in vertex.edges:
        #         if e.vertex1 == vertex:
        #             v = e.vertex2
        #             if v not in vertex.visited:
        #                 vertex.visited.append(v)
        #                 vertex.not_visited.remove(v)
        #                 path.append(v.sign)
        #                 flag = self.dfs(v, path)
        #                 if not flag:
        #
        # return flag
        #return flag




        # if len(vertex.not_visited) != 0:
        #     for v in vertex.not_visited:
        #         for e in v.edges:
        #             if e.vertex1 == vertex:
        #
        #                 if v not in vertex.visited:
        #                     vertex.visited.append(v)
        #                     vertex.not_visited.remove(v)
        #                     self.dfs(v)
        # else:
        #     self.ex[vertex] = vertex.visited









    def is_connected(self):
        count = 0
        for v in self.v_list:
            path = []
            kol, path = self.dfs_connected(v, v, path)
            print(v.sign, 'kolvo',kol, 'path-', path)
            if kol == len(self.v_list):
                count += 1
        if count == len(self.v_list) or count == len(self.v_list) - 1:
            return True
        else:
            return False

    def is_gamilton(self):
        count = 0
        for v in self.v_list:
            path = []
            kol, path = self.dfs_gamilton(v, v, path)
            print(v.sign, 'kolvo', kol, 'path-', path)
            if kol == len(self.v_list):
                count += 1
        if kol == len(self.v_list):
            return True
        else:
            return False



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
        self.matrix.pop(del_v.index)
        self.v_list.remove(del_v)

    def set_v_color(self, vertex, color):
        for v in self.v_list:
            if v.sign == vertex:
                v.color = color



    def add_e_oriented(self, vertex1, vertex2):
        self.e_amount += 1
        sign = 'e' + str(self.e_amount)

        #NOT SURE if we shoul add new vertexes
        for v in self.v_list:
            if v.sign == vertex1:
                v1 = v
            elif v.sign == vertex2:
                v2 = v
        if v1 == None:
            self.add_v(vertex1)
        if v2 == None:
            self.add_v(vertex2)

        e = Edge(self, v1, v2, 1, sign)
        self.e_list.append(e)

        # add EDGE to the matrix
        for count, list in enumerate(self.matrix):
            if v1.index == count:
                for i in range(0, len(list)):
                    if i == v2.index:
                        list[i] = 1
                        v1.degree.append(v2)
                        v1.edges.append(e)
                        v2.degree.append(v1)
                        v2.edges.append(e)


    def add_e_not_oriented(self, vertex1, vertex2):
        self.e_amount += 1
        sign = 'e' + str(self.e_amount)
        for v in self.v_list:
            if v.sign == vertex1:
                v1 = v
            elif v.sign == vertex2:
                v2 = v
        e = Edge(self, v1, v2, 2, sign)
        self.e_list.append(e)

        # add EDGE to the matrix
        for count, list in enumerate(self.matrix):
            if v1.index == count:
                for i in range(0, len(list)):
                    if i == v2.index:
                        list[i] = 1
                        v1.degree.append(v2)
                        v1.edges.append(e)
            if v2.index == count:
                for i in range(0, len(list)):
                    if i == v1.index:
                        list[i] = 1
                        v2.degree.append(v1)
                        v2.edges.append(e)

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

    def set_e_color(self, edge, color):
        for e in self.e_list:
            if e.sign == edge:
                e.color = color

    def search_e(self, v1, v2):
        for e in self.e_list:
            if (e.vertex1 == v1 and e.vertex2 == v2) or (e.vertex1 == v2 and e.vertex2 == v1):
                return e
        return None