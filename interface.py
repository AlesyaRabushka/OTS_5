from kivymd.uix.screen import MDScreen
import os
from kivy.lang import Builder
from graph1 import Graph, Vertex, Edge

class MainScreen(MDScreen):
    def __init__(self):
        super().__init__()
        self.graphs = []
        self.count = 0

        self.vertex_name = ''
        self.vertex_color = ''
        self.edge_name = ''
        self.edge_color = ''

        self.vertex1_name = ''
        self.vertex2_name = ''

        self.new_name = ''
        self.new_vertex_name = ''


    def add_graph(self, name):
        flag = False
        for graph in self.graphs:
            if graph.name == name:
                flag = True
        if flag:
            self.ids.matrix.text = 'The graph with the same name is already existed'
        else:
            self.count += 1
            g = Graph()
            if name == '':
                g.name = 'G'+str(self.count)
            else:
                g.name = name
            self.graphs.append(g)
            self.ids.graph_name.text = g.name

    def add_v(self, name):
        if len(self.graphs) == 0:
            self.add_graph('')
            for g in self.graphs:
                # g.add_v(name)
                if self.ids.graph_name.text == g.name:
                    g.add_v(name)
        else:
            for g in self.graphs:
                if self.ids.graph_name.text == g.name:
                    flag = False
                    for v in g.v_list:
                        print(v.sign)
                        if v.sign == name:
                            flag = True
                    if flag:
                        self.ids.matrix.text = 'The vertex with the same name is already existed'
                    else:
                        g.add_v(name)

    def set_new_v_name(self, name, new_name):
        for g in self.graphs:
            if g.name == self.ids.graph_name.text:
                flag = False
                vertex = None
                count = 0
                for v in g.v_list:
                    if v.sign == new_name:
                        count += 1

                if count > 0:
                    self.ids.matrix.text = 'The vertex with the same name is already existed'
                else:
                    for v in g.v_list:
                        if v.sign == name:
                            count += 1
                            v.sign = new_name
                            self.ids.matrix.text = 'The vertex has been successfully renamed'
                            break
                #if flag:


    def remove_v(self, name):
        for g in self.graphs:
            if g.name == self.ids.graph_name.text:
                g.remove_v(name)

    def add_e_oriented(self, vertex1, vertex2, name):
        for g in self.graphs:
            if g.name == self.ids.graph_name.text:
                flag = False
                for e in g.e_list:
                    if e.sign == name:
                        flag = True

                if flag:
                    self.ids.matrix.text = 'The edge with the same name is already existed'
                else:
                    if not (g.add_e_oriented(vertex1, vertex2, name, 1)):
                        self.ids.matrix.text = 'The vertex does not exist'
                    else:
                        pass



    def add_e_not_oriented(self, vertex1, vertex2, name):
        for g in self.graphs:
            if g.name == self.ids.graph_name.text:
                flag = False
                for e in g.e_list:
                    if e.sign == name:
                        flag = True
                if flag:
                    self.ids.matrix.text = 'The edge with the same name is already existed'
                else:
                    if not g.add_e_not_oriented(vertex1, vertex2, name):
                        self.ids.matrix.text = 'The vertex does not exist'
                    else:
                        pass

    def remove_e(self, edge):
        for g in self.graphs:
            if g.name == self.ids.graph_name.text:
                if not g.remove_e(edge):
                    self.ids.matrix.text = 'The edge does not exist'
                else:
                    pass


    def v_name(self, name):
        self.vertex_name = name
    def new_v_name(self, name):
        self.new_vertex_name = name
    def v_color(self, color):
        self.vertex_color = color
    def return_v_color(self):
        return self.vertex_color
    def return_v_name(self):
        return self.vertex_name
    def return_new_v_name(self):
        return self.new_vertex_name
    # vertexes to create an edge
    def e_v_name1(self, name):
        self.vertex1_name = name
    def e_v_name2(self, name):
        self.vertex2_name = name
    def return_e_v_name1(self):
        return self.vertex1_name
    def return_e_v_name2(self):
        return self.vertex2_name

    def e_name(self, name):
        self.edge_name = name
    def e_color(self, color):
        self.edge_color = color
    def return_e_color(self):
        return self.edge_color
    def return_e_name(self):
        return self.edge_name


    def print_graph_info(self):
        for g in self.graphs:
            if g.name == self.ids.graph_name.text:
                print('matrix')
                g.print_matrix()
                matrix = ''
                for list in g.matrix:
                    matrix += str(list) + '\n'

                connected = ''
                if g.is_connected():
                    connected = '\nConnected: True'

                else:
                    connected = '\nConnected: False'

                vertex_amount = '\nVertexes: ' + str(g.v_amount)
                edge_amount = '\nEdges: ' + str(g.e_amount)

                colors = ''
                for v in g.v_list:
                    if v.color != '':
                        colors += '\n' + str(v.sign) + ' color: ' + str(v.color)
                for e in g.e_list:
                    if e.color != '':
                        colors += '\n' + str(e.sign) + ' color: ' + str(e.color)

                self.ids.matrix.text = matrix + vertex_amount + edge_amount + connected + colors


    def print_hamilton_cycles(self):
        for g in self.graphs:
            if g.name == self.ids.graph_name.text:
                cycles = ''
                cycle = ''
                if g.is_gamilton():
                    ham = g.gam_cycles
                    for list in ham:
                        cycle = ''
                        for index, value in enumerate(list):
                            if index == len(list) - 1:
                                cycle += value
                            else:
                                cycle += value + str('->')
                        cycles += str(cycle) + '\n'
                else:
                    cycles = 'NO Hamiltom cycles'

                self.ids.matrix.text = cycles


    def make_connected(self):
        for g in self.graphs:
            if g.name == self.ids.graph_name.text:
                if g.is_connected():
                    self.ids.matrix.text = 'Graph is already connected'

                else:
                    self.ids.matrix.text = 'Graph is connected now'
                    g.make_connected()

    def print_v_degree(self, vertex):
        for g in self.graphs:
            if g.name == self.ids.graph_name.text:
                degrees = ''
                if vertex != '':
                    for v in g.v_list:
                        if v.sign == vertex:
                            degrees = vertex + ':' + str(v.degrees)


                else:
                    for v in g.v_list:
                        degrees += v.sign + ': ' + str(v.degrees) + '\n'


                self.ids.matrix.text = degrees


    def change_graph(self, new_graph_name):
        for g in self.graphs:
            if g.name == self.new_name:
                self.ids.graph_name.text = new_graph_name


    def find_c_r_d(self):
        for g in self.graphs:
            if g.name == self.ids.graph_name.text:
                #pass
                g.min_path()


    # CHANGE GRAPH NAME
    def change_g_name(self, name):
        self.new_name = name
    def return_change_g_name(self):
        return self.new_name

    def set_v_color(self, vertex, color):
        for g in self.graphs:
            if g.name == self.ids.graph_name.text:
                for v in g.v_list:
                    if v.sign == vertex:
                        v.color = color

    def set_e_color(self, edge, color):
        for g in self.graphs:
            if g.name == self.ids.graph_name.text:
                for e in g.e_list:
                    print(e.sign, edge)
                    if e.sign == edge:
                        e.color = color

Builder.load_file(os.path.join(os.path.dirname(__file__), "graph.kv"))