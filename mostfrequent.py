from collections import Counter

text = "The poem is set in Scandinavia. Beowulf, a hero of the Geats, comes to the aid of Hrothgar," \
       " the king of the Danes, whose mead hall in Heorot has been under attack by a monster known as Grendel. " \
       "After Beowulf slays him, Grendel's mother attacks the hall and is then also defeated. Victorious," \
       " Beowulf goes home to Geatland (Götaland in modern Sweden) and later becomes king of the Geats. " \
       "After a period of fifty years has passed, Beowulf defeats a dragon, but is mortally wounded in the battle." \
       " After his death, his attendants cremate his body and erect a tower on a headland in his memory."

words = text.split()

counter = Counter(words)
top_three = counter.most_common(2)
print(top_three)