import trendet

import matplotlib.pyplot as plt
import seaborn as sns

from datetime import date

class stockDataAnalysis():

    def getStockData(self):
        today = date.today()
        T_split = str(today).split('-')
        fromDate = T_split[2]+'/'+T_split[1]+'/'+str(int(T_split[0]) - 1)
        toDate = T_split[2]+'/'+T_split[1]+'/'+T_split[0]

        sns.set(style='darkgrid')

        stocks=['TCS','HDFC','ITC','SBI','ONGC','NTPC','IOC', 'GAIL','DLF','HPCL']
        for stock in stocks:
            df = trendet.identify_all_trends(stock=stock,
                                             country='India',
                                             from_date=fromDate,
                                             to_date=toDate,
                                             window_size=5,
                                             identify='both')

            df.reset_index(inplace=True)

            plt.figure(figsize=(20, 10))

            ax = sns.lineplot(x=df.index, y=df['Close'])
            ax.set(xlabel='Date')

            labels = df['Up Trend'].dropna().unique().tolist()

            for label in labels:
                sns.lineplot(x=df[df['Up Trend'] == label].index,
                             y=df[df['Up Trend'] == label]['Close'],
                             color='green')

                ax.axvspan(df[df['Up Trend'] == label].index[0],
                           df[df['Up Trend'] == label].index[-1],
                           alpha=0.2,
                           color='green')

            labels = df['Down Trend'].dropna().unique().tolist()

            for label in labels:
                sns.lineplot(x=df[df['Down Trend'] == label].index,
                             y=df[df['Down Trend'] == label]['Close'],
                             color='red')

                ax.axvspan(df[df['Down Trend'] == label].index[0],
                           df[df['Down Trend'] == label].index[-1],
                           alpha=0.2,
                           color='red')

            locs, _ = plt.xticks()
            labels = []

            for position in locs[1:-1]:
                labels.append(str(df['Date'].loc[position])[:-9])

            plt.xticks(locs[1:-1], labels)
            plt.savefig('./template/'+stock+'.jpg')