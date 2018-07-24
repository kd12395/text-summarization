from __future__ import absolute_import
from __future__ import division, print_function, unicode_literals

from sumy.parsers.html import HtmlParser
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer as Summarizer
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words

import web

LANGUAGE = "english"

def make_text(string):
    return string

urls = ('/', 'textarea')
render = web.template.render('templates/')

app = web.application(urls, globals())

my_form = web.form.Form(
                web.form.Textarea('Content', class_='text_description', id='textfield'),
                web.form.Textbox('sentenceCount', class_='textfield', id='sentenceCount'),
                )

class textarea:
    def GET(self):
        form = my_form()
        return render.textarea(form, "Your text goes here.")
        
    def POST(self):
        form = my_form()
        form.validates()
        # print(form.value)
        content = form.value['textfield']
        sentenceCount = form.value['sentenceCount']
        
        parser = PlaintextParser.from_string(content, Tokenizer(LANGUAGE))
        # or for plain text files
        # parser = PlaintextParser.from_file("document.txt", Tokenizer(LANGUAGE))
        stemmer = Stemmer(LANGUAGE)

        summarizer = Summarizer(stemmer)
        summarizer.stop_words = get_stop_words(LANGUAGE)
        

        summarizeString = ""
        for sentence in summarizer(parser.document, sentenceCount):
            summarizeString+=str(sentence)
        
        return make_text(summarizeString)

if __name__ == '__main__':
    app.run()
