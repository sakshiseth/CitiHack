from GoogleNews import GoogleNews
import pandas as pd
import dataframe_image as dfi
from datetime import date,timedelta

class newsDataCapturing():
    def getnewsData(self):
        today = date.today()
        T_split = str(today).split('-')
        toDate = T_split[2]+'/'+T_split[1]+'/'+T_split[0]
        googlenewsMkt=GoogleNews(start=toDate,end=toDate)
        googlenewsMkt.get_news('Market')
        result=googlenewsMkt.results()
        df=pd.DataFrame(result).head(10)
        dfi.export(df, './template/df_styled_Market.jpeg')
        googlenewsBiz=GoogleNews(start=toDate,end=toDate)
        googlenewsBiz.get_news('Business')
        result=googlenewsBiz.results()
        df=pd.DataFrame(result).head(10)
        dfi.export(df, './template/df_styled_Business.jpeg')

