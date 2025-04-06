MAX_FIB_LIMIT = 1200

def generate_fibonacci():
    first_term = 0  # Starting term of Fibonacci sequence
    second_term = 1  # Second term of Fibonacci sequence

    print("Fibonacci Sequence (up to", MAX_FIB_LIMIT, "):")

    while first_term <= MAX_FIB_LIMIT:
        print(first_term, end=" ")

        next_term_in_sequence = first_term + second_term
        first_term = second_term
        second_term = next_term_in_sequence

if __name__ == "__main__":
    generate_fibonacci()
