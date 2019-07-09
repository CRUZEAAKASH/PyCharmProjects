import re

pattern = r"eggs"
string1 = "baconeggseggseggsqaazwsxedcrfvtgbyhujnmkiolp"

if re.search(pattern, string1):
    print("Search found")
else:
    print("Search not found")