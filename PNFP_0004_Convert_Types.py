a = 'hello'

print(list(a)) # ['h', 'e', 'l', 'l', 'o']

print(set(a)) # {'o', 'e', 'l', 'h'}

print(tuple(a)) # ('h', 'e', 'l', 'l', 'o')


a = '123.456'

b = float(a)
c = int(a) # ValueError: invalid literal for int() with base 10: '123.456'
d = int(b) # 123
