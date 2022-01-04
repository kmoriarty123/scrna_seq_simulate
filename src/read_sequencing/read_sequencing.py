"""Read Sequencing.

Simulate the sequencing of reads on the template of terminal fragments and simulates reads of these fragments.
"""
# Imports from built-in modules
from random import choices
from pathlib import Path
from typing import List


def read_sequencing(
    frag_file_name: Path,
    output_file_name: Path = Path.cwd() / 'output_reads.txt',
    num_reads: int = 1000,
    read_len: int = 80,
) -> None:
    """Reads a fasta-formatted file of terminal fragments and simulates reads.

    Simulate the sequencing of reads on the template of terminal
    fragments. Reads are copies of fixed length starting
    from the 5' end of fragments. If the desired read length
    is larger than the fragment length, sequencing would in
    principle proceed into the 3' adaptor and then would perhaps
    yield random bases. For simplicity, here we assume that random
    nucleotides are introduced in this case. Saves a fasta-formatted
    file of reads of identical length, representing 5’
    ends of the terminal fragments as .txt.

    Args:
        frag_file_name: input file path of terminal fragments
        output_file_name: output file path where to store the output
        num_reads: number of total reads to simulate
        read_len: integer of identical read length
    """
    # Read data from terminal fragment file
    # Store fragment descriptions in a list
    frag_desc = []  # type: List[str]

    with open(frag_file_name, 'r') as f:
        for frag_line in f:
            # Store all fragments as a list to parse later
            frag_list = []  # type: List[str]
            # Store combined fragment lines
            frag_str = ""
            while frag_line != "":
                # To stop when the end of file is reached
                if frag_line.startswith('>'):
                    # Determine if this is the first fragment in the file
                    # Ignore the description line (starting with >) of the first fragment
                    if not (len(frag_list) == 0 and frag_str == ""):
                        # Not the first fragment. Append to list.
                        frag_list.append(frag_str)
                    frag_str = ""
                    # Store description line for output file
                    frag_desc.append(frag_line)
                else:
                    frag_str = frag_str + frag_line.rstrip("\n")
                # Read next line
                frag_line = f.readline()
            frag_list.append(frag_str)

    # Store list of random nucleotides from which to sample when read length is too short
    nucleotides = ['A', 'C', 'G', 'T']

    # Calculate sum of all lengths to determine the relative abundance for that fragment
    sum_frags = sum(map(len, frag_list))

    # Open the file to save the reads
    with open(output_file_name, 'w') as fw:

        # Loop through fasta fragments that start with 5'
        for frag in frag_list:
            # Determine number of reads to create from this fragment
            # This might not always provide an exact number of reads that were asked
            # TODO resolve this issue
            num_frag_reads = round((len(frag)/sum_frags) * num_reads)

            for i in range(0, num_frag_reads):
                # If the read length is less than the required length given by the parameter,
                # then add random nucleotides
                if len(frag) < read_len:

                    # Calculate number of random nucleotides to add to the end of the read
                    diff = read_len - len(frag)

                    # Select random nucleotides from list of possible
                    rand_samp = choices(nucleotides, k=diff)

                    # Add the random list to the read and save
                    tmp_read = frag[0:len(frag)] + ''.join(rand_samp)
                else:
                    # Save subset of fragment as read
                    tmp_read = frag[0:read_len]

                # Write read to file and original fragment description
                fw.write(frag_desc[frag_list.index(frag)])
                fw.write(tmp_read + "\n\n")
