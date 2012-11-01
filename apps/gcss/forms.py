#coding=utf-8
from uliweb.form import *

class GcssForm(Form):
    title = StringField(label="标题", required=True);
    content = TextField(label="内容", required=True,rows=10,cols=60);
    code = TextField(label="code", required=True,rows=10,cols=60);
