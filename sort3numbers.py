import random

toSort = list()
#x = toSort.append(int(input('Insert first number: ')))
#y = toSort.append(int(input('Insert second number: ')))
#z = toSort.append(int(input('Insert third number:')))

#.sort()

def selectionSort(listS):
	lLen = len(listS)
	for i in range(0, lLen-1): #j recebe o j-ésimo menor numero
		lowestPos = i
		for j in range(i, lLen): #iteração sob todos os indices NÃO ORDENADOS
			if listS[j] < listS[lowestPos]:
				lowestPos = j
		if lowestPos != i:
			temp = listS[lowestPos]
			listS[lowestPos] = listS[i]
			listS[i] = temp

def bubbleSort(listS):
	swaps = True
	while(swaps):
		swaps = False
		for i in range(0, len(listS) -1):
			if listS[i] > listS[i+1]:
				temp = listS[i]
				listS[i] = listS[i+1]
				listS[i+1] = temp
				if i == len(listS):
					swaps = False
			

def mergeSort(listS):
	pass



llist = [random.randint(0,50) for i in range(6)]
print(llist)
#selectionSort(llist)
bubbleSort(llist)
print(llist)
		
			 
			
