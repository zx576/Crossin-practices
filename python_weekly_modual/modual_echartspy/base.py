#-*- coding:utf-8 -*-
from echarts import Echart,Legend,Bar,Axis

chart = Echart('GDP','this is fake chart')
chart.use(Bar('china',[2,3,4,5]))
chart.use(Legend(['GDP']))
chart.use(Axis('category','bottom',data=[11,12,1,2]))

chart.plot()
