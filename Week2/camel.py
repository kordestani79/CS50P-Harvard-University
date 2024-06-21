def main():

    camel_case_name = input("camelCase: ")
    snake_case_name = ""

    for char in camel_case_name:
        if char.isupper() and snake_case_name:
            snake_case_name += "_"
        snake_case_name += char.lower()

    print("snake case: ", snake_case_name)

if __name__ == "__main__":
    main()
