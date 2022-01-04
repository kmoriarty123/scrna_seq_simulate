"""Command Line Interface."""

import argparse
from src.read_sequencing import read_sequencing


def parse_args() -> argparse.Namespace:
    """Parse CLI arguments.

    Returns: Parsed CLI arguments.
    """
    # initiate parser
    parser = argparse.ArgumentParser(description='Simulate the Sequencing of Reads')

    # add arguments
    parser.add_argument('--frag_file_name',
                        type=str,
                        help='input file name')

    parser.add_argument('--output_file_name',
                        type=str,
                        help='output file name')

    parser.add_argument('--num_reads',
                        type=int,
                        help='desired number of reads')

    parser.add_argument('--read_len',
                        type=int,
                        help='length of each read')

    return parser.parse_args()


def main() -> None:
    """Main function.

    Interprets the arguments from the commandline,
    Runs the functions read_sequencing.
    """
    args = parse_args()
    read_sequencing.read_sequencing(frag_file_name=args.frag_file_name,
                                    output_file_name=args.output_file_name,
                                    num_reads=args.num_reads,
                                    read_len=args.read_len)


if __name__ == '__main__':
    """Initiates main.
    Calls main function only if run from commandline, but not if imported.
    """
    main()
