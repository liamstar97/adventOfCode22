import heapq
import pandas as pd


def calorie_counting() -> list:
    max_elf_heap = []
    with open('data/day1') as file:
        elves = file.read().rsplit('\n\n')
        for i, elf in zip(range(len(elves)), elves):
            calories = map(int, elf.rsplit('\n'))
            heapq.heappush(max_elf_heap, (-sum(calories), i))
    return max_elf_heap


def sum_of_top_three_elves() -> int:
    max_elf_heap = calorie_counting()
    total_calories = 0
    for i in range(3):
        total_calories += heapq.heappop(max_elf_heap)[0] * -1
    return total_calories


if __name__ == '__main__':
    print(heapq.heappop(calorie_counting()))
    print(sum_of_top_three_elves())
