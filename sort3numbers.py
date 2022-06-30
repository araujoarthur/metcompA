import random

toSort = list()
#x = toSort.append(int(input('Insert first number: ')))
#y = toSort.append(int(input('Insert second number: ')))
#z = toSort.append(int(input('Insert third number:')))

#.sort()

def selectionSort(listS):
	lLen = len(listS)
	tempList = list() 
	for j in range(0, lLen): #j recebe o j-ésimo menor numero
		temp = listS[j]
		oldPosLower = 0
		for i in range(j, lLen): #iteração sob todos os indices NÃO ORDENADOS
			if listS[i] < temp:
				listS[i] = temp
				oldPosLower = i
		listS[oldPosLower] = listS[j]
		listS[j] = temp
	for i in range(1, len(listS)):
		print(listS[i])

llist = [random.randint(0,10) for i in range(5)]
selectionSort(llist)
		
			 
			
