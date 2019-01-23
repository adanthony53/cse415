from random import choice
from re import *

GREETINGS = ['hey', 'hi', 'hello', "hola"]
GOODBYES = ['ciao', 'goodbye', 'bye']

NICKNAMES = ['bro', 'man', 'dude', 'fellas']

PLAYERS = ['Tyler Lockett','Doug Baldwin','Bobby Wagner',
'Kam Chancellor','Michael Dickson','Frank Clark']

TEAMS = ['49ers','Rams','Cowboys','Packers','Bears','Broncos',
'Bills','Dolphins','Patriots','Jets','Giants','Eagles','Redskins',
'Ravens','Bengals','Browns','Steelers','Lions','Vikings','Texans',
'Colts','Jaguars','Titans','Falcons','Panthers','Saints','Bucs',
'Chiefs','Chargers','Raiders','Cardinals']

PLACES = ['Arizona','LA','SF','Denver','KC','Oakland','Tennessee',
'Jacksonville','Houston','Indiana','Atlanta','Carolina','New Orleans',
'Tampa','Chicago','Detroit','Green Bay','Minnesota','Baltimore',
'Cincinnati','Cleveland','Pittsburgh','Washington','New York','Philly',
'Dallas','Boston','Miami','Buffalo']

#######################################################
# cyclic counts 

w_questions_count = 0
action_word_count = 0
you_are_count = 0
i_am_count = 0
default_count = 0

#######################################################

def empty_wordlist(wordlist, map):
    if wordlist[0] == '':
        return "Are you too shy to say something?"
    return False

def greeting(wordlist, map):
    if wordlist[0] in GREETINGS:
        return choice(GREETINGS) + " " + choice(NICKNAMES) + "!"
    return False

# cycling feature
def w_questions(wordlist, map):
    w = wordlist[0]
    if wpred(w):
        global w_questions_count
        w_questions_options = ["I dont know the answer.",
        "I wish I know the answer for the " + choice(TEAMS) + '.',
        "Ask " + choice(PLAYERS) + "for more informaiton."]
        w_questions_count += 1
        return w_questions_options[w_questions_count % 3]
    return False

# cycling feature
def action_word(wordlist, map):
    w = wordlist[0]
    if verbp(w):
        global action_word_count
        action_options = ["I " + w + " if I have to.",
        "I " + w + " everytime I play the " + choice(TEAMS) + '.',
        "I am not sure if I " + w + ". Ask " + choice(PLAYERS) + " for more informaiton."]
        action_word_count += 1
        return action_options[action_word_count % 3]
    return False

#
def keyword(wordlist, map):
    options = []
    if 'fan' in wordlist:
        return "Thanks for you support! I have to prepare for with the next game at" + choice(PLACES) + '.'

    if 'goal' in wordlist:
        return 'Winning more superbowl championships and beat the ' + choice(TEAMS) + '.'

    if 'dream' in wordlist:
        return 'Be the Greatest Of All Time with ' + choice(PLAYERS) + '.'

    if 'contract' in wordlist:
        return choice(['I want to get paid for what I am capable of.', 
        'I do not care about salary.',
        'I want a max contrac.t',
        'I want to be the highest paid player.',
        'I want to win more championship, money doesnt matter.'])

    if 'extend' in wordlist:
        return choice(['I will extend with the Seahawks.', 
        'I do not care about teams.',
        'I will explore my options.',
        'I do not want to be in Seattle.',
        'I want to win more championship, teams dont matter.'])

    return False

# cycling feature
def you_are(wordlist, map):
    if wordlist[0:2] == ['you', 'are'] or wordlist[0:2] == ['are', 'you']:
        global you_are_count
        you_are_count += 1
        you_are_options = ["Of course, I am " + stringify(map[2:]) + '.',
                           "You should tell me more about yourself.",
                           "Yes. Only after I beat the" + choice(TEAMS) + " with " + choice(PLAYERS) + "."]
        return you_are_options[you_are_count % 3]
    return False

# cycling feature
def i_am(wordlist, map):
    if wordlist[0:2] == ['i', 'am']:
        global i_am_count
        i_am_count += 1
        print(i_am_count)
        i_am_options = ["Of course, you are " + stringify(map[2:]) + '.',
                           "Thats sounds really interesting.",
                           "You should come to the next game to see " + choice(PLAYERS) + "."]
        return i_am_options[i_am_count % 3]
    return False

#
def who_are_you(wordlist, map):
    if len(wordlist) > 2 and wordlist[0:3] == ['who', 'are', 'you']:
        return 'I am the quarterback for the Seahawks and I play with ' + choice(PLAYERS) + '.' 
    return False

#
def do_you(wordlist, map):
    if wordlist[0:2] == ['do', 'you'] or wordlist[0:2] == ['did', 'you']:
        return "No, I have to make time to practice with " + choice(PLAYERS) + "."
    return False

#
def can_you(wordlist, map):
    if wordlist[0:2] == ['can', 'you'] or wordlist[0:2] == ['could', 'you']:
        return "Of course! If you dont believe me, ask " + choice(PLAYERS) + '.'
    return False

#
def have_you(wordlist, map):
    if wordlist[0:2] == ['have', 'you'] or wordlist[0:2] == ['had', 'you']:
        return "I dont remember. I have to ask " + choice(PLAYERS) + " to make sure."
    return False

#
def will_you(wordlist, map):
    if wordlist[0:2] == ['will', 'you'] or wordlist[0:2] == ['would', 'you']:
        return "I am not sure. I might try that in " + choice(PLACES) + "."
    return False

#
def i_feel(wordlist, map):
    if wordlist[0:2] == ['i', 'feel']:
        i_feel_options = ['Sometimes, I feel the same way.',
            'I have never feel that way before. Can you describe more?']
        return choice(i_feel_options)
    return False

#
def you_feel(wordlist, map):
    if wordlist[0:2] == ['you', 'feel']:
        you_feel_options = ['How do you know that? I actually feel that everyday.',
            'I have never feel that way before.']
        return choice(you_feel_options)
    return False


#
def default_response():
    default_options = ['Thanks guys! Go hawks!',
                         'Sometimes, I want to throw more passes. Do you know that?',
                         "I always consider Aaron Rodgers as a great QB.",
                         'Do you have the feeling that our coach chews way too much gum?',
                         "Talk to you after I dropped off my son.",
                         'Just tell me how you feel now.']
    global default_count
    default_count += 1
    return default_options[default_count % 6]

#######################################################
# memory feature

memory = []

def remember_memory(map):
    memory.append(stringify(map))

def recall_remark():
    if len(memory) < 1:
        return "Sorry, I dont quite remember you said much."
    
    old_remark = choice(memory[:-1])
    recall = ['You said that ' + old_remark + ' earlier, Lets go back to that for a while',
                'Emmmmmm.. Do you not remeber telling me ' + old_remark + '? Huh?']
    return choice(recall)


#######################################################
# complete random feature

def random_response():
    random_options = ['I actually think Sony headphones are better than Bose',
        'I want to chew as much as gums like Coach Carroll.',
        'I cannot tell if the Rams have any future plans.',
        'I guess the ' + choice(TEAMS) + ' will win the superbowl champs in 20 year.']
    return choice(random_options)

def super_random_response():
    super_random_response = ['I wish I play for the ' + choice(TEAMS) + ', they dont have any gameplans, I like that!',
        'I hope I never have to face ' + choice(PLAYERS) + ' in my career.',
        'I hope the Seahawks are located at ' + choice(PLACES) + '.']
    return choice(super_random_response)


######################################################
# check bye(end) statement

def bye_statement(s):
    return s in GOODBYES

######################################################
# preprocessing from shrink

PUNTS = ['Please go on.',
         'Tell me more.',
         'I see.',
         'What does that indicate?',
         'But why be concerned about it?',
         'Just tell me how you feel.']

punt_count = 0

def punt():
    'Returns one from a list of default responses.'
    global punt_count
    punt_count += 1
    return PUNTS[punt_count % 6]

def stringify(wordlist):
    'Create a string from wordlist, but with spaces between words.'
    return ' '.join(wordlist)

punctuation_pattern = compile(r"\,|\.|\?|\!|\;|\:")    

def remove_punctuation(text):
    'Returns a string without any punctuation.'
    return sub(punctuation_pattern,'', text)

def wpred(w):
    'Returns True if w is one of the question words.'
    return (w in ['when','why','where','how'])

def dpred(w):
    'Returns True if w is an auxiliary verb.'
    return (w in ['do','can','should','would'])

def remove_punctuation(input):
    'Returns a string without any punctuation.'
    return sub(punctuation_pattern,'', input)

CASE_MAP = {'i':'you', 'I':'you', 'me':'you','you':'me',
            'my':'your','your':'my',
            'yours':'mine','mine':'yours','am':'are'}

def you_me(w):
    'Changes a word from 1st to 2nd person or vice-versa.'
    try:
        result = CASE_MAP[w]
    except KeyError:
        result = w
    return result

def you_me_map(wordlist):
    'Applies YOU-ME to a whole sentence or phrase.'
    return [you_me(w) for w in wordlist]

def verbp(w):
    'Returns True if w is one of these known verbs.'
    return (w in ['go', 'have', 'be', 'try', 'eat', 'take', 'help',
                  'make', 'get', 'jump', 'write', 'type', 'fill',
                  'put', 'turn', 'compute', 'think', 'drink',
                  'blink', 'crash', 'crunch', 'add'])

