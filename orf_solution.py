def find_all_starts(dna):
    starts = []
    for i in range(len(dna)):
        if dna[i: i+3] == "ATG":
            starts.append(i)
    return starts

def find_first_in_register_stop(dna):
    for i in range(0, len(dna), 3):
        if dna[i:i+3] in ["TGA", "TAG", "TAA"]:
            return i+3
    return -1

def all_orfs_range(dna):
    starts = find_all_starts(dna)
    orfs_ranges = []
    for start in starts:
        end = find_first_in_register_stop(dna[start:])
        if end != -1:
            orfs_ranges.append((start, start+end))
    return orfs_ranges

def longest_orf(dna):
    longest = ""
    for orf_range in all_orfs_range(dna.upper()):
        orf = dna[orf_range[0]: orf_range[1]]
        if len(orf) > len(longest):
            longest = orf
    return longest
