import re

def regexAnwsers_self():
    # open and read the file after the appending:
    f = open("regexRead.txt", "r")
    textOutput = f.read()
    print(textOutput)
    f.close()
    print("-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-")
    print("Is |The Dark Knight| in the list")
    print(text_match(textOutput, "The Dark Knight"))
    return

def text_match(sourceText, findingg):
        patterns = findingg
        if re.search(patterns, sourceText):
            return 'Found a match!'
        else:
            return ('Not matched!')

def regexVideo():
    f = open("myData.txt")
    contents = f.read()
    userinput = input("Enter 1 to view XXX.XXX.XXXX"
                      "\nEnter 2 to view emails"
                      "\nEnter 3 for urls")
    #following get 9 digit numbers from text file myData.txt
    if(int(userinput) == 1):
        #\d means digit and . and any character so can get a phone number from lists
        pattern = re.compile(r'\d\d\d.\d\d\d.\d\d\d\d')
        matches = pattern.finditer(contents)
        for match in matches:
            print(match)
    elif(int(userinput) == 2):
        #following gets CoreyMSchafer@mail, corey.schafer@university.edu, corey-321-schafer@my-work.net
        #online example (r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+') - gets and letter,dot,plus,minus,number,underscore as name followed by @ then number,letter,minus
        #and then a . followed by letter,number, minus, dot,
        pattern = re.compile(r'[a-zA-Z0-9.-]+@[a-zA-Z-]+\.(com|edu|net)')
        matches = pattern.finditer(contents)
        for match in matches:
            print(match)
    elif(int(userinput) == 3):
       urls = '''
       https://www.google.com
       http://coreyms.com
       https://youtube.com
       https://www.nasa.gov
       '''
       #printing groups
       pattern = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')
       #subbed string
       subbed_urls = pattern.sub(r'\2\3', urls)
       print(subbed_urls)
       matches = pattern.finditer(urls)

       for match in matches:
           print(match.group(0))#group 0 is whole group
           print("group 1", match.group(1))
           print("group 2", match.group(2))
           print("group 3", match.group(3))

