# 32․ Ունենք ցուցակներով ցուցակ, սորտավորել փոքր ցուցակները նվազման կարգով։
# Ունենք ։ [[8, 5, 10], [200, 210], [5, 9, 7]]
# Արդյունք : [[10, 8, 5], [210, 200], [9, 7, 5]]

test_list = [[8, 5, 10], [200, 210], [5, 9, 7]]
for ele in test_list:
	ele.sort(reverse = True)
print (str(test_list))
