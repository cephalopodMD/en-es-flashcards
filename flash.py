import csv, random

es2en = {}
with open('es2en.csv', newline='', encoding='utf-8') as file:
    reader = csv.reader(file)
    for row in reader:
        es = row[0]
        ens = row[1:]
        es2en[es] = ens

en2es = {}
with open('en2es.csv', newline='', encoding='utf-8') as file:
    reader = csv.reader(file)
    for row in reader:
        en = row[0]
        ess = row[1:]
        en2es[en] = ess

def is_match(guess, answers):
    if guess in answers:
        return True
    else:
        guess_words = guess.split(' ')
        for answer in answers:
            answer_words = answer.split(' ')
            for guess_word, answer_word in zip(guess_words, answer_words):
                answer_word_possibilities = answer_word.split('/')
                if guess_word not in answer_word_possibilities:
                    break
            else:
                return True
    return False

for word_map in [en2es, es2en] * 5:
    word = random.choice(list(word_map.keys()))
    guess = input(f'{word}: ')
    if is_match(guess, word_map[word]):
        print('  Yay!')
        other_translations = [w for w in word_map[word] if w != guess]
        if other_translations:
            print('  other translations:', ', '.join(other_translations))
        else:
            print('  that\'s the only translation - great job!')
    else: 
        print('  Nope!', )
        print('  translations:', ', '.join(word_map[word]))