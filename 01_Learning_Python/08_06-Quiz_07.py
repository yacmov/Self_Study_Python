# Your company has a report that needs to be completed once a week.
# Reports should always be output in the form shown below.

# - x Weekly Report -
# Department :
# Name :
# Job summary:

# Write a program that creates a report file from week 1 to week 50.

# Condition: Create file names like 'Week 1.txt', 'Week 2.txt', ....


for i in range(1,51):
    with open("Week {0}.txt".format(str(i).zfill(2)), "w", encoding="utf8") as reports:
        reports.write("- {0} weekly Report - \nDepartment :\nName : \nJob summary :".format(str(i).zfill(2)))
        
