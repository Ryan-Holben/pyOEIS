# pyOEIS

pyOEIS is a Python module that can be used to programmatically accessing
The On-Line Encyclopedia of Integer Sequences®, which is located at www.oeis.org.  This project is independent of the OEIS Foundation.  Please support them at www.oeisf.org!

[ _This project is on hiatus, but I will update it someday.  I love this stuff, but it's probably not useful to many people._ ]

## Features
1. OEIS search by sequence elements
2. (_future_) Direct access to sequences as generators, by search and ID
3. (_future_) Basic sequence manipulation and operators

### Example use case #1:
A script which produces a sequence of integers.  OEISpy could then be used to automatically check if the given sequence matches any known in the database, allowing the user to identify the underlying pattern in their data or algorithm.

### Example use case #2:
A script can use OEISpy to abstract away accessing the website, and can directly interact with sequences as locally-stored generators.
