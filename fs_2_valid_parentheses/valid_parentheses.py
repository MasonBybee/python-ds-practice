def valid_parentheses(parens):
    """Are the parentheses validly balanced?

        >>> valid_parentheses("()")
        True

        >>> valid_parentheses("()()")
        True

        >>> valid_parentheses("(()())")
        True

        >>> valid_parentheses(")()")
        False

        >>> valid_parentheses("())")
        False

        >>> valid_parentheses("((())")
        False

        >>> valid_parentheses(")()(")
        False
    """
    paren_list = []
    for paren in parens:
        if paren == '(':
            paren_list.append(paren)
        elif paren == ')':
            if not paren_list:
                return False
            paren_list.pop()
    return not paren_list
        