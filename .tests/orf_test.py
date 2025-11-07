
from orf import find_all_starts, find_first_in_register_stop, all_orfs_range, longest_orf

def test_find_all_starts():
    assert find_all_starts("") == list()
    assert find_all_starts("GGAGACGACGCAAAAC") == list()
    assert find_all_starts("AAAAAAATGAAATGAGGGGGGTATG") == [6, 11, 22]
    assert find_all_starts("GGATGATGATGTAAAAC") == [2, 5, 8]
    assert find_all_starts("GGATGCATGATGTAGAAC") == [2, 6, 9]
    assert find_all_starts("GGGATGATGATGGGATGGTGAGTAGGGTAAG") == [3, 6, 9, 14]
    assert find_all_starts("GGGatgatgatgGGatgGtgaGtagGGACtaaG".upper()) == [3, 6, 9, 14]

def test_find_first_in_register_stop():
    assert find_first_in_register_stop("") == -1
    assert find_first_in_register_stop("GTAATAGTGA") == -1
    assert find_first_in_register_stop("AAAAAAAAAAAAAAATAAGGGTAA") == 18
    assert find_first_in_register_stop("AAAAAACACCGCGTGTACTGA") == 21

def test_all_orfs():
    assert all_orfs_range("") == list()
    assert all_orfs_range("GGAGACGACGCAAAAC") == list()
    assert all_orfs_range("AAAAAAATGAAATGAGGGGGGTATG") == [(6, 15)]
    assert all_orfs_range("GGATGATGATGTAAAAC") == [(2, 14),(5, 14),(8,14)]
    assert all_orfs_range("GGATGCATGATGTAGAAC") == [(6, 15), (9, 15)]
    assert all_orfs_range("GGGATGATGATGGGATGGTGAGTAGGGTAAG") == [(3, 21),(6, 21), (9, 21)]
    assert all_orfs_range("GGGatgatgatgGGatgGtgaGtagGGACtaaG".upper()) == [(3, 21), (6, 21), (9, 21), (14, 32)]

def test_longest_orf():
    assert longest_orf("") == ""
    assert longest_orf("GGAGACGACGCAAAAC") == ""
    assert longest_orf("AAAAAAATGAAATGAGGGGGGTATG") == "ATGAAATGA"
    assert longest_orf("GGATGATGATGTAAAAC") == "ATGATGATGTAA"
    assert longest_orf("GGATGCATGATGTAGAAC") == "ATGATGTAG"
    assert longest_orf("GGGATGATGATGGGATGGTGAGTAGGGTAAG") == "ATGATGATGGGATGGTGA"
    assert longest_orf("GGGatgatgatgGGatgGtgaGtagGGACtaaG") in ["atgGtgaGtagGGACtaa","atgatgatgGGatgGtga"]
