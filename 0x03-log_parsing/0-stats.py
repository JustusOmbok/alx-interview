#!/usr/bin/python3
'''HTTP Request Log Parser
'''
import re


def extract_request_info(log_line):
    '''Extracts information from a line of an HTTP request log.'''
    pattern = (
        r'\s*(?P<ip>\S+)\s*',
        r'\s*\[(?P<date>\d+\-\d+\-\d+ \d+:\d+:\d+\.\d+)\]',
        r'\s*"(?P<request>[^"]*)"\s*',
        r'\s*(?P<status_code>\S+)',
        r'\s*(?P<file_size>\d+)'
    )
    info = {
        'status_code': 0,
        'file_size': 0,
    }
    log_format = '{}\\-{}{}{}{}\\s*'.format(pattern[0], pattern[1], pattern[2], pattern[3], pattern[4])
    match_result = re.fullmatch(log_format, log_line)
    if match_result is not None:
        status_code = match_result.group('status_code')
        file_size = int(match_result.group('file_size'))
        info['status_code'] = status_code
        info['file_size'] = file_size
    return info


def print_log_statistics(total_size, status_code_stats):
    '''Prints accumulated statistics from an HTTP request log.'''
    print('Total file size: {:d}'.format(total_size), flush=True)
    for status_code in sorted(status_code_stats.keys()):
        num = status_code_stats.get(status_code, 0)
        if num > 0:
            print('{:s}: {:d}'.format(status_code, num), flush=True)


def update_metrics(log_line, total_size, status_code_stats):
    '''Updates metrics using a line from an HTTP request log.

    Args:
        log_line (str): Line from the log containing the metrics.

    Returns:
        int: The new total file size.
    '''
    line_info = extract_request_info(log_line)
    status_code = line_info.get('status_code', '0')
    if status_code in status_code_stats.keys():
        status_code_stats[status_code] += 1
    return total_size + line_info['file_size']


def run_log_parser():
    '''Runs the HTTP request log parser.'''
    line_number = 0
    total_file_size = 0
    status_code_stats = {
        '200': 0,
        '301': 0,
        '400': 0,
        '401': 0,
        '403': 0,
        '404': 0,
        '405': 0,
        '500': 0,
    }
    try:
        while True:
            log_line = input()
            total_file_size = update_metrics(
                log_line,
                total_file_size,
                status_code_stats,
            )
            line_number += 1
            if line_number % 10 == 0:
                print_log_statistics(total_file_size, status_code_stats)
    except (KeyboardInterrupt, EOFError):
        print_log_statistics(total_file_size, status_code_stats)


if __name__ == '__main__':
    run_log_parser()
