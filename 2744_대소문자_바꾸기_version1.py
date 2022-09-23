a = input()
for k in a:
    if k.islower():
        print(k.upper(),end ='')
    else:
        print(k.lower(),end='')