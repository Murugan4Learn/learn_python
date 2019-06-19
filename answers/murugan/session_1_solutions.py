


Data types

1. Is python dynamically typed Language or statically typed?

Answer :  Dynamically Typed

2. What is dynamic typing means? Is it efficient than statically typed language?

Answer :  Dynamic type means, No need to declare the type of any data’s. So we can use Data’s easily. Also Efficient to work.

3. What is the difference between integer and float variable?

Answer :  Integer means It’s a Full Numeric Value. 
	Float means It’s a Numeric value with Decimal Points.

4. Which of these are core data types in python?
    (A) Lists
    (B) Dictionary
    (C) Tuples
    (D) Class
 
Answer :  A, B, C

5. What data type is the object below ?
    L = [1, 23, ‘hello’, 1]
    (A) List
    (B) Dictionary
    (C) Tuple
    (D) Array

Answer :  List


6. Which of the following function display's datatype of variables in python?
    (A) datatype(variable)
    (B) type(variable)
    (C) str(variable)
    (D) id(variable)

Answer :  type(variable)

String Operations

7. Create a string variable 'text' and print it. The
   output should be: Hello World

   Sample:
       text = '...'
       print(...)

Answer :  
text = ‘Hello World’
print (text)


8. Create a string variable 'special_string' and print it. The
   output should be:

   Python is an "object-oriented" Programming language

Answer :  
	special_string = ‘Phython is an “object-oriented” Programming language’
					( or )
	special_string = “Phython is an \”object-oriented\” Programming language”
	print (special_string)


9. Create a string variable 'multiline_string' and print it. The
   output should be a multiline string with one line spacing.

   Hint: You may use triple quoted string instead of \n new line character

   line 1: Unlike other high level languages
   line 2: <blank line>
   line 3: Python is interpreted

Answer :  
	multiline_string = “““Unlike other high level languages

	Python is interpreted”””
	print (multiline_string)

10. Create a string variable "news" with value below:
    Air travel to become bit costlier as govt announces hike in aviation security fee from July 1

    Question: Using string slicing print the below values:
              Air travel
              July 1

    Sample:

      print(news[:n])   # empty index at left of : denotes start
      print(news[-n:])  # empty index at right of : denotes start

Answer :  
	news = “Air travel to become bit costlier as govt announces hike in aviation security fee from July 1”
	print (news[0:10])
	print (news[-6

11. Given two string below:

    job_title = "job requirement"
    certs = "certifications in administration is desired"
    added_certs = "additional certifications as below is a plus but not required"
    skills_1 = "azure, windows server"
    skills_2 = "aws, dotnet"

    Use string methods to
      1. capitalize start of each word in job_title
      2. capitalize the first letter of the string certs
      3. capitalize the string completely added_certs
      4. Make the start of each word in skills_1 capitalized
      5. Make the all the words capitalized skills_2

Answer :  
	1. print (job_title.title())	
	2. print (certs.capitalize())
	3. print (added_certs.upper())
	4. print (skills_1.title())
	5. print (skills_2.upper())

12. Create a format string with placeholders "{}" and then,
    Make use of string format function to print the error and error code as below:

    Error occurred during data extraction. Error code is: 121
    Error occurred during string manipulation. Error code is: 221

    where,
      "data extraction and 121" is the formatted string in first example
      "string manipulation and 221" is the formatted string in second example

Answer :
	text = ‘data extraction and 121 {}’
	ret = text.format(‘Error occurred during data extraction. Error code is: 121’)
	print (ret)

	text = ‘ string manipulation and 221 {}’
	ret = text.format(‘Error occurred during string manipulation. Error code is: 221’)
	print (ret)
