from typing import List

from models.result import Result


def even(value: int) -> int:

    return int(value/2)


def odd(value: int) -> int:

    return int((3 * value) + 1)



def collatz_while(seed: int) -> List[Result]:
    res = []
    count = 0
    value = seed

    while True:

        if value == 4:
            break

        if value % 2 == 0:
            value = even(value)

        else:
            value = odd(value)

        result = Result(seed=seed, count=count, value=value)
        count += 1
        res.append(result)
        print(result)
    return res


def collatz(seed):
    # recursive
    pass



if __name__ == '__main__':
    collatz_while(100)