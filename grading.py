def calculate_final_grade():
    # Input values
    E = float(input("Enter the Written Exam grade (E): "))
    CP = float(input("Enter the Midterm Exam grade (CP): "))
    t = int(input("Enter the number of Course Topics (t): "))
    
    # Input grades for each course topic
    CT = []
    for i in range(1, t + 1):
        CT_i = float(input(f"Enter the grade for Course Topic {i} (CT_{i}): "))
        CT.append(CT_i)
    
    LP1 = float(input("Enter the grade for Lab Assignment 1 (LP1): "))
    LP2 = float(input("Enter the grade for Lab Assignment 2 (LP2): "))
    LS = float(input("Enter the overall Lab Activity grade (LS): "))

    # Calculate C
    C = (CP * 8 + sum(CT) * 2) / 10

    # Calculate L
    L = LP1 + LP2

    # Calculate Final Mark
    Mark_Final = (E * 3.5 + 1.5 * C + 4 * L + 10) / 10

    # Bonus Points (BP) condition
    if L == 10 and E > 7 and C > 7:
        BP = min(2, 3.5 * E + 1.5 * C)
        print(f"Bonus Points (BP): {BP}")
    else:
        BP = 0
        print("No Bonus Points (BP) awarded.")

    # Print results
    print(f"Course Activity Grade (C): {C:.2f}")
    print(f"Lab Activity Grade (L): {L:.2f}")
    print(f"Final Mark: {Mark_Final:.2f}")

# Run the function
calculate_final_grade()
