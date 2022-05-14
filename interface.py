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

        self.graph_center = 0
        self.graph_radius = 0
        self.diameter = 0

        self.vertex_text = ''


    def add_graph(self, name):
        flag = False
        for graph in self.graphs:
            if graph.name == name:
                print(graph.name, name)
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

    def delete_graph(self):
        flag = False
        for g in self.graphs:
            if g.name == self.ids.graph_name.text:
                self.graphs.remove(g)
                flag = True

        if not flag:
            self.ids.matrix.text = 'No graph has been found'

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

    # set VERTEX TEXT
    def v_text(self, text):
        self.vertex_text = text
    def return_v_text(self):
        return self.vertex_text
    def set_v_text(self, vertex, text):
        for g in self.graphs:
            if g.name == self.ids.graph_name.text:
                for v in g.v_list:
                    if v.sign == vertex:
                        v.text = text



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

                self.ids.matrix.text = matrix + vertex_amount + edge_amount + connected


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

    def print_v_info(self, vertex):
        for g in self.graphs:
            if g.name == self.ids.graph_name.text:
                flag = False
                # for all vertexes
                if vertex != '':
                    for v in g.v_list:
                        if flag:
                            break
                        else:
                            degrees = ''
                            colors = ''
                            text = ''
                            if v.sign == vertex:
                                degrees = vertex + ' - d: ' + str(v.degrees)
                                if v.color != '':
                                    colors = ' color: ' + str(v.color)
                                if v.text != '':
                                    text = ' text: ' + str(v.text)
                                flag = True

                                self.ids.matrix.text = degrees + colors + text
                # for one vertex
                else:
                    vertexes_info = ''
                    for v in g.v_list:
                        degrees = ''
                        colors = ''
                        text = ''
                        degrees = v.sign + ' d : ' + str(v.degrees)
                        if v.color != '':
                            colors = ' color: ' + str(v.color)
                        if v.text != '':
                            text = ' text: ' + str(v.text)
                        vertex_info = degrees + colors + text
                        vertexes_info += vertex_info + '\n'

                    if vertexes_info == '':
                        self.ids.matrix.text = 'No vertexes have been found'
                    else:
                        self.ids.matrix.text = vertexes_info



    def print_e_info(self):
        for g in self.graphs:
            if g.name == self.ids.graph_name.text:
                edges = ''
                for e in g.e_list:
                    if e.type == 1:
                        e_type = ' -> '
                    elif e.type == 2:
                        e_type = ' = '
                    edge = e.sign + ' : ' + e.vertex1.sign + e_type + e.vertex2.sign
                    if e.color != '':
                        edge += ' color: ' + e.color
                    edges += edge + '\n'
        if edges == '':
            self.ids.matrix.text = 'No edges have been found'
        else:
            self.ids.matrix.text = edges


    def change_graph(self, new_graph_name):
        flag = False
        for g in self.graphs:
            if g.name == self.new_name:
                self.ids.graph_name.text = new_graph_name
                flag = True

        if not flag:
            self.ids.matrix.text = 'No graph has been found'


    def find_c_r_d(self):
        for g in self.graphs:
            if g.name == self.ids.graph_name.text:
                g.min_path()
                g.max_path()
                self.graph_radius = g.graph_radius
                self.diameter = g.diameter
                self.graph_center = g.center_vertex

                r = 'Radius: ' + str(self.graph_radius)
                d = '\nDiameter: ' + str(self.diameter)
                c = '\nCenter: ' + str(self.graph_center)
                self.ids.matrix.text = r + d + c


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


    def dekart_mutiplication(self, graph):
        graph1, graph2 = None, None
        for g in self.graphs:
            if g.name == self.ids.graph_name.text:
                graph1 = g
                break

        for g2 in self.graphs:
            if g2.name == graph:
                graph2 = g2
                break

        if graph1 == None or graph2 == None:
            self.ids.matrix.text = 'No graph has been found'
        else:
            new_name = graph1.name + graph2.name
            self.add_graph(new_name)
            print('added new graph ', new_name)
            for dekart_graph in self.graphs:
                if dekart_graph.name == new_name:
                    dekart_graph.type = 1
                    dekart_edges = []
                    print('start dekart')
                    dekart_edges = graph1.dekart_multiplication(graph2, dekart_graph)
                    string = ''
                    string += 'Dekart multiplication\n'
                    for e in dekart_graph.e_list:
                        string += e.vertex1.sign + '->' + e.vertex2.sign + '\n'

                    self.ids.matrix.text = string
                    break

    # multiple edges
    def show_multi_e(self):
        for g in self.graphs:
            if g.name == self.ids.graph_name.text:
                multi_e = g.search_multiple_e()
                if len(multi_e) == 0:
                    self.ids.matrix.text = 'No multiple edges have been found'
                else:
                    multi_edges = ''
                    for e in multi_e:
                        print(e.sign)
                        if e.type == 1:
                            e_type = ' -> '
                        elif e.type == 2:
                            e_type = ' = '
                        multi_edges += e.vertex1.sign + e_type + e.vertex2.sign + '\n'

                    self.ids.matrix.text = 'Multiple edges:\n' + multi_edges



Builder.load_file(os.path.join(os.path.dirname(__file__), "graph.kv"))