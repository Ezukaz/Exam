def array_rotation_detector(arr1: list, arr2: list) -> bool:
    arr_len = len(arr1)
    if arr_len != len(arr2):
        return False
    i = 0
    doub = arr2 + arr2
    for _ in range(arr_len):
        if arr1 == doub[i:i + arr_len]:
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
