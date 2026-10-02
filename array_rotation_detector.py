def _count(a: list) -> int:
    count = 0
    for _ in a:
        count += 1
    return count


def array_rotation_detector(arr1: list, arr2: list) -> bool:
    if _count(arr1) != _count(arr2):
        return False
    i = 0
    for _ in arr1:
        if arr1 == arr2[i:] + arr2[:i]:
            return True
        i += 1
    return not arr1


def main() -> int:
    a = []
    b = []
    print(array_rotation_detector(a, b))
    return 0


if __name__ == "__main__":
    main()