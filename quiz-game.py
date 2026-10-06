Questions = (("How many elements are in periodic table? :"),
             ("Which animal lays largest eggs? :"),
             ("What is the Most abundant gas in Earth's atmosphere? :" ),
             ("How many bones are in human body? :"),
             ("Which planet in solar system is the hottest? : "),
             ("What is symbol of Gold in periodic table? ;"))


options = (("A. 116","B. 117","C. 118","D. 119"),
           ("A. Whale","B. Crocodile","C. Elephant","D. Ostrich"),
           ("A. Hydrogen","B. Helium","C. Nitrogen","D. Oxygen"),
           ("A. 206","B. 207","C. 208","D. 209"),
           ("A. Mercury","B. Venus","C. Mars","D. Earth"),
           ("A. Ag","B. Au","C. Go","D. He"))


answers = ("C","D","C","A","B","B")
guesses = []
score = 0
question_num = 0

for question in Questions:
    print(question)
    print("_ _ _ _ _ _ _ _ _ _ _ _ _")
    for option in options[question_num]:
        print(option)
    

    guess = input("Enter (A,B,C,D) : ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score +=1
        print("CORRECT!")
    else:
        print("INCORRECT!")
        print(f"{answers[question_num]} is correct answer")

    question_num+=1


print("_ _ _ _ _ _ _ _ _ _ _")
print("      RESULTS        ")
print("_ _ _ _ _ _ _ _ _ _ _")

print("answers:" , end = "")
for answer in answers:
    print(answer , end = "")
print()

print("guesses:" , end = "")
for guess in guesses:
    print(guess , end = "")
print()
