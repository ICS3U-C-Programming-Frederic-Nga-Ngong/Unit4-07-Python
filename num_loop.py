#!/usr/bin/env python3
# Created By: Fred
# Date: Feb 18 2008.
# Display numbers form 1000 to 2000, 5 per line.


def main():
    for counter in range(1000, 2001):
        print("{}".format(counter), end=" ")
        if (counter + 1) % 5 == 0:
            print("")


if __name__ == "__main__":

    main()
