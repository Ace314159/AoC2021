from collections import defaultdict
import itertools

with open("inputs/8.txt") as f:
    lines = list(map(lambda x: [nums.split(" ") for nums in x.strip().split(" | ")], f.readlines()))


def day_one():
    count = 0
    for signal, output in lines:
        for num in output:
            if len(num) in [2, 3, 4, 7]:
                count += 1
    return count


def day_two():
    mapping = {
        "abcefg": 0,
        "cf": 1,
        "acdeg": 2,
        "acdfg": 3,
        "bcdf": 4,
        "abdfg": 5,
        "abdefg": 6,
        "acf": 7,
        "abcdefg": 8,
        "abcdfg": 9,
    }
    counts = defaultdict(set)
    for string, num in mapping.items():
        counts[len(string)].update(set(string))

    def get_final_poss(poss):
        for final_poss in itertools.product(*poss):
            duplicates = set()
            for letter in final_poss:
                if letter in duplicates:
                    break
                duplicates.add(letter)
            if len(duplicates) != len(final_poss):
                continue
            yield final_poss

    def make_mapping(final_poss):
        letter_mapping = {}
        for i, letter in enumerate(final_poss):
            letter_mapping[letter] = chr(i + ord("a"))
        poss_mapping = {}
        for letters, num in mapping.items():
            poss_letters = "".join(sorted(list(map(lambda x: letter_mapping[x], letters))))
            poss_mapping[poss_letters] = num
        return poss_mapping

    ans = 0
    for signal, output in lines:
        poss = []
        for _ in range(len("abcdefg")):
            poss.append(set("abcdefg"))
        for num in signal + output:
            keep = counts[len(num)]
            for letter in num:
                poss[ord(letter) - ord("a")].intersection_update(keep)
            if len(poss) == 0:
                break

        for final_poss in get_final_poss(poss):
            poss_mapping = make_mapping(final_poss)
            good = True
            for num in signal + output:
                num = "".join(sorted(num))
                if num not in poss_mapping:
                    good = False
                    continue
            if good:
                break
        num_int = ""
        for num_str in output:
            num_str = "".join(sorted(num_str))
            num_int += str(poss_mapping[num_str])
        ans += int(num_int)

    return ans


print(day_one())
print(day_two())
