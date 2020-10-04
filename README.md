# luluhypermarket-Scraper
Scrapy tool to scrape products from www.luluhypermarket.com

Not sure if this will be of use to anybody, but still. 
To setup the project build a scrapy project using  'scrapy genspider <project_name>'.
This creates a project with all the required files. Now, in the spiders folder, copy the luluscraper.py file, and set name of bot in the variable defined in the LuluSpider class.
Run scrapy crawl <project_name> to run the project.

P.S - Found a good chrome extension to get the css selector easily - https://chrome.google.com/webstore/detail/css-selector-helper-for-c/gddgceinofapfodcekopkjjelkbjodin.
They have provided a yt video to explain the process. 
The code is currently for the 'fresh-food-grocery' section of the website.

