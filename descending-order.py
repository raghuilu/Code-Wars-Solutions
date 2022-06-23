def descending_order(num):
    # Bust a move right here
    return int("".join(sorted([num for num in str(num)], reverse=True)))