from collections import defaultdict

# Dataset contains data that will be reverse indexed
dataset = [
    "Hello world",
    "This is the WORLD",
    "hello again"
 ] 

def reverse_index(dataset):
    lowset = list(map(lambda x: x.lower(), dataset))

    index_dictionary = {}
    templs = []
    for i, string in enumerate(lowset):
        templs = (string.split(" "))
        for word in templs:
            if word in index_dictionary:
                index_dictionary.update(word = index_dictionary[word].append(i))
            else:
                index_dictionary[word] = [i]
        templs = []
    index_dictionary = {k: v for k, v in index_dictionary.items() if v is not None}
    return index_dictionary
    # don't forget to return your resulting dictionary

# You can see the output of your function here
print(reverse_index(dataset))
