str=input("Enter a String:")
dict = ()
for n in str:
    keys = dict.key()
    if n in keys:
        dict[n] += 1
    else:
        dict[n] = 1
print (dict)
