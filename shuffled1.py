def tables():
	import random,time
	attempts, right, wrong = 0, 0, 0
	#input of table from user
	t = int(raw_input("which table would you like to lookup? "))
	print  'You have selected the table of ', t
	#output of selected table
	for i in range(1,21):
		print t, ' x ', i, ' = ', t*i
	#test multiplication tables
	print 'You will be tested for the table of ', t
	print 'Put 0 as the answer to Exit'
	ans = t
	t1 = time.time()
	while ans != 0:
		rand = random.randint(1,20)
		attempts += 1
		print t, ' x ', rand, " = ? "
		ans = int(raw_input())
		if ans == t*rand: right += 1
		elif ans == 0:
			if right+wrong == 0:
				print 'Thank you for taking the test. Good Bye!'
			else:
				t2 = time.time()
				print 'Your have answered', (right*100)/(right+wrong), '% right in', attempts, 'attempts.'
				print 'Your speed was %.2f' % ((attempts*60)/(t2-t1)), 'attempts per minute or %.2f' % ((t2-t1)/attempts), 'seconds per attempt.'
				print 'Thank you for taking the test. Good Bye!'
		else:
			wrong += 1
			while ans != t*rand:
				print "Incorrect!"
				print t, ' x ', rand, " = ", t*rand
				print t, ' x ', rand, " = ? "
				ans = int(raw_input())
