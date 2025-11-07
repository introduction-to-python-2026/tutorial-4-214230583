# DNA Sequence Analysis Toolkit

This toolkit provides a series of functions for analyzing DNA sequences to identify codon patterns, open reading frames (ORFs), and the longest ORF within a sequence.

## Overview

The project is divided into the following steps:

1. **Finding all start codons**: Locate all occurrences of the `ATG` start codon.
2. **Finding in-register stop codons**: Identify the first stop codon (`TGA`, `TAG`, or `TAA`) in-frame.
3. **Identifying all ORFs**: Determine the ranges of all open reading frames in the sequence.
4. **Finding the longest ORF**: Extract the longest open reading frame from the sequence.

---

## Steps and Implementation Details

### Step 1: Implementing the `find_all_starts` Function
This function scans a DNA sequence and identifies all starting positions of the `ATG` codon.

### Step 2: Implementing the `find_first_in_register_stop` Function
You will write a function called find_first_in_register_stop that scans a DNA sequence and identifies the first occurrence of a stop codon (`TGA`, `TAG`, or `TAA`) in the register (every 3 nucleotides). If the stop codon is not found, the function will return -1.

### Step 3: Implementing the `all_orfs_range` Function
You will implement a function called all_orfs_range that scans a DNA sequence and identifies all open reading frames (ORFs) by finding the start codons (`ATG`) and the corresponding stop codons (`TGA`, `TAG`, `TAA`), and returns the range of each ORF.

### Step 4: Implementing the `longest_orf` Function
You will implement a function called longest_orf that scans a DNA sequence, finds all open reading frames (ORFs), and returns the longest ORF from the sequence.
