from __future__ import absolute_import
from __future__ import division, print_function, unicode_literals
from __future__ import print_function

from sumy.parsers.html import HtmlParser    
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer as Summarizer
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words
from cStringIO import StringIO
import nltk
nltk.download('punkt')
from nltk import word_tokenize,sent_tokenize

import web

LANGUAGE = "english"
SENTENCES_COUNT = 5
buf = StringIO()

p = print

def make_text(string):
    # print(string)
    return string

urls = ('/', 'file')
# render = web.template.render('templates/')

app = web.application(urls, globals())

my_form = web.form.Form()

class file:
    def GET(self):
        # return render.fileupload("Your text goes here.")
        return {}

    def POST(self):
        form = my_form()
        form.validates()
        print(form.value['Isfile'])
        if form.value['Isfile'] == 'true':
            print('Inside if')
            content = form.value['file']
            print(content)
            parser = PlaintextParser.from_string(content, Tokenizer(LANGUAGE))
        else:
            print('Inside else')
            content = form.value['textfield']
            parser = HtmlParser.from_url(content, Tokenizer(LANGUAGE))
        sentenceCount = form.value['sentenceCount']
        # print(content, sentenceCount)
        # x = web.input(myfile={})
        # web.debug(x['myfile'].filename) # This is the filename
        # content = web.debug(x['myfile'].value)

        # parser = PlaintextParser.from_file(url, Tokenizer(LANGUAGE))
        # # or for plain text files
        # # parser = PlaintextParser.from_file("adventure.txt", Tokenizer(LANGUAGE))
        stemmer = Stemmer(LANGUAGE)

        summarizer = Summarizer(stemmer)
        summarizer.stop_words = get_stop_words(LANGUAGE)
        # s = summarizer(parser.document, sentenceCount)

        #print(s)
        summarizeString = ""
        for sentence in summarizer(parser.document, sentenceCount):
            summarizeString+=str(sentence)

        return make_text(summarizeString)

if __name__ == '__main__':
    app.run()
