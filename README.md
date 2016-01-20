# OEISpy

OEISpy is a Python module that can be used to programmatically accessing
The On-Line Encyclopedia of Integer Sequences®, which is located at www.oeis.org.

## Features
1. OEIS search by sequence elements
2. Direct access to sequences as generators, by search and ID
3. Basic sequence manipulation and operators

### Example use case #1:
A script which produces a sequence of integers.  OEISpy could then be used to automatically check if the given sequence matches any known in the database.

### Example use case #2:
A script can use OEISpy to abstract away accessing the website, and can directly interact with sequences as locally-stored generators.
