#! /usr/bin/python3
# -*- coding: utf-8 -*-

import random

def humanShuffle(oldList):
	'''Shuffles a list so that it will appear random to humans, so that nobody is 
	after who they were after before. When shuffling small lists, random.shuffle will
	often produce transformations like [1,2,3,4] -> [1,3,2,4]. This is statistically
	likely and not a problem when true randomness is desired. My function is for 
	when it is more important to appear random to humans than to actually be random.
	'''
	tempList = []
	while len(tempList) < len(oldList):
		a = random.choice(oldList)
		if a not in tempList:
			if len(tempList) > 0: 
				if oldList.index(tempList[-1]) != oldList.index(a) - 1:
					tempList.append(a)
				elif len(tempList) + 1 == len(oldList): #almost there but can't get there
					tempList.insert(1,a)
			elif oldList.index(a) > 0: #tempList is [] but the random player was not first before.
				tempList.append(a)

	if __name__ == '__main__':
		tempString = ''
		for item in tempList:
			tempString = tempString + str(item) + ' '
		print(tempString)
	return tempList

humanShuffle([1,2,3,4])

#sample outputs
#3 2 8 1 7 4 6 5 9 
#7 1 8 3 2 5 9 6 4 
#7 3 8 1 5 9 2 6 4 
#9 1 4 3 2 8 5 7 6 
#4 6 9 1 5 2 8 7 3 
#5 1 8 2 4 3 7 6 9 
#2 8 5 1 7 9 3 6 4 
#6 1 7 5 4 8 2 9 3 
#7 1 9 6 8 3 5 2 4 
#4 7 5 1 9 2 8 3 6

#2143, 2413, 2431, 3142, 3214, 3241, 4132, 4213, 4231, 4321