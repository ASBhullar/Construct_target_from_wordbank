import os
import time


# This python file contains the code to find all unique ways to construct target from given word-bank.
# Each test case file is a python file which will call construct_target.
# Hence, no main function is required in this file.

def construct_target(target_file, word_bank_file):
    # Store the start time of the program
    begin_time = time.time()

    # Read the target word from the target file
    target = open(os.path.dirname(os.getcwd()) + target_file).read()

    # Read all the words from word bank file and store them by splitting the contents of file using space as delimiter
    word_bank = open(os.path.dirname(os.getcwd()) + word_bank_file).read().split()

    # Using tabulation to solve this DP problem.
    # The size of this list will be equal to all possible suffixes of the target i.e. the length of the target
    combinations = []

    for i in range(len(target)):
        combinations.append([])

    if target[0:1] in word_bank:
        combinations[0].append(target[0: 1])

    # Iterate from index 1 to the size of the target word in the dp list.
    for i in range(1, len(target)):

        # If exact suffix is present in word-bank, add this as a possibility to the list of strings at this index
        if target[0: i + 1] in word_bank:
            combinations[i].append(target[0: i + 1])

        # Check through all combinations of words i.e. substrings from 0th index through i + 1 th index
        for j in range(i):
            if target[j + 1: i + 1] in word_bank:
                val = 1
            else:
                val = 0
            if val * len(combinations[j]) > 0:
                for combination in combinations[j]:
                    combinations[i].append(combination + " " + target[j + 1: i + 1])

    if len(target) >= 1:
        # Process the list of all possible combinations to ensure we only pick unique combinations.
        results = construct_unique_lists(combinations[len(target) - 1])
    else:
        results = []
    # Print results in the format given in the assignment and pass the begin time to calculate the total execution time.
    print_results(results, begin_time)


# Returns all possible unique combinations of target from the list of strings provided by construct_target
def construct_unique_lists(combinations: list) -> list:
    results = []
    # Convert the list into set to ensure we only have unique strings.
    unique_combinations = set(combinations)
    for unique_combination in unique_combinations:
        # Store the results in a list format as required by assignment instead of space separated strings.
        results.append(unique_combination.split())
    return results


# Calculate the total execution time of the program and print the results in the required format
def print_results(results: list, begin_time: float):
    end_time = time.time()
    print("Number of ways: " + str(len(results)))
    print('[')
    for result in results:
        print("\t" + str(result))
    print(']')
    print("Runtime: " + str((end_time - begin_time)) + " seconds")
