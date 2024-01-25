#!/usr/bin/env python3
"""Module for  log parsing.
"""

import sys
import signal


def print_stats(total_size, status_codes):
    """Prints the file size and the count of each status code."""
    print("File size: {}".format(total_size))
    for code in sorted(status_codes.keys()):
        print("{}: {}".format(code, status_codes[code]))


def parse_line(line, total_size, status_codes):
    """Parses a log line, updates total size and status code count."""
    try:
        parts = line.split()
        file_size = int(parts[-1])
        status_code = int(parts[-2])

        total_size += file_size
        status_codes[status_code] = status_codes.get(status_code, 0) + 1

        return total_size, status_codes
    except (ValueError, IndexError):
        return total_size, status_codes


def main():
    """Main function that reads input, processes lines, and prints stats."""
    total_size = 0
    status_codes = {}

    try:
        for i, line in enumerate(sys.stdin, start=1):
            total_size, status_codes = parse_line(line.strip(),
                                                  total_size, status_codes)

            if i % 10 == 0:
                print_stats(total_size, status_codes)

    except KeyboardInterrupt:
        print_stats(total_size, status_codes)
        sys.exit(0)


if __name__ == "__main__":
    """Entry point of the script."""
    signal.signal(signal.SIGINT, lambda x, y: sys.exit(0))
    main()
