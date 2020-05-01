#  items =['a','b']
# N= len(items)
# for i in range(3**N):
#     bag1 = []
#     bag2 = []
#     for j in range(N):
#         print('i is ',i)
#         print('j is',j)
#         print('the answer for i // (3 ** j)%3 is',i // (3 ** j)%3)
#         if (i // (3 ** j)) % 3 == 1:
#             bag1.append(items[j])
#         elif (i // (3 ** j)) % 3 == 2:
#             bag2.append(items[j])
#     print(i,bag1,bag2)
#     print('---------') 
dictofsome = {'a':2,'b':3,'c':4,'d':5}
dict_of_love = sorted(dictofsome,key =dictofsome.get,reverse = True)
print(dictofsome.get('c'))

print(dictofsome)
print(dict_of_love)