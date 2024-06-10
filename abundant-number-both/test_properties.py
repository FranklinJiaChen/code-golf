"""
analyzing property of numbers
"""
abundant=[12,
18,
20,
24,
30,
36,
40,
42,
48,
54,
56,
60,
66,
70,
72,
78,
80,
84,
88,
90,
96,
100,
102,
104,
108,
112,
114,
120,
126,
132,
138,
140,
144,
150,
156,
160,
162,
168,
174,
176,
180,
186,
192,
196,
198,
200]

# for i in range(1,212//12):
#     print(i*12,i*12 in abundant)

# abundant12 = [12*i for i in range(1,212//12)]
# not_found = list(set(abundant)-set(abundant12))
# not_found.sort()
# print(not_found)

# for i in range(1,212//18):
#     print(i*18,i*18 in abundant)

# abundant18 = [18*i for i in range(1,218//18)]
# not_found = list(set(abundant)-set(abundant12)-set(abundant18))
# not_found.sort()
# print(not_found)

# def num_divisors(n):
#     return len([i for i in range(1,n) if n%i==0])
# for num in not_found:
#     print(num, num_divisors(num))

# for num in abundant:
#     print(num, num_divisors(num))

# for num in range(1,201):
#     if num_divisors(num)>6 and not num in abundant:
#         print(num, num_divisors(num))

# for num in abundant:
#     if num_divisors(num) < 7:
#         print(num, num_divisors(num))

# for num in abundant:
#     print(num, num_divisors(num)/num)

# for num in range(1,201):
#     if num_divisors(num)>0 and num_divisors(num)/num > 0.1 and not num in abundant:
#         print(num, num_divisors(num)/num)

#doesn't work
# cheat_sheet = ""
# for num in abundant:
#     c = chr(num)
#     cheat_sheet += c

# print(cheat_sheet)

# cheat_sheet = "$(*068<BFHNPTXZ`dfhlprx~ ¢¨®°´ºÀÄÆÈ"

# for c in cheat_sheet:
#     print(ord(c))


# def num_array_to_byte_string(num_array: list[int]) -> str:
#     str = ""
#     for num in num_array:
#         str += num.to_bytes(1, 'big')
#     return str

# print(num_array_to_byte_string(abundant))


# for x in b'~': print(x)
