from characters import characters




most_titles = 0



for person in characters:
    num_titles = len(person['titles'])
    if num_titles > most_titles:




for person in characters:
    num_titles = len(person['titles'])
    if num_titles == most_titles:
        print("%s has %d titles" % (person['name'], most_titles))

print("nope that's it")