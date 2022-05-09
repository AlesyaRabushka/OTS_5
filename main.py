from graph import*
from graph1 import*

if __name__ == '__main__':

    g = Graph()
    g.add_v('v1')
    g.add_v('v2')
    g.add_v('v3')
    g.add_v('v4')


    g.add_e_not_oriented('v1','v2')
    g.add_e_oriented('v1','v3')
    #g.add_e_oriented('v4','v3')
    g.add_e_oriented('v3','v2')
    g.add_e_oriented('v2','v4')
    g.add_e_not_oriented('v4','v1')

    g.print_matrix()
    g.return_degrees()
    # for v in g.v_list:
    #     print('----',v.sign,':')
    #     for i in v.degree:
    #         print(i.sign)
    #     print(len(v.edges))
    #     for i in v.edges:
    #         print(i.vertex1.sign,'->',i.vertex2.sign)
