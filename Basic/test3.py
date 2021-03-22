import matplotlib.pyplot as plt
import sys
import os
import matplotlib as pt
pt.use("Qt5Agg") ##플랏
sys.path.append(r'C:\Users\pc\Desktop\stock\Modeling\Basic\wrapper')

from wrapper import data_pred
from wrapper import visualization

#print(dir())   ####절대경로로 돌려서 불러오고 임포트된거 확인
os.chdir(r'C:\Users\pc\Desktop\stock\Modeling\Basic')
cd ='S&P 500'
path = 'C:/Users/pc/Desktop/stock/Modeling/Basic/data/'
ld = data_pred.LoadData()
df = ld.read_investing_price(path, cd)

## 날짜 처리
df1 = ld.date_formatting(df)

### price 숫자로 처리
df2 = ld.price_formatting(df1)
print(df2['Price'])
print(df2['Price'][2]+df2['Price'][3])  ### 숫자로 변환 굿

### portfolio
portfolio = {
    'World indices' : ['Kospi 200', 'S&P 500', 'Nikkei 225', 'CSI 300']
}   ## 딕셔너리 형태
p_name = 'World indices'
p_cd = portfolio[p_name]
p_df = ld.create_portfolio_df(path, p_name, p_cd)
print(p_df.tail())


### 시각화

v = visualization.Visualize()
base_date = '2017-03-05'
v.index_view(p_df, base_date, p_cd)
plt.show()
###Trend -> moving ave 연습


