# Write a python program to find the wordcount in a file (input.txt) for each line and then print the output.
# o Finally store the output in output.txt file.
#  Example:
# Input: a file includes two lines:
#  Python Course
#  Deep Learning Course
#  Output:
# Python Course
#  Deep Learning Course
# Word_Count:
#  Python: 1
# Course: 2
# Deep: 1
# Learning: 1
import re
fre_word = {}
text_read= open('input.txt', 'r')
text_string = text_read.read().lower()
match_pattern = re.findall(r'\b[a-z]{3,15}\b', text_string)
for word in match_pattern:
    count = fre_word.get(word,0)
    fre_word[word] = count + 1
    
frequency_list = fre_word.keys()

f= open("output.txt","w")
for words in frequency_list:
    result= words + " " + str(fre_word[words])
    f.write(result+"\n")