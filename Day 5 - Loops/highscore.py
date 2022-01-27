# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆
temp = student_scores[0]
for n in range(0, len(student_scores)):
    if(student_scores[n]>temp):
        temp = student_scores[n]

print("The highest score in the class is: " + str(temp))

#Write your code below this row 👇




