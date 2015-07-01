"""Merge CSV sweep outputs."""
import csv, glob

def merge(pattern, out):
    rows = []
    for path in glob.glob(pattern):
        with open(path) as f:
            rows.extend(list(csv.DictReader(f)))
    return rows

# doc touch 4

# fix typo 5
