# Crawler_Stock_market
Kering is a global luxury group, which brings together and grows a group of
iconic fashion, leather goods, jewellery and watch brands: Gucci, Saint Laurent, Bottega Veneta, Balenciaga, Alexander McQueen, Brioni, Boucheron, Pomellato, Dodo, Qeelin, Ulysse Nardin, Girard-Perregaux, as well as Kering Eyewear.
This company is listed on the CAC40 stock exchange, whose prices are available on the Boursorama website. It is from this site that we will collect our data.
We have two problems:
- Is the stock price of a luxury group monotonous, as promised by the description description given by the Kering web page?
- To what extent can Kering's share price be represented by a linear function?

To answer this question, we will study the fluctuations over several periods.
For each period, we will choose the linear regression method.
Data collection
To collect the data on the Boursorama website, we use a crawler based on the BeautifulSoup package. We carried out a first collection on Wednesday 24 November 2021, over an hour and forty minutes of 100 observations. Following this first collection, we could already observe at least one cycle of fluctuations.
It is therefore pointless to test the course linearly over such a long period. For this reason, we reduced the collection time for the following periods to fifty minutes, with the same collection rate, resulting in fifty collected observations. To adjust the first collection with the others, we split it into two successive periods.
After the data collection, we had four class periods, starting at 1:58 pm, 2:48 pm, 3:38 pm, 4:24pm respectively. The last period ended at 5:18pm. 
