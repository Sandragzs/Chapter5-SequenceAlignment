v = "TTCAACCCTTTACGATGCAAGGGAAACCATCCTTTGTATAACAGCGACGGGCTATTCTAAACAATCGCAATGAGATCCGATCGTAACAGGGCTCCCCCATTAGGTACTCGGATCTTCGCAATTCATAGTCGGCCCGACCCTCCCGGAACGCCGTTGCCCTTTATGTGGGCAAATTACGAGGCGTTGTAGTGTTAACATATAGATCACGTGATTCTTACGACGAGTCTAGGCTGCCGGCGGATTTCGTGCCACTTCATGGCCTTCAGAGGCCCGATTGGGCCTGTGCAGGCATGTACCAACTACAGAATTAGAGGGGTCCGTGCGCTTGCGTGGGGGTAAGTGGGGGCGAAGGCATTTCGCGTTTGCTCACTTAAAGGTTGGGCATGCAGGACCTTATCGGCTTAATTCATACTAACGGCCACGACAAATGAGGCAAGCGTCAGCATACTATCAATTCCTACTGTGACGCTCCGGACAACTTGAGGTGCCTCACGCACCAGTCGAACCAGGGCAGTCGAGCTTTACTCCGAGAGTCGGAGTCTGCTCCTGGCGGATGATAACATGAGCGATTCTGAAACATCGAGCTTATTCGTTTCATTGTGAGCAAAGGCTTGGCCAGATGAATCTCGGGGTCTGCAGTGTGACTGTCACGTCTCAATTTAAAATCCAGACAGTCCGGTAATCGATCAGTAGAGTCCGCCCATACAGCAGATGGGGGCATGAATGGTTGTTCCCTCCGATTCTTTGAAGTTCGCTGCCGCCGGCTCAACACGACCAAGGAAGAAGCTGCCCCATCGCTTTAGTACAGGTCCGCAGAAGGATGGGGTAATAAAAGGCAACCGAATTAATTAATAAAAATCAAGTTACAACGTGTACTGAGATACGATCAAAAACATACTTGTTTGAAACTACAGTTCTAGACCGGTATCAGGGCAAC" 
w = "GCAACATCAGGTAGATTCCCAGCCATACAGCAGAACGAGGGCCTGTATGTTAGCTCCCTGCCGATTCTCTTGAAGTTCGCTAGCGACGACTAGACAATCAAGGAAGAAACTGGCCCGCCGCTTTAGCACAGGTCGCACAGAAGGGGTGGAGGTGATGAATAGCCACCGCCAATTCATCTAAGGAGGGTCAGGCGATGCGGATGCCTGAGATACTCAAAGAACTCTTCGTTCGATTCACACCAGTCCAGTGGCGGGTACGAGAGCAACAGATCGACTCGGTATCATTAACTCGCCACGAGATGCTGACCACTGCCACGGAGTTTTAGTGTGCAAATATTCACAAGCTCCAAAGTCGTGTTGAGACATTGGGGCGTGGAAGTGCAAGTATTAGGGTTTGGTGAGAGGGTTAGCGAGATTGCGTTAAGCCTCCTGTTCATAGTAACAGATGCTTCGACGATGGTTTCTTTCGCAATCTAAACGAGATTTTCCGGTAACTGAGCGATAGACCTTACGGTCGGACTTAACGTTCCTTTTAGTGCTATTGCACGTGAACCATATAACAATACGCCCATCCGGAACCGAGGGATCGAGCATGAAGTCGCTACGACCGTAGTCACACAATTATGTATGTCTGGGAACATCAACAGGATTAGTTAGGTAGAATTAGCGCTGTAGCGACGAGTAATCTCTGACATCTGCATCGCCTCGAATTGCCCGTAGCAGAGCCATACCGTCCGATTATTTGGACTGAATGGAACCACGAAAAGTCAACAATTGGCATAGCATTGGAGCTGTGTCTTATTAGAGGTGATATCTGCATTCTCAAATACGACGCGGACGTGACTCCCGCTTCCTCGGACGAACTCGCAACGGGTGCCTCGGGACCGAAATTCGGTCTGCATGTTGCAAGCCAGTCACATTACGTGTTCTCCTAACAAGGCTGTGAGGTAGACCA" 
n, m = len(v), len(w)
match, mismatch, indel = 1, -2, -2 
dp = [[0]*(m+1) for _ in range(n+1)]  #Matrix of size (n+1)x(m+1) filled with 0s, used for storing scores
backtrack = [[None]*(m+1) for _ in range(n+1)] #Matrix to store traceback directions
for i in range(1, n+1): #Loop over rows (v)
    for j in range(1, m+1): #Loop over columns (w)
        diag = dp[i-1][j-1] + (match if v[i-1] == w[j-1] else mismatch) #Compute score if aligning v[i-1] with w[j-1]
        up = dp[i-1][j] + indel #Compute score if introducing a gap in w (deletion in w)
        left = dp[i][j-1] + indel #Compute score if introducing a gap in v (insertion in v)
        current_max = max(diag, up, left) #Take the maximum of the three possibilities (no zero-reset)
        dp[i][j] = current_max #Store score in matrix
        #Record which move led to the current max for traceback
        if current_max == diag:
            backtrack[i][j] = "diag"
        elif current_max == up:
            backtrack[i][j] = "up"
        else:
            backtrack[i][j] = "left"
max_score = max(dp[n][j] for j in range(m+1)) #Find max in last row
max_pos_col = dp[n].index(max_score) #Column index of max score
max_pos = (n, max_pos_col)  #Starting position for traceback
#Traceback from max_pos until we reach start of v or start of w
i, j = max_pos
v_aln, w_aln = "", "" #Initialize aligned sequence strings

while i > 0 and j > 0: #Continue until start of v or w
    if backtrack[i][j] == "diag":
        v_aln = v[i-1] + v_aln #Add character from v
        w_aln = w[j-1] + w_aln #Add character from w
        i -= 1
        j -= 1
    elif backtrack[i][j] == "up":
        v_aln = v[i-1] + v_aln #Add character from v
        w_aln = "-" + w_aln #Add gap in w
        i -= 1
    elif backtrack[i][j] == "left":
        v_aln = "-" + v_aln #Add gap in v
        w_aln = w[j-1] + w_aln #Add character from w
        j -= 1
    else:
        break  #Safety break in case of unexpected value
print("Optimal overlap alignment score:", max_score)
print(v_aln)
print(w_aln) 
#Code provided by ChatGPT
