def square_filter(start, end):
    squares = [n * n for n in range(start, end + 1)]

    even_squares = [s for s in squares if s % 2 == 0]
    odd_squares = [s for s in squares if s % 2 != 0]

    print("All squares:", squares)
    print("Even squares:", even_squares)
    print("Odd squares:", odd_squares)