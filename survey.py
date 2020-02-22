# importing the regular expression
import re
# this is the regular expression that checks for non-standard characters
name_exp = r'[^\d\`\~\!\@\#\$\%\^\&\*\(\)|-|_\+\=\{\}\[\]\:\;\'\"\<\,\>\.\?\/\\]+'
# this is the regular expression that checks for a-z A-Z characters only
alpha_exp = r'[a-zA-Z]+'

# this is the input line that asks for your first name
fname = str(input("Enter your first name: "))
# this is the while loop that runs the validation check
while re.fullmatch(name_exp, fname) == None:
    print("The first name you provided is not valid")
    fname = str(input("Enter your first name: "))

# this is the input line that asks for your last name
lname = str(input("Enter your last name: "))
# this is the while loop that runs the validation check
while re.fullmatch(name_exp, lname) == None:
    print("The last name you provided is not valid") 
    lname = str(input("Enter your last name: "))
# this combines the first and last name
fullname = f"{fname} {lname}"

# this is the input line that asks for the date of birth
dob = (input("Enter your birthday in the format MM/DD/YYYY: "))
# this is the while loop that runs the validation check
while re.fullmatch(r'\d{2}\/\d{2}\/\d{4}', dob) == None:
    print("The birthdate you provided is not valid.")
    dob = input("Enter your birthday in the format MM/DD/YYYY: ")

# this is the input that asks for the email address
EMail = str(input("Enter your Email Adress: "))

# this is the input that asks for the zipcode
Zip = int(input("Enter your Zip Code: "))

# this is the input that asks for the race
Race = str(input("Enter your race (optional): "))

#this is the input that asks for the age
Age = int(input("Enter your age: "))

# this is the input that asks for the sex
Sex = str(input("Enter your sex: "))

# this is a closing thank you response
closing = f"Thank you for your input {fullname}."
print(closing) 
