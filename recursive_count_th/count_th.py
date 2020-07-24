'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    #seems similar to sliding window
    #naive is to loop through word until we find a "t", if the next character is "h"
    #increase count
    #we must ignore capital
    #we must stop 1 position before end
    # count = 0
    # for index, letter in enumerate(word):
    #     if index == len(word) - 2:
    #         return count
    #     if letter == "t" and word[index+1] == "h":
    #         count +=1
    # return count
    #base case
    if not word:
        return 0   
    elif word[:2] == "th":
        return 1 + count_th(word[1:])
    else:
        return count_th(word[1:])
    
if __name__ == '__main__':
    count_th("thhtthht")
