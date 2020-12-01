m1 = int(input("Enter m1:"))
m2 = int(input("Enter m2:"))
m3 = int(input("Enter m3:"))
m4 = int(input("Enter m4:"))
m5 = int(input("Enter m5:"))
avg = (m1+m2+m3+m4+m5)/5
if avg>90:
  print("Grade A")
elif(avg>80 and avg<=90):
  print("Grade B")
elif(avg>70 and avg<=80):
  print("Grade C")
elif(avg>60 and avg<=70):
  print("Grade D")
else:
  print("Grade E")
  