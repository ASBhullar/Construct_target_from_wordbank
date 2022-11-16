import os
import time


def construct_target(target_file, word_bank_file):
    target = open(os.path.dirname(os.getcwd()) + target_file).read()
    print(target)
    word_bank = []
    for line in open(os.path.dirname(os.getcwd()) + word_bank_file).readlines():
        word_bank.append(line.strip())
    print(word_bank)
    begin_time = time.time()
    combinations = []

    for i in range(len(target)):
        combinations.append([])

    if target[0:1] in word_bank:
        combinations[0].append(target[0: 1])

    for i in range(len(target)):
        if target[0: i + 1] in word_bank:
            combinations[i].append(target[0: i + 1])

        for j in range(i):
            if target[j + 1: i + 1] in word_bank:
                val = 1
            else:
                val = 0
            if val * len(combinations[j]) > 0:
                for combination in combinations[j]:
                    combinations[i].append(combination + " " + target[j + 1: i + 1])

    results = construct_unique_lists(combinations[len(target) - 1])
    print_results(results, begin_time)


def construct_unique_lists(combinations: list) -> list:
    results = []
    unique_combinations = set(combinations)
    for unique_combination in unique_combinations:
        results.append(unique_combination.split())
    return results


def print_results(results: list, begin_time: float):
    end_time = time.time()
    print("Number of ways: " + str(len(results)))
    print('[')
    for result in results:
        print("\t" + str(result))
    print(']')
    print("Runtime: " + str((end_time - begin_time) * 10**3) + " milliseconds")
