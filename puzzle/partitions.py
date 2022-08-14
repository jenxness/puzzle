import argparse
import sys
from functools import reduce
from itertools import combinations


def partition(target, size, pool):
    return [
        combination
        for combination in combinations(pool, size)
        if sum(combination) == target
    ]


def common(results):
    subset = reduce(lambda x, y: set(x) & set(y), results)
    return subset


def _parse_elements(data):
    result = []
    for element in data:
        try:
            result.append(int(element))
        except ValueError:
            if '..' in element:
                start, end = element.split('..')
                result += list(range(int(start), int(end) + 1))
            else:
                raise ValueError(f'{element} is not an integer or a range')

    return set(result)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Calculate which subsets of a pool of numbers sum up to a target sum.')

    parser.add_argument('target', type=int, help='target sum')
    parser.add_argument('size', type=int, help='subset size')
    parser.add_argument(
        '-p', '--pool',
        nargs='+',
        default=list(range(1, 10)),
        help='options pool (space separated integers or ranges "n..m"); if not provided, defaults to 1-9',
    )
    parser.add_argument(
        '-i', '--ignore',
        nargs='+',
        help='elements that must not be used (space-separated integers or ranges "n..m")'
    )

    args = parser.parse_args()

    pool = _parse_elements(args.pool)

    if args.ignore:
        pool -= _parse_elements(args.ignore)

    pool = sorted(pool)

    print(f'Attempting to find {args.size}-element subsets of {", ".join(map(str, pool))} that sum up to {args.target}...')

    solutions = partition(args.target, args.size, pool)

    if not solutions:
        print('No results.')
        sys.exit()
    elif len(solutions) == 1:
        print('1 result!')
    else:
        print(f'{len(solutions)} results!')

    for result in solutions:
        print(f'{" + ".join(map(str, result))} = {args.target}')

    if len(solutions) > 1:
        subset = common(solutions)
        if subset:
            print(f'Elements present in each solution: {", ".join(map(str, subset))}.')
