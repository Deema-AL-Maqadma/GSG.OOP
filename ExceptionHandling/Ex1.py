# 1. Catching Specific Exceptions
# This handles both input conversion errors and division by zero
try:
  num = int(input("Enter a number: "))
  result = 10 / num
  print(f"Result = {result}")
except ValueError:
  print("You must enter a valid number.")
except ZeroDivisionError:
  print("Cannot divide by zero.")

#---------------------------------------------------------------

#2. Catching Type Errors and NoneType Issues
# Shows how Python catches runtime type issues
def print_upper(text):
  try:
     print(text.upper())
  except AttributeError:
     print("Invalid input: expected a string, got NoneType or other.")
print_upper(None)

#---------------------------------------------------------------

# 3. Catching File Errors
# Demonstrates file handling with exception awareness
try:
  with open("nonexistent.txt") as file:
    content = file.read()
except FileNotFoundError:
 print("The file does not exist.")

#---------------------------------------------------------------

#4. Raising Exceptions Manually
# The raise keyword is used to trigger exceptions based on custom logic
def set_age(age):
  if age < 0:
    raise ValueError("Age cannot be negative")
try:
  set_age(-5)
except ValueError as e:
 print("Error:", e)

#---------------------------------------------------------------

# 5. Custom Exceptions/ Shows how to define and use a custom exception class.
class InvalidAgeError(Exception):
  pass
def validate_age(age):
  if age < 0 or age > 120:
     raise InvalidAgeError("Age must be between 0 and 120.")
try:
  validate_age(150)
except InvalidAgeError as e:
  print("Caught custom exception:", e)

#---------------------------------------------------------------

#6. General Exception Handling / Catches any unhandled exception type. Should be used sparingly
try:
  #risky_code()
  print("******")
except Exception as e:
  print("An unexpected error occurred:", e)

#---------------------------------------------------------------

try:
  file_name = "data.txt"
  f = open(file_name, "r")
  content = f.read()
  if not content:
    raise ValueError("File is empty.")
except FileNotFoundError:
  print("Error: File does not exist.")
except ValueError as ve:
  print("Error:", ve)
except TypeError:
  print("Error: Invalid operation on file.")
except Exception as e:
  print("General error:", e)
finally:
  try:
    f.close()
    print("File closed successfully.")
  except NameError:
    print("File was never opened, so nothing to close.")

#---------------------------------------------------------------

# 8. File Handling with Exceptions and else
try:
   number = int(input("Enter a number: "))
except ValueError:
   print("That's not a valid integer.")
else:
   print("Good job! You entered:", number)