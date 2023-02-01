from collections import defaultdict

state_capitals = {
    'Arkansas': 'Little Rock',
    'Colorado': 'Denver',
    'California': 'Sacramento',
    'Georgia': 'Atlanta'
}

state_capitals = defaultdict(lambda: 'Boston')
#If we try to access the dict with a non-existent key, python will return us the default value i.e. Boston

state_capitals['Arkansas'] = 'Little Rock'
state_capitals['California'] = 'Sacramento'

print(state_capitals['Arkansas']) # 'Little Rock'
print(state_capitals['California']) # 'Sacramento'
print("\n")
print(state_capitals['Alabama']) #'Boston'
print("\n")
print(state_capitals)


"""
Little Rock
Sacramento


Boston


defaultdict(<function <lambda> at 0x7ff0976cfa30>, 
{'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Alabama': 'Boston'})
"""
