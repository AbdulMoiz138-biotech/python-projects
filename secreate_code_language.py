# -*- coding: utf-8 -*-
"""secreate code language.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1yZ4wXpeYqr5jdPj6EwmaY0s8m0jwil6s

in this code i make a secreat language in which each word the first letter replace to last and 3 random alphabets add to intial and final of a word
"""

import random
import string
def secrete_code(language):

  words=language.split()

  alphabet=string.ascii_letters
  start=''.join(random.choices(alphabet,k=3))
  end=''.join(random.choices(alphabet,k=3))


  for i,word in enumerate(words):

    if len(word)== 1:
      print(word,end=' ')
      continue
    elif len(word)==2:
      print(word[::-1],end=' ')
      continue
    else:
      modified_word=word[1:]+word[0]
      code_word=start+modified_word+end
      print(code_word,end=' ')
      continue

    return





data=secrete_code("I am Abdul moiz of biotechnology student")
print(data)