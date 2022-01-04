"""Test Issue 7."""

import pandas as pd
from src.read_sequencing import read_sequencing


def test_read_sequencing(tmpdir):
    """Tests the output, input file name and separator."""
    read_sequencing(
        frag_file_name='./tests/resources/test_terminal_fragments.txt',
        num_reads=80,
        read_len=10,
        num_seq_cyc=5,
        output_file_name=tmpdir / 'reads.txt'
    )
    df_out = pd.read_table(tmpdir / 'reads.txt', header=None)
    assert df_out.shape[0] == 80 * 5
