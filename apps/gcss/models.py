#coding=utf-8
from uliweb.orm import *

class gcss (Model):
	title=Field(CHAR)
	content=Field(TEXT)
	csscode=Field(TEXT)
	jscode=Field(TEXT)
	examplecode=Field(TEXT)
