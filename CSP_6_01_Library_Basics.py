
#Please modify the below functions so they fulfill the described process.
#You must use a function from analytics.py in each question to receive credit.
#There is no provided test file. You must make and submit one yourself. (check older test files for reference)


# Modify the below function such that it takes in a list of prices and returns that list with 15% added value
def process_expenses(rawPrices):
    updated_prices = []
    for price in rawPrices:
        new_price = analytics.apply_markup(price, 0.15)
        updated_prices.append(new_price)
    return updated_prices


# Modify the below function such that it asks the user for n scores and then returns the highest score and the average score of the list.
def analyze_scores(n):
    scores = []
    for i in range(n):
        score = float(input("Enter score: "))
        scores.append(score)

    highest = analytics.get_highest(scores)
    average = analytics.get_average(scores)

    return highest, average


# Modify the below function such that it takes in a list of strings and returns that list with all spaces removed
#and all letters lower case.
def sanitize_usernames(usernames):
    return analytics.clean_text(usernames)


# Modify the list such that it takes in a list as an argument and returns a version of the list with all values over 100.
def identify_outliers(values):
    return analytics.filter_threshold(values, 100)


# Modify the below function such that it takes in a list of items and asks the user for an item to search for.
#Sanitize the list to only be lower case worsd with no extra spaces
#Then return the location of the word using binary search if the list is in order and linear search if it is not.
#example items = ["  Apple", "Banana ", "  CHERRY  ", " date "]
def search_and_report(items):
    cleaned = analytics.clean_text(items)

    target = input("Enter item to search for: ").strip().lower()

    if cleaned == sorted(cleaned):
        low = 0
        high = len(cleaned) - 1

        while low <= high:
            mid = (low + high) // 2

            if cleaned[mid] == target:
                return mid
            elif cleaned[mid] < target:
                low = mid + 1
            else:
                high = mid - 1

        return -1
    else:
        for i in range(len(cleaned)):
            if cleaned[i] == target:
                return i
        return -1
