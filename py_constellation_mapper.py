def make_constellation(coord: list[tuple[int, int]], dimention: int) -> list[str]:
    output = ["." * dimention for _ in dimention]
    for y, x in coord:
        if x < dimention and y < dimention:
            output[y] = output[y][:x] + "*" + output[y][x + 1:]
    return output


print(make_constellation([(0, 0), (5, 5)], 3))
