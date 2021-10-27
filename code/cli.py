import argparse
import transcript_sampler.py as transcript

parser = argparse.ArgumentParser(description='Sample Transcripts')
parser.add_argument('integer', metavar='N', type=int,
                    help='number to sample')
parser.add_argument('file_name', metavar='N', type=str,
                    help='source file name')
parser.add_argument('file_name', metavar='N', type=str,
                    help='dest file name')

if __name__ == '__main__':


    args = parser.parse_args()
    print(args.accumulate(args.integers))