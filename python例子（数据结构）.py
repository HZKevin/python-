items = [ ("product1",2),("product2", 1)]

prices = []
# for item in items:
#     prices.append(item[1])
# print(prices)
prices = list(map(lambda item :item[1],items))
print(prices)
filtered = list(filter(lambda item:item[1]>1,items))
print(filtered)

list1=[1,2,3]
list2=[5,6,7]
print(list(zip("abc",list1,list2)))

# values ={}
# for x in range(5):
#     values[x] =x*2

values = {x:x *2 for x in range(5)}
print(values)

values2 = [x*2 for x in range(10)]
for x in values2:
    print(x)

from sys import getsizeof
values3 = (x*2 for x in range(10000))
print("gen:", getsizeof(values3))
values3 = [x*2 for x in range(10000)]
print("list:", getsizeof(values3))

val = list(range(5))
val = [*range(5),*"hello"]
print(val)

first ={"x": 1}
second ={"x": 10, "y":2}
combined = {**first, **second,"z":1}
print(combined)


sentence = "this is cat"
char_freq ={}
for char in sentence:
    if char in char_freq:
        char_freq[char] += 1
    else:
        char_freq[char] = 1
print(char_freq)
#计算句子的出现频率总量（包含空格）
from pprint import pprint
senten = "this is dog"

char_freq2 ={}
for char in sentence:
    if char in char_freq2:
        char_freq2[char] += 1 
    else:
        char_freq2[char] = 1
pprint(char_freq2, width=1)
#以tuple形式展示出现频率
print(sorted(char_freq2.items()))
#using lambda 
print(sorted(char_freq2.items(),key=lambda kv:kv[1],reverse=True))

