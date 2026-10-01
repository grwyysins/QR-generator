def ask_question(question, options, answer):
    print("\n" + question)
    for key, value in options.items():
        print(f"{key}. {value}")
    return input("Your answer: ").strip().upper() == answer

def main():
    questions = [
        ("Which keyword defines a function?", {"A":"func", "B":"def", "C":"make"}, "B"),
        ("Which type stores key-value pairs?", {"A":"List", "B":"Tuple", "C":"Dictionary"}, "C"),
        ("Which symbol starts a comment?", {"A":"#", "B":"//", "C":"*"}, "A"),
    ]
    score = 0
    for q, options, answer in questions:
        if ask_question(q, options, answer):
            print("Correct!")
            score += 1
        else: print("Incorrect.")
    print(f"\nFinal score: {score}/{len(questions)}")

if __name__ == "__main__":
    main()
