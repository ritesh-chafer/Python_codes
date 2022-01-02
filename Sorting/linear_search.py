def find_index(value,items):
    for index, item in enumerate(items):
        if item == value:
            print(f"Item found at {index}")

fruits = ["apple", "banana", "gauva", "kiwi"]
find_index("apple",fruits)

