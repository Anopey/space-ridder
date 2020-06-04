print("make sure to enter the text you want formatted into input.txt!\n")
file_name = input("enter a valid file name for the .txt file that will be created to host formatted output. Do so without the .txt extension: ")

f= open("input.txt", "r")
text = f.read()

formatted = ""
lengthminus = len(text) - 1
for i in range(0, lengthminus):
	if(text[i] != '\n' or (text[i + 1] == '\n')):
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