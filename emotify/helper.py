d={":-D":"😀",":-)":"🙂",":-|":"😐",":-(":"🙁",":-\\":"😕",":-*":"😗",":-O":"😮",":-#":"🤐","':-D":"😅","':-(":"😓",":'-)":"😂",":'-(":"😢",":-P":"😛",";-P":"😜","X-P":"😝","X-)":"😆","O:-)":"😇",";-)":"😉",":-$":"😳",":-":"😶","B-)":"😎",":-J":"😏","}:-)":"😈","}:-(":"👿",":-@":"😡"}

for key in d.keys():
    print(key)

print(list(d.keys()))

for value in d.values():
    print(value)
print(list(d.values()))

key_list = list(d.keys())

# last char in key
last_char = [key[-1] for key in key_list]

# last chars that are unique
unique_last_char = [key for key in last_char if last_char.count(key) == 1]

print(unique_last_char)

print(len("|\\*O#$-J@"))