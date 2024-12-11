def build_transition_table(pattern):
    m = len(pattern)
    states = [{} for _ in range(m + 1)]

    for state in range(m + 1):
        for num in range(10): 
            next_state = state
            while next_state > 0 and (next_state == m or pattern[next_state] != num):
                next_state -= 1
            if next_state < m and pattern[next_state] == num:
                next_state += 1
            states[state][num] = next_state
    return states


def finite_automata_string_matching(text, pattern):
    table = build_transition_table(pattern)
    state = 0
    matches = []

    for i, num in enumerate(text):
        if num in table[state]:
            state = table[state][num]
        else:
            state = 0

        if state == len(pattern):  
            matches.append(i - len(pattern) + 1)
            state = 0  
    return matches

text = [2, 7, 3, 8, 5, 7, 3, 8, 1, 7, 3, 9]
pattern = [7, 3, 8]

print("Text:", text)
print("Pattern:", pattern)

matches = finite_automata_string_matching(text, pattern)
print("Pattern found at indices:", matches)
