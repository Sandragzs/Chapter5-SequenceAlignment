# Middle Edge in Linear Space — BLOSUM62, gap = 5
# ----- embedded input -----
s = "GPDCTRSGSEQFNDVYHMSPADSWTMYFYMGKGDPDSQEMWDPVHHNTVIEICRSPVLFNNCARYRDQPGPPSLHCVTILGFLERWKFKSTDAFSTSRDFEFVRDIENPHHASDVGDTVPRTSWLWRWRYRMKLKTQMMIGACEPDNLIMCSVTSRSMSLAFWMKLPQVGVCTQGQDMWNKGWAFVTLCKPYCMTGRCRWWWGKFETSAYQSVTLNPGHTDMMWHILGNPMFRRIFHNIWMPNQCSNVYTENFVMCSPYMYWLGVEYMSLKPQDKYVDQDINEVRHVQYVHMYDWTVSHICMQLGGDGGPNRCGDYLGCYTCFTYSWDYQMPDPHEGAGISFCLNGGSLSTYGSNVIFYRMEVEYFGTAMWTCKMGVETRKMNLWCRRACEDHIVVAAKWGRMKLDRIITSQAGETIIRDYMWFVYPVLEATMDKICGLMMTRHEWNNELNNRDSAYLNQSQFFADCLRICIATQIDSTIKLYPDGICDTVDVDKDQYFCLYMDLIEFELMIQSVNCGRDAGIHCEGIQGYKFMFSFASGKQWHVRFDWQPLQLYVTYRYVAVGKYQIEGNDYAGDGNELFASVHMSMLEQDHDNIHVSVCMHPHEYTVFYMDMQVRKCLAQWYFHNHNHAHPKFCEVCLVRMQLFNCYLCLYFSHVVAMSNYDTNDPHRGALCPVTMPNSVHNQFSLYYNCWGSMAMAKLSHGDWMCLSECDTCHPIWSTRLAAPMYSPRMNRIWQYRREKKYHFFYSVETDGPVYTTHHSGIFWTHMNKLRFFCDCVPWLLKSITTTVRAQSPLEWMIKTIICPYGEMISMACFNDIAVRYHKYWRHFVIEWQKIWIIISGVMDYMYACMDCFKHMNSCWTQYCDKTEMMLQPRKFSRAFVPSMSAAQVCKKDWVEENLRHWKVDNMALKSTLYAQSGKASRDGKTYHNSNGNGNPDYGREQVATPERRPCYRDAWWMYRGSASCGCKCNYETVRAEAETCQIDAITGCFFVKLPTVAHPYFQGYYNMETYKDQIKNCTIMLTHMDRQPNWED"
t = "VCSMLSTTEQIQCLCSAGFTPLVTQRVHSLSYAMLRLGMGKIRWSGKVKPHGSNICIPYACYWAVLDKECLLWVACLIRIHVGWHMSWCAIKINLWNWWTTDQIIVQHWKCMFLELSTIAICHSIGCSTEHDSLEWNFPVHCIRGWTGDFRYYYIVHQKLWGSCGNLPDACLIFKVAYMMTNERMEWSRAVSCINDLFYCYVTVLPLCIHYHPMWDRTVSTFSCCIQYHWYYSRKWWKPYGPNMCVQRLDWRRNFMYIHFFHIDWYLCTWCYSAYFIMWVAYLWSEPFNRNWPIGVFGFSGSAHNLNMCFHCTLIACCRHSIGIEGFCMLIWAWRKEVMFYVAYTNPNDSMWYATMFFETSTPCRKTDDHWQTHMKARAQCNDKGMDHAGHGGAQKTYLTCKPYGQNSSNAYNWRMVMGDNKWQQYPAEMDVEWHGPGECCMVCIDMDVRNFYYNRDSAYLNCLRICISTQIDSRIKLYPDGDCDLVHADHDKDQSNDAWQFFCLLIEFEDYIQMICMLDAGIHCEGIQGYKFMFSFASGCQWHVRFIPEWQPLQLQNIEVGKYQIEGNMTGDMYVYAGDGNELFASVHEHWYDGHCRPMAVVTIQTGPFPHYRPNWHWKSSDSVWMAVCFDFSQGNGCDDCHTFSDDEEASMLKAIWAHGQMTSYHTAQGGGPNVRSKNITHLWEVMFLKREEWRLIMNHPLALTMRQCVWHWTFNVWNEGDFWRHIDERPQLGNDYECRRADYYNNNKPTKMLMQIHGDYPEYDITQMEAIQHINMNNTQAYDKYTWEMYRGEHAPPKWLISMVHHVAIEPAHVIDKDYFCANFPNMLFNATEQMALDDISVYYQDIQGMGPQYINCLLWADLYAMNCESWSPVLRIWQCFGHYECMMKVIIAYSFPIQAIVATPDTPCPGEWRRVVRHTSVICWPLWYRKETVTGQIMRTQWGVEHHTEWCRQSNCAQMHVRHLCWECMHMWFHCNHDENWNDWGSWVRNIKGHQPQEDVQKVTSCVCDISNKVCWGSSSDYQNETMKDKDKFWRL"   # <- your sample
# --------------------------

BLOSUM62_TXT = """
   A  R  N  D  C  Q  E  G  H  I  L  K  M  F  P  S  T  W  Y  V  B  Z  X  *
A  4 -1 -2 -2  0 -1 -1  0 -2 -1 -1 -1 -1 -2 -1  1  0 -3 -2  0 -2 -1  0 -4
R -1  5  0 -2 -3  1  0 -2  0 -3 -2  2 -1 -3 -2 -1 -1 -3 -2 -3 -1  0 -1 -4
N -2  0  6  1 -3  0  0  0  1 -3 -3  0 -2 -3 -2  1  0 -4 -2 -3  4  0 -1 -4
D -2 -2  1  6 -3  0  2 -1 -1 -3 -4 -1 -3 -3 -1  0 -1 -4 -3 -3  1  2 -1 -4
C  0 -3 -3 -3  9 -3 -4 -3 -3 -1 -1 -3 -1 -2 -3 -1 -1 -2 -2 -1 -3 -3 -2 -4
Q -1  1  0  0 -3  5  2 -2  0 -3 -2  1  0 -3 -1  0 -1 -2 -1 -2  0  3 -1 -4
E -1  0  0  2 -4  2  5 -2  0 -3 -3  1 -2 -3 -1  0 -1 -3 -2 -2  1  4 -1 -4
G  0 -2  0 -1 -3 -2 -2  6 -2 -4 -4 -2 -3 -3 -2  0 -2 -2 -3 -3 -1 -2 -1 -4
H -2  0  1 -1 -3  0  0 -2  8 -3 -3 -1 -2 -1 -2 -1 -2 -2  2 -3  0  0 -1 -4
I -1 -3 -3 -3 -1 -3 -3 -4 -3  4  2 -3  1  0 -3 -2 -1 -3 -1  3 -3 -3 -1 -4
L -1 -2 -3 -4 -1 -2 -3 -4 -3  2  4 -2  2  0 -3 -2 -1 -2 -1  1 -4 -3 -1 -4
K -1  2  0 -1 -3  1  1 -2 -1 -3 -2  5 -1 -3 -1  0 -1 -3 -2 -2  0  1 -1 -4
M -1 -1 -2 -3 -1  0 -2 -3 -2  1  2 -1  5  0 -2 -1 -1 -1 -1  1 -3 -1 -1 -4
F -2 -3 -3 -3 -2 -3 -3 -3 -1  0  0 -3  0  6 -4 -2 -2  1  3 -1 -3 -3 -1 -4
P -1 -2 -2 -1 -3 -1 -1 -2 -2 -3 -3 -1 -2 -4  7 -1 -1 -4 -3 -2 -2 -1 -2 -4
S  1 -1  1  0 -1  0  0  0 -1 -2 -2  0 -1 -2 -1  4  1 -3 -2 -2  0  0  0 -4
T  0 -1  0 -1 -1 -1 -1 -2 -2 -1 -1 -1 -1 -2 -1  1  5 -2 -2  0 -1 -1  0 -4
W -3 -3 -4 -4 -2 -2 -3 -2 -2 -3 -2 -3 -1  1 -4 -3 -2 11  2 -3 -4 -3 -2 -4
Y -2 -2 -2 -3 -2 -1 -2 -3  2 -1 -1 -2 -1  3 -3 -2 -2  2  7 -1 -3 -2 -1 -4
V  0 -3 -3 -3 -1 -2 -2 -3 -3  3  1 -2  1 -1 -2 -2  0 -3 -1  4 -3 -2 -1 -4
B -2 -1  4  1 -3  0  1 -1  0 -3 -4  0 -3 -3 -2  0 -1 -4 -3 -3  4  1 -1 -4
Z -1  0  0  2 -3  3  4 -2  0 -3 -3  1 -1 -3 -1  0 -1 -3 -2 -2  1  4 -1 -4
X  0 -1 -1 -1 -2 -1 -1 -1 -1 -1 -1 -1 -1 -1 -2  0  0 -2 -1 -1 -1 -1 -1 -4
* -4 -4 -4 -4 -4 -4 -4 -4 -4 -4 -4 -4 -4 -4 -4 -4 -4 -4 -4 -4 -4 -4 -4  1
"""

def _score_table(txt=BLOSUM62_TXT):
    rows = [ln.split() for ln in txt.strip().splitlines()]
    hdr = rows[0]
    S = {}
    for r in rows[1:]:
        a, vals = r[0], list(map(int, r[1:]))
        for b, v in zip(hdr, vals):
            S[(a, b)] = v
            S[(b, a)] = v
    return S

SCORE = _score_table()
GAP = 5

def last_column(s: str, t: str):
    """Scores of the last DP column for aligning s vs t (linear space)."""
    n = len(s)
    prev = [-i * GAP for i in range(n + 1)]
    for j in range(1, len(t) + 1):
        cur = [0] * (n + 1)
        cur[0] = -j * GAP
        for i in range(1, n + 1):
            cur[i] = max(
                prev[i - 1] + SCORE[(s[i - 1], t[j - 1])],  # diagonal
                prev[i] - GAP,                              # down (gap in t)
                cur[i - 1] - GAP                            # right (gap in s)
            )
        prev = cur
    return prev

def middle_edge(s: str, t: str):
    """Return ((i, j), (k, l)) — the middle edge for s vs t."""
    s, t = s.strip().upper(), t.strip().upper()
    n, m = len(s), len(t)
    mid = m // 2

    # to middle column
    F = last_column(s, t[:mid])

    # from middle column to sink (on reversed strings)
    Br  = last_column(s[::-1], t[mid:][::-1]);  B  = [Br[n - i] for i in range(n + 1)]
    Br1 = last_column(s[::-1], t[mid+1:][::-1]); Bp = [Br1[n - i] for i in range(n + 1)]

    # crossing row (tie → larger i)
    i_star = max(range(n + 1), key=lambda i: (F[i] + B[i], i))

    # score three outgoing edges; tie preference: diag > down > right
    choices = []
    if i_star < n and mid < m:  # diagonal
        choices.append((F[i_star] + SCORE[(s[i_star], t[mid])] + Bp[i_star + 1],
                        2, (i_star, mid), (i_star + 1, mid + 1)))
    if i_star < n:              # down
        choices.append((F[i_star] - GAP + B[i_star + 1],
                        1, (i_star, mid), (i_star + 1, mid)))
    if mid < m:                 # right
        choices.append((F[i_star] - GAP + Bp[i_star],
                        0, (i_star, mid), (i_star, mid + 1)))

    _, _, u, v = max(choices, key=lambda x: (x[0], x[1]))
    return u, v

# Compute and print
(u_i, u_j), (v_i, v_j) = middle_edge(s, t)
print(f"({u_i}, {u_j}) ({v_i}, {v_j})")