print("WELCOME TO QUIZ COMPETITION")
print("-"*40)

name = str(input("Enter Your Name:"))
a = str(input("Are You Ready To Start Quiz? Yes/No:"))

if a=="yes" or a=="Yes":
    print("Let's Start The Quiz")
else:
    print("Okay,", name, "Let's Start The Quiz Later.")
    exit()
print("-"*40)

score = 0

print("1. What is the capital city of France?")
print("A) Paris \nB) London \nC) Berlin \nD) Madrid")
ans = str(input("Enter Your Answer: ")).upper()
if ans == "A":
    print("Correct Answer.")
    score += 2
else:
    print("Incorrect Answer. Correct Answer is A) Paris.")
    score -= 1

print("\n2. Who was the first person to walk on the Moon?")
print("A) Yuri Gagarin \nB) Neil Armstrong \nC) Buzz Aldrin \nD) John Glenn")
ans = str(input("Enter Your Answer: ")).upper()
if ans == "B":
    print("Correct Answer.")
    score += 2
else:
    print("Incorrect Answer. Correct Answer is B) Neil Armstrong.")
    score -= 1

print("\n3. Which gas is most abundant in the Earth's atmosphere?")
print("A) Oxygen \nB) Carbon Dioxide \nC) Hydrogen \nD) Nitrogen")
ans = str(input("Enter Your Answer: ")).upper()
if ans == "D":
    print("Correct Answer.")
    score += 2
else:
    print("Incorrect Answer. Correct Answer is D) Nitrogen.")
    score -= 1

print("\n4. In which year did India gain independence from British rule?")
print("A) 1945 \nB) 1947 \nC) 1950 \nD) 1965")
ans = str(input("Enter Your Answer: ")).upper()
if ans == "B":
    print("Correct Answer.")
    score += 2
else:
    print("Incorrect Answer. Correct Answer is B) 1947.")
    score -= 1

print("\n5. What is the largest planet in our Solar System?")
print("A) Earth \nB) Mars \nC) Jupiter \nD) Saturn")
ans = str(input("Enter Your Answer: ")).upper()
if ans == "C":
    print("Correct Answer.")
    score += 2
else:
    print("Incorrect Answer. Correct Answer is C) Jupiter.")
    score -= 1

print("\n6. Which river is the longest in the world?")
print("A) Nile \nB) Amazon \nC) Yangtze \nD) Mississippi")
ans = str(input("Enter Your Answer: ")).upper()
if ans == "A":
    print("Correct Answer.")
    score += 2
else:
    print("Incorrect Answer. Correct Answer is A) Nile.")
    score -= 1

print("\n7. Who wrote the national anthem of India, 'Jana Gana Mana'?")
print("A) Mahatma Gandhi \nB) Rabindranath Tagore \nC) Subhas Chandra Bose \nD) Jawaharlal Nehru")
ans = str(input("Enter Your Answer: ")).upper()
if ans == "B":
    print("Correct Answer.")
    score += 2
else:
    print("Incorrect Answer. Correct Answer is B) Rabindranath Tagore.")
    score -= 1

print("\n8. What is the chemical symbol for Gold?")
print("A) Au \nB) Ag \nC) Fe \nD) Pb")
ans = str(input("Enter Your Answer: ")).upper()
if ans == "A":
    print("Correct Answer.")
    score += 2
else:
    print("Incorrect Answer. Correct Answer is A) Au.")
    score -= 1

print("\n9. Which country hosted the 2024 Summer Olympics?")
print("A) Japan \nB) Brazil \nC) France \nD) China")
ans = str(input("Enter Your Answer: ")).upper()
if ans == "C":
    print("Correct Answer.")
    score += 2
else:
    print("Incorrect Answer. Correct Answer is C) France.")
    score -= 1

print("\n10. What is the smallest country in the world by land area?")
print("A) Monaco \nB) San Marino \nC) Liechtenstein \nD) Vatican City")
ans = str(input("Enter Your Answer: ")).upper()
if ans == "D":
    print("Correct Answer.")
    score += 2
else:
    print("Incorrect Answer. Correct Answer is D) Vatican City.")
    score -= 1

print("-"*40)
print("Your Quiz Completed Successfully.")
print(name,"Your Final Score is:",score)
print("Your Performance is:")
if score>=18:
    print("Excellent")
elif score>=12:
    print("Good")
elif score>=8:
    print("Average")
elif score>=4:
    print("Below Average")
else:
    print("Poor")