# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
count = 0
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆
  count+=student_heights[n]
avg = round(count/len(student_heights))
print(avg)

#Write your code below this row 👇




