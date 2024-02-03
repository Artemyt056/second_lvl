def check_brackets(expression):
    """
    In this example, the check_brackets function takes
    a string and returns True if all the brackets in the string conform to the rules of the
    Python language, and False otherwise

    :accepted:str
    :return: True or False
    """
    stack = []
    bracket_pairs = {'{': '}', '[': ']', '(': ')'}

    for char in expression:
        if char in bracket_pairs.keys():
            stack.append(char)
        elif char in bracket_pairs.values():
            if not stack or bracket_pairs[stack.pop()] != char:
                return False

    return not stack


def main():
    string1 = "{}{}{}()()()[({})]"
    string2 = "{[}{}{}()(])()[(}}"

    result1 = check_brackets(string1)
    result2 = check_brackets(string2)

    print(f"For string '{string1}': {result1}")
    print(f"For string '{string2}': {result2}")


if __name__ == "__main__":
    main()
