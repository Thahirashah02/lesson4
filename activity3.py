# take marks as input from user
print("Enter Marks Obtained in 4 Subjects: ")
Chemistry = int(input("Chemistry :"))
Biology = int(input("Biology :"))
Physics = int(input("Physics :"))
Maths = int(input("Maths :"))

# Let's calculate the percentage of marks
sum = Chemistry+Biology+Physics+Maths
print("sun of Chemistry,Biology,Physics and Maths")

perc = (sum/400)*100

print(end="Percentage Mark = ")
print(perc)