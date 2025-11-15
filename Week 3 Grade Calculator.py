# Lab Exercise 1: Grade Calculator
score = int(input("Enter your score (0-100): "))

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print("Your grade is:", grade)

if grade == "A":
    print("Excellent work!")








# Lab Exercise 2: Limited Login Attempts
correct_pin = "1234"
attempts = 0
max_attempts = 3
login_successful = False

while attempts < max_attempts:
    print("Attempt", attempts + 1, "of", max_attempts)
    entered_pin = input("Enter your PIN: ")
    
    if entered_pin == correct_pin:
        print("PIN accepted! Welcome.")
        login_successful = True
        break
    else:
        print("Incorrect PIN.")
        attempts += 1

if not login_successful:
    print("Too many incorrect attempts. Account locked.")








# Lab Exercise 3: Filtering Even Numbers
numbers = [1,2,3,4,5,6,7,8,9,10]

for number in numbers:
    if number % 2 != 0:
        continue
    print(number)
