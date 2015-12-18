while(1):
	answer = 0
	print('Calculator')
	print("       ")
	x = input('Please key in the fist number =>')
	OP =  input('Please key in the Operator =>')
	y = input('Please key in the sencond number =>')
	x = int(x)
	y = int(y)
	if OP == '+':
		answer = x + y
		print('')
		print('Answer is :' )
		print(answer)				
	if OP == '-':
		answer = x - y
		print('')
		print('Answer is :' )
		print(answer)		 		
	if OP == '*':
		answer = x * y
		print(' ')
		print('Answer is :' )
		print(answer)		 		
	if OP == '/':
		answer = x / y
		print('')
		print('Answer is :' )
		print(answer)		
	if answer == 0:
		print('')
		print('Calculate ERROR')		


	

	print('                     ')
	print('                      ')

