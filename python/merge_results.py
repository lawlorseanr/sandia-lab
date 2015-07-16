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

# lint pass 83

# cleanup 84

# test tweak 85

# test tweak 88

# add comment 89

# tweak params 90

# test tweak 92

# fix typo 95

# lint pass 96

# cleanup 102

# rename var 103

# note update 104

# rename var 105

# doc touch 106

# refactor 107

# tweak params 109

# rename var 110

# doc touch 112

# lint pass 117

# rename var 118

# note update 120

# lint pass 121

# tweak params 122

# cleanup 137

# note update 138

# note update 144

# note update 146

# test tweak 147

# lint pass 150

# tweak params 158

# tweak params 160

# lint pass 166

# test tweak 168

# lint pass 171
