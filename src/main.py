"""Main module to extract, transform and load data
"""
import extract
import transform

MIN_CONTROL_NUMBER = 1
MAX_CONTROL_NUMBER = 20000
SIZE = 1000

def main():
    extract.main()
    transform.main()


if __name__ == '__main__':
    main()