import re

pattern = r"eggs"

str1 = "eggseggseggseggs"
str2 = "baconeggseggsbacon"

if(re.match(pattern, str1)):
    print("first pattern matched")
else:
    print("first pattern didn't match")

if(re.match(pattern, str2)):
    print("second pattern matched")
else:
    print("second pattern didn't match")