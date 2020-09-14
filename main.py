import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--no_fizz',    action="store_true")
    parser.add_argument('--no_buzz',    action="store_true")
    parser.add_argument('--no_bang',    action="store_true")
    parser.add_argument('--no_bong',    action="store_true")
    parser.add_argument('--no_fezz',    action="store_true")
    parser.add_argument('--no_reverse', action="store_true")
    args = parser.parse_args()

    lower = 1
    upper = int(input("Enter a maximum number: "))

    for i in range(lower, upper+1):
        fizz = i % 3 == 0
        buzz = i % 5 == 0
        bang = i % 7 == 0
        bong = i % 11 == 0
        fezz = i % 13 == 0
        reverse = i % 17 == 0
        output = []

        if (not args.no_bong) and bong:
            if (not args.no_fezz) and fezz:
                output.append("Fezz")
            output.append("Bong")
        else:
            if (not args.no_fizz) and fizz:
                output.append("Fizz")
            if (not args.no_fezz) and fezz:
                output.append("Fezz")
            if (not args.no_buzz) and buzz:
                output.append("Buzz")
            if (not args.no_bang) and bang:
                output.append("Bang")

        if (not args.no_reverse) and reverse:
            output.reverse()

        if len(output) > 0:
            print(''.join(output))
        else:
            print(i)


if __name__ == "__main__":
    main()
