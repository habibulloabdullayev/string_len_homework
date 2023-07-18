def main(s):
    """
    A string variable s is given. Return the "*" sign that is equal to the length of this variable.
    Args:
        s: string
    Returns:
        string
    """
    s1 = s
    n =len(s1)
    return n*('*')
print(main('code'))