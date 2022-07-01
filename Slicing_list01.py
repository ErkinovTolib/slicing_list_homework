def main(numbers):
    """
    A list called numbers is given. Return the items in the odd index.
    Args:
        numbers(list): parameter
    Returns:
        list: return answer.
    """

    return numbers[0::2]
print(main([1,12,3,9,5,9]))