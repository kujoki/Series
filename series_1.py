'''
s = 0
a = [float(i) for i in input().split()]
#Первый вариант нахождения суммы
for _ in range(9):
    s+=a[_]
print(s)
#Второй вариант нахождения суммы
s = sum(a)
print(s)
#Чем плохо? Список, не ограниченный в памяти.

#Еще один красивый вариант со списком
A = [float(input()) for i in range(10)]
A = sum(A)
print(A)
'''
#Тоже самое только с циклом
N = 10
s = 0
while N != 0:
    k = float(input())
    s+=k
    N-=1
print (s)

