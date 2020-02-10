# # #exercise1
# # def nested_sum(t):
# #     a=0
# #     for i in t:
# #         a+=sum(i)
# #     return a
# # t = [[1,2], [3], [4,5,6]]
# # print(nested_sum(t))
#
# #exercise2
def cumsum(t):
    a=0
    a_t=[]
    for i in t:
        a+=i
        a_t=a_t+[a]
    return a_t
t = [1, 2, 3]
print(cumsum(t))
#
# # exercise3
# # def middle(t):
# #     return t[1:-1]
# # t=[1,2,3,4]
# # print(middle(t))
#
# #exercise4
# # def chop(t):
# #     del t[0]
# #     del t[-1]
# # t=[1,2,3,4]
# # chop(t)
# # print(t)
#
# #exercise5
# # def is_sorted(t):
# #     a=list(t)
# #     a.sort()
# #     return a==t
# # t = [1,2,2]
# # print(is_sorted(t))
# # t = ['b','a']
# # print(is_sorted(t))
#
# #exercise6
# # def is_anagram(a,b):
# #     a.sort()
# #     b.sort()
# #     return a==b
# # a=['a','b','c','d']
# # b=['d','c','b','a']
# # print(is_anagram(a,b))
#
# #exercise7
# # def has_duplicates(t):
# #     a=list(t)
# #     a.sort()
# #     for i in range(len(t)-1):
# #         if a[i]==a[i+1]:
# #             return True
# #     return False
# # t = ['a','b','a']
# # print(has_duplicates(t))
# #exercise8
# import random
#
# def random_birthday(n):
#     t = []
#     for i in range(n):
#         birthday = random.randint(1, 365)
#         t.append(birthday)
#     return t
#
# def has_duplicates(t):
#     a = list(t)
#     a.sort()
#     for i in range(len(t) - 1):
#         if a[i] == a[i + 1]:
#             return True
#     return False
#
# def count_match(students, experiment):  ##计算23个同学在1000次试验中，有多少次至少有一对同学同一天过生日的
#     count = 0
#     for i in range(experiment):
#         lst = random_birthday(students)
#         if has_duplicates(lst):
#             count += 1
#     return count
#
# students = 23
# experiment= 10000
# count = count_match(students, experiment)
# print(f'After {experiment} simulations with {students}students,'
#       f'there were {count}experiments successfully matched.'
#       f'The probability of matching success is {count / experiment}' )
#
#
#
#
#
#
#
for i in range(1,1):
    print(i)
