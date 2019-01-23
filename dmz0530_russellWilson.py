from re import *
from rw3_rules import *


def chatbot():
    'Russell Wilson is the top-level chatbot, contianing the main loop.'
    print(introduce())
    while True:
        theInput = input('TYPE HERE:>> ')
        wordlist, _ = text_processing(theInput)
        if bye_statement(wordlist[0]):
            print('Goodbye!')
            return
        print(respond(theInput))

def introduce():
    return ('I am Russell Wilson, quarterback of the Seattle Seahawks.' +\
    '\n You can contact my agent Mingzhong Deng at dmz0530@uw.edu.')

def agentName():
    return "RW3"

#########################################

total = 0
have_greeting = False
have_random_response = False
have_super_random = False
have_memory = False
have_default = False

def respond(theInput):
    global total
    global have_greeting
    global have_random_response
    global have_super_random
    global have_memory
    global have_default

    total += 1
    wordlist, map = text_processing(theInput)

    # empty statements
    res = empty_wordlist(wordlist, map)
    if res != False:
        return res

    # greeting (at most once)
    if have_greeting == False:
        res = greeting(wordlist, map)
        if res != False:
            have_greeting = True
            return res

    remember_memory(map)

    # respond w questions
    res = w_questions(wordlist, map)
    if res != False:
        return res

    # respond action word statements
    res = action_word(wordlist, map)
    if res != False:
        return res

    # respond keyword statements
    res = keyword(wordlist, map)
    if res != False:
        return res

    # respond you are xxx statements
    res = you_are(wordlist, map)
    if res != False:
        return res

    # respond i am xxx statements
    res = i_am(wordlist, map)
    if res != False:
        return res

    # respond who are you questions
    res = who_are_you(wordlist, map)
    if res != False:
        return res

    # respond do you questions
    res = do_you(wordlist, map)
    if res != False:
        return res

    # respond can you questions
    res = can_you(wordlist, map)
    if res != False:
        return res

    # respond have you questions
    res = have_you(wordlist, map)
    if res != False:
        return res

    # respond will you questions
    res = will_you(wordlist, map)
    if res != False:
        return res
    
     
    # memory feature
    if have_memory == False and total > 8:
        res = recall_remark()
        if res != False:
            have_memory = True
            return res
    

    # i feel statements
    res = i_feel(wordlist, map)
    if res != False:
        return res

    # you feel statements
    res = you_feel(wordlist, map)
    if res != False:
        return res

    # random response
    if have_random_response == False:
        have_random_response = True
        return random_response()

    # super random response
    if have_super_random == False:
        have_super_random = True
        return super_random_response()

    # default response
    have_default = True
    return default_response()


def text_processing(input):
    wordlist = split(' ', remove_punctuation(input))
    wordlist[0] = wordlist[0].lower()
    map = you_me_map(wordlist)
    map[0] = map[0].capitalize()
    return (wordlist, map)

if __name__ == "__main__":
    chatbot()