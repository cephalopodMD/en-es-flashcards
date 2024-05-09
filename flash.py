import csv, random

pronoun_equivalents = [
    ['he', 'she', 'you-formal'], 
    ['they', 'you-plural'],
    ['him', 'her']
]
pronoun_equivalents_map = {}
for ps in pronoun_equivalents:
    for p in ps:
        pronoun_equivalents_map[p] = ps

es2en = {}
en2es = {}
with open('es2en.csv', newline='', encoding='utf-8') as file:
    reader = csv.reader(file)
    for row in reader:
        es = row[0]
        ens_raw = row[1:]
        ens = set(ens_raw)
        for en in ens_raw:
            words = en.split(' ')
            for i, word in enumerate(words):
                if '/' in word:
                    for option in word.split('/'):
                        ens.add(' '.join(words[:i] + [option] + words[i+1:]))
                elif word in pronoun_equivalents_map:
                    for option in pronoun_equivalents_map[word]:
                        ens.add(' '.join(words[:i] + [option] + words[i+1:]))
        es2en[es] = list(ens)
        for en in ens:
            en2es[en] = en2es.get(en, [])
            en2es[en].append(es)

correct = 0
for i in range(100):
    word_map = [en2es, es2en][i%2]
    word = random.choice(list(word_map.keys()))
    guess = input(f'{word}: ')
    if guess in word_map[word]:
        print('  Good job!')
        other_translations = [w for w in word_map[word] if w != guess]
        if other_translations:
            print('  other translations:', ', '.join(other_translations))
        else:
            print('  that\'s the only translation you know')
        correct += 1
    else: 
        print('  Nope!', )
        translations = word_map[word]
        if len(translations) > 1:
            print('  translations:', ', '.join(translations))
        else:
            print('  translation:', translations[0])
    print(f'  {100 * correct/(i+1):.1f}% correct so far')