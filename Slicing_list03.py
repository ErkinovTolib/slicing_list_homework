def main(list1):
    """
    A list of several elements is given. Return this list by adding the reverse.
    Args:
        list1(list): parameter
    Returns:
        list: return answer.
    """
    list = list1 + list1[::-1]
    return list
print(main([1,12,3,9,5,9]))