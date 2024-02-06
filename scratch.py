# Entry point for the command line search
import sys

from searcheng import searcheng
from utils import utils


def main():
    args = sys.argv
    if len(args) < 2:
        raise Exception("arg string to search not found")
    to_search = utils.sanitize(args[1])
    matching_results = searcheng.search(to_search)
    return matching_results


if __name__ == "__main__":
    print('Scratch - Command Line Web Search Engine')
    main()

