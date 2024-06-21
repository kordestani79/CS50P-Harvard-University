def main():
    user_answer = input("What is the answer to the Great Question of Life, the Universe, and Everything? ")
    if user_answer.strip().lower() in ["42", "forty-two", "forty two"]:
        print("Yes")
    else:
        print("No")

main()
