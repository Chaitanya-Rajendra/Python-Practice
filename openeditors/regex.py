#REGEX()- Search looks for a pattern anywhere inside a string.
# import re
# text = "The rain in Spain"
# result = re.search("rain", text)
# print(result)

# We need to use search when we want to know if this pattern exists 
# in the string

#re.match() - it checks the pattern only at the beginning of the string.
# import re
# text = "The rain in Spain"
# result = re.match("The", text)
# print(result)

#re.fullmatch() - it requires entire string to kmatch the pattern.
# import re
# text = "The rain in Spain"
# result = re.fullmatch("The rain in Spain", text)
# print(result)/

# re.findall() - it inds all occurrences of a pattern 
# and returns them as a list.

# import re
# text = "The rain in Spain"
# result = re.findall(r"\d+", text)
# #\d - digits (digits from 0 to 9)
# #\d+ - one or more digits
# print(result)

#\w - word characters (letters, digits, and underscores)
#\w+ - one or more word characters

# import re
# text = "The rain in Spain"
# result = re.findall(r"\w+", text)
# print(result)

# ^ - Start of String- the pattern must start at begining of string

# import re
# pattern = r"^The"
# print(re.search(pattern, "The rain in Spain")) 

#Quantifiers - they specify how many times a pattern should occur.
# *, +, ?, {n}, {n,}, {n,m}

#* -Zero or more occurrences of the preceding pattern.
# r"ab*" - a, ab, abb, abbb, abbbb, etc.
# Because b can occur zero or more times

# + - one or more
# r"ab+" - ab, abb, abbb, abbbb, etc.
# Because b must occur at least once

# ? - zero or one
# r"colo?r?" - color, colour

#{}- exact number
#r"^\d{4}$" - means exatly 4 digits
# 1234(correct), 123(wrong), 12345(wrong)
# r"^\d{4, 6}$" - means 4 to 6 digits are valid

import re
value = input()
pattern = r"^\d+$"

if re.fullmatch(pattern, value):
    print("Valid input")
else:
    print("Invalid input")


