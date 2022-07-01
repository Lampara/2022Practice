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
    #following get 9 digit numbers from text file myData.txt
    pattern = re.compile(r'\d\d\d.\d\d\d.\d\d\d\d')
    matches = pattern.finditer(contents)

    for match in matches:
        print(match)

        #stoped at 19:17
