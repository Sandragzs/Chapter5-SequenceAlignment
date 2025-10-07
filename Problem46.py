# Define the BLOSUM62 substitution matrix as a dictionary of dictionaries
BLOSUM62 = {
    'A': {'A':4,'C':0,'D':-2,'E':-1,'F':-2,'G':0,'H':-2,'I':-1,'K':-1,'L':-1,'M':-1,'N':-2,'P':-1,'Q':-1,'R':-1,'S':1,'T':0,'V':0,'W':-3,'Y':-2},
    'C': {'A':0,'C':9,'D':-3,'E':-4,'F':-2,'G':-3,'H':-3,'I':-1,'K':-3,'L':-1,'M':-1,'N':-3,'P':-3,'Q':-3,'R':-3,'S':-1,'T':-1,'V':-1,'W':-2,'Y':-2},
    'D': {'A':-2,'C':-3,'D':6,'E':2,'F':-3,'G':-1,'H':-1,'I':-3,'K':-1,'L':-4,'M':-3,'N':1,'P':-1,'Q':0,'R':-2,'S':0,'T':-1,'V':-3,'W':-4,'Y':-3},
    'E': {'A':-1,'C':-4,'D':2,'E':5,'F':-3,'G':-2,'H':0,'I':-3,'K':1,'L':-3,'M':-2,'N':0,'P':-1,'Q':2,'R':0,'S':0,'T':-1,'V':-2,'W':-3,'Y':-2},
    'F': {'A':-2,'C':-2,'D':-3,'E':-3,'F':6,'G':-3,'H':-1,'I':0,'K':-3,'L':0,'M':0,'N':-3,'P':-4,'Q':-3,'R':-3,'S':-2,'T':-2,'V':-1,'W':1,'Y':3},
    'G': {'A':0,'C':-3,'D':-1,'E':-2,'F':-3,'G':6,'H':-2,'I':-4,'K':-2,'L':-4,'M':-3,'N':0,'P':-2,'Q':-2,'R':-2,'S':0,'T':-2,'V':-3,'W':-2,'Y':-3},
    'H': {'A':-2,'C':-3,'D':-1,'E':0,'F':-1,'G':-2,'H':8,'I':-3,'K':-1,'L':-3,'M':-2,'N':1,'P':-2,'Q':0,'R':0,'S':-1,'T':-2,'V':-3,'W':-2,'Y':2},
    'I': {'A':-1,'C':-1,'D':-3,'E':-3,'F':0,'G':-4,'H':-3,'I':4,'K':-3,'L':2,'M':1,'N':-3,'P':-3,'Q':-3,'R':-3,'S':-2,'T':-1,'V':3,'W':-3,'Y':-1},
    'K': {'A':-1,'C':-3,'D':-1,'E':1,'F':-3,'G':-2,'H':-1,'I':-3,'K':5,'L':-2,'M':-1,'N':0,'P':-1,'Q':1,'R':2,'S':0,'T':-1,'V':-2,'W':-3,'Y':-2},
    'L': {'A':-1,'C':-1,'D':-4,'E':-3,'F':0,'G':-4,'H':-3,'I':2,'K':-2,'L':4,'M':2,'N':-3,'P':-3,'Q':-2,'R':-2,'S':-2,'T':-1,'V':1,'W':-2,'Y':-1},
    'M': {'A':-1,'C':-1,'D':-3,'E':-2,'F':0,'G':-3,'H':-2,'I':1,'K':-1,'L':2,'M':5,'N':-2,'P':-2,'Q':0,'R':-1,'S':-1,'T':-1,'V':1,'W':-1,'Y':-1},
    'N': {'A':-2,'C':-3,'D':1,'E':0,'F':-3,'G':0,'H':1,'I':-3,'K':0,'L':-3,'M':-2,'N':6,'P':-2,'Q':0,'R':0,'S':1,'T':0,'V':-3,'W':-4,'Y':-2},
    'P': {'A':-1,'C':-3,'D':-1,'E':-1,'F':-4,'G':-2,'H':-2,'I':-3,'K':-1,'L':-3,'M':-2,'N':-2,'P':7,'Q':-1,'R':-2,'S':-1,'T':-1,'V':-2,'W':-4,'Y':-3},
    'Q': {'A':-1,'C':-3,'D':0,'E':2,'F':-3,'G':-2,'H':0,'I':-3,'K':1,'L':-2,'M':0,'N':0,'P':-1,'Q':5,'R':1,'S':0,'T':-1,'V':-2,'W':-2,'Y':-1},
    'R': {'A':-1,'C':-3,'D':-2,'E':0,'F':-3,'G':-2,'H':0,'I':-3,'K':2,'L':-2,'M':-1,'N':0,'P':-2,'Q':1,'R':5,'S':-1,'T':-1,'V':-3,'W':-3,'Y':-2},
    'S': {'A':1,'C':-1,'D':0,'E':0,'F':-2,'G':0,'H':-1,'I':-2,'K':0,'L':-2,'M':-1,'N':1,'P':-1,'Q':0,'R':-1,'S':4,'T':1,'V':-2,'W':-3,'Y':-2},
    'T': {'A':0,'C':-1,'D':-1,'E':-1,'F':-2,'G':-2,'H':-2,'I':-1,'K':-1,'L':-1,'M':-1,'N':0,'P':-1,'Q':-1,'R':-1,'S':1,'T':5,'V':0,'W':-2,'Y':-2},
    'V': {'A':0,'C':-1,'D':-3,'E':-2,'F':-1,'G':-3,'H':-3,'I':3,'K':-2,'L':1,'M':1,'N':-3,'P':-2,'Q':-2,'R':-3,'S':-2,'T':0,'V':4,'W':-3,'Y':-1},
    'W': {'A':-3,'C':-2,'D':-4,'E':-3,'F':1,'G':-2,'H':-2,'I':-3,'K':-3,'L':-2,'M':-1,'N':-4,'P':-4,'Q':-2,'R':-3,'S':-3,'T':-2,'V':-3,'W':11,'Y':2},
    'Y': {'A':-2,'C':-2,'D':-3,'E':-2,'F':3,'G':-3,'H':2,'I':-1,'K':-2,'L':-1,'M':-1,'N':-2,'P':-3,'Q':-1,'R':-2,'S':-2,'T':-2,'V':-1,'W':2,'Y':7},
}

sig = 11  # gap opening penalty
ε = 1   # gap extension penalty

def global_affine_alignment(v, w):
    n, m = len(v), len(w) # lengths of the two strings

    # Initialize DP matrices
    M = [[0]*(m+1) for _ in range(n+1)] # best score aligning v and w that ends with a match/mismatch
    X = [[0]*(m+1) for _ in range(n+1)] # best score aligning v and w that ends with a gap in w
    Y = [[0]*(m+1) for _ in range(n+1)] # best score aligning v and w that ends with a gap in v

    # Traceback matrices for each DP matrix (store which matrix we came from at (i, j), to reconstruct the path)
    back_M = [['']*(m+1) for _ in range(n+1)]
    back_X = [['']*(m+1) for _ in range(n+1)]
    back_Y = [['']*(m+1) for _ in range(n+1)]

    # Initialize first row and column
    for i in range(1, n+1):
        M[i][0] = -sig - (i-1)*ε
        X[i][0] = -sig - (i-1)*ε
        Y[i][0] = float('-inf') # because we cannot end with a gap in v if w has length 0.
    for j in range(1, m+1):
        M[0][j] = -sig - (j-1)*ε
        Y[0][j] = -sig - (j-1)*ε
        X[0][j] = float('-inf') # because we cannot end with a gap in w if v has length 0.

    # Fill matrices
    for i in range(1, n+1): #Iterates over the grid.
        for j in range(1, m+1):
            s = BLOSUM62[v[i-1]][w[j-1]] # substitution score between characters v[i-1] and w[j-1].

            # Match/Mismatch matrix
            M[i][j] = max(M[i-1][j-1], X[i-1][j-1], Y[i-1][j-1]) + s #Best alignment if current cell ends with aligning v[i-1] and w[j-1]
            #Record whether we came from M, X, or Y:
            if M[i][j] == M[i-1][j-1] + s:
                back_M[i][j] = 'M'
            elif M[i][j] == X[i-1][j-1] + s:
                back_M[i][j] = 'X'
            else:
                back_M[i][j] = 'Y'

            # Gap in w (insertion in v)
            X[i][j] = max(M[i-1][j] - sig, X[i-1][j] - ε)
            back_X[i][j] = 'M' if X[i][j] == M[i-1][j] - sig else 'X' # Either open a gap (from M) or extend it (from X)

            # Gap in v (deletion in v)
            Y[i][j] = max(M[i][j-1] - sig, Y[i][j-1] - ε)
            back_Y[i][j] = 'M' if Y[i][j] == M[i][j-1] - sig else 'Y' # Either open a gap (from M) or extend it (from Y)

    # Find final max score
    final_score = max(M[n][m], X[n][m], Y[n][m]) # Chooses the best alignment score from the last cell (n, m) across all matrices
    # Record where the optimal path ends
    if final_score == M[n][m]:
        matrix = 'M'
    elif final_score == X[n][m]:
        matrix = 'X'
    else:
        matrix = 'Y'

    # Traceback
    aln_v, aln_w = [], [] # Prepare two empty lists for aligned sequences
    i, j = n, m # Start at the bottom-right cell (n, m)
    while i > 0 or j > 0: # iterate till we get to 0,0
        if matrix == 'M': # If in M: align characters from both sequences
            if back_M[i][j] == 'M':
                aln_v.append(v[i-1]); aln_w.append(w[j-1])
                i -= 1; j -= 1; matrix = 'M'
            elif back_M[i][j] == 'X': 
                aln_v.append(v[i-1]); aln_w.append(w[j-1])
                i -= 1; j -= 1; matrix = 'X'
            else:
                aln_v.append(v[i-1]); aln_w.append(w[j-1])
                i -= 1; j -= 1; matrix = 'Y'

        elif matrix == 'X': # If in X: align character from v with gap (-)
            if back_X[i][j] == 'M':
                aln_v.append(v[i-1]); aln_w.append('-')
                i -= 1; matrix = 'M'
            else:
                aln_v.append(v[i-1]); aln_w.append('-')
                i -= 1; matrix = 'X'

        elif matrix == 'Y': # If in Y: align gap with character from w
            if back_Y[i][j] == 'M':
                aln_v.append('-'); aln_w.append(w[j-1])
                j -= 1; matrix = 'M'
            else:
                aln_v.append('-'); aln_w.append(w[j-1])
                j -= 1; matrix = 'Y'

    # Reverse alignments
    aln_v = ''.join(reversed(aln_v))
    aln_w = ''.join(reversed(aln_w))

    return final_score, aln_v, aln_w


v = "YTPEDFLPQVSHKKPRFSRMMFVIIDFTQLHVVGEKMWPQFSDQQEGIVRLLGTNCAYLVISNSWNQGPHHHVAL"
w = "YWYLQWDPMWSECFLDISAPIFSRAMFVIIDFVGEKMWPQFSDQQEGIVRLLGTNCAYPIGIELNQGPHHCVAL"

score, a1, a2 = global_affine_alignment(v, w)
print(score)
print(a1)
print(a2)