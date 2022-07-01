import re

text_to_search = '''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890
Ha HaHa
MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )
coreyms.com
321-555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234
Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T
'''

sentence = 'Start a sentence and then bring it to an end'
#from git hub
# pattern = re.compile(r'start', re.I)
#
# matches = pattern.search(sentence)

#first example
#is case sensitive
# pattern = re.compile(r'abc')
# matches = pattern.finditer(text_to_search)
# for match in matches:
#     print(match)
# print(text_to_search[1:4])

#search for a period
# pattern = re.compile(r'\.')
# matches = pattern.finditer(text_to_search)
# for match in matches:
#     print(match)
# print(text_to_search[1:4])





print(matches)
print ('\tTab')     #print a tab
print (r'\tTab')    #prints \t instead of tabbing, Called Raw

