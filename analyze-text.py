# End Goal: compare two text files containing the output from an OCR'd PDF - one by Adobe and 
# one by me. Give each file a utility score, presumably stating how useful that output would be.

# read text from ocr-by-adobe.pdf
# read text from ocr-by-myapp.pdf

# count # of "words" in ocr-by-adobe.pdf
# count # of "words" in ocr-by-myapp.pdf

# compare list of "words" from ocr-by-adobe.pdf to dictionary words and total
# compare list of "words" from ocr-by-myapp.pdf to dictionary words and total

# output a table with word counts and valid word % for each file

# Other things to know:
#   * number of pages with/without text
#   * maybe get word frequency, just to see?
#   * maybe add a list of words to exclude from score?