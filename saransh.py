data = {}

def topscorer(sub):
	top = data[0][sub]
	for key,value in data.items():
		for subject,marks in value.items():
			if subject==sub:
				if marks>top:
					top = marks

	return "Highest marks in "+str(sub)+ " is "+str(top)

def main():
	n = int(input("Enter no of students:"))
	for i in range(n):
		print("Enter marks of student "+ str(i))
		english = int(input("English Marks: "))
		maths = int(input("Maths Marks: "))
		history = int(input("History Marks: "))
		science = int(input("Science Marks: "))
		percent = (english+maths+history+science)/4;
		data[i]={"english":english,"maths":maths,"history":history,"science":science,"percent":percent}

	for key,value in data.items():
		for subject,percentage in value.items():
			if subject=="percent":
				print("Student "+str(key)+" "+str(percentage))

	print(topscorer('english'))
	print(topscorer('maths'))
	print(topscorer('history'))
	print(topscorer('science'))


if __name__== "__main__":
	main()
