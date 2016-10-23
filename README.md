#About the Hack !

Naver Translator (http://labspace.naver.com/nmt/) has better translation quality for Korean to English than Google Translate. 
But, it does not expose API or allow more than 200 characters.

So my hack uses Selenium APIs to control a Chrome browser to load the Naver translator for the following :-

1. Allow More than 200 words, in fact you can translate a full Article

2. Allow APIs : Translate API and Speech API (uses the installed Voice installed on a MacOS)

The Goal is to allow Naver Translator to be used for general Translation services. We could build a Chrome Plugin to extend 
this hack further. 

###How to Use ?

1. Have an installed Chrome browser on your Mac
2. Have Python and Selenium library installed 
3. Have ChromeDriver installed and available on the PATH environment variable
4. Run the api.py using `export WEBDRIVER=chrome; python api.py`
5. If phantomjs is to needed, then you can run the program by `export WEBDRIVER=phantomjs; python api.py`

###Known issues

1. PhantomJS causes frequent issues while loading the page. Hence the default is set to `chrome`




