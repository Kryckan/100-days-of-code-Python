# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

lower_one = name1.lower()
lower_two = name2.lower()
combined_name = lower_one + lower_two

t = combined_name.count("t")
r = combined_name.count("r")
u = combined_name.count("u")
e = combined_name.count("e")
l = combined_name.count("l")
o = combined_name.count("o")
v = combined_name.count("v")
e = combined_name.count("e")

first_int = (t + r + u + e) * 10
second_int = l + o + v + e

tot = first_int + second_int

if (tot < 10) or (tot > 90):
    print(f"Your score is {tot}, you go together like coke and mentos.")
elif (tot >= 40) and (tot <= 50):
    print(f"Your score is {tot}, you are alright together.")
else:
    print(f"Your score is {tot}.")
