'''
replace spaces with %20
note: s.replace() returns a new string
'''
def urlify(s,len):
    s1=s.replace(" ","%20")
    return s1[:len]

print(urlify("Mr John Smith     ",13))
