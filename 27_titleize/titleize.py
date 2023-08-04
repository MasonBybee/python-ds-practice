def titleize(phrase):
    """Return phrase in title case (each word capitalized).

        >>> titleize('this is awesome')
        'This Is Awesome'

        >>> titleize('oNLy cAPITALIZe fIRSt')
        'Only Capitalize First'
    """
    words = phrase.lower().split()
    for i in range(len(words)):
        words[i] = words[i].capitalize()
    return ' '.join(words)

    # built in method for future use phrase.title()