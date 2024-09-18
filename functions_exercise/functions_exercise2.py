# Exercise 2: Functions with and without Parameters
# We will also put into practice what you did or learned on control structures
# Please mind your arguments!!!!


# 1. Write a function without a parameter called 'get_user_input'
    # This function must take user inputs 'Username, age and email'
    # validate the AGE using a loop and conditional statements
        # If the AGE is not an Integer print "Not an Integer, Enter a valid age!"
        # If the AGE is less than 17 print "You are young"
        # If the Age is more than 65 print "You are too old"  
    # Return all the inputs
def get_user_input():
    username = input("Enter your username here: ")
    age = input("Enter your age here: ")
    email = ''

    digits = ['0','1','2','3','4','5','6','7','8','9']

    flag = True

    for n in age:
        if n not in digits:
            flag = False
            break
    
    if flag == False:
        print("Not an Integer, Enter a valid age!")
        get_user_input()
    else:
        email = input("Enter your email here: ")
        num_ = int(age)
        if num_ < 17:
            print("You are young")
        elif num_ > 65:
            print("You are too old")
    
    
    return username, age, email

#print(get_user_input())

# 2. On the function below 'validate_username'
    # Validate the username that comes as a parameter
    # Use a loop to check all the characters on the username 
    # If the chars are not strings return False else return True
    # If the username is an empty string return False
    # Return the boolean

def validate_Username(username):
    if username:
       flag = username.isalpha()
    else:
       flag = False
    
    return flag
    #pass

#print(validate_Username('johndoe'))


# 3. Pass the parameters to the function below 'display_user_info'
    # Underneath the User Information print the following:
        # 'Username : <username>'
        # 'Age      : <age>'
        # 'Email    : <email>
    # return 'Thanks!, Details captured.'

def display_user_info(username, age, email):
    print("\nUser Information:")
    print(f"Username : <{username}>\nAge\t : <{age}>\nEmail\t : <{email}>")
    message = 'Thanks!, Details captured.'
    return message

#print(display_user_info('john doe',23,'jd101@gmail.com'))

# 4. Call all the functions
    # If 'validate_username' function returns False
        # write a loop to and take new input for the username and take it to be evaluated 'validate_username'
    # if 'validate_username' returns True then you can display the user Info   
def main():
    info = get_user_input()
    name = info[0]
    age = info[1]
    mail = info[2]
    flag = validate_Username(name)
    if flag == False:
        while flag == False:
            name = input("Enter username here: ")
            flag = validate_Username(name)
    
    display_user_info(name,age,mail)
    #pass


if __name__ == "__main__":
   #call the main function
   main()
    #pass