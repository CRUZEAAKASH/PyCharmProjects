import re

pattern = r"[A-Za-z][A-Z][0-9]"

if re.search(pattern, "qA1"):
    print("Match found")
else:
    print("Match not found")


if re.match(pattern, "aA1"):
    print("Match found")
else:
    print("Match not found")