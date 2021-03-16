# define punctuation
punctuations = '''!()-[]{};:'",<>./?@#$%^&*_~'''



wordsfile = open("Duo words.txt", encoding='utf-8')
words = wordsfile.readlines()


newsentencefile = open("NewSentences.txt", encoding='utf-8')
new = newsentencefile.readlines()
print(new)
validword = False
walid = True 
addsen = []
nope = []

for x in new:
    no_punct = ""
    for char in x:
        if char not in punctuations:
            no_punct = no_punct + char
    valid = True
    for w  in no_punct.split():
        validword = False
        print("valid word set to false")
        for check in words:
            #print(check.strip().lower() + " == " + w.strip())
            if check.strip().lower() == w.strip().lower():
                validword = True
                print("valid word is true:  " + check.strip().lower())
                print("HELL YEAH")
        if not validword:
            valid = False
    if valid:
        print(x)
        addsen.append(x)
    else:
        print("BAD " + x)
        nope.append(x)
        

add = open("add.txt", 'a', encoding='utf-8')
add.writelines(addsen)
add.close()

wordsfile.close()
newsentencefile.close()

newsentencefile = open("NewSentences.txt", 'w', encoding='utf-8')

newsentencefile.writelines(nope)