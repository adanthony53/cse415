def five_x_cubed_plus_1(x):
    return 5*(x**3)+1

def pair_off(l):
    res = []
    if len(l) == 0:
        return res
    
    num = 0
    for item in l:
        if num % 2 == 0:
            temp = [item]
        else:
            temp.append(item)
            res.append(temp)
        num = num + 1
    
    if len(temp) == 1:
        res.append(temp)
    return res

def mystery_code(text):
    if type(text) != str:
        return "Invalid Input!"
    res = ""
    for ch in text:
        if ch.isalpha():
            if ch.isupper():
                CH = chr(97 + (ord(ch) - 46) % 26)
            else:
                CH = chr(65 + (ord(ch) - 78) % 26)
        else:
            CH = ch

        res = res + CH
    return res

def past_tense(words):
    res = []
    irregulars = {'have':'had', 'to have':'had', 'be':'was', 'to be':'was', 
        'eat':'ate', 'to eat':'ate', 'go':'went', 'to go':'went', 
        'to is':'was', 'to are':'were', 'to am':'was', 
        'is':'was', 'are':'were', 'am':'was'}
    vowel = ["a", "e", "i", "o", "u"]
    consonant = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m",
                 "n", "p", "q", "r", "s", "t", "u", "v", "x", "z"]
    for word in words:
        if word in irregulars:
            res.append(irregulars[word])
        elif word.endswith("e"):
            res.append(word + "d")
        elif word.endswith("y") and word[-2] not in vowel:
            res.append(word[:-1] + "ied")
        elif (word[-1] in consonant and 
              word[-2] in vowel and 
              word[-3] not in vowel):
            res.append(word + word[-1] + "ed")
        else:
            res.append(word + "ed")
    return res
