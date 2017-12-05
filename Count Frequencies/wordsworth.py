#!/usr/bin/env python
# Author: 0jag
# Modified by: Gabriel Montalvo
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
import collections
import re
import json

class Namespace:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

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


    def __init__(self, options):

        args = Namespace(
            allow_digits = options['allow_digits'],
            ignore_list = options['ignore_list'],
            inputfile = options['inputfile'],
            max_n_word = options['max_n_word'],
            top_n = options['top_n'])

        self.ignore_list = args.ignore_list
        self._allow_digits = args.allow_digits
        self._inputfile = args.inputfile
        self._max_n_word = args.max_n_word
        self._top_n = args.top_n

        self.init_word_counters()
        self.read_file()
        self.compute_stats()


    def calc(self):

        results = {
            'file': str(self._inputfile),
            'longest_word': str(self.word_stats['longest_word']) + ' (' + str(self.word_stats['max_length']) + ')',
            'shortest_word': str(self.word_stats['shortest_word']) + ' (' + str(self.word_stats['min_length']) + ')',
            'mean_word_length_per_char': self.word_stats['mean_length'],
            'total_words_parsed': int(str(self.word_stats['total_words']).split('.')[0]),
            'total_chars_parsed': self.word_stats['total_chars']
        }

        for i in range(self.max_n_word):
            total_entries = sum(self.counters[i].values())
            unique_entries = len(self.counters[i])

            if total_entries > 0:
                m = self.counters[i].most_common(min(unique_entries, self._top_n))
                n = len(m[0][0].split(' '))

                tmp = {}

                for i in range(0, min(unique_entries, self._top_n)):
                    n_word = m[i][0]
                    count = m[i][1]
                    perc = 100.0 * (count / float(total_entries))

                    tmp[str(i + 1)] = n_word + ' (' + str(count).split('.')[0] + ' = ' + str(perc)[:5] + '%' + ')'

                results['commonest_' + str(n) + '_words'] = tmp

        total_dev = 0.0
        freq_chars = {}

        for char in sorted(iter(self.word_stats['char_percentages'])):
            perc = self.word_stats['char_percentages'][char]

            # Percentage deviation from random distribution of characters.
            dev = 100.0 * (abs((100.0 / 26.0) - perc) / (100.0 / 26.0))
            total_dev += dev

            freq_chars[char] = str(perc)[:4] + '% (' + str(dev)[:4] + '% deviation from random)'

        results['frequency_analysis'] = freq_chars
        results['total_deviation'] = float(str(total_dev).split('.')[0])

        average_dev = total_dev / 26.0

        results['average_deviation'] =  float(str(average_dev)[:4])
        results['lexical_density'] = float(str(self.word_stats['lexical_density'])[:5])

        return json.dumps(results, sort_keys=True, indent=4, separators=(',', ': '))

    def init_word_counters(self):
        self.max_n_word = self._max_n_word
        self.n_words = ['' for i in range(self.max_n_word)]
        self.prev_n_words = ['' for i in range(self.max_n_word)]
        self.counters = [collections.Counter() for i in range(self.max_n_word)]


    def read_file(self):
        if self._allow_digits:
            self.words = re.findall(r"['\-\w]+", open(self._inputfile).read().lower())
        else:
            self.words = re.findall(r"['\-A-Za-z]+", open(self._inputfile).read().lower())


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

