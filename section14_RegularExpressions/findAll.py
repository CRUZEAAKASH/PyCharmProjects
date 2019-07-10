import re

pattern = r"eggs"

String = "We have eggs in our string. eggs just eggstoeggs count the presence of eggs in the string"

print(re.findall(pattern, String))

print(re.findall(pattern, String).__len__())


