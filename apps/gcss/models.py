#coding=utf-8
from uliweb.orm import *

class gcss (Model):
	title=Field(CHAR)
	content=Field(TEXT)
	code=Field(TEXT)

