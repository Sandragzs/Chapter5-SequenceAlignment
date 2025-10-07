BLOSUM62 = { #matrix for aa alignment
    'A': {'A': 4,  'C': 0,  'D': -2, 'E': -1, 'F': -2, 'G': 0,  'H': -2, 'I': -1, 'K': -1, 'L': -1, 'M': -1, 'N': -2, 'P': -1, 'Q': -1, 'R': -1, 'S': 1,  'T': 0,  'V': 0,  'W': -3, 'Y': -2},
    'C': {'A': 0,  'C': 9,  'D': -3, 'E': -4, 'F': -2, 'G': -3, 'H': -3, 'I': -1, 'K': -3, 'L': -1, 'M': -1, 'N': -3, 'P': -3, 'Q': -3, 'R': -3, 'S': -1, 'T': -1, 'V': -1, 'W': -2, 'Y': -2},
    'D': {'A': -2, 'C': -3, 'D': 6,  'E': 2,  'F': -3, 'G': -1, 'H': -1, 'I': -3, 'K': -1, 'L': -4, 'M': -3, 'N': 1,  'P': -1, 'Q': 0,  'R': -2, 'S': 0,  'T': -1, 'V': -3, 'W': -4, 'Y': -3},
    'E': {'A': -1, 'C': -4, 'D': 2,  'E': 5,  'F': -3, 'G': -2, 'H': 0,  'I': -3, 'K': 1,  'L': -3, 'M': -2, 'N': 0,  'P': -1, 'Q': 2,  'R': 0,  'S': 0,  'T': -1, 'V': -2, 'W': -3, 'Y': -2},
    'F': {'A': -2, 'C': -2, 'D': -3, 'E': -3, 'F': 6,  'G': -3, 'H': -1, 'I': 0,  'K': -3, 'L': 0,  'M': 0,  'N': -3, 'P': -4, 'Q': -3, 'R': -3, 'S': -2, 'T': -2, 'V': -1, 'W': 1,  'Y': 3},
    'G': {'A': 0,  'C': -3, 'D': -1, 'E': -2, 'F': -3, 'G': 6,  'H': -2, 'I': -4, 'K': -2, 'L': -4, 'M': -3, 'N': 0,  'P': -2, 'Q': -2, 'R': -2, 'S': 0,  'T': -2, 'V': -3, 'W': -2, 'Y': -3},
    'H': {'A': -2, 'C': -3, 'D': -1, 'E': 0,  'F': -1, 'G': -2, 'H': 8,  'I': -3, 'K': -1, 'L': -3, 'M': -2, 'N': 1,  'P': -2, 'Q': 0,  'R': 0,  'S': -1, 'T': -2, 'V': -3, 'W': -2, 'Y': 2},
    'I': {'A': -1, 'C': -1, 'D': -3, 'E': -3, 'F': 0,  'G': -4, 'H': -3, 'I': 4,  'K': -3, 'L': 2,  'M': 1,  'N': -3, 'P': -3, 'Q': -3, 'R': -3, 'S': -2, 'T': -1, 'V': 3,  'W': -3, 'Y': -1},
    'K': {'A': -1, 'C': -3, 'D': -1, 'E': 1,  'F': -3, 'G': -2, 'H': -1, 'I': -3, 'K': 5,  'L': -2, 'M': -1, 'N': 0,  'P': -1, 'Q': 1,  'R': 2,  'S': 0,  'T': -1, 'V': -2, 'W': -3, 'Y': -2},
    'L': {'A': -1, 'C': -1, 'D': -4, 'E': -3, 'F': 0,  'G': -4, 'H': -3, 'I': 2,  'K': -2, 'L': 4,  'M': 2,  'N': -3, 'P': -3, 'Q': -2, 'R': -2, 'S': -2, 'T': -1, 'V': 1,  'W': -2, 'Y': -1},
    'M': {'A': -1, 'C': -1, 'D': -3, 'E': -2, 'F': 0,  'G': -3, 'H': -2, 'I': 1,  'K': -1, 'L': 2,  'M': 5,  'N': -2, 'P': -2, 'Q': 0,  'R': -1, 'S': -1, 'T': -1, 'V': 1,  'W': -1, 'Y': -1},
    'N': {'A': -2, 'C': -3, 'D': 1,  'E': 0,  'F': -3, 'G': 0,  'H': 1,  'I': -3, 'K': 0,  'L': -3, 'M': -2, 'N': 6,  'P': -2, 'Q': 0,  'R': 0,  'S': 1,  'T': 0,  'V': -3, 'W': -4, 'Y': -2},
    'P': {'A': -1, 'C': -3, 'D': -1, 'E': -1, 'F': -4, 'G': -2, 'H': -2, 'I': -3, 'K': -1, 'L': -3, 'M': -2, 'N': -2, 'P': 7,  'Q': -1, 'R': -2, 'S': -1, 'T': -1, 'V': -2, 'W': -4, 'Y': -3},
    'Q': {'A': -1, 'C': -3, 'D': 0,  'E': 2,  'F': -3, 'G': -2, 'H': 0,  'I': -3, 'K': 1,  'L': -2, 'M': 0,  'N': 0,  'P': -1, 'Q': 5,  'R': 1,  'S': 0,  'T': -1, 'V': -2, 'W': -2, 'Y': -1},
    'R': {'A': -1, 'C': -3, 'D': -2, 'E': 0,  'F': -3, 'G': -2, 'H': 0,  'I': -3, 'K': 2,  'L': -2, 'M': -1, 'N': 0,  'P': -2, 'Q': 1,  'R': 5,  'S': -1, 'T': -1, 'V': -3, 'W': -3, 'Y': -2},
    'S': {'A': 1,  'C': -1, 'D': 0,  'E': 0,  'F': -2, 'G': 0,  'H': -1, 'I': -2, 'K': 0,  'L': -2, 'M': -1, 'N': 1,  'P': -1, 'Q': 0,  'R': -1, 'S': 4,  'T': 1,  'V': -2, 'W': -3, 'Y': -2},
    'T': {'A': 0,  'C': -1, 'D': -1, 'E': -1, 'F': -2, 'G': -2, 'H': -2, 'I': -1, 'K': -1, 'L': -1, 'M': -1, 'N': 0,  'P': -1, 'Q': -1, 'R': -1, 'S': 1,  'T': 5,  'V': 0,  'W': -2, 'Y': -2},
    'V': {'A': 0,  'C': -1, 'D': -3, 'E': -2, 'F': -1, 'G': -3, 'H': -3, 'I': 3,  'K': -2, 'L': 1,  'M': 1,  'N': -3, 'P': -2, 'Q': -2, 'R': -3, 'S': -2, 'T': 0,  'V': 4,  'W': -3, 'Y': -1},
    'W': {'A': -3, 'C': -2, 'D': -4, 'E': -3, 'F': 1,  'G': -2, 'H': -2, 'I': -3, 'K': -3, 'L': -2, 'M': -1, 'N': -4, 'P': -4, 'Q': -2, 'R': -3, 'S': -3, 'T': -2, 'V': -3, 'W': 11, 'Y': 2},
    'Y': {'A': -2, 'C': -2, 'D': -3, 'E': -2, 'F': 3,  'G': -3, 'H': 2,  'I': -1, 'K': -2, 'L': -1, 'M': -1, 'N': -2, 'P': -3, 'Q': -1, 'R': -2, 'S': -2, 'T': -2, 'V': -1, 'W': 2,  'Y': 7}
}
sigma = 5  
v = "AGACTACGTCCCAGCCTGGGCTCTTTGAGAGGGATCGACAGTCCGCGACCTACCCTGTTAGTTGTGCCATCTAACGTCCGATCGTTTAATAGGGGAGGTGAAGCCCGGAGCAATTTTGCACAGAGAACGAGCCCTGATAATGGGAAAGTTAGACTCGATATTTAGCGACCCTTCAGTTGGACCCCCTGCGAGCCCACCCTTACCGCCAGTGCGACGGGGATTGTTTTTAGGTTCTTCTGTGTAAGCCTTATAAGGCACGGGGCCCTCTTCACCTCAACTCAGTTAACTTTCTGCCCTGTTACGGAACAGAAGAACGGTATGCAGCCGACCTTTAGGATCCCACACTGGGATCTATGTACTAACTCCCCCAGATGCCTACTACCCGACTAGGTCGGTAACCTATTAGTCCCTGAGGCTGTCTATAGGAAATTAATGCCGGAGAACTCCCATAGGGTTCTTTAGCTCGTTCGGTTTTCAGGAACCCCAGTGCCATTATTATCGAGTTGTTGCCTGCCCCAGTACCACAATTGCCGAGAAGCCCGGCAAGTAGTGGGCATCCGTTACTAGTCGAAACCCGTCGGTGCTCTGCAGATCTGCGCCAAGACAAAACTGCAATCGAAGAGCTTCCGCGATGGTGACAAAGCTGAAGGCCATCCTACCGGAACATTAAAACCAGTCCCGAGACCTCCCCTCTTAAGAATTGCGTATGATGGCGTACTCCATGTACTTTAGCAAACTTGCGGCCGACGTCGTCTGTGATCATAAAGACGGCGGAATTAGGTTTTCGCTACTTTGGTGATTAGCGCATCCATCACTTCACCCCAACGAGACCTACTATTCGTAGCACGTAGGGCTTAAGCCGAAGAGACGACATTCTCACTAACCGTTGTAGTTTAAGGA"
w = "AGACTACGTATCTTCTTTAAGAGGGTGCTCACGTCACACCGCGCCTACCCTGTTATAAATAGGTTGTGCCATCTAATAGGACGTCAGCGGTCGTTTAATAGGGGAGCGTAGATTAAGCCAGGCCGCTATTTTCGACATTGGCACAGAGCACGAGCCCTGATGGGTTAGAATCTGGCTATTTAGCCTTCAGTTGGACCCCCAGCGAGCTACCCTCCGCCAGCGCGACGGGGATTGATAGCCGGTCGTGTTAGGTCCCCCTCGGTGTGATGTGTGAGCCTTCTCAGCACGACGGAGAGCCAGCCCTCTCTCAGTTAACTTTCTGCCTTGTTGCCTCAGAAGAAGGGTCGCGAGTCTGCAGCCGGCGCACCGTTTAGGACTCAGGATTCGTAACACTGGGTTCTAAGTTCCCTACTACCCAACTAGGTCGGTAACCTCCTTTAACTTCTGAGACTGATCTGCAATTAATGCTGGAGGCACTCTTTAGCTCGTTCGGTTTTCAGGAGTAGTAGCCCCTAGTTCCATTGTCGAGTTGTGGCCTCAGCGCTGATGTATATTCAACCGCCAATTGCCCTGAAGCCCAGCTCGGCCGGGGCGATATCCGTTACTAGTGACTCGAAAACTCCTTTCGGGGAGATATTGGTGCTCTGCGCGCTATGTATAGGAATGCAATCGAAGAGCTTCCTGACAAGCCATATCCGATCTCAACCGTAAGATTAAAACCAATCCGGAGAAGTCTTAAGATGAGTTGGTAGGTGCTGAACATATGGCGTACTCCATGTAGCTATCAGAGATTGCGGCCGACGTCGTCTAACAATGATCCTAAAGACTAGGTTTTCTTTGGTAATTGTTGCAGCCATCCATCACTTCACCCCAACGAGATCTACTATACGTAGCCTTTCACCGTAGGGCTTGCCGACAGAGCGACGCCACATTCTCACTAACCGTTGTAGTTTTATTCTCCAGGT"
n = len(v)
m = len(w)
dp = [[0]*(m+1) for _ in range(n+1)] #stores max alignment scores
backtrack = [[None]*(m+1) for _ in range(n+1)] #stores the direction for the optimal moves
for i in range(1, n+1): #first column
    dp[i][0] = -i*sigma #gap penalty for deletion
    backtrack[i][0] = "up" #gap in w
for j in range(1, m+1): #first row
    dp[0][j] = -j*sigma #gap penalty for insertion
    backtrack[0][j] = "left" #gap in v
for i in range(1, n+1):
    for j in range(1, m+1):
        match = dp[i-1][j-1] + BLOSUM62[v[i-1]][w[j-1]] #score if aa are aligned 
        delete = dp[i-1][j] - sigma #score if gap in w is inserted (deletion)
        insert = dp[i][j-1] - sigma #score if gap in v is inserted (insertion)
        dp[i][j] = max(match, delete, insert) #take best score from the three options mentioned above (match, deletion or insertion)
        if dp[i][j] == match: #save best scores for backtracking
            backtrack[i][j] = "diag" #match/mismatch for diagonals
        elif dp[i][j] == delete:
            backtrack[i][j] = "up" #gap in w for ups
        else:
            backtrack[i][j] = "left" #gap in v for lefts
i, j = n, m
v_aligned = "" #aligned versions of v
w_aligned = "" #aligned versions of w
while i > 0 or j > 0: #moved until source is reached
    if backtrack[i][j] == "diag":
        v_aligned = v[i-1] + v_aligned #Add aa in v
        w_aligned = w[j-1] + w_aligned #Add aa in w
        i -= 1
        j -= 1
    elif backtrack[i][j] == "up":
        v_aligned = v[i-1] + v_aligned #Add aa in v
        w_aligned = "-" + w_aligned #Add gap in w
        i -= 1
    else:
        v_aligned = "-" + v_aligned #Add gap in v
        w_aligned = w[j-1] + w_aligned #Add aa in w
        j -= 1
print("Maximum alignment score:", dp[n][m])
print("Alignment:")
print(v_aligned)
print(w_aligned)

#Code provided by ChatGPT
#Note, BLOSUM62 matrix can be imported from an existing biopythom module or by making it into a .txt file and importing it from there