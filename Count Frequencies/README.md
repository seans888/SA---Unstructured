wordsworth
==========
Here is an example of some typical output you can expect to see.
![Alt text](/screenshots/screenshot5.png?raw=true "screenshot5.png")
## Setup
Before you get started you need to install the python `blessings` library to colorize the terminal output. 
```
$ sudo pip install blessings
```

### Basic Usage:
#### Example 1: Print the top 50 n-grams in textfile.txt
```
$ python wordsworth.py --filename textfile.txt --top 50
```

```
$ python wordsworth.py -f textfile.txt -t 50
```
#### Example 2: Print the top n-grams of up to 10 words in textfile.txt
```
$ python wordsworth.py --filename textfile.txt --ntuple 10
```
```
$ python wordsworth.py -f textfile.txt -n 10
```
#### Example 3: Ignore the words 'the', 'a' and '--'.
```
$ python wordsworth.py --filename textfile.txt --ignore the,a,--
```
```
$ python wordsworth.py -f textfile.txt -i the,a,--
```
#### Example 4: Ignore just '--'.
```
$ python wordsworth.py --filename textfile.txt --ignore ,--
```
```
$ python wordsworth.py -f textfile.txt -i ,--
```
### NLTK-enabled wordsworth:
wordsworth-nltk.py provides extended analysis, including a frequency analysis of verbs, nouns, adjectives, pronouns etc.
To run this script you will need to install the python [Natural Language Toolkit (NLTK)](https://github.com/nltk)
and the Brown and Punkt datasets which is used for token tagging. Fortunately this is very simple to install.

Step 1. Install NLTK 
```
$ sudo pip install nltk
```
Step 2. Launch the python interpreter
```
$ python
```
Step 3. Download the `Brown` and `Punkt` dataset
```python
>>> import nltk
>>> nltk.download('brown')
>>> nltk.download('punkt')
```

### Example output:

![Alt text](/screenshots/screenshot1.png?raw=true "screenshot1.png")
<br>
![Alt text](/screenshots/screenshot2.png?raw=true "screenshot2.png")
<br>
![Alt text](/screenshots/screenshot3.png?raw=true "screenshot3.png")
<br>
![Alt text](/screenshots/screenshot4.png?raw=true "screenshot4.png")
<br>
![Alt text](/screenshots/screenshot6.png?raw=true "screenshot6.png")
<br>
![Alt text](/screenshots/screenshot7.png?raw=true "screenshot7.png")
