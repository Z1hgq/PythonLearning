# python 3

import csv
import pandas as pd
from io import StringIO
from urllib import request


url='https://archive.ics.uci.edu/ml/machine-learning-databases/pima-indians-diabetes/pima-indians-diabetes.data'
s = request.urlopen(url).read().decode('utf8')  # 1 读取数据串

dfile = StringIO(s)      # 2 将字符串转换为 StringIO对象，使其具有文件属性
creader = csv.reader(dfile)  # 3 将流 转换为可迭代的 reader（csv row）
dlists=[rw for rw in creader]  # 4 其他转换、操作
