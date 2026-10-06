def list_intersection_finder(lists: list[list[int]]) -> list[int]:
    output = []
    if lists:
        combine = set(lists[0])
        for i, l in enumerate(lists):
            if not l:
                return []
            if i == 0:
                continue
            combine &= set(l)
        output = sorted(list(combine))
    return output


def list_intersection_finder2(lists: list[list[int]]) -> list[int]:
    if not lists:
        return []
    return sorted(set(lists[0]).intersection(*lists[1:]))
