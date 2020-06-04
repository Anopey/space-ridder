print("make sure to enter the text you want formatted into input.txt!\n")
file_name = input("enter a valid file name for the .txt file that will be created to host formatted output. Do so without the .txt extension: ")

f= open("input.txt", "r")
text = f.read()

formatted = ""
lengthminus = len(text) - 1
flag = false
for i in range(0, lengthminus):
	flag = false
	flag = (text[i + 1] == '\n')
	if(text[i] != '\n' or flag):
		if(flag) || text[i] == '\n':
			formatted += '\n' #dont get rid of double \n
		formatted += text[i]
		continue
	formatted += ' '
#now for last index without losing performance
if(text[lengthminus] != '\n'):
	formatted += text[lengthminus]

f = open("output/" + file_name + ".txt", "w")
f.write(formatted)
f.close()

print("Your file has been created! Have a nice day :)")