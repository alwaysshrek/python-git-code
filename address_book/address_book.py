import pickle, os

#Classes
class Person:
	"""Class for person"""

	"""Includes the person's name, age, email, phone"""

	#first_name = 'dummy'
	#last_name = 'dummy'
	#age = '18'
	#email = 'dummy@dummy.com'
	#pnum = 'dummy'
	
	def __init__ (self, first_name, last_name, age, email, pnum):
		self.first_name = first_name.lower()
		self.last_name = last_name.lower()
		self.age = age
		self.email = email
		self.pnum = pnum

#Global functions

#Prints the menu
def print_menu():
	"""Function to print the menu to operate the Address Book. """

	os.system('clear')

	print '-----------------'
	print 'Address book menu'
	print '-----------------'
	print '1.List'
	print '2.Add'
	print '3.Delete'
	print '4.Modify'
	print '0.Exit'

#Prints the press any menu to continue
def confirm_menu():
	"""Function to print confirm to continue menu. """

	print "Press any key to continue...",
	raw_input()

# --------------- MAIN STARTS ---------------  

#Load the data from the file to the ABook dictionary object
#Check if the file exists and is non-zero size
if os.path.isfile('/tmp/abook.txt') and os.stat('/tmp/abook.txt').st_size != 0:
	abookfile = open('/tmp/abook.txt', 'rb')

	#Read the pickled file using a while loop - since pickle reads only one object at a time
	try:
		while True:
			ABook = pickle.load(abookfile)
	except EOFError:
		abookfile.close()
else:
	#If the file exists and/or is empty - Initialize the dictionary containing Person objects
	ABook = {}


#Test data
#ABook['Akkad'] = Person('Akkad', 'Bakkad','27','akkad@bakkad.com','9920099200')

#Accept input as per the menu structure
while True:
	print_menu()

	try:
		input = int(raw_input('Enter an input: '))

		#List the people
		if input == 1:
			#Iterate over all the Person objects in the ABook dictionary
			for key, value in ABook.iteritems():
				print 'Name is {} and Phone # is {}'.format(str(value.first_name), str(value.pnum))
			confirm_menu()
		
		#Add into the book
		elif input == 2:
			inp_first_name = raw_input('Enter first name: ')
			inp_last_name = raw_input('Enter last name: ')
			inp_age = raw_input('Enter age: ')
			inp_email = raw_input('Enter email: ')
			inp_pnum = raw_input('Enter phone#: ')

			#Make a person object
			ABook[inp_first_name] = Person(inp_first_name, inp_last_name, inp_age, inp_email, inp_pnum)

			confirm_menu()
		
		#Delete people
		elif input == 3:
			inp_name = raw_input('Input the first name to delete : ')
			if inp_name not in ABook:
				print "Entry does not exist in ABook. Please retry."
				pass
			else:
				del ABook[inp_name]
				print "Deleted {} from ABook..".format(str(inp_name))

			confirm_menu()
		
		#Modify people details
		elif input == 4:
			inp_name = raw_input('Input the first name to modify : ')

			if inp_name not in ABook:
				print "Entry does not exist in ABook. Please retry."
				pass
			else:
				print "Enter new information for inp_name, press enter to keep same."

				inp_first_name = raw_input('New first name [' + ABook[inp_name].first_name + ']: ')
				inp_last_name = raw_input('New last name [' + ABook[inp_name].last_name + ']: ')
				inp_age = raw_input('New age [' + ABook[inp_name].age + ']: ')
				inp_email = raw_input('New email [' + ABook[inp_name].email + ']: ')
				inp_pnum = raw_input('New phone# [' + ABook[inp_name].pnum + ']: ')

				if inp_first_name: ABook[inp_name].first_name = inp_first_name
				if inp_last_name: ABook[inp_name].last_name = inp_last_name
				if inp_age: ABook[inp_name].age = inp_age
				if inp_email: ABook[inp_name].email = inp_email
				if inp_pnum: ABook[inp_name].pnum = inp_pnum

				print "Modified {} from ABook..".format(str(inp_name))

			confirm_menu()
		
		#Wants to exit
		elif input == 0:
			if len(ABook):
				with open('/tmp/abook.txt', 'wb') as abookfile:
					#abookfile.seek(0)
					pickle.dump(ABook, abookfile)
			print "Exiting program.."
			break
				
		#All other values are error
		else:
			raise ValueError

	except:
		print "Invalid input, please enter again."
		confirm_menu()
		pass