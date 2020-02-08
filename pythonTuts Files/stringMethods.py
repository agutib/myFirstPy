"""
All String Function/Method
* len() = count number of Strings
* in - This Method returns boolean expression
* (.) or Dot Method
   - .upper()
   - .lower()
   - .title()
   - .find()
   - .replace()
"""
course = "Python Beginners"

# Using len()
print (len(course))

# all Types in Dot Method
# lets use the course variable again
# first Dot Method will be .upper()
print (course.upper())
# .lower()
print (course.lower())
# .title()
print (course.title())
# .find()
print (course.find("s"))
# .replace()
print (course.replace("Beginners" , "Intermediate"))
