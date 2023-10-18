import math
import random
import datetime


# user-defined functions start
# 0)Module Programs
# 1)Basic Programs
# 2)Conditional Programs
# 3)List Programs
# 4)Tuples Programs
# 5)Dictionary Programs
# 6)Patterns
def ex():
    print("EXIT Input")


def math_module_f():
    val = int(input("Enter a number"))
    print("Square root of ", val, " = ", math.sqrt(val))


def random_f():
    print("Random  from seed-")
    random.seed()
    print(random.random())
    print("Random from randint-")
    print(random.randint(0, 100))


def swapping():
    # swapping
    x = input("Enter value of x: ")
    y = input("Enter value of y: ")
    print("Value of x before swap:", x)
    print("Value of y before swap:", y)

    print("<------------------>")
    z = x
    x = y
    y = z
    print("Value of x after swap:", x)
    print("Value of y after swap:", y)


def addition():
    first_num = float(input("Enter first number: "))
    second_num = float(input("Enter second number: "))
    sum_result = first_num + second_num
    print("Sum:", sum_result)


def subtraction():
    first_num = float(input("Enter first number: "))
    second_num = float(input("Enter second number: "))
    difference = first_num - second_num
    print("Difference:", difference)


def multiplication():
    first_num = float(input("Enter first number: "))
    second_num = float(input("Enter second number: "))
    product = first_num * second_num
    print("Product:", product)


def division():
    first_num = float(input("Enter first number: "))
    second_num = float(input("Enter second number: "))
    if second_num == 0:
        print("Error: Division by zero")
    else:
        quotient = first_num / second_num
        print("Quotient:", quotient)


def area_of_circle():
    pie = 3.14
    value_r = float(input("Enter value of radius: "))
    area_of_c = pie * value_r * value_r
    print("Area of Circle:", area_of_c)


def area_of_triangle():
    half = 0.5
    base = float(input("Enter base: "))
    height = float(input("Enter height: "))
    area_of_tri = half * base * height
    print("Area of Triangle:", area_of_tri)


def area_of_rectangle():
    length = float(input("Enter length: "))
    breadth = float(input("Enter breadth: "))
    area_of_rec = length * breadth
    print("Area of Rectangle:", area_of_rec)


def simple_interest():
    principal = float(input("Enter the principal amount: "))
    rate = float(input("Enter the rate of interest: "))
    time = float(input("Enter the time period (in years): "))
    interest = (principal * rate * time) / 100
    print("Simple Interest:", interest)


def f_to_c():
    fahrenheit = float(input("Enter the temperature in Fahrenheit: "))
    celsius = (fahrenheit - 32) / 1.8
    print("Celsius Equivalent:", celsius)


def c_to_f():
    celsius = float(input("Enter the temperature in Celsius: "))
    fahrenheit = (celsius * 1.8) + 32
    print("Fahrenheit Equivalent:", fahrenheit)


def circum_of_circle():
    pie = 3.14
    radius = float(input("Enter the radius of the circle: "))
    circumference = 2 * pie * radius
    print("Circumference of Circle:", circumference)


def discriminant():
    a = float(input("Enter the coefficient a: "))
    b = float(input("Enter the coefficient b: "))
    c = float(input("Enter the coefficient c: "))
    discriminant_value = (b ** 2) - (4 * a * c)
    if discriminant_value > 0:
        print("Two real solutions, Discriminant Value =", discriminant_value)
    elif discriminant_value == 0:
        print("One real solution, Discriminant Value =", discriminant_value)
    else:
        print("No real solutions, Discriminant Value =", discriminant_value)


def area_of_square():
    side = float(input("Enter the length of a side: "))
    area = side * side
    print("Area of Square:", area)


def area_of_trapezoid():
    longer_base = float(input("Enter the length of the longer base: "))
    shorter_base = float(input("Enter the length of the shorter base: "))
    height = float(input("Enter the height: "))
    area = 0.5 * (longer_base + shorter_base) * height
    print("Area of Trapezoid:", area)


def area_of_ellipse():
    a = float(input("Enter the length of semi-major axis (a): "))
    b = float(input("Enter the length of semi-minor axis (b): "))
    area = 3.14 * a * b
    print("Area of Ellipse:", area)


def surface_area_rectangular_prism():
    length = float(input("Enter the length of the rectangular prism: "))
    width = float(input("Enter the width of the rectangular prism: "))
    height = float(input("Enter the height of the rectangular prism: "))
    surface_area = 2 * ((length * width) + (width * height) + (height * length))
    print("Surface Area of Rectangular Prism:", surface_area)


def surface_area_triangular_prism():
    base_length = float(input("Enter the length of the base of the triangular prism: "))
    base_width = float(input("Enter the width of the base of the triangular prism: "))
    height = float(input("Enter the height of the triangular prism: "))
    side1_length = float(input("Enter the length of side 1: "))
    side2_length = float(input("Enter the length of side 2: "))
    side3_length = float(input("Enter the length of side 3: "))
    base_area = 0.5 * base_length * base_width
    lateral_surface_area = base_length * height + (0.5 * side1_length * height) + (0.5 * side2_length * height) + (
            0.5 * side3_length * height)
    surface_area = base_area + lateral_surface_area
    print("Surface Area of Triangular Prism:", surface_area)


def surface_area_pentagonal_prism():
    apothem = float(input("Enter the length of the apothem: "))
    base_perimeter = float(input("Enter the perimeter of the base: "))
    height = float(input("Enter the height of the pentagonal prism: "))
    surface_area = (5 * apothem * base_perimeter / 2) + (5 * height * base_perimeter / 2)
    print("Surface Area of Pentagonal Prism:", surface_area)


def surface_area_hexagonal_prism():
    apothem = float(input("Enter the length of the apothem: "))
    base_perimeter = float(input("Enter the perimeter of the base: "))
    height = float(input("Enter the height of the hexagonal prism: "))
    surface_area = (6 * apothem * base_perimeter / 2) + (6 * height * base_perimeter / 2)
    print("Surface Area of Hexagonal Prism:", surface_area)


def area_of_pentagon():
    a = float(input("Enter the side length of the pentagon: "))
    b = float(input("Enter the apothem length of the pentagon: "))
    area = (5 * a * b) / 2
    print("Area of Pentagon:", area)


def volume_of_cuboid():
    length = float(input("Enter the length of the cuboid: "))
    width = float(input("Enter the width of the cuboid: "))
    height = float(input("Enter the height of the cuboid: "))
    volume = length * width * height
    print("Volume of Cuboid:", volume)


def surface_area_cuboid():
    length = float(input("Enter the length of the cuboid: "))
    width = float(input("Enter the width of the cuboid: "))
    height = float(input("Enter the height of the cuboid: "))
    surface_area = 2 * ((length * width) + (width * height) + (height * length))
    print("Surface Area of Cuboid:", surface_area)


def volume_of_cube():
    side = float(input("Enter the side length of the cube: "))
    volume = side * side * side
    print("Volume of Cube:", volume)


def surface_area_cube():
    side = float(input("Enter the side length of the cube: "))
    surface_area = 6 * side * side
    print("Surface Area of Cube:", surface_area)


def volume_of_cone():
    radius = float(input("Enter the radius of the cone: "))
    height = float(input("Enter the height of the cone: "))
    volume = (1 / 3) * 3.14 * radius ** 2 * height
    print("Volume of Cone:", volume)


def curved_surface_area_of_cone():
    r = float(input("enter value of r"))
    lh = float(input("enter value of l(slant height)"))
    csa_c = 3.14 * r * lh
    print("CSA of cone=", csa_c)


def curved_surface_area_of_cylender():
    r = float(input("enter value of r"))
    h = float(input("enter value of h(height)"))
    csa_c = 2 * 3.14 * r * h
    print("CSA of cylender=", csa_c)


def total_surface_area_of_cylender():
    r = float(input("enter value of r"))
    h = float(input("enter value of h(height)"))
    tsa_c = (2 * 3.14 * r * h) + (2 * 3.14 * r * r)
    print("TSA of cylender=", tsa_c)


def volume_of_sphere():
    r = float(input("enter value of r"))
    vol = 1 / 3 * 3.14 * r * r * r
    print("Volume of sphere=", vol)


def surface_area_of_sphere():
    r = float(input("enter value of r"))
    s_area = 4 * 3.14 * r * r
    print("surface area of sphere=", s_area)


def vote_eligibility_age_checker():
    age = float(input("enter age"))
    if age >= 18:
        print("You are Eligible")
    else:
        print("You are not eligible")


def even_or_odd_number_verifier():
    num = float(input("Enter the number for verification"))
    if num % 2 == 0:
        print("The number is even")
    else:
        print("number is odd")


def divisibility_of_seven_checker():
    num = float(input("Enter the number for verification"))
    if num % 7 == 0:
        print("The number is divisible by 7")
    else:
        print("The number is not divisible by 7")


def multiple_of_five():
    num = float(input("Enter the number"))
    if num % 5 == 0:
        print("the number is a multiple of five\nHello")
    else:
        print("the number is not a multiple of five\nbye")


def electricity_bill_calculator():
    unit = float(input("Enter the number of units"))
    if unit <= 100:
        print("No Charge")
    elif unit > 100:
        charge = unit * 5
        print("Charge=", charge)
    elif unit >= 200:
        charge = unit * 10
        print("Charge=", charge)
    elif unit >= 300:
        charge = unit * 15
        print("Charge=", charge)
    elif unit >= 350:
        charge = unit * 20
        print("Charge=", charge)
    else:
        print("(invlid)Exiting")


def marksheet():
    eng = float(input("Enter the percentage of English"))
    hindi = float(input("Enter the percentage of Hindi"))
    math = float(input("Enter the percentage of Maths"))
    sci = float(input("Enter the percentage of Science"))
    social = float(input("Enter the percentage of social"))
    french = float(input("Enter the percentage of french"))
    percentage = (eng + hindi + math + sci + social + french) / 6
    print("percentage=", percentage)
    if percentage < 28:
        print("Fail(E)")
    elif 28 < percentage < 33:
        print("Boundary Pass(D)")
    elif 33 < percentage < 65:
        print("pass(C)")
    elif 65 < percentage < 75:
        print("pass with second division(B)")
    elif 75 < percentage < 85:
        print("pass with first division(B+)")
    elif 85 < percentage < 95:
        print("pass with first division plus(A)")
    else:
        print("Pass with highest division(A+)")


def bike_road_tax():
    cost_of_the_bike = float(input("Enter the cost of the bike"))
    if cost_of_the_bike > 100000:
        tax = (cost_of_the_bike * 15) / 100
        total_cost_of_the_bike = tax + cost_of_the_bike
        print("total cost of the bike=", total_cost_of_the_bike)
    elif 100000 > cost_of_the_bike > 50000:
        tax1 = (cost_of_the_bike * 10) / 100
        total_cost_of_the_bike = cost_of_the_bike + tax1
        print("total cost of the bike=", total_cost_of_the_bike)
    else:
        tax2 = (cost_of_the_bike * 5) / 100
        total_cost_of_the_bike = cost_of_the_bike + tax2
        print("total cost of the bike=", total_cost_of_the_bike)


def leap_year_check():
    year = int(input("Enter year"))
    if year % 4 == 0:
        print("It is a leap year")
    else:
        print("not a leap year")


def day_check():
    day = int(input("Enter the number 1-7"))
    number = day
    if number < 0 or number > 7:
        print("Invald day")
    elif number == 1:
        print("Monday")
    elif number == 2:
        print("Tuesday")
    elif number == 3:
        print("Wednesday")
    elif number == 4:
        print("Thursday")
    elif number == 5:
        print("Friday")
    elif number == 6:
        print("Saturday")
    elif number == 7:
        print("Sunday")
    else:
        print("Invalid Error")


def month_check():
    day = int(input("Enter the number 1-12"))
    number = day
    if number < 0 or number > 12:
        print("Invald month")
    elif number == 1:
        print("January")
    elif number == 2:
        print("Feburary")
    elif number == 3:
        print("March")
    elif number == 4:
        print("April")
    elif number == 5:
        print("May")
    elif number == 6:
        print("June")
    elif number == 7:
        print("July")
    elif number == 8:
        print("August")
    elif number == 9:
        print("September")
    elif number == 10:
        print("October")
    elif number == 11:
        print("November")
    elif number == 12:
        print("December")
    else:
        print("Invalid Error")


def greatest_among_two():
    num1 = int(input("Enter the number"))
    num2 = int(input("Enter the Second Number"))
    if num1 > num2:
        print("first number is greater")
    else:
        print("Second number is Greater")


def greatest_among_three():
    num1 = int(input("Enter the first number"))
    num2 = int(input("Enter the Second Number"))
    num3 = int(input("Enter the third Number"))
    if num1 > num2 and num1 > num3:
        print("first number is greater")
    elif num2 > num3:
        print("Second number is Greater")
    else:
        print("Third number is greater")


def emp_bonus():
    salary = int(input("Enter the salary number"))
    experience = int(input("Enter the years of experience"))
    if experience > 10:
        sal = (10 * salary) / 100
        f_sal = salary + sal
        print("Bonus+salary=", f_sal)
    elif 6 <= experience <= 10:
        sal = (8 * salary) / 100
        f_sal = salary + sal
        print("Bonus+salary=", f_sal)
    else:
        sal = (6 * salary) / 100
        f_sal = salary + sal
        print("Bonus+salary=", f_sal)


def type_of_triangle_check():
    side1 = float(input("Enter the first side of the triangle"))
    side2 = float(input("Enter the second side of the triangle"))
    side3 = float(input("Enter the third side of the triangle"))
    if side1 == side2 == side3:
        print("equvilateral triangle")
    elif side1 == side2 or side3 == side2 or side1 == side3:
        print("Isosceles Triangle")
    elif side1 != side2 and side2 != side3 and side3 != side1:
        print("Scalene Triangle")


def list_i():
    lst = [1, 2, 3, 4, 5]
    print("List=", lst)


def list_append_function():
    lst = [1, 2, 5, 6]
    print("Append Function")
    print("pre-initialised list(before append function)", lst[::])
    print("Enter element to be appended(float value)")
    e = float(input(""))
    lst.append(e)
    print("List after append", lst[::])


def list_user_input():
    print("List with User Input")
    # creating an empty list
    lst = []

    # number of elements as input
    n = int(input("Enter number of elements : "))

    # iterating till the range
    for i in range(0, n):
        ele = int(input())
        # adding the element(appending it)
        lst.append(ele)

    print(lst)


# menu for iterative programs
def list_of_small_iterative_programs():
    print(" ""While"" and ""for"" programs")


#
def dictionary_functions_demo():
    print("Dictionary Functions Demo")

    # Create a dictionary
    my_dict = {"name": "Alice", "age": 30, "city": "Wonderland"}

    # Accessing values
    print("Name:", my_dict["name"])
    print("Age:", my_dict.get("age"))

    # Adding a new key-value pair
    my_dict["country"] = "Unknown"
    print("Dictionary after adding 'country':", my_dict)

    # Modifying a value
    my_dict["age"] = 31
    print("Dictionary after updating 'age':", my_dict)

    # Removing a key-value pair
    del my_dict["city"]
    print("Dictionary after deleting 'city':", my_dict)

    # Checking if a key exists
    if "name" in my_dict:
        print("'name' key exists in the dictionary")

    # Get a list of all keys
    keys = list(my_dict.keys())
    print("Keys in the dictionary:", keys)

    # Get a list of all values
    values = list(my_dict.values())
    print("Values in the dictionary:", values)

    # Get a list of key-value pairs (items)
    items = list(my_dict.items())
    print("Key-Value pairs in the dictionary:", items)


#
def dictionary_pre_i():
    print("")
    dict1 = {1: "A", 2: "B", 3: "C"}
    print(dict1)


#
#
def user_input_to_dict():
    print("User Input to Dictionary Demo")

    # Create an empty dictionary to store user input
    user_data = {"name": input("Enter your name: "), "age": int(input("Enter your age: ")),
                 "city": input("Enter your city: ")}

    print("User Data:")
    for key, value in user_data.items():
        print(f"{key}: {value}")
    print(user_data)


#
# menu for dictionary related functions
def dictionary_functions():
    print("dictionary_functions")
    print("1)Dictionary Pre Initialised")
    print("2)Dictionary with user input")
    print("3)Dictionary few basic functions")
    print("Enter an Integer to choose an option")
    ch = int(input("Enter"))
    if ch == 1:
        dictionary_pre_i()
    elif ch == 2:
        user_input_to_dict()
    elif ch == 3:
        dictionary_functions_demo()
    else:
        print("Invalid input")


def tupple_functions_ls():
    print("Tuple Functions")

    # Create a tuple
    my_tuple = (1, 2, 3, 4, 5)
    print("Pre-Initialised Tuple", my_tuple)

    # Access elements of the tuple
    print("Tuple elements:", my_tuple)
    print("First element:", my_tuple[0])
    print("Last element:", my_tuple[-1])

    # Get the length of the tuple
    print("Length of the tuple:", len(my_tuple))

    # Count occurrences of a value in the tuple
    count = my_tuple.count(3)
    print("Count of 3 in the tuple:", count)

    # Find the index of a value in the tuple
    index = my_tuple.index(4)
    print("Index of 4 in the tuple:", index)

    # Slicing the tuple
    sliced_tuple = my_tuple[1:4]
    print("Sliced tuple:", sliced_tuple)


# menu for tupple functions
def tupple_functions():
    print("Tuple Functions")
    print("Choose an Option(Enter Integer")
    print("1)Pre-Intialised Tupple")
    print("2)Tupple_Slice")
    print("3)Tupple Functions")
    choice_1 = int(input("Enter Value"))
    if choice_1 == 1:
        pre_intialised_tupple()
    elif choice_1 == 2:
        tupple_slice()
    elif choice_1 == 3:
        tupple_functions_ls()
    else:
        print("invalid input")


def pre_intialised_tupple():
    tup = (1, 2, 3)
    print("pre-initialised tupple = ", tup)


def tupple_slice():
    print("Tuple Slicing")
    val1 = int(input("Enter a value for tuple initialisation"))
    val2 = int(input("Enter a 2nd value"))
    val3 = int(input("Enter a 3rd value"))
    val4 = int(input("Enter a 4th value"))
    val5 = int(input("Enter a 5th value"))
    print("Putting values inside tuple and slicing it")
    tup = (val1, val2, val3, val4, val5)
    print("Tuple = ", tup)
    print("[::] = ", tup[::])
    print("[1:2:1] = ", tup[1:2:1])
    print("[1:3:2] = ", tup[1:3:2])
    print("[2:5:1] = ", tup[2:5:1])
    print("[4:1:-1] = ", tup[4:1:-1])
    print("Do you want to enter values for slicing manually? 1=yes 0=no")
    choice1 = int(input("Enter 1 or 0"))
    if choice1 == 1:
        print("Ok")
        m_v_start = int(input("Enter start value"))
        m_v_stop = int(input("Enter stop value"))
        m_v_step = int(input("Enter step size"))
        print("You Entered these value", m_v_start, m_v_stop, m_v_step)
        ret = [m_v_start, m_v_stop, m_v_step]
        print("tuple after your slice", ret)
    elif choice1 == 0:
        print("OK")
        print("Exiting Program")
    else:
        print("Invalid Input")
        print("Exiting Program")


# p
def l_py():
    print("Left sided pyramid")
    #
    for i in range(1, 5 + 1):
        spaces = (1 + i) * ' '
        blocks = '*' * i
        print(spaces + blocks)

    #


def r_py():
    print("Right sided pyramid")
    #
    for i in range(1, 5 + 1):
        spaces = ' ' * (5 - i)
        blocks = '*' * i
        print(spaces + blocks)

    #


def f_py():
    print("full centered pyramid")
    #
    for i in range(1, 5 + 1):
        spaces = ' ' * (5 - i)
        blocks = '*' * (2 * i - 1)
        print(spaces + blocks)

    # Example usage:

    #


def i_f_py():
    print(" full inverted pyramid")

    for i in range(5, 0, -1):
        spaces = ' ' * (5 - i)
        blocks = '*' * (2 * i - 1)
        print(spaces + blocks)


def i_r_py():
    print("inverted right pyramid")

    for i in range(5, 0, -1):
        spaces = ' ' * (5 - i)
        blocks = '*' * i
        print(spaces + blocks)


def i_l_py():
    for i in range(5, 0, -1):
        spaces = ' ' * (5 - i)
        blocks = '*' * i
        print(spaces + blocks)


# menu for pattern programs
def patterns_in_py():
    print("Patterns In Python(Values for rows/cols have been pre initialised by default)")
    print("Choose an Option(Enter Integer")
    print("1)Left Sided Pyramid")
    print("2)Right sided Pyramid")
    print("3)Full Pyramid")
    print("4) Full Inverted Pyramid")
    print("5)Left Sided Inverted Pyramid")
    print("6)Right Sided Inverted Pyramid")
    co = int(input("Enter Choice-"))
    if co == 1:
        l_py()
    elif co == 2:
        r_py()
    elif co == 3:
        f_py()
    elif co == 4:
        i_f_py()
    elif co == 5:
        i_l_py()
    elif co == 6:
        i_r_py()
    else:
        print("invalid input")


# menu for list functions
def list_functions():
    print("Choose an Option(Enter Integer")
    print("1)List Pre-Declaration with Output")
    print("2)List with User Input and Outputting it")
    print("3)List append")
    print("4)List all basic functions")
    print("5)List Slicing")
    list_f_c = int(input("Enter a choice"))
    if list_f_c == 1:
        list_i()
    elif list_f_c == 2:
        list_user_input()
    elif list_f_c == 3:
        list_append_function()
    elif list_f_c == 4:
        list_functions_l()
    elif list_f_c == 5:
        list_slicing_demo()


#
#
def list_slicing_demo():
    print("List Slicing Demo")

    # Create a list
    my_list = [1, 2, 3, 4, 5, 6, 7]

    # Basic list slicing
    sliced_list = my_list[1:5]
    print("Basic List Slicing:", sliced_list)

    # Extended slicing with step
    extended_slicing = my_list[1:6:2]
    print("Extended List Slicing with Step 2:", extended_slicing)

    # Negative indexing
    negative_slicing = my_list[-3:-1]
    print("Negative Indexing List Slicing:", negative_slicing)

    # Slicing from the beginning
    start_slicing = my_list[:4]
    print("Slicing from the Beginning:", start_slicing)

    # Slicing till the end
    end_slicing = my_list[3:]
    print("Slicing Till the End:", end_slicing)


#
#
def list_functions_l():
    print("List Functions")

    # Create a list
    my_list = [1, 2, 3, 4, 5]

    # Access elements of the list
    print("List elements:", my_list)
    print("First element:", my_list[0])
    print("Last element:", my_list[-1])

    # Get the length of the list
    print("Length of the list:", len(my_list))

    # Append an element to the list
    my_list.append(6)
    print("List after appending 6:", my_list)

    # Remove an element from the list
    my_list.remove(3)
    print("List after removing 3:", my_list)

    # Insert an element at a specific index
    my_list.insert(2, 7)
    print("List after inserting 7 at index 2:", my_list)

    # Count occurrences of a value in the list
    count = my_list.count(4)
    print("Count of 4 in the list:", count)

    # Find the index of a value in the list
    index = my_list.index(5)
    print("Index of 5 in the list:", index)

    # Slicing the list
    sliced_list = my_list[1:4]
    print("Sliced list:", sliced_list)


#


def working_with_functions():
    print("Enter an integer value")
    print("1)Function (Hello World)")
    print("2)Addition of two numbers with parameters")
    f_choice = int(input("Enter option"))
    if f_choice == 1:
        hello_world()
    elif f_choice == 2:
        add_f1()


def hello_world():
    print("Hello World")


def add_f2(f, s):
    sum = f + s
    print(sum)


def add_f1():
    print("Enter first Number")
    f = int(input())
    print("Enter second Number")
    s = int(input())
    add_f2(f, s)


def types_of_argc():
    print("1)Positional Argc")
    print("2)Keyword Argc")
    print("3)Default Argc")
    print("4)Variable length Argc")
    print("5)Keyword Variable Length Argc")
    t_choice = int(input("Enter an Integer Value as an option"))
    if t_choice == 1:
        pos_a()
    elif t_choice == 2:
        kwd_a()
    elif t_choice == 3:
        de_a()
    elif t_choice == 4:
        vl_a()
    elif t_choice == 5:
        kwd_vl_a()
    else:
        print("Invalid Integer")


def pos_a():
    print("Positional Arguments")
    print("passing values x,y positionally to the function pos_a1()")
    x = int(input("Enter  value of x"))
    y = int(input("Enter  value of y"))
    # function call with values passed positionally
    pos_a1(x, y)


def pos_a1(x, y):
    sum1 = x + y
    print("Sum of x,y=", sum1)


def kwd_a():
    print("Keyword Arguments")
    print("enter a name")
    # name=input("Enter-")
    # age = int(input("Enter age-"))

    kwd_a1(age="3", name="rohan")  # argc with name value pair


def kwd_a1(name, age):
    print("name=", name, "age=", age)


def de_a():
    print("Default Arguments")
    print("Do you want to enter a name")
    inp = int(input("Enter 1 = yes else anything other than 1 = no"))
    if inp == 1:
        print("OK,(default value will not be taken)")
        name = input("enter")
        de_a1(name)
    else:
        print("Default values will be taken")
        de_a1()


def de_a1(name="player(default value is taken"):
    print("name=", name)


def vl_a():
    print("Variable length Arguments")
    x = int(input("Enter  value of x"))
    y = int(input("Enter  value of y"))
    z = int(input("Enter value of z"))
    vl_a1(x, y, z)


def vl_a1(*num):
    print("values inside tupple=", num[0], num[1], num[2])
    print("tupple=", num[::])


def kwd_vl_a():
    print(" Keyword Variable length Arguments")
    kwd_vl_a1(x=1, y=2, z=3)


def kwd_vl_a1(**num):
    print("values inside dictionary=", num['x'], num['y'], num['z'])
    print("dictionary=", num)


def about_this_program():
    print("Written By-Juzer Baatwala")
    print("to be submitted to Himanshu sir")


def date_time_functions():
    print("Date and Time functions")

    # Get the current date and time
    current_datetime = datetime.datetime.now()
    print("Current Date and Time:", current_datetime)

    # Access specific components of the date and time
    current_date = current_datetime.date()
    current_time = current_datetime.time()

    print("Current Date:", current_date)
    print("Current Time:", current_time)

    # Format a date and time as a string
    formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
    print("Formatted Date and Time:", formatted_datetime)

    # Parse a date and time from a string
    date_str = "2023-10-18 14:30:00"
    parsed_datetime = datetime.datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
    print("Parsed Date and Time:", parsed_datetime)


#
def generate_fibonacci_series():
    n = int(input("Enter the limit"))
    fibonacci_series = []
    a, b = 0, 1
    for _ in range(n):
        fibonacci_series.append(a)
        a, b = b, a + b
        print(fibonacci_series)


#
def factorial():
    n = int(input("Enter the number-"))
    if n == 0:
        return 1
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
            print(result)

#
# user-defined functions end
# Main function

print("Welcome!")
print("Enter an option (Integer):")
print("0. EXIT")
print("1. Swapping of 2 variables with a third variable")
print("2. Addition")
print("3. Subtraction")
print("4. Multiplication")
print("5. Division")
print("6. Area of Circle")
print("7. Area of Triangle")
print("8. Area of Rectangle")
print("9. Simple Interest")
print("10. Fahrenheit to Celsius converter")
print("11. Celsius to Fahrenheit")
print("12. Circumference of Circle")
print("13. Discriminant")
print("14. Area of Square")
print("15. Area of Trapezoid")
print("16. Area of Ellipse")
print("17. Surface Area of Rectangular Prism")
print("18. Surface Area of Triangular Prism")
print("19. Surface Area of Pentagonal Prism")
print("20. Surface Area of Hexagonal Prism")
print("21. Area of Pentagon")
print("22. Volume of Cuboid")
print("23. Surface Area of Cuboid")
print("24. Volume of Cube")
print("25. Surface Area of Cube")
print("26. Volume of Cone")
print("27. Curved Surface Area of Cone")
print("28. Curved Surface Area of Cylinder")
print("29. Total Surface Area of Cylinder")
print("30. Volume of Sphere")
print("31. Surface Area of Sphere")
print("32. vote_eligibility_age_checker")
print("33. even_or_odd_number_verifier")
print("34. divisibility_of_seven_checker")
print("35. multiple_of_five")
print("36. electricity_bill_calculator")
print("37. marksheet")
print("38. bike_road_tax")
print("39. leap_year_check")
print("40. day_check")
print("41. month_check")
print("42. greatest_among_two")
print("43. greatest_among_three")
print("44. emp_bonus")
print("45. type_of_triangle_check")
print("46. list_functions")
print("47. tupple_functions")
print("48. dictionary_functions")
print("49. patterns_in_py")
print("50. list_of_small_iterative_programs")
print("51. Working_with_functions")
print("52. types_of_argc")
print("53. About This Program")
print("54 Random Number Generator")
print("55. Square root of a number using math module")
print("56. Date_and_Time_Functions")
print("57. fibonacci_series")
print("58. Factorial of a number")

choice = int(input("Enter your choice: "))
if choice == 0:
    ex()
elif choice == 1:
    swapping()
elif choice == 2:
    addition()
elif choice == 3:
    subtraction()
elif choice == 4:
    multiplication()
elif choice == 5:
    division()
elif choice == 6:
    area_of_circle()
elif choice == 7:
    area_of_triangle()
elif choice == 8:
    area_of_rectangle()
elif choice == 9:
    simple_interest()
elif choice == 10:
    f_to_c()
elif choice == 11:
    c_to_f()
elif choice == 12:
    circum_of_circle()
elif choice == 13:
    discriminant()
elif choice == 14:
    area_of_square()
elif choice == 15:
    area_of_trapezoid()
elif choice == 16:
    area_of_ellipse()
elif choice == 17:
    surface_area_rectangular_prism()
elif choice == 18:
    surface_area_triangular_prism()
elif choice == 19:
    surface_area_pentagonal_prism()
elif choice == 20:
    surface_area_hexagonal_prism()
elif choice == 21:
    area_of_pentagon()
elif choice == 22:
    volume_of_cuboid()
elif choice == 23:
    surface_area_cuboid()
elif choice == 24:
    volume_of_cube()
elif choice == 25:
    surface_area_cube()
elif choice == 26:
    volume_of_cone()
elif choice == 27:
    curved_surface_area_of_cone()
elif choice == 28:
    curved_surface_area_of_cylender()
elif choice == 29:
    total_surface_area_of_cylender()
elif choice == 30:
    volume_of_sphere()
elif choice == 31:
    surface_area_of_sphere()
elif choice == 32:
    vote_eligibility_age_checker()
elif choice == 33:
    even_or_odd_number_verifier()
elif choice == 34:
    divisibility_of_seven_checker()
elif choice == 35:
    multiple_of_five()
elif choice == 36:
    electricity_bill_calculator()
elif choice == 37:
    marksheet()
elif choice == 38:
    bike_road_tax()
elif choice == 39:
    leap_year_check()
elif choice == 40:
    day_check()
elif choice == 41:
    month_check()
elif choice == 42:
    greatest_among_two()
elif choice == 43:
    greatest_among_three()
elif choice == 44:
    emp_bonus()
elif choice == 45:
    type_of_triangle_check()
elif choice == 46:
    list_functions()
elif choice == 47:
    tupple_functions()
elif choice == 48:
    dictionary_functions()
elif choice == 49:
    patterns_in_py()
elif choice == 50:
    list_of_small_iterative_programs()
elif choice == 51:
    working_with_functions()
elif choice == 52:
    types_of_argc()
elif choice == 53:
    about_this_program()
elif choice == 54:
    random_f()
elif choice == 55:
    math_module_f()
elif choice == 56:
    date_time_functions()
elif choice == 57:
    generate_fibonacci_series()
elif choice == 58:
    factorial()

else:
    print("Invalid input. Please try again.")
# EF07 786
