# Web crawler and analysis

Preprocessing:
* Find all unknown words, then
* Create map of abbreviation => stem
* ... and acronym => expanded
* Convert values to MKS system of measure
* Possible to apply units to values when unit is in title?

Canonicalization:
* Lemmatize / stem and identify unknowns
* Map unknowns to stem
* Identify similar attributes - automatic: same stems, manual: partial matches and no matches
* Canonicalize all attributes and annotate data

Features:
* Bag of words (titles and values)
* Digit present
* Decimal present
* Units present

Clustering:
* Count of units in common
* Range of values have overlap

Debugging:
* Unidentified words
* Unitless values
