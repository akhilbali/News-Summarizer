from django.shortcuts import render
from django.http import HttpResponse
from web.forms import InputForm
from web.extract import Extract
from textrank.summary import Summary

def home(request):
	return render(request,"home.html",{})

def result(request):
	if request.method=="POST":
		inputform=InputForm(request.POST or None)		
		if inputform.is_valid():
			url = inputform.cleaned_data['url']
			number = inputform.cleaned_data['number']
			text = Extract(url).get_data()
			summary=Summary(text).lines(number)
			#text="<h1> %s </h1>", (number)
			return render(request,"result.html",{"lines":summary})

		else:
			print (inputform.errors)
