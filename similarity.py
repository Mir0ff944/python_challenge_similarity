import re

# asks user to input 2 strings
while True:
    string1, string2 = raw_input ("Enter a string: "), raw_input("Enter second string: ")
    if re.match("^[a-zA-Z\s]*$", string1) and re.match("^[a-zA-Z\s]*$", string2):
        break
    else:
        print "Please enter a valid string. No numbers or other symbols allowed"


def similarity_check(str1, str2):

    # using filter and lambda expression to remove empty spaces between the strings
    str1 = filter(lambda x: x !=" ", str1)
    str2 = filter(lambda x: x !=" ", str2)

    # empty list to store similar letters
    similar = []

    # nested for loop to check each and every letter from both strings
    # when there are similar letters, they will be appendet to the list
    for letter in str1:
        for x in str2:
            if letter == x:
                similar.append(x)

    # calculating the similarity ration between both strings
    # and rounding it up to 2 numbers after the decimal
    ratio = round(float(len(similar))/(len(str1) + len(str2)), 2)

    print 'The similarity ratio is %s between "%s" and "%s"' %(ratio, str1, str2)

    # simple if statement to print false if the strings are completely different
    if ratio == 0.0:
        return False
    else:
        return ratio

# calling the function with the 2 string parameters
similarity_check(string1, string2)
