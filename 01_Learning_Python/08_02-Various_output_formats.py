# Leave empty spaces blank, align to the right, but secure a total of 10 spaces
print("{0: >10}".format(500))

# Positive numbers are displayed as +, negative numbers are displayed as -
print("{0: >+10}".format(500))

# Underline blanks left aligned
print("{0:_<+10}".format(500))

# Put a comma every 3 digits
print("{0:,}".format(100000000000))

# Put a comma every 3 digits
print("{0:+,}".format(100000000000))

# Comma every 3 digits, add sign, secure digits ^ fill
print("{0:^<+30,}".format(100000000000))

# Decimal point output
print("{0:f}".format(5/3))

# Output a specific number of decimal places (rounded to 3 decimal places)
print("{0:.2f}".format(5/3))