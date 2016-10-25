#About the Hack !

Naver Translator (http://labspace.naver.com/nmt/) has better translation quality for Korean to English than Google Translate. 
But, it does not expose API or allow more than 200 characters.

So my hack uses Selenium APIs to control a Chrome browser to load the Naver translator for the following :-

1. Allow More than 200 words, in fact you can translate a full Article

2. Allow APIs : Translate API and Speech API (uses the installed Voice installed on a MacOS)

3. A Proof of concept added to demonstrate integration with Slack as a bot

The Goal is to allow Naver Translator to be used for general Translation services. We could build a Chrome Plugin to extend 
this hack further. 

###How to Use ?

1. Have an installed Chrome browser on your Mac
2. Ensure Python 2.7.x is installed. Install Selenium and Flask library : `pip install selenium flask`
3. Have ChromeDriver installed and available on the PATH environment variable (http://chromedriver.storage.googleapis.com/index.html?path=2.24/)
4. Run the api.py using `export WEBDRIVER=chrome; python api.py`
5. If phantomjs is to needed, then you can run the program by `export WEBDRIVER=phantomjs; python api.py`. Please ensure you have phantomjs libraries on your machine. More on this later. 
6. To use the Slack bot, do the following :- 
  a. Get the Slack API Token, and set the environment variable `export SLACK_BOT_TOKEN=<TOKEN>`
  b. Run `python print_bot_id.py` to get the Slack Bot ID. The Bot username is `translator` by default.
  c. Set the environmebt variable `export BOT_ID=<BOTID>`
  d. Run the Bot `python translate_bot.py`
  e. Add the `translator` bot to you Slack Channel
  f. Access the bot `@translator translate 이것은 대단한 데모이다.`

###Known issues

1. PhantomJS causes frequent issues while loading the page. Hence the default is set to `chrome`




