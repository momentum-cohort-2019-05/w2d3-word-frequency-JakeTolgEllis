STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with'
]
sentence_list = []
word_list = []
count_data = {}
import re

def clean_text(doc):
    for i in doc:
        sentence_list = i.split(" ")
        for x in sentence_list:
            if (x.lower() not in STOP_WORDS) and (x != ''):
                z = re.sub(r'[^A-Za-z]', '', x)
                word_list.append(z.lower())

def word_count(word):
    return count_data[word]

def print_word_freq(file):
    fullDoc = file.readlines()
    clean_text(fullDoc)
    
    for i in word_list:
        if count_data.get(i) == None:
            count_data[i] = 1
        else:
            count_data[i] = count_data[i] + 1
    list_words= []
    
    for i in count_data:
        list_words.append(i)
        list_words.sort(key = word_count, reverse = True)

    for i in list_words:
            print(i, (" ")*(9 - len(i)), "  |    ", count_data[i], ("*" * count_data[i]))        
            if list_words.index(i) == 9:
                break





if __name__ == "__main__":
    import argparse
    from pathlib import Path

    parser = argparse.ArgumentParser(
        description='Get the word frequency in a text file.')
    parser.add_argument('file', help='file to read')
    args = parser.parse_args()

    try:
        f = open(Path(args.file))
        f.close()
    except FileNotFoundError:
        print("Get outta here! (file not found)")
        exit()
    file = open(Path(args.file))
    print_word_freq(file)
    file.close()    