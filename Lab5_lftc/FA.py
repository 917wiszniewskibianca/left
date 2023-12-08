
class FA:
    def __init__(self, filename):
        self.states = []
        self.alphabet = []
        self.transition = {}
        self.initial_state = ""
        self.final_states = []
        self.read_file(filename)

    def read_file(self, filename):
        with open(filename) as f:
            self.states = f.readline().strip().replace(" ", "").split(",")
            if len(self.states) == 0:
                raise RuntimeError("Error while parsing states")
            self.alphabet = f.readline().strip().replace(" ", "").split(",")
            if len(self.alphabet) == 0:
                raise RuntimeError("Error while parsing alphabet")
            self.initial_state = f.readline().strip()
            if len(self.initial_state) == 0:
                raise RuntimeError("Error while parasing initial state")
            self.final_states = f.readline().strip().replace(" ", "").split(",")
            if len(self.final_states) == 0:
                raise RuntimeError("Error while parsing final states")
            for read_line in f:
                line = read_line.strip().replace(" ", "").split("=")
                pair = line[0].strip().split(",")
                for letter in pair[1]:
                    self.transition.setdefault((pair[0], letter), []).append(line[1])


    def deterministic(self):
        return False if any([elem for elem in self.transition.values() if len(elem) > 1]) else True

    def check_sequence(self, sequence):
        if self.deterministic():
            state = self.initial_state
            for path in sequence:
                if (state, str(path)) not in self.transition.keys():
                    return  False, None
                state = self.transition[(state, str(path))][0]
            return state in self.final_states, state
        return False

    def __repr__(self):
        return " States: " + str(self.states) + "\n Alphabet: " + str(
            self.alphabet) + "\n Transition Functions: " + str(
            self.transition) + "\n Initial state: " + self.initial_state + "\n Final states: " + str(self.final_states)
"""
Deterministic Finite Automata (DFA): 
    In a DFA, for each input symbol, there is exactly one defined transition from each state. 
    This means that given a current state and an input symbol, the automaton always transitions to a specific next state.
Nondeterministic Finite Automata (NFA):
    In an NFA, there can be multiple possible transitions from a state for a given input symbol. 
    This means the automaton can transition to multiple states simultaneously based on the same input symbol.
"""
