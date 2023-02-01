state_capitals = {
    'Arkansas': 'Little Rock',
    'Colorado': 'Denver',
    'California': 'Sacramento',
    'Georgia': 'Atlanta'
}

ca_capital = state_capitals['California']
print(ca_capital)

for state in state_capitals.keys():
    print('{} is the state for the capital {}'.format(state, state_capitals[state]))

print("\n")

for capital in state_capitals.keys():
    print('{} is the capital of {}'.format(state_capitals[capital], capital))
    
    
