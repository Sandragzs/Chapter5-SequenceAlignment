# 1. Defining the function

BLOSUM62_TEXT = """\
   A  R  N  D  C  Q  E  G  H  I  L  K  M  F  P  S  T  W  Y  V
A  4 -1 -2 -2  0 -1 -1  0 -2 -1 -1 -1 -1 -2 -1  1  0 -3 -2  0
R -1  5  0 -2 -3  1  0 -2  0 -3 -2  2 -1 -3 -2 -1 -1 -3 -2 -3
N -2  0  6  1 -3  0  0  0  1 -3 -3  0 -2 -3 -2  1  0 -4 -2 -3
D -2 -2  1  6 -3  0  2 -1 -1 -3 -4 -1 -3 -3 -1  0 -1 -4 -3 -3
C  0 -3 -3 -3  9 -3 -4 -3 -3 -1 -1 -3 -1 -2 -3 -1 -1 -2 -2 -1
Q -1  1  0  0 -3  5  2 -2  0 -3 -2  1  0 -3 -1  0 -1 -2 -1 -2
E -1  0  0  2 -4  2  5 -2  0 -3 -3  1 -2 -3 -1  0 -1 -3 -2 -2
G  0 -2  0 -1 -3 -2 -2  6 -2 -4 -4 -2 -3 -3 -2  0 -2 -2 -3 -3
H -2  0  1 -1 -3  0  0 -2  8 -3 -3 -1 -2 -1 -2 -1 -2 -2  2 -3
I -1 -3 -3 -3 -1 -3 -3 -4 -3  4  2 -3  1  0 -3 -2 -1 -3 -1  3
L -1 -2 -3 -4 -1 -2 -3 -4 -3  2  4 -2  2  0 -3 -2 -1 -2 -1  1
K -1  2  0 -1 -3  1  1 -2 -1 -3 -2  5 -1 -3 -1  0 -1 -3 -2 -2
M -1 -1 -2 -3 -1  0 -2 -3 -2  1  2 -1  5  0 -2 -1 -1 -1 -1  1
F -2 -3 -3 -3 -2 -3 -3 -3 -1  0  0 -3  0  6 -4 -2 -2  1  3 -1
P -1 -2 -2 -1 -3 -1 -1 -2 -2 -3 -3 -1 -2 -4  7 -1 -1 -4 -3 -2
S  1 -1  1  0 -1  0  0  0 -1 -2 -2  0 -1 -2 -1  4  1 -3 -2 -2
T  0 -1  0 -1 -1 -1 -1 -2 -2 -1 -1 -1 -1 -2 -1  1  5 -2 -2  0
W -3 -3 -4 -4 -2 -2 -3 -2 -2 -3 -2 -3 -1  1 -4 -3 -2 11  2 -3
Y -2 -2 -2 -3 -2 -1 -2 -3  2 -1 -1 -2 -1  3 -3 -2 -2  2  7 -1
V  0 -3 -3 -3 -1 -2 -2 -3 -3  3  1 -2  1 -1 -2 -2  0 -3 -1  4
"""

def parse_blosum62(text):
    lines = text.strip().splitlines()
    header = lines[0].split()
    matrix = {}
    i = 1
    while i < len(lines):
        parts = lines[i].split()
        row_letter = parts[0]
        matrix[row_letter] = {}
        j = 1
        while j < len(parts):
            col_letter = header[j - 1]
            matrix[row_letter][col_letter] = int(parts[j])
            j += 1
        i += 1
    return matrix

def column_scores_strings(v_seg, w_seg, gap_penalty, blosum):
    """
    Compute DP column scores for global alignment of v_seg vs w_seg
    using linear gap penalty (gap_penalty) and BLOSUM62 (blosum).
    Returns the scores for the LAST column (len(w_seg)) for all rows 0..len(v_seg).
    Uses O(len(v_seg)) memory.
    """
    n = len(v_seg)
    m = len(w_seg)

    # prev[i] = score at cell (i, 0) initially = -i * gap
    prev = [0] * (n + 1)
    i = 1
    while i <= n:
        prev[i] = prev[i - 1] - gap_penalty
        i += 1

    # iterate columns 1..m
    j = 1
    while j <= m:
        curr = [0] * (n + 1)
        curr[0] = -j * gap_penalty
        i = 1
        while i <= n:
            s = blosum[v_seg[i - 1]][w_seg[j - 1]]
            match = prev[i - 1] + s
            delete = prev[i] - gap_penalty      # gap in w (move down)
            insert = curr[i - 1] - gap_penalty  # gap in v (move right)
            best = match
            if delete > best:
                best = delete
            if insert > best:
                best = insert
            curr[i] = best
            i += 1
        prev = curr
        j += 1

    return prev  # scores in last column for all rows

def middle_edge_subproblem(v, w, top, bottom, left, right, gap_penalty, blosum):
    """
    Compute the middle edge (i, j) -> (k, l) for the subproblem:
      v[top:bottom] vs w[left:right], using linear gap penalty.
    Returns absolute indices (i, j, k, l) in the full grid.

    Tie-breaks (to match Rosalind sample):
      - When choosing middle row i*, prefer a LOWER row on ties (larger i).
      - When choosing the middle edge, prefer DOWN > DIAG > RIGHT on ties.
    """
    n = bottom - top
    m = right - left
    mid_off = m // 2                  # offset within [left, right)
    mid_col = left + mid_off          # absolute middle column

    # Slices for this subproblem
    v_sub = v[top:bottom]
    w_left = w[left:mid_col]          # columns up to (not including) mid_col
    w_right = w[mid_col:right]        # columns from mid_col to right
    # For considering RIGHT move we also need w[mid_col+1:right]
    if mid_off + 1 <= m:
        w_right_skip = w[mid_col + 1:right]
    else:
        w_right_skip = ""

    # Forward scores to the middle column
    forward = column_scores_strings(v_sub, w_left, gap_penalty, blosum)

    # Backward scores from end to middle (compute on reversed slices)
    v_rev = v_sub[::-1]
    w_right_rev = w_right[::-1]
    back_full_rev = column_scores_strings(v_rev, w_right_rev, gap_penalty, blosum)
    if len(w_right_skip) > 0:
        back_skip_rev = column_scores_strings(v_rev, w_right_skip[::-1], gap_penalty, blosum)
    else:
        # Aligning v_sub[i:] vs "" => score = -(len)*gap
        back_skip_rev = [0] * (len(v_sub) + 1)

    # Map reversed results back to the original rows
    back_mid = [0] * (n + 1)        # scores from (i, mid_col) to (bottom, right)
    back_midplus = [0] * (n + 1)    # scores from (i, mid_col+1) to (bottom, right)
    i = 0
    while i <= n:
        back_mid[i] = back_full_rev[n - i]
        back_midplus[i] = back_skip_rev[n - i]
        i += 1

    # ---- Fix #1: choose i*; on ties, prefer LOWER row (larger i) ----
    best_sum = -10**12
    i_star = 0
    i = 0
    while i <= n:
        total = forward[i] + back_mid[i]
        if total > best_sum or (total == best_sum and i > i_star):
            best_sum = total
            i_star = i
        i += 1

    # ---- Fix #2: choose middle edge with DOWN > DIAG > RIGHT ----
    k = top + i_star
    l = mid_col
    best_dir = None
    best_score = -10**12

    have_diag = (i_star < n and mid_off < m)   # (i*, mid) -> (i*+1, mid+1)
    have_down = (i_star < n)                   # (i*, mid) -> (i*+1, mid)
    have_right = (mid_off < m)                 # (i*, mid) -> (i*,   mid+1)

    # 1) Prefer DOWN first (wins ties)
    if have_down:
        down_score = forward[i_star] - gap_penalty + back_mid[i_star + 1]
        best_dir = "down"
        best_score = down_score
        k = top + i_star + 1
        l = mid_col

    # 2) Take DIAG only if strictly better
    if have_diag:
        diag_score = forward[i_star] + blosum[v_sub[i_star]][w[mid_col]] + back_midplus[i_star + 1]
        if diag_score > best_score:
            best_dir = "diag"
            best_score = diag_score
            k = top + i_star + 1
            l = mid_col + 1

    # 3) Take RIGHT only if strictly better
    if have_right:
        right_score = forward[i_star] - gap_penalty + back_midplus[i_star]
        if right_score > best_score:
            best_dir = "right"
            best_score = right_score
            k = top + i_star
            l = mid_col + 1

    i_abs = top + i_star
    j_abs = mid_col
    return i_abs, j_abs, k, l, best_dir


def hirschberg_align(v, w, top, bottom, left, right, gap_penalty, blosum):
    """
    Returns two lists [chars...] for the alignment of v[top:bottom] vs w[left:right].
    """
    # Base cases
    if left == right:
        # align v-substring to gaps
        av = []
        aw = []
        i = top
        while i < bottom:
            av.append(v[i])
            aw.append('-')
            i += 1
        return av, aw
    if top == bottom:
        av = []
        aw = []
        j = left
        while j < right:
            av.append('-')
            aw.append(w[j])
            j += 1
        return av, aw

    # Find middle edge
    i, j, k, l, direction = middle_edge_subproblem(v, w, top, bottom, left, right, gap_penalty, blosum)

    # Recurse on left block
    left_av, left_aw = hirschberg_align(v, w, top, i, left, j, gap_penalty, blosum)

    # Add the middle edge as one aligned column
    mid_av = []
    mid_aw = []
    if direction == "diag":
        mid_av.append(v[i])
        mid_aw.append(w[j])
    elif direction == "down":
        mid_av.append(v[i])
        mid_aw.append('-')
    else:  # "right"
        mid_av.append('-')
        mid_aw.append(w[j])

    # Recurse on right block
    right_av, right_aw = hirschberg_align(v, w, k, bottom, l, right, gap_penalty, blosum)

    # Concatenate: left + middle + right
    out_v = []
    out_w = []
    # left
    p = 0
    while p < len(left_av):
        out_v.append(left_av[p])
        out_w.append(left_aw[p])
        p += 1
    # middle
    q = 0
    while q < len(mid_av):
        out_v.append(mid_av[q])
        out_w.append(mid_aw[q])
        q += 1
    # right
    r = 0
    while r < len(right_av):
        out_v.append(right_av[r])
        out_w.append(right_aw[r])
        r += 1

    return out_v, out_w

def hirschberg_align(v, w, top, bottom, left, right, gap_penalty, blosum):
    """
    Recursively build the alignment of v[top:bottom] vs w[left:right]
    using Hirschberg's linear-space divide-and-conquer with the middle edge.
    Returns two lists of characters that you can join into strings.
    """
    # Base case: w-substring is empty -> align v-substring to gaps
    if left == right:
        av = []
        aw = []
        i = top
        while i < bottom:
            av.append(v[i])
            aw.append('-')
            i += 1
        return av, aw

    # Base case: v-substring is empty -> align w-substring to gaps
    if top == bottom:
        av = []
        aw = []
        j = left
        while j < right:
            av.append('-')
            aw.append(w[j])
            j += 1
        return av, aw

    # Find the middle edge for this subproblem
    i, j, k, l, direction = middle_edge_subproblem(v, w, top, bottom, left, right, gap_penalty, blosum)

    # Recurse on the left block: v[top:i] vs w[left:j]
    left_av, left_aw = hirschberg_align(v, w, top, i, left, j, gap_penalty, blosum)

    # Add the middle edge as one aligned column
    mid_av = []
    mid_aw = []
    if direction == "diag":
        mid_av.append(v[i])
        mid_aw.append(w[j])
    elif direction == "down":
        mid_av.append(v[i])
        mid_aw.append('-')
    else:  # "right"
        mid_av.append('-')
        mid_aw.append(w[j])

    # Recurse on the right block: v[k:bottom] vs w[l:right]
    right_av, right_aw = hirschberg_align(v, w, k, bottom, l, right, gap_penalty, blosum)

    # Concatenate: left + middle + right
    out_v = []
    out_w = []
    p = 0
    while p < len(left_av):
        out_v.append(left_av[p])
        out_w.append(left_aw[p])
        p += 1
    q = 0
    while q < len(mid_av):
        out_v.append(mid_av[q])
        out_w.append(mid_aw[q])
        q += 1
    r = 0
    while r < len(right_av):
        out_v.append(right_av[r])
        out_w.append(right_aw[r])
        r += 1

    return out_v, out_w

def global_score_only(v, w, gap_penalty, blosum):
    """
    Compute ONLY the global alignment score (no traceback) in O(n) memory
    using standard DP (linear gap).
    """
    # Reuse column_scores_strings on full strings
    last_col = column_scores_strings(v, w, gap_penalty, blosum)
    return last_col[len(v)]

# 2. Importing the file
file = "Problem 48/rosalind_ba5l.txt"
with open(file, 'r') as f:
    data = f.readlines()
    v = data[0].strip().upper()
    w = data[1].strip().upper()

# v = "PLEASANTLY"
# w = "MEANLY"

# 3. Printing the results
blosum = parse_blosum62(BLOSUM62_TEXT)
gap_penalty = 5
score = global_score_only(v, w, gap_penalty, blosum)
av_list, aw_list = hirschberg_align(v, w, 0, len(v), 0, len(w), gap_penalty, blosum)
aligned_v = "".join(av_list)
aligned_w = "".join(aw_list)

print(score)
print(aligned_v)
print(aligned_w)
