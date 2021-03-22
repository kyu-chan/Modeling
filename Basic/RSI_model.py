import pandas as pd
import matplotlib.pyplot as plt
import pandas as pd
import sys
import os
import matplotlib as pt
pt.use("Qt5Agg") ##플랏
sys.path.append(r'C:\Users\pc\Desktop\stock\Modeling\Basic\wrapper')

from wrapper import data_pred
from wrapper import trading
from wrapper import trend
from wrapper import visualization

os.chdir(r'C:\Users\pc\Desktop\stock\Modeling\Basic')
cd ='KOSPI 200'
path = 'C:/Users/pc/Desktop/stock/Modeling/Basic/data/'

portfolio = {
    'World indices' : ['Kospi 200', 'S&P 500', 'Nikkei 225', 'CSI 300']
}   ## 딕셔너리 형태
p_name = 'World indices'
p_cd = portfolio[p_name]

ld = data_pred.LoadData()
df = ld.read_master_file(path,p_name)

base_date = '2018-01-08'
sample_df = pd.DataFrame()
#지금은 cd를 kospi column으로 잡아놈
sample_df[cd] = df[cd].copy()
sample_df = sample_df.dropna() ### na제거
sample_df['diff'] = sample_df[cd] - sample_df[cd].shift(1) ##한칸씩 뒤로 미뤄 뺴서, 전일과의 차이를 입력
#print(sample_df.head(3))
'''
d, ad, u, au = 0, 0., 0, 0.  ###  # of down, sum of down, # of up, sum of up
for i in range(20):
    diff = sample_df.shift(i).loc[base_date, 'diff']  ## i일 전의 diff값을 읽어와서
    if diff >= 0:  #양수이면
        u += 1   # count 해주고
        au += diff ##누적으로 더해줘
    elif diff < 0: #음수면
        d += 1 # count 해주고
        ad -= diff ## 누적으로 빼줘( 음수니까 마이너스해줘야 플러스로 돌아오지)
#print(u, au, d, ad)
rsi = (au/(au+ad)) * 100
print(rsi)
'''
###위를 바탕으로 trading 모듈에 짜놨고 되는지 확인해보자
trading.Trade.rsi(df=sample_df, period= 10)
##이건 간단하게 확인해본 것이라 객체를 따로 안만들게 self 뺴고 넣었다.
#print(sample_df.head())

##시각화
#v = visualization.Visualize()
#v.multi_line_view(sample_df, base_date, [cd], ['RSI10'], (15,3))
#plt.show()


## trend 모듈안에 WRSI 트렌드에 가중을 주는 모델
tr = trend.Trend()
wrsi = tr.WRSI(sample_df, cd, 20, base_date)
#print(wrsi.tail())
v = visualization.Visualize()
v.multi_line_view(wrsi, base_date, [cd], ['WRSI20'], (15,3))
plt.show()
