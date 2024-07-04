import sys

def dfa_simulate(info: str):
    states = []
    state_to_idx = {}
    alphabet, *table, input_str = info.split("\n")
    alphabet = alphabet.split()
    for idx, row in enumerate(table):
        states.append({})
        start, accept, name, *info = row
        if start == '>':
            cur_state = states[idx]
            state_name = name
        if accept == 'F':
            states[idx]['F'] = 'Accept'
        else:
            states[idx]['F'] = 'Reject'
        for idx2, i in enumerate(info[1::2]):
            states[idx][alphabet[idx2]] = i
        state_to_idx[name] = idx
    for c in input_str[1:-1]:
        state_name = cur_state[c]
        cur_state = states[state_to_idx[state_name]]
    print(state_name, cur_state['F'])

for arg in sys.argv[1:]:
    dfa_simulate(arg)