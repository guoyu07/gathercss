#coding=utf-8
from uliweb.form import *

class GcssForm(Form):
    title = StringField(label="标题", required=True);
    content = TextField(label="内容", required=True,rows=10,cols=40);
    csscode = TextField(label="CSS代码粘贴",rows=10,cols=40);
    jscode = TextField(label="JS代码粘贴", rows=10,cols=40);
    examplecode = TextField(label="使用样例代码", rows=10,cols=40);
