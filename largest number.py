# Python program to find the largest number among the three input numbers...
num_1 = float(input("Enter Number_1 :"))
num_2 = float(input("Enter Number_2 :"))
num_3 = float(input("Enter Number_3 :"))
if (num_1 >= num_2 and num_1 >= num_3):
    print("Number_1 is large")
elif (num_2 >= num_1 and num_2 >= num_3):
    print("Number_2 is large")
else :
    print("Number_3 is large")
