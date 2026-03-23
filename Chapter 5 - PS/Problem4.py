s = set()
s.add(20)
s.add(20.0)
s.add('20')

print(s)  # Python treats 20 and 20.0 as same value (20 == 20.0)

l = len(s)
print(l)