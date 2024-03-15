# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


# Write your code below this row 👇

num_of_heights = 0
sum_of_heights = 0

for i in student_heights:
    num_of_heights += 1
    sum_of_heights += int(i)

print(round(sum_of_heights / num_of_heights))
