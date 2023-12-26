# 25 December 2023
'''
This Python script implements a console-based User Register/Login system with color-coded messages. 
Users can choose to register, where the script generates a suggested password or allows them to enter a custom one.
Registered user data, including username, password, name, age, and recovery code, is stored in a file ("data.txt").
For login, the script validates user credentials and offers options to edit account details, delete the account,
or search for other users. It also includes a password recovery feature. Despite functionality, the code has some
logical errors and inefficiencies.
'''
import random
try:
# ANSI escape codes for text color

    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    BLUE = "\033[94m"
    LIGHT_MAGENTA = "\033[95m"
    ENDC = "\033[0m"  # Reset color to default

    print(f"{LIGHT_MAGENTA}Crystal's User Register/Login page!{ENDC}")

    reg_or_log = input(f"Would you like to ({BLUE}R{ENDC})egister or ({BLUE}L{ENDC})ogin? ").lower()
    while reg_or_log not in ["r", "l"]:
        print(RED + "Please enter either R or L\n" + ENDC)
        reg_or_log = input(f"Would you like to ({BLUE}R{ENDC})egister or ({BLUE}L{ENDC})ogin? ").lower()

    special_characters = ["!", "@", "#", "$", "%", "^", "&", "*", "~"]
    alphabets = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
                 "v", "w", "y", "z"]
    numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

    special_character = random.choice(special_characters)
    special_character2 = random.choice(special_characters)
    alphabet1 = random.choice(alphabets)
    alphabet2 = random.choice(alphabets)
    alphabet3 = random.choice(alphabets)
    alphabet4 = random.choice(alphabets)
    alphabet5 = random.choice(alphabets)
    number = random.choice(numbers)

    password = f"{special_character}{alphabet1}{special_character2}{alphabet3}{alphabet2}{alphabet5}{number}{alphabet4}"

    if reg_or_log == "r":
        r_username = input("Username: ")
        while len(r_username) < 3:
            print(RED + "Please have at least 3 characters in your username." + ENDC)
            r_username = input("Username: ")
        suggested_pass = input(f"Suggested password {password}\n[y/n]: ").lower()

        while suggested_pass not in ["y", "n"]:
            print(RED + "Please enter either Y or N" + ENDC)
            suggested_pass = input(f"Suggested password {password}\n[y/n]: ").lower()
        if suggested_pass == "n":
            r_password = input("Password: ")

            while len(r_password) < 4:
                print(RED + "Please have more than 4 characters in your password" + ENDC)
                r_password = input("Password: ")

            while not any(char.isdigit() for char in r_password):
                print(RED + "Please include a number in your password" + ENDC)
                r_password = input("Password: ")

            while not any(char in special_characters for char in r_password):
                print(RED + "Please have a special character in your password" + ENDC)
                r_password = input("Password: ")
        elif suggested_pass == "y":
            r_password = password
        name = input("Name: ")
        while True:
            age = input("Age: ")
            break

            if age.isdigit():
                print("")

            else:
                print(RED + "Please enter a valid age!" + ENDC)
                age = input("Age: ")
                break
        try:
            code = input(
                "Please enter a code that can be used to\nrecover your account in case your password is forgotten:\n(Make a 4-digit code that you can be able to remember)\n")
        except:
            print(f"{RED}Please enter an integer!{ENDC}")
            print(f"{YELLOW}Account was not made.{ENDC}")
        with open("data.txt", "a") as file:
            file.write(f"Username: {r_username}\nPassword: {r_password}\nName: {name}\nAge: {age}\nCode: {code}")
        print(GREEN + "Account made successfully!" + ENDC)

    if reg_or_log == "l":
        l_username = input("Username: ")
        l_password = input("Password: ")

        with open("data.txt", "r") as file:
            lines = file.readlines()

        user_data = {}
        for i in range(0, len(lines), 5):
            username = lines[i].split(":")[1].strip()
            password = lines[i + 1].split(":")[1].strip()
            name = lines[i + 2].split(":")[1].strip()
            age = lines[i + 3].split(":")[1].strip()
            code = lines[i + 4].split(":")[1].strip()

            user_data[username] = {'password': password, 'name': name, 'age': age, 'code': code}

        if l_username in user_data:
            if user_data[l_username]['password'] == l_password:
                print(GREEN + "-------------" + ENDC)
                print(GREEN + "Login successful!" + ENDC)
                print(GREEN + "-------------" + ENDC)
                print(f"Welcome, {user_data[l_username]['name']}!")
                print(YELLOW + "-------------" + ENDC)
                print(YELLOW + "Account information:" + ENDC)
                print(YELLOW + "-------------" + ENDC)
                print(f"Username: {BLUE}{l_username}{ENDC}")
                print(f"Password: {BLUE}{user_data[l_username]['password']}{ENDC}")
                print(f"Name: {BLUE}{user_data[l_username]['name']}{ENDC}")
                print(f"Age: {BLUE}{user_data[l_username]['age']}{ENDC}")

                options_btn = input("Enter /e for options: ").lower()
                if options_btn == '/e':
                    print(f"{LIGHT_MAGENTA}------------------------------------{ENDC}")
                    print(f"{LIGHT_MAGENTA}Enter 1 to edit your account details\nEnter 2 to delete your account\nEnter 3 to search a user{ENDC}")
                    print(f"{LIGHT_MAGENTA}------------------------------------\n{ENDC}")
                    option = int(input(""))
                    if option == 1:
                        edit_details = input(
                            f"Would you like to edit your ({BLUE}U{ENDC})sername, ({BLUE}N{ENDC})ame, or ({BLUE}A{ENDC})ge? ").lower()
                        while edit_details not in ["u", "n", "a"]:
                            print(f"{RED}Please enter either U, N, or A!{ENDC}")
                            edit_details = input(
                                f"Would you like to edit your ({BLUE}U{ENDC})sername, ({BLUE}N{ENDC})ame, or ({BLUE}A{ENDC})ge? ").lower()
                        if edit_details == 'u':
                            new_username = input("New username: ")

                            # Check if the new username is not already in use
                            if new_username not in user_data:
                                # Update the username in the user_data dictionary
                                user_data[new_username] = user_data.pop(l_username)
                                print(f"{GREEN}Username successfully updated!{ENDC}")

                            else:
                                print(f"{RED}Username already in use! Please choose a different one.{ENDC}")

                        elif edit_details == 'n':
                            new_name = input("New name: ")
                            # Update the name in the user_data dictionary
                            user_data[l_username]['name'] = new_name
                            print(f"{GREEN}Name successfully updated!{ENDC}")

                        elif edit_details == 'a':
                            while True:
                                new_age = input("New age: ")
                                if new_age.isdigit():
                                    # Update the age in the user_data dictionary
                                    user_data[l_username]['age'] = new_age
                                    print(f"{GREEN}Age successfully updated!{ENDC}")
                                    break
                                else:
                                    print(RED + "Please enter a valid age!" + ENDC)

                        # Save the updated data to the file
                        with open("data.txt", "w") as file:
                            for username, data in user_data.items():
                                file.write(
                                    f"Username: {username}\nPassword: {data['password']}\nName: {data['name']}\nAge: {data['age']}\nCode: {data['code']}\n")
                    elif option == 2:
                        delete = input(f"{BLUE}Are you sure you want to delete your account? [Y/N]: {ENDC}").lower()
                        while delete not in ["y", "n"]:
                            print(f"{RED}Enter either Y or N!{ENDC}")
                            delete = input(f"{BLUE}Are you sure you want to delete your account? [Y/N]: {ENDC}").lower()
                        if delete == "y":
                            # Remove the user's data from the user_data dictionary
                            del user_data[l_username]
                            print(f"{GREEN}Account deleted!{ENDC}")

                            # Save the updated data to the file
                            with open("data.txt", "w") as file:
                                for username, data in user_data.items():
                                    file.write(
                                        f"Username: {username}\nPassword: {data['password']}\nName: {data['name']}\nAge: {data['age']}\nCode: {data['code']}\n")
                    elif option == 3:
                        search = input("Search a user: ")
                        if search not in user_data:
                            print(f'{RED}The username "{search}" does not exist.{ENDC}')
                        else:
                            searched_user = user_data[search]
                            print(f"{GREEN}-------------{ENDC}")
                            print(f"{GREEN}User found!{ENDC}")
                            print(f"{GREEN}-------------{ENDC}")
                            print(f"Username: {BLUE}{search}{ENDC}")
                            print(f"Name: {BLUE}{searched_user['name']}{ENDC}")
                            print(f"Age: {BLUE}{searched_user['age']}{ENDC}")


            else:
                print(RED + "Invalid password. Login failed." + ENDC)

                forget = input(YELLOW + "Did you forget your password? [Y/N]: " + ENDC).lower()

                while forget not in ["y", "n"]:
                    print(RED + "Please enter either Y or N!" + ENDC)

                    forget = input(YELLOW + "Did you forget your password? [Y/N]: " + ENDC).lower()

                if forget == "y":

                    code_rec = input("Please enter your 4-digit recovery code: ")

                    while l_username not in user_data or user_data[l_username]['code'] != code_rec:
                        print(f"{RED}Incorrect username or code!{ENDC}")

                        l_username = input("Username: ")

                        code_rec = input("Please enter your 4-digit recovery code: ")

                    if user_data[l_username]['code'] == code_rec:
                        new_pass = input(f"{BLUE}New password: {ENDC}")

                        c_new_pass = input(f"{BLUE}Confirm New password: {ENDC}")

                while len(c_new_pass) < 4:
                    print(RED + "Please have more than 4 characters in your password" + ENDC)
                    new_pass = input(f"{BLUE}New password: {ENDC}")
                    c_new_pass = input(f"{BLUE}Confirm New password: {ENDC}")

                while not any(char.isdigit() for char in c_new_pass):
                    print(RED + "Please include a number in your password" + ENDC)
                    new_pass = input(f"{BLUE}New password: {ENDC}")
                    c_new_pass = input(f"{BLUE}Confirm New password: {ENDC}")

                while not any(char in special_characters for char in c_new_pass):
                    print(RED + "Please have a special character in your password" + ENDC)
                    new_pass = input(f"{BLUE}New password: {ENDC}")
                    c_new_pass = input(f"{BLUE}Confirm New password: {ENDC}")

                while new_pass != c_new_pass:
                    print(f"{RED}Passwords do not match!{ENDC}")
                    new_pass = input(f"{BLUE}New password: {ENDC}")
                    c_new_pass = input(f"{BLUE}Confirm New password: {ENDC}")

                user_data[l_username]['password'] = new_pass

                with open("data.txt", "w") as file:
                    for username, data in user_data.items():
                        file.write(
                            f"Username: {username}\nPassword: {data['password']}\nName: {data['name']}\nAge: {data['age']}\nCode: {data['code']}\n")

                print(f"{GREEN}Password successfully reset!{ENDC}")
        elif l_username not in user_data:
            print(f"{RED}Incorrect username or password.{ENDC}")
except ValueError:
    print("")
