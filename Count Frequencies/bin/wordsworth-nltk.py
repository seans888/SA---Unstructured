#!/usr/bin/env python

# Name: wordsworth
# Description: Frequency analysis tool
# Licence: GPLv3
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

import re
import collections
import nltk

# Font effects --> fancy console colours in bash
underline = "\x1b[1;4m"
black = "\x1b[1;30m"
red = "\x1b[1;31m"
green = "\x1b[1;32m"
yellow = "\x1b[1;33m"
blue = "\x1b[1;34m"
purple = "\x1b[1;35m"
turquoise = "\x1b[1;36m"
normal = "\x1b[0m"

previous_word = ''
previous_pair = ''
previous_triple = ''
previous_quad = ''

word_stats = {
              'total_chars': 0,
              'total_words': 0,
              'total_sentences': 0,
              'max_length': 0,
              'min_length': 999,
              'mean_length': -1,
              'longest_word': '',
              'shortest_word': '',
              'char_counts': {
                              'a': 0.0, 'b': 0.0, 'c': 0.0, 'd': 0.0, 'e': 0.0, 'f': 0.0,
                              'g': 0.0, 'h': 0.0, 'i': 0.0, 'j': 0.0, 'k': 0.0, 'l': 0.0,
                              'm': 0.0, 'n': 0.0, 'o': 0.0, 'p': 0.0, 'q': 0.0, 'r': 0.0,
                              's': 0.0, 't': 0.0, 'u': 0.0, 'v': 0.0, 'w': 0.0, 'x': 0.0,
                              'y': 0.0, 'z': 0.0
                             },
              'char_percentages': {
                                   'a': 0.0, 'b': 0.0, 'c': 0.0, 'd': 0.0, 'e': 0.0, 'f': 0.0,
                                   'g': 0.0, 'h': 0.0, 'i': 0.0, 'j': 0.0, 'k': 0.0, 'l': 0.0,
                                   'm': 0.0, 'n': 0.0, 'o': 0.0, 'p': 0.0, 'q': 0.0, 'r': 0.0,
                                   's': 0.0, 't': 0.0, 'u': 0.0, 'v': 0.0, 'w': 0.0, 'x': 0.0,
                                   'y': 0.0, 'z': 0.0
                                  },
              'lexical_density': -1,
              'ARI_score': -1
             }


def print_n_word_frequencies(n_word_counter, top_n, output_file, tag=None):
    total_entries = sum(n_word_counter.values())
    unique_entries = len(n_word_counter)
    if total_entries > 0:
        m = n_word_counter.most_common(min(unique_entries, top_n))
        n = len(m[0][0].split(' '))

        if tag == None:
            print '\n===' + blue + ' Commonest ' + str(n) + '-words' + normal + ' ==='
            out.write('\n=== Commonest ' + str(n) + '-words ===\n')
        else:
            print '\n===' + blue + ' Commonest ' + tag + normal + ' ==='
            out.write('\n=== Commonest ' + tag + ' ===\n')

        for i in range(0, min(unique_entries, top_n)):
            n_word = m[i][0]
            count = m[i][1]
            perc = 100.0 * (count / float(total_entries))

            print (str(i + 1) + ' = ' + purple + n_word +
                   normal + ' (' + purple + str(count).split('.')[0] + normal +
                   ' = ' + purple + str(perc)[:5] + '%' + normal + ')')

            output_file.write(str(i + 1) + ' = ' + n_word + ' (' + str(count).split('.')[0] +
            ' = ' + str(perc)[:5] + '%)\n')


def print_results(word_stats, output_file):
    print '\n===' + blue + ' RESULTS ' + normal + '==='
    out.write('=== RESULTS ===\n')

    print 'File = ' + purple + str(args.inputfile) + normal
    out.write('File = ' + str(args.inputfile) + '\n')

    print ('Longest word = ' + purple + str(word_stats['longest_word']) + normal +
           ' (' + purple + str(word_stats['max_length']) + normal + ')')

    out.write('Longest word = ' + str(word_stats['longest_word']) +
           ' (' + str(word_stats['max_length']) + ')\n')

    print ('Shortest word = ' + purple + str(word_stats['shortest_word']) + normal +
           ' (' + purple + str(word_stats['min_length']) + normal + ')')

    out.write('Shortest word = ' + str(word_stats['shortest_word']) +
           ' (' + str(word_stats['min_length']) + ')\n')

    print ('Mean word length /chars = ' + purple + str(word_stats['mean_length']) +
            normal)

    out.write('Mean word length /chars = ' + str(word_stats['mean_length']) + '\n')

    print ('Total words parsed = ' + purple +
            str(word_stats['total_words']).split('.')[0] + normal)

    out.write('Total words parsed = ' +
            str(word_stats['total_words']).split('.')[0] + '\n')

    print ('Total chars parsed = ' + purple + str(word_stats['total_chars']) +
            normal)

    out.write('Total chars parsed = ' + str(word_stats['total_chars']) + '\n')

    for i in range(max_n_word):
        print_n_word_frequencies(counters[i], args.top_n, out)

    print_n_word_frequencies(personal_pronoun_counter, args.top_n, out, tag="Personal Pronouns")
    print_n_word_frequencies(noun_counter, args.top_n, out, tag="Nouns")
    print_n_word_frequencies(adjective_counter, args.top_n, out, tag="Adjectives")
    print_n_word_frequencies(adverb_counter, args.top_n, out, tag="Adverbs")
    print_n_word_frequencies(verb_counter, args.top_n, out, tag="Verbs")

    total_dev = 0.0

    print '\n===' + blue + ' FREQUENCY ANALYSIS ' + normal + '==='
    out.write('\n=== FREQUENCY ANALYSIS ===\n')

    # Display information about character frequencies.
    for char in sorted(word_stats['char_percentages'].iterkeys()):
        bar = ''
        perc = word_stats['char_percentages'][char]

        # Percentage deviation from random distribution of characters.
        dev = 100.0 * (abs((100.0 / 26.0) - perc) / (100.0 / 26.0))
        total_dev += dev

        for i in range(0, int(perc)):
            bar += '#'

        print (char + ' |' + red + bar + normal + ' ' + str(perc)[:4] +
                '% (' + str(dev)[:4] + '% deviation from random)')

        out.write(char + ' |' + bar + ' ' + str(perc)[:4] + '% (' +
                str(dev)[:4] + '% deviation from random)\n')

    print ('\nTotal percentage deviation from random = ' +
            str(total_dev).split('.')[0] + '%')

    out.write('\nTotal percentage deviation from random = ' +
            str(total_dev).split('.')[0] + '%')

    average_dev = total_dev / 26.0

    print ('Average percentage deviation from random = ' +
            str(average_dev)[:4] + '%')

    out.write('\nAverage percentage deviation from random = ' +
              str(average_dev)[:4] + '%')

    print '\n===' + blue + ' WORD LENGTH ' + normal + '==='
    out.write('\n\n=== WORD LENGTH ===\n')

    # Display data above word length frequency.
    length_counts = word_length_counter.most_common()
    for length in length_counts:
        l = length[0]
        perc = 100.0 * length[1] / float(word_stats['total_words'])
        bar = ''
        for i in range(0, int(perc)):
            bar += '#'

        print (l + ' |' + red + bar + normal + ' ' + str(perc)[:4] +
                '% (' + str(length[1]) + ')')

        out.write(l + ' |' + bar + ' ' + str(perc)[:4] +
                '% (' + str(length[1]) + ')\n')

    print ('\nLexical density = ' + str(word_stats['lexical_density'])[:5] + '%')

    out.write('\nLexical density = ' + str(word_stats['lexical_density'])[:5] + '%')

    print ('ARI (Automated Readability Index) score = ' + str(word_stats['ARI_score'])[:5])

    out.write('\nARI (Automated Readability Index) score = ' + str(word_stats['ARI_score'])[:5] + '%')

    print '\nWritten results to ' + args.inputfile.split('.')[0] + '-stats.txt\n'


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description='Perform letter, word and n-tuple frequency analysis on text files.')
    parser.add_argument('--filename', '-f', dest='inputfile', required=True, help='Text file to parse.')
    parser.add_argument('--ntuple', '-n', dest='max_n_word', required=False, default=4, type=int, help='The maximum length n-tuple of words. Default is 4.')
    parser.add_argument('--top', '-t', dest='top_n', required=False, default=20, type=int, help='List the top t most frequent n-words. Default is 20.')
    parser.add_argument('--allow-digits', '-d', dest='allowdigits', default=False, required=False, help='Allow digits to be parsed (true/false). Default is false.')
    parser.add_argument('--ignore', '-i', dest='ignore_list', required=False, help='Comma-delimted list of things to ignore')
 
    args = parser.parse_args()

    ignore_list = str(args.ignore_list).split(",")

    # Dynamically allocated n-word counters
    max_n_word = args.max_n_word
    n_words = ['' for i in range(max_n_word)]
    prev_n_words = ['' for i in range(max_n_word)]
    counters = [collections.Counter() for i in range(max_n_word)]

    # Word length counter
    word_length_counter = collections.Counter()

    # Read in all of the words in a file
    print "[+] Reading text from '" + args.inputfile + "'..."
    text = open(args.inputfile).read().lower()

    # Use nltk to classify/tag each word/token.
    print "[+] Tokenizing text..."
    text = open(args.inputfile).read().lower()
    tokenizer = nltk.tokenize.RegexpTokenizer(r'\w+|[^\w\s]+')
    tokens = tokenizer.tokenize(text)

    print "[+] Tagging tokens..."
    tagger = nltk.UnigramTagger(nltk.corpus.brown.tagged_sents())
    tagged_tokens = tagger.tag(tokens)

    print "[+] Tallying tags..."
    personal_pronoun_counter = collections.Counter()
    adjective_counter = collections.Counter()
    adverb_counter = collections.Counter()
    noun_counter = collections.Counter()
    verb_counter = collections.Counter()

    for token in tagged_tokens:

        if token[1] == None:
            continue

        elif 'PPS' in token[1]:
            personal_pronoun_counter[token[0]] += 1

        elif 'JJ' in token[1]:
            adjective_counter[token[0]] += 1

        elif 'NN' in token[1]:
            noun_counter[token[0]] += 1

        elif 'RB' in token[1]:
            adverb_counter[token[0]] += 1

        elif 'VB' in token[1]:
            verb_counter[token[0]] += 1

    # Shall we include digits?
    if args.allowdigits:
        words = re.findall(r"['\-\w]+", text)
    else:
        words = re.findall(r"['\-A-Za-z]+", text)

    print "[+] Counting sentences..."
    word_stats['total_sentences'] = len(nltk.sent_tokenize(text.decode('utf-8')))

    print "[+] Performing frequency analysis of n-words..."
    for word in words:
    
        if word in ignore_list:
            continue
        
        word = word.strip(r"&^%$#@!")

        # Allow hyphenated words, but not hyphens as words on their own.
        if word == '-':
            continue

        # Record all word lengths
        length = len(word)
        word_length_counter[str(length)] += 1

        # Record longest word length
        if length > word_stats['max_length']:
            word_stats['max_length'] = length
            word_stats['longest_word'] = word

        # Record shortest word length
        if length < word_stats['min_length']:
            word_stats['min_length'] = length
            word_stats['shortest_word'] = word

        # Keep track of the total number of words and chars read.
        word_stats['total_chars'] += length
        word_stats['total_words'] += 1.0

        # Tally the charaters in each word.
        for char in word:
            if char.lower() in word_stats['char_counts']:
                word_stats['char_counts'][char.lower()] += 1.0

        # Tally words.
        for i in range(1, max_n_word):
            if prev_n_words[i - 1] != '':
                n_words[i] = prev_n_words[i - 1] + ' ' + word
                counters[i][n_words[i]] += 1

        n_words[0] = word
        counters[0][word] += 1

        for i in range(0, max_n_word):
            prev_n_words[i] = n_words[i]

    # Calculate the mean word length
    word_stats['mean_length'] = word_stats['total_chars'] / word_stats['total_words']

    # Calculate relative character frequencies
    for char in word_stats['char_counts']:
        char_count = word_stats['char_counts'][char]
        total_chars = word_stats['total_chars']
        percentage = 100.0 * (char_count / total_chars)
        word_stats['char_percentages'][char] = percentage

    # Calculate the lexical density of the text.
    total_unique_words = len(counters[0])
    total_words = sum(counters[0].values())
    word_stats['lexical_density'] = 100.0 * total_unique_words / float(total_words)

    # Calculate the ARI score.
    # See http://www.usingenglish.com/members/text-analysis/help/readability.html
    total_words = sum(counters[0].values())
    ASL = total_words / float(word_stats['total_sentences'])
    ALW = word_stats['total_chars'] / float(total_words)
    word_stats['ARI_score'] = (0.5 * ASL) + (4.71 * ALW) - 21.43

    # Print results
    out = open(args.inputfile.split('.')[0] + '-stats.txt', 'w')
    print_results(word_stats, out)
    out.close()
