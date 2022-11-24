from random import randint
import time

#Создадим еще массив и посмотрим что быстрее работает

#Cоздаем рекурсию
class Node: #node узел
    def __init__(self,key) ->None:
        self.key = key
        self.right = None
        self.left = None
        self.parent = None
#функция фставки
def insert_tree(root,node):
    if root is None:
        root = node
    else:
        if root.key> node.key:     #значит мы должны идти в правую часть
            if root.left is None:   #не существует левого сына
                root.left=node
            else:           # иначеон существует
                insert_tree(root.left,node)
        elif root.key< node.key:
            if root.right is None: #то естьне существует в данном случае
               root.right=node
            else:  # иначе существует правый сын и мы должны пойти туда
                insert_tree(root.right,node)
#создадим функцию чтоб мы могли сортировать наше дерево
# Функция сортировки по возростанию
def sort_max(root): #Создали root сортировка по возростанию
    if root != None:
        sort_max(root.left)
        print(root.key)
        sort_max(root.right)
def sort_min(root): #сортировка по убыванию
     if root != None:
         sort_min(root.right)
         print(root.key)
         sort_min(root.left)
#найдем минимальное значение которое существует
def search_min(root):
    if root.left is None:
        return root.key
    else:
        return search_min(root.left)
#найдем максимальное значение которое существует
def search_max(root):
    if root.right is None:
        return root.key
    else:
        return sort_max(root.right)

tree = Node(46) #наше дерево с основанием 8
mas =[46]
# insert_tree(tree,Node(3)) #вставка в наше дерево
# insert_tree(tree,Node(1))
# insert_tree(tree,Node(6))
# insert_tree(tree,Node(4))
# insert_tree(tree,Node(7))
# insert_tree(tree,Node(10))
# insert_tree(tree,Node(14))
# insert_tree(tree,Node(13))
# print(tree.right.right)
# q = search_min(tree)
# print(q)
# y = sort_min(tree)
# print(y)
start=time.time()
for i in range(100): # генерируем узлы
    insert_tree(tree,Node(randint(10,92)))
sort_max(tree)
end = time.time()
result1 = end-start
start = time.time()
for i in range(100):
    mas.append(randint(10,92)) #добовляем в массивэлементы
mas.sort()    #сортировка массива
for element in mas:
    print(element)
end = time.time()
result2 = end-start
print('binary_sort={arg1:9.5f}  , massiv_sort = {arg2:9.5f}'.format(arg1=result1,arg2=result2))


