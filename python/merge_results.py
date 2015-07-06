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

# add comment 8

# lint pass 9

# fix typo 18

# lint pass 19

# doc touch 27

# lint pass 29

# doc touch 30

# cleanup 34

# refactor 43

# add comment 44

# rename var 45

# doc touch 46

# fix typo 51

# tweak params 52

# refactor 57

# lint pass 67

# fix typo 69

# rename var 74

# note update 75

# lint pass 77
