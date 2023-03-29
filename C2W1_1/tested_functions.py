def adder(*args):
    if len(args) < 2:
        raise ValueError("At least two arguments required")
    if any([type(x) != int for x in args]):
        raise TypeError("All arguments must be integers")
    return sum(args)


def divider(*args):
    if len(args) != 2:
        raise ValueError("Exactly two arguments required")
    if any([type(x) != int for x in args]):
        raise TypeError("All arguments must be integers")
    if args[1] == 0:
        raise ValueError("Division by zero not allowed")

    result = args[0]/args[1]
    if result.is_integer():
        return int(result)
    else:
        return result