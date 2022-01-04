""" Read Sequencing

Former: random start
"""


def read_sequencing(frag_file_name, output_file_name, num_reads, read_len, num_seq_cyc):
    """Reads a fasta-formatted file of terminal fragments and simulates reads of these fragments.

    Simulate the sequencing of reads on the template of terminal
    fragments. Reads are copies of fixed length starting
    from the 5' end of fragments. If the desired read length
    is larger than the fragment length, sequencing would in
    principle proceed into the 3' adaptor and then would perhaps
    yield random bases. For simplicity, here we assume that random
    nucleotides are introduced in this case.

    :param output_file_name: file name where to store the output
    :param num_seq_cyc: integer of number of cycles
    :param read_len: integer of identical read length
    :param num_reads: number of total reads to simulate
    :param frag_file_name: input file of terminal fragments

    Output:
    Fasta-formatted file ("../output/reads.csv") of reads of identical length, representing 5’
    ends of the terminal fragments
    """

    # Import classes
    from random import choices, randrange
    import numpy as np

    # Read data from terminal fragment file
    # Store fragments in a list

    f = open(frag_file_name, "r")
    frag_line = f.readline()
    frag_list = []
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
        else:
            frag_str = frag_str + frag_line.rstrip("\n")
        frag_line = f.readline()
    frag_list.append(frag_str)
    # print(frag_list)
    f.close()

    # Initiate list to store reads from modified fragments
    fasta_list = list()

    # store list of random nucleotides from which to sample when read length is too short
    nucleotides = ['A', 'C', 'G', 'T']

    # Calculate sum of all lengths to determine the relative abundance for that fragment
    sum_frags = sum(map(len, frag_list))

    # Repeat the read process for given number of cycles
    for j in range(0, num_seq_cyc):

        # Loop through fasta fragments that start with 5'
        for frag in frag_list:

            # Determine number of reads to create from this fragment
            # This might not always provide an exact number of reads that were asked
            # TODO resolve this issue
            num_frag_reads = round((len(frag)/sum_frags) * num_reads)

            for i in range(0, num_frag_reads):

                # Obtain random first position for the read on the fragment
                rand_start = randrange(0, len(frag))

                # Calculate the difference of start position and length of read
                diff_start_end = len(frag)-rand_start

                # If length of read is greater than difference of start to end, then add random nucleotides
                if diff_start_end < read_len:

                    # Calculate number of random nucleotides to add to the end of the read
                    diff = read_len - diff_start_end

                    # Select random nucleotides from list of possible
                    rand_samp = choices(nucleotides, k=diff)

                    # Add the random list to the read and save
                    tmp_read = frag[rand_start:len(frag)] + ''.join(rand_samp)
                else:
                    # Save subset of fragment as read
                    tmp_read = frag[rand_start:(rand_start + read_len)]

                # append read to list
                fasta_list.append(tmp_read)

    # Save list to file
    np.savetxt(output_file_name,
               fasta_list,
               delimiter=",",
               fmt='%s')
