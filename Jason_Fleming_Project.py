#Author: Jason Fleming

def main(a_type_list, a_price_list,a_booking_num_list, e_type_list, e_booking_list, passed_startup = False, another_booking = False):
    if not passed_startup:
        student_name = "Jason Fleming"
        student_number = "R00221324"
        print("STUDENT INFORMATION")
        print("=" * 28)
        print(f"Student Name: {student_name}")
        print(f"Student Number: {student_number}")
        print("=" * 28)
        passed_startup = True
        a_type_list, a_price_list, a_booking_num_list = read_booking_file()
        e_type_list, e_booking_list = read_extra_files()
    current_booking_number = 0
    for i in range(len(a_type_list)):
        current_booking_number = current_booking_number + int(a_booking_num_list[i])
    if not another_booking:
        choice = get_menu()
    else:
        choice = 1
    if choice == 1:
        if current_booking_number < 30:
            get_user_info(a_type_list, a_price_list, a_booking_num_list, current_booking_number, e_type_list, e_booking_list)
        else:
            input("Sorry you have reached the maximum amount of booking. Press enter to return to the menu")
            main(a_type_list, a_price_list,a_booking_num_list, e_type_list, e_booking_list,True)
    elif choice == 2:
        get_review_bookings(a_type_list, a_price_list, a_booking_num_list, e_type_list, e_booking_list)
    else:
        exit_program(a_type_list, a_price_list,a_booking_num_list, e_type_list, e_booking_list)


# A function to get the booking information from the user
def get_user_info(a_type_list, a_price_list, a_booking_num_list, current_booking_num, e_type_list, e_booking_list):
    user_surname = get_family_name("What is your surname: ")
    user_phone = get_family_phone("What is your contact phone number: ")
    booking_type = get_booking_type(a_type_list, a_price_list, a_booking_num_list)
    for i in range(len(a_type_list)):
        if booking_type == i:
            type_picked = a_type_list[i]
            acc_price = a_price_list[i]
            a_booking_num_list[i] = int(a_booking_num_list[i]) + 1
    number_in_group = get_group_num("How many is in your group: ")
    number_of_kids = get_num_kids("How many children in the group will be attending the kids club: ", number_in_group)
    e_booking_list[0] = int(e_booking_list[0]) + number_of_kids
    purchase_pool_pass = get_yes_no("Do you wish to purchase a family pool pass? y/n: ")
    kids_cost = number_of_kids * 100
    if purchase_pool_pass == "y":
        pool_cost = 150
        e_booking_list[1] = int(e_booking_list[1]) + 1
    else:
        pool_cost = 0
    created_booking_number = current_booking_num + 1
    string_b_num = str(created_booking_number)
    if len(string_b_num) < 2:
        string_b_num = "0" + string_b_num
    display_booking_details(user_surname, string_b_num, user_phone, type_picked, acc_price, number_in_group, number_of_kids, purchase_pool_pass, kids_cost, pool_cost)
    more_booking = get_yes_no("Do you want to make another booking? y/n: ")
    if more_booking == "y":
        main(a_type_list, a_price_list,a_booking_num_list, e_type_list, e_booking_list,True, True)
    else:
        return_menu = get_yes_no("Do you want to return to the main menu? y/n: ")
        if return_menu == "y":
            main(a_type_list, a_price_list,a_booking_num_list, e_type_list, e_booking_list,True)
        else:
            exit_program(a_type_list, a_price_list,a_booking_num_list, e_type_list, e_booking_list)


# A function to display the booking information before it is saved. I did not include the phone number in the confirm
# booking as the sample did not include it but I felt that the company should have contact details for the client so
# it is included in the text file
def display_booking_details(name, booking_num, phone, a_type, a_price, num_people, num_kids_club, pool_pass, kids_cost, pool_cost):
    print("Booking Details")
    print("-" * 28)
    space = " "
    print(space)
    s_name = f"Name:{space:19}{name}"
    s_booking_num = f"Booking Number:{space:9}{booking_num:}"
    s_phone = f"Phone number:{space:11}{phone}"
    s_a_type = f"Accommodation Type:{space:5}{a_type}"
    s_num_people = f"No of people:{space:11}{num_people}"
    s_num_kids_club = f"Number for kids club:{space:3}{num_kids_club}"
    pool = "No"
    if pool_pass == "y":
        pool = "Yes"
    s_pool = f"Pool Pass:{space:14}{pool}"
    s_a_price = f"Cost of Accommodation:{space:2}€{a_price}"
    total_cost = int(a_price) + int(kids_cost) + int(pool_cost)
    s_total_cost = f"Total Cost:{space:13}€{total_cost}"
    print(f"{s_name}\n{s_booking_num}\n{s_a_type}\n{s_num_people}\n{s_num_kids_club}\n{s_pool}\n{s_a_price}\n{s_total_cost}")
    confirm_booking = get_yes_no("Do you want to confirm this booking? y/n: ")
    if confirm_booking == "y":
        with open(f"{name}_{booking_num}.txt", "x") as created_file:
            print(f"{s_name}\n{s_booking_num}\n{s_phone}\n{s_a_type}\n{s_num_people}\n{s_num_kids_club}\n{s_pool}\n{s_a_price}\n{s_total_cost}", file=created_file)
            created_file.close()


#functions to try failsafe the input from the user
def get_family_name(question):
    while True:
        try:
            result = input(question)
            length = len(result)
            if length != 0 and length < 15:
                break
            else:
                print("Error Occurred: The name needs to be less than 15 characters")
        except ValueError:
            print("Error Occurred: Please enter a non-empty string")
    return result


def get_family_phone(question):
    while True:
        try:
            result = str(input(question))
            if len(str(result)) >= 12:
                print("Error Occurred: Phone number must be less than 12 characters")
            else:
                if int(result) >= 0 and len(str(result)) < 12:
                    break
                else:
                    print("Error Occurred: Please enter a real number less than 12 digits")
        except ValueError:
            print("Error Occurred: Please enter a real number less than 12 digits test")

    return result


def get_booking_type(a_type_list, a_price_list, a_booking_num_list):
    print("Please choose your accommodation type:")
    for i in range(len(a_type_list)):
        print(f"{i + 1}. {a_type_list[i]}, (€{a_price_list[i]}), {a_booking_num_list[i]} booked")
    while True:
        try:
            booking_type = int(input("=>"))
            if (len(a_type_list)) >= booking_type > 0:
                break
            else:
                print(f"Error Occurred: Please enter a number between 1 and {len(a_type_list)}")
        except ValueError:
            print(f"Error Occurred: Please enter a number between 1 and {len(a_type_list)}")
    booking_type = booking_type - 1
    return booking_type


def get_group_num(question):
    while True:
        try:
            num = int(input(question))
            if num > 0:
                break
            else:
                print("Error: Occurred: Number must be greater than 0")
        except ValueError:
            print("Error Occurred: please enter a positive number for your group")
    return num


def get_num_kids(question, group_num):
    while True:
        try:
            num = int(input(question))
            if group_num > num >= 0:
                break
            else:
                print("Error Occurred: Number must be less than the total number of the group")
        except ValueError:
            print("Error Occurred: Please enter a positive number")
    return num


def get_yes_no(question):
    while True:
        try:
            result = input(question)
            lower_result = result.lower()
            if lower_result == "y" or lower_result == "n":
                break
            else:
                print("Error Occurred: Please enter a y for yes or n for no")
        except ValueError:
            print("Error Occurred: Please enter a y for yes or n for no")

    return lower_result


#A function to display the menu and to get a proper choice
def get_menu():
    print("LONG ISLAND HOLIDAY")
    print("=" * 28)
    while True:
        try:
            choice = int(input("1.Make a booking\n2.Review Booking\n3.Exit\nPlease enter the number of the option you wish to select: "))
            if 4 > choice > 0:
                break
            else:
                print("Error Occurred: Please enter a number between 1 and 3 for the option that you want")
        except ValueError:
            print("Error Occurred: Please enter a number for the option that you want")
    return choice


# A function to display a summary of the bookings made so far
def get_review_bookings(a_type_list, a_price_list, a_booking_num_list, e_type_list, e_booking_list):
    print("LONG ISLAND HOLIDAY - Review Booking")
    print("=" * 28)
    income_per_type = []
    total_booked = 0
    income = 0
    for i in range(len(a_type_list)):
        print(f"{a_type_list[i]}: {a_booking_num_list[i]}")
        income = int(a_price_list[i]) * int(a_booking_num_list[i])
        income_per_type.append(income)
        total_booked = total_booked + int(a_booking_num_list[i])
    print(f"Total no. of Pool Passes: {e_booking_list[1]}")
    print(f"Total number for Kids Club: {e_booking_list[0]}")
    kids_income = int(e_booking_list[0]) * 100
    pool_income = int(e_booking_list[1]) * 150
    total_acc_income = 0
    for n in range(len(a_type_list)):
        total_acc_income = total_acc_income + int(income_per_type[n])
    total_expected_income = total_acc_income + kids_income + pool_income
    if total_booked != 0:
        average = total_expected_income / total_booked
    else:
        average = 0
    remaining_sites = 30 - total_booked
    most_pop_site = ""
    most_pop_site_num = 0
    if total_booked >= 5:
        for i in range(len(a_type_list)):
            if int(a_booking_num_list[i]) > most_pop_site_num:
                most_pop_site_num = int(a_booking_num_list[i])
                most_pop_site = str(a_type_list[i])
            elif int(a_booking_num_list[i]) == most_pop_site_num:
                most_pop_site = most_pop_site, "and", str(a_type_list[i])
        print(f"Most popular accommodation: {most_pop_site}")
    print(f"Expected Income: €{total_expected_income}")
    print(f"Average per booking: €{average:.2f}")
    print(f"Number of sites remaining: {remaining_sites}")
    return_menu = get_yes_no("Do you want to return to the main menu? y/n: ")
    if return_menu == "y":
        main(a_type_list, a_price_list,a_booking_num_list, e_type_list, e_booking_list,True)
    else:
        exit_program(a_type_list, a_price_list,a_booking_num_list, e_type_list, e_booking_list,)


# Functions to read and edit text files
def read_booking_file():
    a_type_list = []
    a_price_list = []
    a_booking_num_list = []
    filename = "Bookings_2022.txt"
    openfile = open(filename)
    for line in openfile:
        line_data = line.split(",")
        a_type_list.append(line_data[0])
        a_price_list.append(line_data[1])
        a_booking_num_list.append(line_data[2].rstrip())
    openfile.close()
    return a_type_list, a_price_list, a_booking_num_list


def save_to_booking_file(a_type_list, a_price_list, a_booking_num_list):
    i = 0
    for i in range(len(a_type_list)):
        if i == 0:
            with open("Bookings_2022.txt", "w") as booking_file:
                booking_file.write(f"{a_type_list[i]},{a_price_list[i]},{a_booking_num_list[i]}\n")
                booking_file.close()
        elif i < len(a_type_list):
            with open("Bookings_2022.txt", "a+") as booking_file:
                booking_file.write(f"{a_type_list[i]},{a_price_list[i]},{a_booking_num_list[i]}\n")
                booking_file.close()
        else:
            with open("Bookings_2022.txt", "a+") as booking_file:
                booking_file.write(f"{a_type_list[i]},{a_price_list[i]},{a_booking_num_list[i]}")
                booking_file.close()
    booking_file.close()


def read_extra_files():
    e_type_list = []
    e_booking_list = []
    filename = "extras.txt"
    openfile = open(filename)
    for line in openfile:
        line_data = line.split(",")
        e_type_list.append(line_data[0])
        e_booking_list.append(line_data[1].rstrip())
    openfile.close()
    return e_type_list, e_booking_list


def save_to_extra_file(e_type_list,e_booking_list):
    for i in range(len(e_type_list)):
        if i == 0:
            with open("extras.txt", "w") as extra_file:
                extra_file.write(f"{e_type_list[i]},{e_booking_list[i]}\n")
                extra_file.close()
        else:
            with open("extras.txt", "a+") as extra_file:
                extra_file.write(f"{e_type_list[i]},{e_booking_list[i]}")
                extra_file.close()


# A function to exit the program
def exit_program(a_type_list, a_price_list,a_booking_num_list, e_type_list, e_booking_list):
    print("The files will be updated when you exit the program")
    exit_code = get_yes_no("Are you sure you want to exit? y/n: ")
    if exit_code == "y":
        save_to_booking_file(a_type_list, a_price_list, a_booking_num_list)
        save_to_extra_file(e_type_list, e_booking_list)
        print("Files updated")
        print("Exiting....")
        print("Thank you")
        exit()
    else:
        main(a_type_list, a_price_list,a_booking_num_list, e_type_list, e_booking_list,True)


main(0,0,0,0,0)
