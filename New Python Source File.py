a = [1231, "1", "Hello", ["World"], "asdad", 123]
count = 0

for i in a:
    if type(i) == str:
        count += 1

print("Number of strings:", count)
