#coding=utf-8
from uliweb import expose

from models import gcss 
from forms import GcssForm
from uliweb import function



@expose('/gcss')
def gcss():
	gacss = gcss.all()
	return {'gacss':gacss}

@expose('/gcss/new')
def new():
        form = GcssForm()
        if request.method == 'POST':
                flag = form.validate(request.params)
                if flag:
                        n = gcss(**form.data)
                        n.save();
	return {'form':form}

@expose('/gcss/css')
def css():
	gacss=gcss.all()
	return {'gacss':gacss}

@expose('/gcss/js')
def js():
	gacss=gcss.all()
	return {'gacss':gacss}

@expose('/gcss/delete/<id>')
def delete(id):
	n = gcss.get(gcss.c.id == id)
	if n:
		n.delete()
	return redirect('/gcss');

@expose('/gcss/src/<id>')
def src(id):
	n=gcss.get(gcss.c.id==id)
	if n:
		return {'n':n}
	return redirect('/gcss')
	
@expose('/gcss/display/<id>')
def display(id):
	n=gcss.get(gcss.c.id==id)
	if n:
		return {'n':n}
	return redirect('/gcss')

@expose('/gcss/edit/<id>')
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
			n.csscode = form.data.csscode
			n.jscode = form.data.jscode
			n.save()
		return redirect('/gcss');
