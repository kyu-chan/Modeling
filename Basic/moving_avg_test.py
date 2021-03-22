import matplotlib.pyplot as plt
import pandas as pd
import sys
import os
import matplotlib as pt
pt.use("Qt5Agg") ##플랏
sys.path.append(r'C:\Users\pc\Desktop\stock\Modeling\Basic\wrapper')

from wrapper import data_pred
from wrapper import trading
from wrapper import visualization

os.chdir(r'C:\Users\pc\Desktop\stock\Modeling\Basic')
cd ='KOSPI 200'
path = 'C:/Users/pc/Desktop/stock/Modeling/Basic/data/'

## 이용할 인덱스 포트폴리오
portfolio = {
    'World indices' : ['Kospi 200', 'S&P 500', 'Nikkei 225', 'CSI 300']
}   ## 딕셔너리 형태
p_name = 'World indices'
p_cd = portfolio[p_name]

###모듈
ld = data_pred.LoadData()
df = ld.read_master_file(path, p_name)
#print(df.head())

##단기, 중기 기준
short = 5
mid = 20

##ma 데이터프레임을 구축
ma = pd.DataFrame()
ma[cd] = df[cd]   ## 시세를 일단 넣어주고
ma['short'] = df[cd].rolling(short).mean()  ### rolling으로 단위를 계속 유지하면서 mean계산을 쌓아나감
ma['mid'] = df[cd].rolling(mid).mean()    ### 판다스 기능이니 유용하게 쓸 것
#print(ma.head(20))

###기준일자 설정
base_date = '2018-01-08'
ma = ma[base_date:].copy()
#print(ma.head())

### 시각화
#v = visualization.Visualize()
#v.price_view(ma, base_date, [cd], (10,2), make_file=False)
#plt.show()

### 이평 비교 시각화
#v = visualization.Visualize()
#v.price_view(ma, base_date, [cd,'short' ,'mid'], (10,2), make_file=False)
#plt.show()

### 골든크로스, 데드크로스 기본적 구현
ma['s-m'] = ma['short'] - ma['mid']
#print(ma.head(50))

##  trading 모듈에다가 def 짜고
trd = trading.Trade()
book = trd.create_trade_book(ma, [cd])
#print(book.head())  ##일종의 작전노트

### 짜놓은거 실행
book = trd.trend_trading(ma,book, cd, 's-m')
#print(book.head(50))
## 포지션 산출
book = trd.position(book, [cd])
#print(book.tail())

##손익 테스팅
fund_rtn = trd.returns(book, [cd])
##print(fund_rtn)

##벤치마크 대비 수익률
bm_rtn = trd.benchmark_return(book, [cd])
#print(bm_rtn)

## 벤치대비 초과수익률
exs_rtn = trd.excess_return(fund_rtn, bm_rtn)
##print(exs_rtn)



################