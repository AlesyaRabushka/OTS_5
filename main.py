from graph import*
from graph1 import*

if __name__ == '__main__':

    g = Graph()
    g.add_v('v1')
    g.add_v('v2')
    g.add_v('v3')

    g.add_e_not_oriented('v1','v2')
    g.add_e_oriented('v3', 'v2')
    g.add_v('v4')
    g.add_v('v5')

    g.add_e_oriented('v4', 'v3')
    g.add_e_oriented('v4', 'v5')



    g.print_matrix()

    # g.remove_v('v2')
    # print('remove vertex')
    g.remove_e('e2')
    print('remove e')

    print()
    g.print_matrix()
    print('vertexes: ', g.return_v_amount())
    print('edges: ', g.return_e_amount())
    g.return_degrees()
    print('v degree:')
    g.return_v_degree('v2')

    print(g.is_connected())
    print(g.center())

    # graph = Graph('first')
    # graph.add_oriented_e('v1', 'v2')
    # graph.add_oriented_e('v2', 'v1')
    # graph.add_oriented_e('v2', 'v3')
    # graph.add_oriented_e('v3', 'v5')
    # graph.add_not_oriented_e('v5', 'v2')
    # graph.add_v('v5')
    # graph.add_v('v6')
    # print('v', graph.v_amount)
    #
    # graph.print()
    # print(graph.e_list)
    # graph.del_e('v1', 'v2')
    # print(graph.list)
    # # graph.del_v('v2')
    # #
    # # print(graph.list)
    # print('v', graph.v_amount)
    # print('e',graph.e_amount)
    #
    # graph.print()
    # print(graph.e_list)

