# importing external module from difflib library
from difflib import SequenceMatcher

# asks user to input 2 strings
string1, string2 = raw_input ("Enter a string: "), raw_input("Enter second string: ")

# defining similarity function, requiring 2 paraments
def similarity_str(str1, str2):
    # calling the external module with first parameter to skip empty spaces and 2 strings
    match = SequenceMatcher(lambda x:x == " ", str1, str2)
    # calculating ration and rounding it up to 2 spaces after the decimal
    strratio = round(match.ratio(), 2)

    print 'The similarity ratio is %s between "%s" and "%s"' %(strratio, str1, str2)

    # simple if statement to print false if the strings are completely different
    if strratio == 0.0:
        return False
    else:
        return strratio

# calling the function with the 2 string parameters
similarity_str(string1, string2)
