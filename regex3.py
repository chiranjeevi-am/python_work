#3. Companies in europe reports their financial numbers of semi annual basis and you can have a document like this.
# To exatract quarterly and semin annual period you can use a regex as shown below

text = '''
Tesla's gross cost of operating lease vehicles in FY2021 Q1 was $4.85 billion.
BMW's gross cost of operating vehicles in FY2021 S1 was $8 billion.
'''

import re
pattern = 'FY(\d{4}) (Q[1-4]|S[1-2]) [^\$]* \$([\d\.]*)'

pattern1 = 'FY(\d{4} (?:Q[1-4]|S[1-2])) [^$]* \$([\d\.]*)'

pattern2 = 'FY(\d{4}) (Q[1-4]|S[1-2]) [^$]* \$([\d\.]*)'

t = re.findall(pattern, text)
t1 =re.findall(pattern1, text)

t2 = re.findall(pattern2,text)
print(t)
print(t1)
print(t2)