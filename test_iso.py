import PyBliss

# Isomorphism test

G = PyBliss.from_dimacs('./data/ag/ag2-3-1')
H = PyBliss.from_dimacs('./data/ag/ag2-3-2')

# Canonical maps id -> canon_id
G.canonical_labeling()
H.canonical_labeling()

# Print Canonical traces
print(str(G.relabel(G.canonical_labeling())))
print(str(H.relabel(H.canonical_labeling())))


# Tests

# should be True

G = PyBliss.from_dimacs('./data/ag/ag2-3-1')
H = PyBliss.from_dimacs('./data/ag/ag2-3-2')

str(H.relabel(H.canonical_labeling())) == str(G.relabel(G.canonical_labeling()))

# should be True

G = PyBliss.from_dimacs('./data/cfi-rigid-t2/cfi-rigid-t2-0020-01-1')
H = PyBliss.from_dimacs('./data/cfi-rigid-t2/cfi-rigid-t2-0020-01-2')

str(H.relabel(H.canonical_labeling())) == str(G.relabel(G.canonical_labeling()))

# should be False

G = PyBliss.from_dimacs('./data/cfi-rigid-t2/cfi-rigid-t2-0020-01-1')
H = PyBliss.from_dimacs('./data/cfi-rigid-t2/cfi-rigid-t2-0020-02-1')

str(H.relabel(H.canonical_labeling())) == str(G.relabel(G.canonical_labeling()))

# Automorphism Group

def report(perm, text = None):
    print text, perm

G.find_automorphisms(report, "Aut gen:")
