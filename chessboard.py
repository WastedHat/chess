x = 1
y = 1

for y in range(1, 9):

	for x in range(97, 105):
		board = (chr(x),9-y,[])
		#print(board)

		print("{:>2}{:>}".format(chr(x),9-y), end=" ")
		#print(x," ",y)
	print()


#for letter in range(97,105):
	#board[2].append(chr(letter))


