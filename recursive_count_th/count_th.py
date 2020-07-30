'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    
    # TBC
    # cur_letter = 0
    # next_letter = 1

    if len(word) < 2: 
        return 0
    if word[0] is 't' and word[1] is 'h':

        return 1 + count_th(word[1:])
    else:
        return count_th(word[1:])
            
    



a_word = 'ththeththtt'
print(a_word[2:len(a_word)])

print(count_th(a_word))