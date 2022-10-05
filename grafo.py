import networkx as nx
import pyttsx3
from attr import attr


#configuracion voz
engine = pyttsx3.init()
engine.setProperty('rate', 120)
engine.setProperty('voice', 'spanish')
engine.setProperty('volume', 2)

#creacion grafo
g = nx.MultiDiGraph()

#agregacion nodos
g.add_node("q0")
g.add_node("q1")
g.add_node("q2")

#agregar aristas
g.add_edge("q0","q0","$",attr='$')
g.add_edge("q0","q1","A",attr="A")
g.add_edge("q0","q2","B",attr="B")
g.add_edge("q0","q2","C",attr="C")
g.add_edge("q1","q1","A",attr="A")
g.add_edge("q1","q2","C",attr="C")
g.add_edge("q1","q2","B",attr="B")
g.add_edge("q2","q2","B",attr="B")
g.add_edge("q2","q2","C",attr="C")

def buscar(g,palabra):
    c = 0
    nodo = 0
    acumulado = ""
    
    if palabra == "$":
        return "aceptado"
    else:
        for i in palabra:
            c+=1
            if g.get_edge_data("q0","q1")['A']['attr'] == i and c==1:
                acumulado+=i
                nodo = 1
                if len(palabra) == c and acumulado==palabra:
                    return "aceptado"
                else:
                    continue
            elif g.get_edge_data("q1","q1")['A']['attr'] == i and nodo==1:
                acumulado+=i
                nodo = 1
                if len(palabra) == c and acumulado==palabra:
                    return "aceptado"
                else:
                    continue
            elif g.get_edge_data("q1","q2")['B']['attr'] == i or g.get_edge_data("q1","q2")['C']['attr'] == i and nodo==1:
                acumulado+=i
                nodo=2
                if len(palabra) == c and acumulado==palabra:
                    return "aceptado"
                else:
                    continue
            elif g.get_edge_data("q2","q2")['B']['attr'] == i or g.get_edge_data("q2","q2")['C']['attr'] == i and nodo==2:
                acumulado+=i
                nodo = 2
                if len(palabra) == c and acumulado==palabra:
                    return "aceptado"
                else:
                    continue
            elif g.get_edge_data("q0","q2")['B']['attr'] == i or g.get_edge_data("q0","q2")['C']['attr'] == i and c==1 and nodo==0:
                acumulado+=i
                nodo = 2
                if len(palabra) == c and acumulado==palabra:
                    return "aceptado"
                else:
                    continue
            else:
                return "No aceptado"            
    
# if buscar(g,"ACCCC") == "aceptado":
#     engine.say("aceptado")
#     engine.runAndWait()
# else:
#     engine.say("No aceptado")
#     engine.runAndWait()

# for c in g.adjacency():
#     print(c)

from automata.fa.dfa import DFA

dfa = DFA(
    states = { 'q0' ,  'q1' ,  'q2' }, 
    input_symbols = { 'A' ,  'B' , 'C' }, 
    transitions = { 
        'q0' :  { 'A' :  'q1' , 'B' :  'q2', 'C' : 'q2' }, 
        'q1' :  { 'A' :  'q1' , 'B' :  'q2' , 'C': 'q2'}, 
        'q2' :  { 'B' :  'q2' ,  'C' :  'q2' } 
    }, 
    initial_state = 'q0' , 
    final_states = { 'q1' , 'q2' , 'q3' } 
)

dfa.read_input('A')


dfa2 = DFA(
    states={'q0', 'q1', 'q2'},
    input_symbols={'0', '1'},
    transitions={
        'q0': {'0': 'q0', '1': 'q1'},
        'q1': {'0': 'q0', '1': 'q2'},
        'q2': {'0': 'q2', '1': 'q1'}
    },
    initial_state='q0',
    final_states={'q1'}
)

obj = dfa2.read_input_stepwise('01')

def buscar(dfa, palabra):
    if dfa2.accepts_input('AA'):
        return 'aceptado'
    else:
        return 'denegado'