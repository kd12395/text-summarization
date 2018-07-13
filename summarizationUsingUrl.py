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

import web

LANGUAGE = "english"
SENTENCES_COUNT = 5
buf = StringIO()

p = print

def make_text(string):
    return string
def get_print():
    return print   # or return it :)

urls = ('/', 'tutorial')
render = web.template.render('templates/')

app = web.application(urls, globals())

my_form = web.form.Form(
                web.form.Textbox('', class_='textfield', id='textfield'),
                )

class tutorial:
    def GET(self):
        form = my_form()
        return render.tutorial(form, "Your text goes here.")

    def POST(self):
        form = my_form()
        form.validates()
        url = form.value['textfield']
        parser = HtmlParser.from_url(url, Tokenizer(LANGUAGE))
        # or for plain text files
        # parser = PlaintextParser.from_file("document.txt", Tokenizer(LANGUAGE))
        stemmer = Stemmer(LANGUAGE)

        summarizer = Summarizer(stemmer)
        summarizer.stop_words = get_stop_words(LANGUAGE)
        s = summarizer(parser.document, SENTENCES_COUNT)

        #print(s)
        summarizeString = ""
        for sentence in summarizer(parser.document, SENTENCES_COUNT):
            summarizeString+=str(sentence)

        return make_text(summarizeString)

if __name__ == '__main__':
    app.run()
