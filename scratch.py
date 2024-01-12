# Entry point for the command line search
import sys

from searcheng import searcheng
from utils import utils


def main():
    args = sys.argv
    if len(args) < 2:
        raise Exception("arg containing string to search not found")
    to_search = args[1]
    if type(to_search) != str:
        raise TypeError("arg to search needs to be a string")
    to_search = utils.sanitize(to_search)
    matching_results = searcheng.search(to_search)
    return matching_results


if __name__ == "__main__":
    print('Scratch - Command Line Web Search Engine')
    main()

