from graph import*

if __name__ == '__main__':
    graph = Graph('first')
    graph.add_oriented_e('v1', 'v2')
    graph.add_oriented_e('v2', 'v1')
    graph.add_oriented_e('v2', 'v3')
    graph.add_oriented_e('v3', 'v5')
    graph.add_not_oriented_e('v5', 'v2')
    graph.add_v('v5')
    graph.add_v('v6')
    print('v', graph.v_amount)

    graph.print()
    print(graph.e_list)
    graph.del_e('v1', 'v2')
    print(graph.list)
    # graph.del_v('v2')
    #
    # print(graph.list)
    print(graph.v_amount)
    print(graph.e_amount)

    graph.print()
    print(graph.e_list)

