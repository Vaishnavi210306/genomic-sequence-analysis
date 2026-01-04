def gc_content(sequence):
    g = sequence.count("G")
    c = sequence.count("C")
    total = len(sequence)

    if total == 0:
        return 0

    return (g + c) / total * 100
