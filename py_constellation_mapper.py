def constellation_mapper(stars: list[tuple[int, int]], dim: int) -> list[str]:
    output = [["." for _ in dim] for _ in dim]
    for row, col in stars:
        if (0 <= row < dim) and (0 <= col < dim):
            output[row][col] = "*"
    return output


print(constellation_mapper([(0, 0), (5, 5)], 3))
