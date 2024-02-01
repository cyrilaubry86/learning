



# def mix_up(word1, word2):
#     split1 = []
#     for i in word1:
#         split1.append(i)
#     split2 = []
#     for i in word2:
#         split2.append(i)
    
#     word_1_rest = split1[2:]
#     word_2_rest = split2[2:]
    
#     word_1_first_letters = split2[0:2]
    
#     join1 = "".join(word_1_first_letters)
#     join2 = "".join(word_1_rest)
#     new_word_1 = join1 +  join2
    
#     word_2_first_letters = split1[0:2]
    
#     join3 = "".join(word_2_first_letters)
#     join4 = "".join(word_2_rest)
#     new_word_2 = join3 +  join4
    
#     #return new_word_1 + " " + new_word_2
#     return print(f'{new_word_1}, {new_word_2}')



# mix_up('dog', 'dinner')


# def gerundio(verb):
#     """Turns Spanish infinitive verbs (which end in "ar", "er", "ir")
#     into the gerund forms (which end in "ando" or "iendo).
#     When a verb ends in "ar", the "ar" is replaced with "ando".
#     When a verb ends in "er" or "ir", the end is replaced with "iendo"."""
#     #global verb_joined
#     if verb[-2:] == 'ar':
#         verb_1_split = []
#         for i in verb:
#             verb_1_split.append(i)
#         print(verb_1_split)
#         verb_1_split[-2:] = ['a', 'n', 'd', 'o']
#         print(verb_1_split)
#         verb_1_joined = "".join(verb_1_split)
#         return(verb_1_joined)
        
#     else:
#         verb_1_split = []
#         for i in verb:
#             verb_1_split.append(i)
#         print(verb_1_split)
#         verb_1_split[-2:] = ['i', 'e', 'n', 'd', 'o']
#         print(verb_1_split)
#         verb_1_joined = "".join(verb_1_split)
#         return(verb_1_joined)

  
# gerundio('abrir')




def not_bad(sentence):
    """Returns a new string where the first substring in a sentence
    that starts with "not" and ends with "bad" is replaced by the word "good".
    Returns the original string if no matching substring is found.

    >>> not_bad('This dinner is not that bad!')
    'This dinner is good!'
    >>> not_bad('This movie is not so bad!')
    'This movie is good!'
    >>> not_bad('This dinner is bad!')
    'This dinner is bad!'
    """
    if "not" in sentence:
        start = sentence.find("not")
        split = []
        for i in sentence:
            split.append(i)
        split[start:] = ['g', 'o', 'o', 'd']
        new_sentence = "".join(split)
        return new_sentence + "!"
    else:
        return sentence

        
        
        
        
        
not_bad('This dinner is not that bad!')
#not_bad('This dinner is bad!')