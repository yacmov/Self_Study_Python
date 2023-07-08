jumin = "990120-1234567"

print("Gender\t\t: " + jumin[7]) # Get the 7th information
print("Year\t\t: " + jumin[:2]) # Brings information from 0 to just before 2.
print("Month\t\t: " + jumin[2:4])
print("Day\t\t: " + jumin[4:6])
print("Birthday\t: " + jumin[:6])

print("Last 7 numbers\t: " + jumin[7:])
print("Last 7 numbers\t: " + jumin[-7:])