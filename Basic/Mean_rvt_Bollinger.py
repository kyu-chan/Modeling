###통계학도로서 나는 기본적으로 불린저밴드기법은 말이 안된다고 생각함
###하지만 구현을 해보는 목적으로 프로젝트를 해보겠음
import pandas as pd
import numpy as np
import sys
import matplotlib as pt
import matplotlib.pyplot as plt
pt.use("Qt5Agg") ##플랏
sys.path.append(r'C:\Users\pc\Desktop\stock\Modeling\Basic\wrapper')
from wrapper import data_pred
from wrapper import visualization
from wrapper import trading

path = 'C:/Users/pc/Desktop/stock/Modeling/Basic/data/'
cd = 'S&P 500'
file_name = path+cd+' Historical Data.csv'
df = pd.read_csv(file_name, index_col='Date')
#print(df)

###전처리
ld = data_pred.LoadData()
df = ld.date_formatting(df)
df = ld.price_df_trimming(df, cd) ##시세만 때서 처리
#print(df)

##볼린저 밴드 계산
n = 20
sigma = 2

##센터라인
df['center'] = df[cd].rolling(n).mean()
##어퍼 bound
df['ub'] = df['center'] + sigma*df[cd].rolling(n).std()
##로워 bound
df['lb'] = df['center'] - sigma*df[cd].rolling(n).std()
#print(df)


####데이터 샘플링
base_date = '2018-01-08'
sample = df[base_date:].copy()
#print(sample[10:30])

## trading book 생성
trd = trading.Trade()
trd.create_trade_book(sample,cd)


#print(trd.book)
#print(sample)
## 조건 생성   ##trading bollinger_band로 생성
trd.BB_trade(df, base_date,trd.book,cd,n,sigma)
#print(trd.book.tail())
###수익률
trd.returns(trd.book, cd)
print(trd.book['2018-02-01':'2018-03-20'])

###벤치마크 수익률
bm_rtn = round( trd.book[cd].iloc[-1] / trd.book[cd].iloc[0], 4)
#print( "BM return : ", bm_rtn )
##초과수익률
ACC_rtn = trd.book['acc return'].iloc[-1]
exs_rtn = ACC_rtn - bm_rtn
#print( 'Excess return : ', round(exs_rtn, 4))

###시각화 해보자
v = visualization.Visualize()
#v.BB_trend_view(sample, cd)
###plt.show()

### 언제 포지션 들고 있었는지
#v.position_view(trd.book, cd)
#plt.show()



