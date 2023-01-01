#Поиски
#1) Линейный
#2) Двоичный
#3) Прыжками
#4) Интерполяционный

#---------------------------------------------------------------------#

#Список(массив) для 1 варианта
array_1 = [1, 4, 465, 246, 135, 354, 143, 657]

#Список(массив) для 2 варианта
#Обязательное условие список должен быть упорядоченным
#по возрастанию или по убыванию (самый распрастранненый по возрастанию)
array_2 = [1, 7, 8, 12, 17, 22, 99, 143, 234, 543, 1002, 1231]

#Список(массив) для 3 варианта
#Обязательное условие список должен быть упорядоченным
#по возрастанию
array_3 = [1, 5, 7, 12, 35, 65, 85, 124, 212, 233, 256]

#Список(массив) для 4 варианта
#Обязательное условие список должен быть упорядоченным
#по возрастанию
array_4 = [2, 4, 7, 9, 12, 18, 27, 48, 49, 77, 84, 90, 94, 102, 105]

#---------------------------------------------------------------------#

#Реализания первого варианта
#Задача найти номер элемента первого списка со значение 135 (4)
#Скорость выполнения задачи O(n); n = кол-ву элементу

def first_task():
	for index in range(len(array_1)):
		if array_1[index] == 135:
			break

	return index

#Реализация второго варианта
#Задача найти номер элемента вторго списка со значением 22 (5)
#Скорость выполнения задачи O(log n); n = кол-ву элементу

def second_task():
	left = 0
	right = len(array_2)-1
	mid = (left+right)//2
	
	index = -1

	while (right >= left) and (index==-1):
		if array_2[mid] == 22:
			index = mid
		elif array_2[mid] < 22:
			left = mid
			mid = (left+right)//2
		elif array_2[mid] > 22:
			right = mid
			mid = (left+right)//2

	return index

#Реализация третьего варианта
#Задача найти номер элемента третьего спсика со значением 85 (6)
#Скорость выполнения задачи O(sqrt(n)); n = кол-ву элементу

def third_task():
	lenght = len(array_3)
	jump = int(lenght**0.5)

	#Я возвожу длину списка в 0.5 степень, чтобы не подтягивать
	#библиотку math,
	#так же n**0.5 = sqrt(n)
	#Так же вы можете использовать библиотеку math
	#Вот пример:
	#import math
	#jump = int(math.sqrt(lenght))

	left, right = 0, 0
	while left < lenght and array_3[left] <= 85:
		right = min((lenght, left+jump))
		if array_3[left] <= 85 and array_3[right] >= 85:
			break
		left+=jump
	if left >= lenght or array_3[left] > 85:
		return -1
	right = min((lenght-1, right))
	index = left
	while index <= right and array_3[index] <= 85:
		if array_3[index] == 85:
			return index
		index+=1
	return -1

#Реализания четвертого варианта
#Задача найти номер элемента четвертого списка со значение 90 (11)
#Скорость выполнения задачи O(log n); n = кол-ву элементу

def fourth_task():
	left, right = 0, len(array_4)-1

	while left <= right and 90 >= array_4[left] and 90 <= array_4[right]:
		index = left + int((float(right-left)/(array_4[right] - array_4[left])) * (90 - array_4[left]))
		if array_4[index] == 90:
			return index
		elif array_4[index] < 90:
			left = index + 1
		elif array_4[index] > 90:
			right = index - 1
	return -1


#---------------------------------------------------------------------#

#Проверка выполнения алгоритма
#Чтобы проверить алгоритм
#В блоке ниже уберите знак комментария перед началом строки

if __name__ == '__main__':
	#print(first_task()) #Ответ 4
	#print(second_task()) #Ответ 5
	#print(third_task()) #Ответ 6
	#print(fourth_task()) #Ответ 11
	pass