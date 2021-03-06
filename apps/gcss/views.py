#coding=utf-8
from uliweb import expose

from models import gcss 
from forms import GcssForm
from uliweb import function



@expose('/gcss')
def gcss_index():
	gacss = gcss.all().order_by(gcss.c.datetime)
	return {'gacss':gacss}

@expose('/gcss/new')
def new():
        form = GcssForm()
        if request.method == 'POST':
                flag = form.validate(request.params)
                if flag:
                        n = gcss(**form.data)
			if request.params.get('preview'):
				response.template="preview.html"
				return {'csscode':form.data.csscode,'jscode':form.data.jscode,\
					'examplecode':form.data.examplecode,'preview':"1"}
			if request.params.get('save'):
             			n.save()
	return {'form':form,'preview':"0"}

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
		form = GcssForm(data={'title':p.title,'content':p.content,'csscode':p.csscode,'jscode':p.jscode,'examplecode':p.examplecode})
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
			n.examplecode = form.data.examplecode
			n.save()
		return redirect('/gcss')
