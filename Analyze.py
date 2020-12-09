from Weather.Citi_Weather_Impact import makeWeatherConclusion
from Stock_Market.Stock_Data import stockDataAnalysis
from News_Channel.News_Data import newsDataCapturing

# Get the Pie chart representation of the weather of Indian metropolitian cities which may affect the market.
# Forecast may help as an alert for an impact over region specific market
prepareWeatherConclusion = makeWeatherConclusion()
prepareWeatherConclusion.getWeatherConclusionAsImage()


# Get the indian stocks trend of one to analyze the overall market trend of an year.
# This data will be helpful in predicting the future impacts.
prepareStockAnalysis = stockDataAnalysis()
prepareStockAnalysis.getStockData()

# Get the top market and business related news for a quick review over the top contents
# This data will cover several news related links across all the available ones
prepareNewsData = newsDataCapturing()
prepareNewsData.getnewsData()

# Moving towards social media Hashtagging for prediction over popular trends that may an impact on the market.
# Hashtagging will be categorized to understand the severity of the current trend.
# Extracting hashtags from Twitter/Facebook/LinkedIn/Reddit

