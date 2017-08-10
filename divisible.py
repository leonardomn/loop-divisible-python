#2. Write a loop from 1 to 100 and for each number:
#  - If the number is divisible by 3, write foo.
#  - If the number is divisible by 5, write bar.
#  - If the number is divisible by 3 and 5 (ex: 15), write foobar.
#  - Otherwise, just print out the number.

#variable number to count
x = 1

#we can use while and a for too
while x <= 100:
	#if the rest is 0
	if x % 3 == 0:
		print("Number: %i is foo" % x)
	#if the rest is 0
	elif x % 5 == 0:
		print("Number: %i is bar" % x)
	#if the rest is 0 for both
	elif x % 3 == 0 and x % 5 == 0:
		print("Number: %i is foobar" % x)
	#add +1 for the variable to count
	else:
		print("Number: %i isn't divisible for 3 and/or 5" % x)
	x += 1