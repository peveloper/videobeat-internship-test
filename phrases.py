from sys import argv
import string


def group_words(text, group_size):
    '''
    Returns a list of group_size grouped words
    '''
    word_list = text.split()
    # filter and remove punctuation
    word_list = list(map(lambda w: w.strip(string.punctuation), word_list))
    # filter any blank remaining
    word_list = list(filter(None, word_list))
    # print word_list
    group_list = []
    for k in range(len(word_list)):
        start = k
        end = k + group_size
        group_slice = word_list[start: end]
        if len(group_slice) == group_size:
            group_list.append(" ".join(group_slice))
    return group_list

# parse cmd line arguments
script, filename = argv

# config max group_size and number of result displayed
max_group_size = 5
top_results = 20

# open file
filereader = open(filename)

print "Reading %r ..." % filename, "\n"
text = filereader.read()

phrases = []

for group_size in range(1, max_group_size + 1):
    group_list = group_words(text, group_size)
    group_set = set(group_list)
    for group in group_set:
        count = text.count(group)
        phrases.append((group, (count, count * group_size)))

phrases = sorted(phrases, key=lambda phrase: phrase[1][1], reverse=True)

# print top 20 phrases
for i in range(0, top_results):
    s = "'%s' -> appears %d times with weight %d"
    print (s % (phrases[i][0], phrases[i][1][0], phrases[i][1][1]))
