#Дано целое число N и набор из N вещественных чисел.  Вывести в том же
# порядке округленные числа, а также их сумму

#Еще один красивый вариант со списком, выводим поэлементно
S = 0 #начальное условие для суммы
Num = int(input('Enter N: '))
A = [float(input('Enter A: ')) for i in range(Num)]
for _ in range(len(A)):
    A[_] = round((A[_]),0) #функция trunc отбрасывает целую часть
    S+=A[_]
for _ in range(len(A)):
    print (A[_])
print(S)

'''
#Выводим новое число сразу после введения предыдущего
Num = int(input('Enter N: '))
N = Num
s = 0 # начальное условие для суммы
while N != 0:
    k = round(float(input('Enter A: ')),0)
    print (k)
    s+=k
    N-=1 
print (s)
'''
