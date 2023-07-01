def read_records(file_path):
    records = []
    with open('records.txt', 'r') as file:
        header = file.readline().strip().split(', ')
        for line in file:
            first_name, last_name, age, sex, stream = line.strip().split(', ')
            records.append({
                header[0]: first_name,
                header[1]: last_name,
                header[2]: int(age),
                header[3]: sex,
                header[4]: stream
            })
    return records


def display_records(records):
    for record in records:
        print(", ".join(f"{key}: {value}" for key, value in record.items()))
    print()


def sort_records(records, sort_option):
    ascending = True
    if sort_option.startswith('-'):
        ascending = False
        sort_option = sort_option[1:]  # Remove the leading hyphen

    return sorted(records, key=lambda x: x[sort_option], reverse=not ascending)


def main():
    file_path = 'records.txt'
    records = read_records(file_path)

    while True:
        print("Menu:")
        print("1. Sort order")

        choice = input("Enter your choice: ")

        if choice == '1':
            print("Sort options:")
            print("1. First Name")
            print("2. Last Name")
            print("3. Age")
            print("4. Sex")
            print("5. Stream")

            sort_choice = input("Enter your sort choice (1, 2, 3, 4, 5): ")
            ascending = input("Enter sort order (A for ascending, D for descending): ").upper()

            sort_option = {
                '1': 'First Name',
                '2': 'Last Name',
                '3': 'Age',
                '4': 'Sex',
                '5': 'Stream'
            }.get(sort_choice)

            if sort_option:
                if ascending == 'D':
                    sort_option = '-' + sort_option
                sorted_records = sort_records(records, sort_option)
                display_records(sorted_records)


if __name__ == "__main__":
    main()