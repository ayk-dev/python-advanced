import logging

logging.basicConfig(filename='demo-log.log', level=logging.DEBUG)


def fibonacci(n):
    if n == 0:
        logging.debug('Calculating of 0, this is 0')
        return 0
    if n == 1:
        logging.debug('Calculating of 1, this is 1')
        return 1
    prev_fibonacci = fibonacci(n - 1)
    logging.debug(f'prev_fibonacci = {prev_fibonacci}')
    two_prev_fibonacci = fibonacci(n - 2)
    logging.debug(f'two_prev_fibonacci = {two_prev_fibonacci}')

    return prev_fibonacci + two_prev_fibonacci


n = int(input())
fibonacci(n)