import sys
import matplotlib as pt
import matplotlib.pyplot as plt
pt.use("Qt5Agg") ##플랏
sys.path.append(r'C:\Users\pc\Desktop\stock\Modeling\Basic\wrapper')
import pandas as pd
import numpy as np
from wrapper import data_pred
from wrapper import visualization
from wrapper import trading

file = 'Practice data.csv'
path = 'C:/Users/pc/Desktop/stock/Modeling/Basic/data/'
df = pd.read_csv(path+file, index_col='Date')
#print(df)  ##전처리 필요하겠네
ld = data_pred.LoadData()
df = ld.date_formatting(df)
#print(df)

base_date = '2019-01-01'
cd = 'Inverse'  ##종목
## 일단 시각화
'''
v = visualization.Visualize()
v.price_view(df, base_date, cd, (10,3))
plt.show()
'''
### 1000원 밑에서 사고 1000위에서 파는 것 구현해보자
'''
for i in df.index:
    price = df.loc[i,cd]
    if price < 1000:
        print(i, 'buy')
    elif price > 1000:
        print(i, 'sel')
'''
##트레이딩 북 생성
'''
book = pd.DataFrame()
book[cd] = df[cd]
book['t ' +cd] = ''
book['p ' +cd] = ''
'''
#print(book)    ###요 과정을 wrapper의 trading.py에 만들어 놓음 create_trade_book(df,cd)

## TRD

trd = trading.Trade()
trd.create_trade_book(df, cd)
#trd.book   객체에 잘 저장 됐구만
trd.trade(df, trd.book, cd, 1000, 1000)
#print(trd.book)
#### 포지션 표시를 정하자,  long(l), zero(z)- 안갖고있는거, short(s)
#### 전날과 현재를 같이 표시해주자, zz면 어제 오늘 빈손, zl이면 어제 빈손 오늘 삼
#### 오늘 포지션은 두번쨰 이니셜로
trd.position(trd.book, cd)
##print(trd.book)

##수익률 산출기능 구현, 실행
## trading.py에 returns로 만들어 놈
trd.returns(trd.book, cd)
print(trd.book)