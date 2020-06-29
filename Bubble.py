# a = [1, 5, 3, 7, 2, 4]
# for i in range(len(a)):
#     for j in range(len(a)-1):
#         if a[j] > a[j+1]:
#             a[j], a[j+1] = a[j+1], a[j]
# print(a)
"""
函数法
"""

# def bubble(list1):
#     for i in range(len(list1)):
#         for j in range(len(list1)-1):
#             if list1[j] > list1[j + 1]:
#                 list1[j], list1[j + 1] = list1[j + 1], list1[j]
#     return list1
# print(bubble(list1=[1, 5, 3, 2, 6]))


"""
类法
"""

class Bob:
    def __init__(self, a):
        self.a = a

    def sort(self):
        for i in range(len(self.a)):
            for j in range(len(self.a) - 1):
                if self.a[j] > self.a[j + 1]:
                    self.a[j], self.a[j + 1] = self.a[j + 1], self.a[j]
        return self.a

b = Bob([5, 2, 7, 1, 0])
print(b.sort())
