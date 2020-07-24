'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    
    # TBC
    # look at the first and second letter of 
    # the word, if it matches t and h then add one to the counter and continue looping
    # else continue recursively being called but now do the second index (1) till the rest so that you can move up
    # pair_count = 0
    while len(word) > 1:
        pair_count = 0
        if word[0] == "t" and word[1] == "h":
          pair_count = pair_count + 1
          count_th(word[2:])
        else:
            count_th(word[1:])
        return pair_count

print(count_th("uderthan"))
            