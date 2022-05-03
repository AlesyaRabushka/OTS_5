from graph import*
from graph1 import*

if __name__ == '__main__':

    g = Graph()
    g.add_v('v1')
    g.add_v('v2')
    g.add_v('v3')
    g.add_v('v4')
    g.add_v('v5')

    g.add_e_oriented('v1', 'v2')
    g.add_e_oriented('v3', 'v2')
    g.add_e_oriented('v3', 'v5')
    g.add_e_oriented('v3', 'v4')
    g.add_e_oriented('v2', 'v4')
    g.add_e_oriented('v4', 'v5')
    g.add_e_oriented('v4', 'v1')



    g.print_matrix()

    # g.remove_v('v2')
    # print('remove vertex')
    # g.remove_e('e2')
    # print('remove e')



    print('connected', g.is_connected())
    g2 = Graph()
    g2.add_v('v1')
    g2.add_v('v2')
    g2.add_v('v3')
    g2.add_v('v4')

    g2.add_e_oriented('v1','v2')
    g2.add_e_not_oriented('v2','v3')
    g2.add_e_not_oriented('v3','v4')
    g2.add_e_oriented('v4','v1')
    print('gamilton', g2.is_gamilton())

    g3 = Graph()
    g3.add_v('v1')
    g3.add_v('v2')
    g3.add_v('v3')
    #g3.add_v('v4')

    g3.add_e_oriented('v1','v2')
    g3.add_e_oriented('v1','v3')
    g3.add_e_not_oriented('v2','v3')

    print(g3.is_connected())
    # g3.print_matrix()
    # for v in g3.v_list:
    #     print(v.connection)