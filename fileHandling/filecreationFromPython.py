name = "creating file and writing data in that newly created file"
file = open("output1.txt", "w")
file.write(name)
file.close()

file = open("output1.txt", "r")
content = file.read()
print(content)
file.close()

file = open("output1.txt", "a")
file.write("\nEntering the second line")
file.close()

file = open("output1.txt", "r")
content = file.read()
print(content)
file.close()