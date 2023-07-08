import re
# abcd, book, desk
# ca?e
# care, cafe, case, cave

p = re.compile("ca.e") 
# . (ca.e) : a word > care, cafe, case (O) | caffe (X)
# ^ (^de): starting > desk, destination (O) | fade (X)
# $ (se$): end > case, base (O) | face(X)

def print_match(m):
    if m:
        print(f"m.group(): {m.group()}") # matching words return
        print(f"m.string(): {m.string}") # input words return
        print(f"m.start(): {m.start()}") # matching start index
        print(f"m.end(): {m.end()}") # matching end index
        print(f"m.span(): {m.span()}") # matching start/end index


    else:
        print("No Matching")

# m = p.match("careless") # matching from begining so becoming true
# print_match(m)
# # print(m.group())

# m = p.search("good care") # any given words matching
# print_match(m)

lst = p.findall("careless")
print(lst) # return matchign list