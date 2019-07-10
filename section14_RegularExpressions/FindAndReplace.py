import re

string = "my name is John, Hi I'm John"
pattern = r"John"
newString = re.sub(pattern, "Rob", string)
print(newString)