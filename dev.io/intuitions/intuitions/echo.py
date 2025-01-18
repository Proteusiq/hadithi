def echo(thing: str) -> str:
    """Echo Me-o.

    Parroting function to reecho by substituting i with o

    Args:
        thing: Description of input argument.

    Returns:
        Description of return value
    """

    return "".join(letter if letter != 'i' else 'o' for letter in thing)
