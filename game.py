s = '0100101'
s = list(s)
len_s = len(s)
mid = len_s//2
print(mid)
first, second = 0,0
first = 0
second = mid+1
count = 0
if s%2 == 0:

    print('even')
else:
    while second < len_s:
        if s[first] == s[second]:
            first += 1
            second += 1
        elif(s[second-1] == s[first]):
            temp = s[second]
            s[second] = s[second-1]
            s[second-1] = temp
            count += 1 

    print('odd')

print(first, second)

# string_start = s[:mid]
# string_end = s[mid+1:]
# swap_counter = 0
# print(string_start)
# print(string_end)
# zeros_end = string_end.count('0')
# ones_end = string_end.count('1')
# zeros_start = string_start.count('0')
# ones_start = string_start.count('1')
# if ones_end != ones_start and zeros_end != zeros_start:
#     print('-1')
# else:
#     for i in range(len(string_end)):
#         if(string_end[i] != string_start[i]):
#             swap_counter += 1
