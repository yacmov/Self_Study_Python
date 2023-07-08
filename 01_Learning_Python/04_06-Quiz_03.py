# Example) http://naver.com
# Rule 1: Excluding http:// => naver.com
# Rule 2: Excluding the part after the first dot (.) => naver
# Rule 3: The first three remaining letters + the number of letters + the number of 'e's in the letter + "!" composed of
#                        (nav)                         (5)                           (1)                 (!)

# Example) Generated password: nav51!

original_url = "http://naver.com"
url = original_url.replace("http://", "")
url = url[:url.find(".")]
#print(url)
password = url[:3] + str(len(url)) + str(url.count("n")) + "!"
print("Site name \t\t: {0} \nGenerated password \t: {1}".format(original_url, password))
