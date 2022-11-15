while True:
    x = input()
    if x == '#':
        break
    t = 0
    for s in ['a','e','i','o','u']:
        t += x.count(s)
        t += x.count(s.upper())
    print(t)