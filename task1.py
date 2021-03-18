# Не изобретая велосипед (подойдёт для примера из документа с заданиями)
def task1_A(array):
	try:		
		return array.index('0')
	except ValueError:
		return 'В этом массиве нет нулей'

# Непосредственно алгоритм поиска
def task1_B(array):
	for i, n in enumerate(array):
		if n == '0' or n == 0:
			return i
	return 'В этом массиве нет нулей'


print(task1_A([1,1,1,1,1,1,1,1,0,0,0,0])) 

