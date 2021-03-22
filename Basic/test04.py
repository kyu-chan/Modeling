import sys
import matplotlib as pt
pt.use("Qt5Agg") ##플랏
sys.path.append(r'C:\Users\pc\Desktop\stock\Modeling\Basic\wrapper')

from wrapper import pract

pt = pract.Pract()
#price = pt.DDM(5000, 0.10, 0.05)
#print(price)


#price = pt.DCF(0.02, 1000,1000,1000)
#print(price)
