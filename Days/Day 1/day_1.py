# 1. Create a greeting for your program.

# 2. Ask the user for the city that they grew up in.

# 3. Ask the user for the name of a pet.

# 4. Combine the name of their city and pet and show them their band name.

# 5. Make sure the input cursor shows on a new line:

# Solution: https://replit.com/@appbrewery/band-name-generator-end

GREETING = (
    "Hello user! \nThis is a small program that will generate your future band name!"
)
print(GREETING)
city_name = input("In which city did you grow up? \n")
pet_name = input("What was your first pets name? \n")

print("This could be your band name: " + city_name + " " + pet_name)
