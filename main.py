from graph import*
from graph1 import*

if __name__ == '__main__':

    g = Graph()
    g.add_v('v1')
    g.add_v('v2')
    g.add_v('v3')
    g.add_v('v4')
    g.add_v('v5')
    g.add_v('v6')

    g.add_e_oriented('v1', 'v2')
    g.add_e_oriented('v2', 'v3')
    g.add_e_oriented('v3', 'v4')
    g.add_e_oriented('v4', 'v5')
    g.add_e_oriented('v5', 'v6')
    g.add_e_oriented('v6', 'v1')

    g.add_e_oriented('v3', 'v5')
    g.add_e_oriented('v4', 'v1')
    g.add_e_oriented('v2', 'v5')
    g.add_e_oriented('v2', 'v1')

    g.print_matrix()
    print('is gamilton?',g.is_gamilton())