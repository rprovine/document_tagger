import re
from pg_sample_texts import DIV_COMM, MAG_CART

documents = [DIV_COMM, MAG_CART]

# The named group 'title' looks for
# title_search = re.compile(r'(?:title:\s*)(?P<title>(.*)[ ]*?\n[ ]*(.*))', re.IGNORECASE)
title_search = re.compile(r"""
                          (?:title:\s*) #look for 'title: ' in the original text.
                          (?P<title>        #then capture the following group which we'll
                                            #call title and can access with that name later

                          (                 #title consists of words, which are
                            (
                              \S*           #one or more non-white spaces
                              (\ )?         #followed by zero or 1 spaces
                                            # note how we have to use a slash to escape
                                            # the space character, since re.VERBOSE mode ignores
                                            # unescaped whitespace in your pattern.

                            )+              # title has 1 or more such words
                          )
                          (                 #and this set of words can optionally be followed
                            (\n(\ )+)       #by a new line character, plus a few spaces
                            (\S*(\ )?)*     #and then one or more additional words
                          )*                #and this * means the title can encompass
                          )""",             #however many extra lines we need
                          re.IGNORECASE | re.VERBOSE)  #note the #appearance of | above.
                                            #This allows us to set multiple flags to our regex.
                                            #See: http://docs.python.org/dev/howto/regex.html#compilation-flags


author_search = re.compile(r'(author:)(?P<author>.*)', re.IGNORECASE)
translator_search = re.compile(r'(translator:)(?P<translator>.*)', re.IGNORECASE)
illustrator_search = re.compile(r'(illustrator:)(?P<illustrator>.*)', re.IGNORECASE)
for i, doc in enumerate(documents):
  title = re.search(title_search, doc).group('title')
  author = re.search(author_search, doc)
  if author:
    author = author.group('author')
  translator = re.search(translator_search, doc)
  if translator:
    translator = translator.group('translator')
  illustrator = re.search(illustrator_search, doc)
  if illustrator:
    illustrator = illustrator.group('illustrator')
  print "***" * 25
  print "Here's the info for doc {}:".format(i)
  print "Title:  {}".format(title)
  print "Author(s): {}".format(author)
  print "Translator(s): {}".format(translator)
  print "Illustrator(s): {}".format(illustrator)
  print "\n"