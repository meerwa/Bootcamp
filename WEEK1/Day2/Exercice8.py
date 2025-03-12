def star_wars_quiz():

    data = [
        {"question": "What is Baby Yoda's real name?", "answer": "Grogu"},
        {"question": "Where did Obi-Wan take Luke after his birth?", "answer": "Tatooine"},
        {"question": "What year did the first Star Wars movie come out?", "answer": "1977"},
        {"question": "Who built C-3PO?", "answer": "Anakin Skywalker"},
        {"question": "Anakin Skywalker grew up to be who?", "answer": "Darth Vader"},
        {"question": "What species is Chewbacca?", "answer": "Wookiee"}
    ]
    
    correct_answers = 0
    incorrect_answers = 0
    wrong_answers = []

    print("\n Welcome to the Star Wars Quiz! \n")
    
    for item in data:
        user_answer = input(item["question"] + " ").strip()
        if user_answer.lower() == item["answer"].lower():
            print(" Correct!\n")
            correct_answers += 1
        else:
            print(" Incorrect!\n")
            incorrect_answers += 1
            wrong_answers.append({
                "question": item["question"],
                "your_answer": user_answer,
                "correct_answer": item["answer"]
            })

 
    print("\n Quiz Completed! ")
    print(f" Correct Answers: {correct_answers}")
    print(f" Incorrect Answers: {incorrect_answers}\n")

    if incorrect_answers > 0:
        print("Here are the questions you got wrong:")
        for wrong in wrong_answers:
            print(f" {wrong['question']}")
            print(f" Your Answer: {wrong['your_answer']}")
            print(f" Correct Answer: {wrong['correct_answer']}\n")

    if incorrect_answers > 3:
        play_again = input(" You got more than 3 wrong. Do you want to try again? (yes/no): ").strip().lower()
        if play_again == "yes":
            star_wars_quiz()
        else:
            print("Thanks for playing! May the Force be with you. ")


star_wars_quiz()
