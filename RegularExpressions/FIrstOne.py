import re

pattern = r"eggs"

str = "wqeggseggseggseggs"

if(re.match(pattern, str)):
    print("Match found")
else:
    print("No Match found")