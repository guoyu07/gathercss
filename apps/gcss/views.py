#coding=utf-8
from uliweb import expose

from models import gcss 
from forms import GcssForm
from uliweb import function


@expose('/')
def index():
	gacss = gcss.all()
	form = GcssForm()
	if request.method == 'POST':
		flag = form.validate(request.params)
		if flag:
			n = gcss(**form.data)
			n.save();
	return {'gacss':gacss,'form':form}

@expose('/delete/<id>')
def delete(id):
	n = gcss.get(gcss.c.id == id)
	if n:
		n.delete()
	return redirect('/');

@expose('/edit/<id>')
def edit(id):
	if request.method == 'GET':
		p = gcss.get(gcss.c.id==id)
		form = GcssForm(data={'title':p.title,'content':p.content,'code':p.code})
		return {'form':form}
	elif request.method == 'POST':
		form = GcssForm()
             	flag = form.validate(request.params)
		n = gcss.get(gcss.c.id == id)
		if n:
			n.title = form.data.title
			n.content = form.data.content
			n.code = form.data.code
			n.save()
		return redirect('/');
