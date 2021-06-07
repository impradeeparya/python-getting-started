# Define a string s = 'colorless'. Write a Python statement that changes this to "colourless" using only the slice and concatenation operations.

s = 'colorless'
print(s[:4] + 'u' + s[4:])
