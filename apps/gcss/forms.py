#coding=utf-8
from uliweb.form import *

class GcssForm(Form):
    title = StringField(label="标题", required=True);
    content = TextField(label="内容", required=True,rows=10,cols=40);
    csscode = TextField(label="CSS代码粘贴",rows=10,cols=40);
    jscode = TextField(label="JS代码粘贴", rows=10,cols=40);
    examplecode = TextField(label="使用样例代码", rows=10,cols=40);
    preview=Submit(value="预览",_class="button",name="preview")
    save=Submit(value="保存",_class="button",name="save")
    form_buttons=[preview,save]
