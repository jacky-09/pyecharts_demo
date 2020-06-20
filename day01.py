from pyecharts.charts import * # 图表
from pyecharts.components import Table # 表格
from pyecharts import options as opts # 配置
from pyecharts.commons.utils import JsCode 
import random # 随机数
import datetime #时间


# 直方图
x_data = ["水笔","铅笔","钢笔","圆珠笔"] # x轴数据
y_data = [40,30,98,42] # y轴数据
bar = Bar() # 初始化图表
bar.add_xaxis(x_data) # x轴
bar.add_yaxis('', y_data) # y轴
bar.render() # 渲染html文件
# return render_notebook() # 渲染到notebook,这里不细讲


# 折线图
x_data = ['Apple', 'Huawei', 'Xiaomi', 'Oppo', 'Vivo', 'Meizu'] # x轴数据
y_data = [123, 153, 89, 107, 98, 23] # y轴数据
line = Line() # 初始化图表
line.add_xaxis(x_data) # x轴
line.add_yaxis('', y_data) # y轴
line.render() # 渲染html文件


# 散点图
x_data = ['Apple', 'Huawei', 'Xiaomi', 'Oppo', 'Vivo', 'Meizu'] # x轴数据
y_data = [123, 153, 89, 107, 98, 23] # y轴数据
scatter = Scatter() # 初始化
scatter.add_xaxis(x_data) # x轴渲染
scatter.add_yaxis('', y_data) # y轴渲染
scatter.render() # 渲染HTML