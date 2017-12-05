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

from __future__ import print_function # for Python 2 backwards compatibility
from blessings import Terminal
import collections
import re

# Blessings for terminal colors
term  = Terminal()
underline = term.underline
black = term.black
red = term.red
green = term.green
yellow = term.yellow
blue = term.blue
purple = term.purple
turquoise = term.turquoise
normal = term.normal

class wordsworth:
    args = 0
    ignore_list = []
    out = 0
    words = []
    previous_word = ''
    previous_pair = ''
    previous_triple = ''
    previous_quad = ''
    max_n_word = 4
    n_words = []
    prev_n_words = []
    counters = []

    word_stats = {
                  'total_chars': 0,
                  'total_words': 0,
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
                  'lexical_density': -1
                  }


    def __init__(self, commandline_args):
        args = commandline_args
        self.ignore_list = str(args.ignore_list).split(",")
        

    def print_n_word_frequencies(self, n_word_counter):
        total_entries = sum(n_word_counter.values())
        unique_entries = len(n_word_counter)
        if total_entries > 0:
            m = n_word_counter.most_common(min(unique_entries, args.top_n))
            n = len(m[0][0].split(' '))

            print('\n===' + blue + ' Commonest ' + str(n) + '-words' + normal + '===')

            for i in range(0, min(unique_entries, args.top_n)):
                n_word = m[i][0]
                count = m[i][1]
                perc = 100.0 * (count / float(total_entries))

                print((str(i + 1) + ' = ' + purple + n_word +
                    normal + ' (' + purple + str(count).split('.')[0] + normal +
                    ' = ' + purple + str(perc)[:5] + '%' + normal + ')'))


    def print_results(self):
        print('\n===' + blue + ' RESULTS ' + normal + '===')

        print('File = ' + purple + str(args.inputfile) + normal)
        print('Longest word = ' + purple + str(self.word_stats['longest_word']) + normal +
            ' (' + purple + str(self.word_stats['max_length']) + normal + ')')

        print('Shortest word = ' + purple + str(self.word_stats['shortest_word']) + normal +
            ' (' + purple + str(self.word_stats['min_length']) + normal + ')')

        print('Mean word length /chars = ' + purple + str(self.word_stats['mean_length']) +
                normal)

        print('Total words parsed = ' + purple +
                str(self.word_stats['total_words']).split('.')[0] + normal)

        print('Total chars parsed = ' + purple + str(self.word_stats['total_chars']) +
                normal)

        for i in range(self.max_n_word):
            self.print_n_word_frequencies(self.counters[i])

        total_dev = 0.0
        print('\n===' + blue + ' FREQUENCY ANALYSIS ' + normal + '===')
        for char in sorted(iter(self.word_stats['char_percentages'])):
            bar = ''
            perc = self.word_stats['char_percentages'][char]

            # Percentage deviation from random distribution of characters.
            dev = 100.0 * (abs((100.0 / 26.0) - perc) / (100.0 / 26.0))
            total_dev += dev

            for i in range(0, int(perc)):
                bar += '#'
            print(char + ' |' + red + bar + normal + ' ' + str(perc)[:4] +
                    '% (' + str(dev)[:4] + '% deviation from random)')

        print('\nTotal percentage deviation from random = ' +
                str(total_dev).split('.')[0] + '%')

        average_dev = total_dev / 26.0

        print('Average percentage deviation from random = ' +
                str(average_dev)[:4] + '%')

        print('Lexical density = ' + str(self.word_stats['lexical_density'])[:5] + '%')

    def init_word_counters(self):
        self.max_n_word = args.max_n_word
        self.n_words = ['' for i in range(self.max_n_word)]
        self.prev_n_words = ['' for i in range(self.max_n_word)]
        self.counters = [collections.Counter() for i in range(self.max_n_word)]


    def read_file(self):
        print("[+] Analysing '" + args.inputfile + "'")
        if args.allow_digits:
            self.words = re.findall(r"['\-\w]+", open(args.inputfile).read().lower())
        else:
            self.words = re.findall(r"['\-A-Za-z]+", open(args.inputfile).read().lower())


    def compute_stats(self):
        for word in self.words:
        
            if word in self.ignore_list:
                continue
        
            word = word.strip(r"&^%$#@!")

            # Allow hyphenated words, but not hyphens as words on their own.
            if word == '-':
                continue

            length = len(word)

            # Record longest word length
            if length > self.word_stats['max_length']:
                self.word_stats['max_length'] = length
                self.word_stats['longest_word'] = word

            # Record shortest word length
            if length < self.word_stats['min_length']:
                self.word_stats['min_length'] = length
                self.word_stats['shortest_word'] = word

            # Keep track of the total number of words and chars read.
            self.word_stats['total_chars'] += length
            self.word_stats['total_words'] += 1.0

            # Note the charaters in each word.
            for char in word:
                if char.lower() in self.word_stats['char_counts']:
                    self.word_stats['char_counts'][char.lower()] += 1.0

            # Tally words.
            for i in range(1, self.max_n_word):
                if self.prev_n_words[i - 1] != '':
                    self.n_words[i] = self.prev_n_words[i - 1] + ' ' + word
                    self.counters[i][self.n_words[i]] += 1

            self.n_words[0] = word
            self.counters[0][word] += 1

            for i in range(0, self.max_n_word):
                self.prev_n_words[i] = self.n_words[i]

        # Calculate the mean word length
        self.word_stats['mean_length'] = self.word_stats['total_chars'] / self.word_stats['total_words']

        # Calculate relative character frequencies
        for char in self.word_stats['char_counts']:
            char_count = self.word_stats['char_counts'][char]
            total_chars = self.word_stats['total_chars']
            percentage = 100.0 * (char_count / total_chars)
            self.word_stats['char_percentages'][char] = percentage

        # Calculate the lexical density of the text.
        total_unique_words = len(self.counters[0])
        total_words = sum(self.counters[0].values())
        self.word_stats['lexical_density'] = 100.0 * total_unique_words / float(total_words)


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description='Perform letter, word and n-tuple frequency analysis on text files.')
    parser.add_argument('--filename', '-f', dest='inputfile', required=True, help='Text file to parse.')
    parser.add_argument('--ntuple', '-n', dest='max_n_word', required=False, default=4, type=int, help='The maximum length n-tuple of words. Default is 4.')
    parser.add_argument('--top', '-t', dest='top_n', required=False, default=20, type=int, help='List the top t most frequent n-words. Default is 20.')
    parser.add_argument('--allow-digits', '-d', dest='allow_digits', default=False, required=False, help='Allow digits to be parsed (true/false). Default is false.')
    parser.add_argument('--ignore', '-i', dest='ignore_list', required=False, help='Comma-delimted list of things to ignore')

    args = parser.parse_args()

    w = wordsworth(args)
    w.init_word_counters()
    w.read_file()
    w.compute_stats()
    w.print_results()
