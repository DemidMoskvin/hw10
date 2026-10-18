a = [1231, '1', "Hello", ['World'], "asdad", 123]
b=0
for i in a:
    if type(i)==str:
        b+=1
print(b)
