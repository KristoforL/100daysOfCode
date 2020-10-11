#Python Module of the week wehere I will be looking into the strings constants and templates

#Capwords: This function capitalizes the words in the string

import string

s = "i really like pie. i can't wait for thanksgiving."
print(s)
print(string.capwords(s))

#You can get the same results from splitting the string capitalizing each word then joining them back together. 

#Templates: 

values = {'var' : 'foo'}

t = string.Template("""
Variable : $var
Escape : $$
Variable in text: ${var}iable
""")

print('TEMPLATE:', t.substitute(values))

s = """
Variable        : %(var)s
Escape          : %%
Variable in text: %(var)siable
"""

print('INTERPOLATION:', s % values)

s = """
Variable        : {var}
Escape          : {{}}
Variable in text: {var}iable
"""

print('FORMAT:', s.format(**values))
