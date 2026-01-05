# EX1 Music Library Manager 

print("Welcome to the Music Library Manager!")

# 1. Initialize Data Structures
songs = []
genre_count = {}

# 2. Collect Song Information
for i in range(1, 6):
    print(f"\nEnter Song {i}:")
    name = input("Song Name: ")
    genre = input("Genre: ")

    # 3. Store Data
    songs.append((name, genre))
    genre_count[genre] = genre_count.get(genre, 0) + 1

# 4. Display Results 
print("\n=== Music Library Summary ===")
for index, (name, genre) in enumerate(songs, start=1):
    print(f"{index}. {name} - ({genre})")

print("\n=== Genre Statistics ===")
for genre, count in genre_count.items():
    print(f"{genre}: {count} song(s)")

# Identify the most popular genre
most_popular_genre = max(genre_count, key=genre_count.get)
print(f"Most popular genre: {most_popular_genre} with {genre_count[most_popular_genre]} song(s)")



# EX2: Student Grade Analyzer

# Part A: Data Collection
Student_records = []




for i in range (1,7):
    print(f"Enter student {i} info :")
    name = input("Name: ")
    score = int(input("Score (0-100): "))
    Student_records.append ((name, score))

    # Part B : Stats
    score = [score for _, score in Student_records]

    Stats = {
        "highest" : max(score),
        "lowest" : min(score),
        "average" : sum(score) / len(score)
    }


# Part C : Unique Grades

unique_grades = set(score)

# Part D : Grade Distribution

grade_distribution = {}
for s in score :
    grade_distribution[s] = grade_distribution.get(s, 0) + 1
    # Display Results
print("\n=== STUDENT RECORDS ===")
for idx, (name, score) in enumerate (Student_records, start=1):
    print (f"{idx}. {name} - Score: {score}")

print ("\n=== Class Statistics ===")
print (f"Highest Score: {Stats['highest']}")
print (f"Lowest Score: {Stats['lowest']}")
print (f"Average Score: {Stats['average']:.2f}")

print("\n=== Unique Scores ===")
print (unique_grades)
print (f"total unique scores: {len(unique_grades)}")

print ("\n=== Grade Distribution ===")
for score, count in grade_distribution.items():
    print (f"Score {score}: {count} student(s)")




# Ex3: Personal Expense Tracker

# 1. Initialize Data Structures
expenses_records = []
category_totals = {}
unique_categories = set()

# 2. Collect Expense Data
for i in range (1, 6):
    print (f"Enter expense {i} details :")
    category = input ("Category: ")
    amount = float (input ("Amount: "))
    date = input ("Date (YYYY-MM-DD): ")
    expenses_records.append ((category, amount, date))

    # 3. Categorize and Sum Expenses
    for category, amount, _ in expenses_records:
        unique_categories.add(category)
        category_totals[category] = category_totals.get(category, 0) + amount

    # 4. Calculate Overall Statistics
    all_amounts = [amount for _, amount, _ in expenses_records]

    total_spending = sum(all_amounts)
    average_spending = total_spending / len(all_amounts)
    highest_expense = max(expenses_records, key=lambda x: x[1])
    lowest_expense = min(expenses_records, key=lambda x: x[1])

    overall_stats = {
    "total_spending": total_spending,
    "average_spending": average_spending,
    "highest_expense": highest_expense,
    "lowest_expense": lowest_expense
}



# 5. Generate Spending Report
print("\n=== OVERALL SPENDING SUMMARY ===")
print(f"Total Spending: ${overall_stats['total']:.2f}")
print(f"Average Expense: ${overall_stats['average']:.2f}")
print(f"Highest Expense: ${overall_stats['highest'][1]:.2f} "
      f"(Category: {overall_stats['highest'][0]}, Date: {overall_stats['highest'][2]})")
print(f"Lowest Expense: ${overall_stats['lowest'][1]:.2f} "
      f"(Category: {overall_stats['lowest'][0]}, Date: {overall_stats['lowest'][2]})")

print("\n=== UNIQUE CATEGORIES SPENT ON ===")
print(unique_categories)
print(f"Total unique categories: {len(unique_categories)}")

print("\n=== SPENDING BY CATEGORY ===")
for cat, total in category_totals.items():
    print(f"{cat}: ${total:.2f}")


