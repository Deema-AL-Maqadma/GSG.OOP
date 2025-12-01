class InvalidAgeError(Exception):
   pass
def validate_age():
    try:

       age= int(input("Enter your age"))
       if 0>age or age>120:
          raise InvalidAgeError("Age cannot be negative")
       
    except ValueError as e:
       print(f"Error ",e)

    except TypeError as e:
       print(f"Error Type",e)

    except InvalidAgeError as e:
       print(f"Error age/ ",e)


    finally:
       print("Done")

validate_age()
