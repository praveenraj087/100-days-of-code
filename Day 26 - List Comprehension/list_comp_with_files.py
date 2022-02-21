with open("file1.txt") as file1:
  file1_lines = file1.readlines()

with open("file2.txt") as file2:
  file2_lines = file2.readlines()

line1 = []
line2 = []
for i in file1_lines:
  int_num = int(i)
  line1.append(int_num)
for i in file2_lines:
  int_num = int(i)
  line2.append(int_num) 
  
result = [num for num in line1 if num in line2 ]
# Write your code above 👆

print(result)


