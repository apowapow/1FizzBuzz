def main():
    lower = 1
    max_upper = 1000000
    upper = int(input("Enter a maximum number [1-{0}]: ".format(max_upper)))

    if lower <= upper <= max_upper:
        for i in range(lower, upper+1):
            fizz = i % 3 == 0
            buzz = i % 5 == 0
            bang = i % 7 == 0
            bong = i % 11 == 0
            fezz = i % 13 == 0
            reverse = i % 17 == 0
            output = []

            if bong:
                if fezz:
                    output.append("Fezz")
                output.append("Bong")
            else:
                if fizz:
                    output.append("Fizz")
                if fezz:
                    output.append("Fezz")
                if buzz:
                    output.append("Buzz")
                if bang:
                    output.append("Bang")

            if reverse:
                output.reverse()

            if len(output) > 0:
                print(''.join(output))


if __name__ == "__main__":
    main()
