from automata.fa.dfa import DFA

dfa = DFA(
    states={'q0','q1','q2'},
    input_symbols={'a', 'b','c','$'},
    transitions={
        'q0': {'a':'q1','b':'q2','c':'q2'},
        'q1': {'a':'q1','b':'q2','c':'q2'},
        'q2': {'b':'q2','c': 'q2'}
    },
    initial_state='q0',
    final_states={'q0','q1','q2'}
)

def buscar(dfa, palabra):
    if dfa.accepts_input(palabra):
        return 'aceptado'
    else:
        return 'denegado'

# print(buscar(dfa,'$'))


# dfa.show_diagram(path='static/image/dfa.png')