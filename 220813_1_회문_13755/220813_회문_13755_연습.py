# # 회문_13755
# lst = [['a','b','c'],['d','e','f'],['g','h','i']]
#
# print(lst[0][0:2])
# print(lst[0][0 : 3][::-1])
# print(lst[0:2])
# print(lst[0 : 3][0][::-1])

def rev(lst):
    a=[]
    for r in range(len(lst)-1, -1, -1):
        a.append(lst[r])
    return a


a=[1,2,3,4,5]
print(a[-2])
print(rev(a))