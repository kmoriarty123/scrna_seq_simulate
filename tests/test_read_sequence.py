"""Test Functionality of Read Sequencing"""

# imports from built-in modules
from pathlib import Path

# imports from third-party modules
import pandas as pd

# imports from _this_ package
from src.read_sequencing import read_sequencing


def test_read_sequencing(tmpdir):
    """Tests the correct number of reads were generated and the correct length of reads."""
    read_sequencing.read_sequencing(
        frag_file_name=Path.cwd() / 'tests/resources/test_terminal_fragments.txt',
        num_reads=10,
        read_len=80,
        output_file_name=tmpdir / 'reads.txt'
    )
    df_out = pd.read_table(tmpdir / 'reads.txt', header=None)
    assert df_out.shape[0] == 10 * 2
    assert len(df_out.iloc[lambda x: x.index % 2 == 1, 0][1]) == 80
