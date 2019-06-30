name = "Hello!!!!!!!!!!!!! What are you doing mannnn"
file = open("output.txt", "w")
file.write(name)
file.close()

file = open("output.txt", "r")
content = file.read()
print(content)
file.close()