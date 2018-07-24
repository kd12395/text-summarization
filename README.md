# text-summarization
Text summarization uses 'sumy' for summarizing text. Summarization can be done either by providing URL, or by Uploading .txt and .pdf File, or by providing specific content.

Dependencies:
pip install sumy

----------MultipleServer------------
Here, need to run 3 python file to execute these 3 functionalities. Each file is for each functionality. 

To run the server,
python <filename> 8082
(Provide any specific port, default port is 8080)

Then open the url: http://0.0.0.0:8082/


---------SingleServer------------
Here, no specific file for individual functionality.

just run single file,
python summarization.py 8082

and open index.html file in your browser.
