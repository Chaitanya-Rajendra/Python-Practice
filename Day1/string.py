# name = "codegnan"
# print(name[-8:-4])
#string slicing

# List and Array are same in python

# List is ordered data structure. It is mutable and collection of objects.

# chey = [10, 20, 30, 40, 50]
# print(chey)

# ordered
# proper order is maintained

#2. Allows Duplicates
#mutable - we can change elements
# list_name[index] = new_value

# chey[0] = 100
# print(chey)

#list can contain different data types

# student = ["codegnan", 10, 20.5, True]
# print(student)

#adding elements
#append() - adds element at the end of the list

# student.append([60,70,80])
# print(student)

#extend() - adds multiple elements at the end of the list
# a=[10, 20, 30]
# b=[40, 50, 60]
# a.extend(b)
# print(a)

# a.pop()
# a.remove()
# print(a)

#Indexing

# lang = "Python"
# print(lang)

# print(lang[0])
# print(lang[1])
# print(lang[2])
# print(lang[3])
# print(lang[4])
# print(lang[5])


#String Slicing

#word = "Python"
#print(word[-6:-1]) # returns "Pytho"

#variable_name[start : stop : step]
#print(word[0:6:2]) # returns "Pto"

#print(word[::-3]) # returns "Ph"

#result = word.replace("P", "J") # returns "Jython"


# text = "python"
# for char in text:
#     if char == "h":
#         continue
#     print(char, end = "")

#concatination

# first_name = "Chaitanya"
# last_name = "Rajendra"
# full_name = first_name + " " + last_name
# print(full_name)

#Methods
# word = "PyThon is A proGramming Language"
# print(word.upper()) # returns "PYTHON IS A PROGRAMMING LANGUAGE"
# print(word.lower()) # returns "python is a programming language"
# print(word.title()) # returns "Python Is A Programming Language"
# print(word.capitalize()) # returns "Python is a programming language"
# print(word.strip()) # returns "PyThon is A proGramming Language"
# print(word.lstrip()) # returns "PyThon is A proGramming Language      "
# print(word.rstrip()) # returns "    PyThon is A proGramming Language"
# print(word.replace("PyThon", "Java")) # returns "Java is A proGramming Language"


# company = "codegnan is a software company"
# print(company.startswith("codegnan")) # returns True
# print(company.endswith("company")) # returns True

# company = "python, Java, C++, C#, JavaScript"
# print(company.split(", ")) # returns ['python', 'Java', 'C++', 'C#', 'JavaScript']

# list2 = ["python", "Java", "C++", "C#", "JavaScript"]
# print(" ".join(list2)) # returns "python Java C++ C# JavaScript"


#isalpha - checks if all characters in the string are alphabetic
#isalnum - checks if all characters in the string are alphanumeric
#isdigit - checks if all characters in the string are digits
#isspace - checks if all characters in the string are whitespace
#islower - checks if all characters in the string are lowercase
#isupper - checks if all characters in the string are uppercase
#istitle - checks if the string is titlecased


