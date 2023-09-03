def _detectPunctuation(plainText):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    punctuationList = []
    i = 0
    for character in plainText:
        # if the character is not present in the alphabet, add it to the punctuation list
        if character not in alphabet:
            punctuationList.append(str(i) + "-" + character) # append the index followed by the chracter to the list
    return punctuationList

def _removePunctuation(plainText, punctuationList):
    plainText = list(plainText)
    for i in range(len(punctuationList)):
        listItem = punctuationList[i]
        index = int(listItem[0])
        plainText[index] = "#" # replace the punctuation with a hashtag
    return plainText # return the modified plain text

def _restorePunctuation(plainText, punctuationList):
    plainText = list(plainText)
    for i in range(len(punctuationList)):
        listItem = punctuationList[i].split("-") # get the item from the list, then split it into index and char
        index = int(listItem[0])
        character = listItem[1]
        plainText[index] = character # replace the placeholder char in plainText with the correct punctuation
    return plainText # return the modified plain text