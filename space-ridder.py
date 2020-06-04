text = input("enter the text you want formatted: ")
file_name = input("enter a valid file name for the .txt file that will be created to host formatted output: ")

formatted = ""
for i in range(0, len(text)):
	if(text[i] != '\n' or (text[i + 1] == '\n')):
		formatted += char
		continue

f = open(file_name, "w")
f.write(formatted)
f.close()

print("Your file has been created! Have a nice day :)")