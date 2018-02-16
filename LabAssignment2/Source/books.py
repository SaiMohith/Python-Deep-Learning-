#  This program is to print all the available books in the given range by the user


def list_books(start, end):
    books = {"Python": 50, "Java": 40, "Hadoop": 90, "Pig": 100, "C++": 20, "MachineLearning": 90, "DeepLearning": 150}
    books_list = []
    if low < 0 or high < 0:
        print("I know you're trying to trick me. Please enter the values again.")
    else:
        for key in books:
            if books[key] in range(start, end+1):
                books_list.append(key)
    print("\n Books Available in your range: ", books_list)


low = int(input("\n Please enter the lower value of the range: "))
high = int(input("\n Please enter the high value of the range: "))
list_books(low, high)
