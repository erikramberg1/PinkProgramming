#
# Get input from user, lower ensures that comparison is fair
#

wordinput=input("Please input a word ").lower()


#
# Create starting parameters
#
# The variable storage is used for comparisons
#
storage=wordinput[0] #      collect the first letter from the word.
checkword=wordinput[1:] #   remove the first letter from the word, and put it into a new variable
state=0 #                   State is important, because it determines the results of a break of the whileloop below

#
# While loop, as long as there are letters we can compare letters, when one letter is left, it is unique
#

while len(checkword) >=1:

    #
    # Create a variable and insert data corresponding to where the letter stored in storage can be found in the rest of the word
    #

    duplicatevalue=checkword.find(storage)

    #
    # If the letter is duplicated it will return an index, larger than -1
    # If that is the case we want to remove that letter from our checkword
    #
    if duplicatevalue > -1:
        checkword=checkword.replace(str(storage),"")

        #
        # If we are down to our last letter through this loop, the last letter must be unique
        #

        if len(checkword) == 1:
            storage=checkword[0]
            print ("The letter {} is the first unique letter in this word".format(storage))
            state = 1
            break

        #
        # If we are down to no letters with this loop, there are NO unique letters
        #

        if len(checkword) <=0:
            break


        #
        # After our edits we need to update the letter we are comparing, and the word we are comparing to
        #

        storage = checkword[0]
        checkword = checkword[1:]

    #
    # If the letter is unique, the index returns -1, in that case we return this info and break the loop
    # state is changed so that the last message "no unique letters" isn't sent.
    #

    else:
        print ("The letter {} is the first unique letter in this word".format(storage))
        break
        state = 1
#
# If we reach this code, there are no unique letters in the word
#

if state == 0:
    print("There are no unique letters in this word")