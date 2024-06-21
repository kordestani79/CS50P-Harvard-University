def main():
    months = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ]

    while True:
        user_input = input("Enter a date (MM/DD/YYYY or Month Day, Year): ").strip()

        # Check if the input contains '/' or ','
        if '/' not in user_input and ',' not in user_input:
            print("Invalid date format. Please try again.")
            continue

        try:
            # Try to parse the date in the format MM/DD/YYYY
            month, day, year = user_input.split("/")
            month = int(month)
            day = int(day)
            year = int(year)

            if 1 <= month <= 12 and 1 <= day <= 31 and 0 <= year <= 9999:
                print(f"{year:04d}-{month:02d}-{day:02d}")
                break

        except ValueError:
            pass

        try:
            # Try to parse the date in the format Month Day, Year
            month_str, day_str, year_str = user_input.split(" ")
            month = months.index(month_str.capitalize()) + 1
            day = int(day_str.strip(","))
            year = int(year_str)

            if 1 <= month <= 12 and 1 <= day <= 31 and 0 <= year <= 9999:
                print(f"{year:04d}-{month:02d}-{day:02d}")
                break

        except (ValueError, IndexError):
            pass

        print("Invalid date format. Please try again.")

if __name__ == "__main__":
    main()
