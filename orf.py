def find_all_starts(dna):
  starts = []
  while "ATG" in dna:
    starts.append(dna.find("ATG"))
    dna = dna.replace("ATG", "atg",1)
  return starts

def find_first_in_register_stop(dna):
 for index in range(0,len(dna),3):
  if dna[index:index+3] in ["TGA", "TAG", "TAA"]:
    return index + 3
 return -1

def all_orfs_range(dna):
    starts = find_all_starts(dna)
    orfs_ranges = []

    for start in starts:
        # Slice the DNA sequence from the current start
        sliced_dna = dna[start:]

        # Find the first stop codon in the sliced DNA
        end_relative_to_sliced = find_first_in_register_stop(sliced_dna)

        # If a stop codon is found, calculate the real end position and add the ORF range
        if end_relative_to_sliced != -1:
            end = start + end_relative_to_sliced
            
            # Validate ORF length: The total number of bases (between the beginning and ending codons)
            # must be a multiple of 3. This means (end - start) must be a multiple of 3 and >= 6 (ATG + stop).
            if (end - start) % 3 == 0 and (end - start) >= 6:
                orfs_ranges.append((start, end))

    return orfs_ranges

def longest_orf(dna):
    """
    Finds the DNA sequence of the longest Open Reading Frame (ORF) 
    in a given DNA sequence. Requires the function all_orfs_range.
    """
    # 1. Get ORF Ranges: A list of (start, end) tuples.
    orf_ranges = all_orfs_range(dna)
    
    # 2. Initialize Longest ORF: Start with an empty string.
    longest = ""
    
    # 3. Iterate Over ORFs:
    for start, end in orf_ranges:
        # Slice the DNA sequence to get the current ORF string.
        current_orf = dna[start:end]
        
        # 4. Update Longest ORF:
        # Check if the current ORF is strictly longer than the stored longest ORF.
        if len(current_orf) > len(longest):
            longest = current_orf
            
    # 5. Return the Longest ORF DNA sequence.
    return longest



