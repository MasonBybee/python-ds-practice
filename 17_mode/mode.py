def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of times.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """
    num_count = {}
    for num in nums:
        num_count[num] = num_count.get(num, 0) + 1

    most_common = None
    most_occurrences = max(num_count.values())
    for num, count in num_count.items():
        if count == most_occurrences:
            most_common = num
            break

    return most_common