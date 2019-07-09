import re

pattern = r"bread(eggs)*bread"

if re.match(pattern, "breadeggs bread"):
    print("Match foind")

