# Genomic Sequence Analysis

This Python project reads DNA sequences from FASTA files,
computes GC content and sequence length, stores results in a SQLite database,
and visualizes the data with a scatter plot.

## Features

- FASTA file parsing
- GC content calculation (biologically meaningful metric)
- SQLite database storage
- Matplotlib visualization (length vs GC content)

## How to Run

1. Place your `.fasta` file inside the `data/` folder.
2. Run:
   ```bash
   python src/fasta_parser.py
3.Check the console output, database, and the scatter plot.
## File Structure
genomic-sequence-analysis/
│── data/
│   └── sequences.fasta
│── src/
│   ├── fasta_parser.py
│   └── metrics.py
└── sequences.db
