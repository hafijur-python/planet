from django.http import HttpResponse
from django.shortcuts import  get_object_or_404,render
from django.http import HttpResponseRedirect,HttpResponse
from django.core.urlresolvers import reverse 
from django.core import serializers
from django.http import JsonResponse
import json
import os
import re 
from appli.models import Planet
from .form import PlanetForm
from django.shortcuts import render_to_response
# from django.contrib.auth.models import Planets
def file_create(request):

	file=open('planets.json') 
	  
	data = json.load(file)
	all=[]
	for i in data:
		a=i['name']
		b=i['caption']
		c=i['temperature']
		e=i['radius']
		d=i['detail']
		g= i['image']
		Joindata=(a,b,c,e,d,g)
		planetdata='<br>'.join(Joindata)
		all.append(planetdata)
		if Planet:
		    savedata =Planet(name=a,caption=b,temperature=c,radius=e,detail=d, images = g)
		savedata.save()
	else:
		pass

	
 	# x = serializers.serialize("json", Planet.objects.all())
 	# new = {'x':x}
	return HttpResponse(all)

def description(request):
	li=[]
	file_open=open('planets.json','r')
	load_p= json.load(file_open)
	for i in load_p:
		a=i['name']
		b=i['caption']
		c=i['temperature']
		e=i['radius']
		d=i['detail']
		g= i['image']
		x= (a+b+c+e+d)
		if Planet:
			li.append(x)
		else:
			pass
			savedata =Planet(name=a,caption=b,temperature=c,radius=e,detail=d,image=g)
			savedata.save()
	return HttpResponse()


def single(request,id):
	y = serializers.serialize("json",Planet.objects.filter( pk=id))
	

	
	
	  
	return HttpResponse(y)
### end of program 




def planet_detail(request,id):
	try:
		planet_detail=Planets.objects.get(pk=id)
	except planet_detail.DoesNotExist:
		raise Http404('planet DoesNotExist')
	return render(request,'home/planet_detail.html',{'planet_detail':planet_detail})
# 	return HttpResponse('you are looking at the ressults of the poll%s' %question_id)

def planets(request):
	planets_list=Planets.objects.all()
	
	# print planets_list

 	data=serializers.serialize('json',(planets_list))
 	
	
	return render(request,'home/json.html',{'data':data})

def addplanet(request):
    # form =PlanetForm()
    # planet_formset = BookFormset(instance=Author())

    if request.POST:
        form = PlanetForm(request.POST)
        if form.is_valid():
        	name = request.POST.get('name','')
        	caption = request.POST.get('caption','')
        	temperature = request.POST.get('temperature','')
        	radius= request.POST.get('radius','')
        	detail= request.POST.get('detail','')
        	planet_obj=Planets(name=name,caption=caption,temperature=temperature,radius=radius,detail=detail)
      #   	planet_obj = json.loads(request.POST)
      #   	for o in planet_obj:
      #   		record = Planets(name = o.name, caption = o.caption)
    		# record.save()

        	planet_obj = form.save()
        	print planet_obj
		return HttpResponseRedirect('addplanet')
    else:
    	form =PlanetForm()


    return render(request,'home/addplanet.html',{
        'form': form, 
    })  












# from django.shortcuts import render
# from django.http import HttpResponse
# from django.shortcuts import  get_object_or_404,render
# from django.http import HttpResponseRedirect,HttpResponse
# from rest_framework.response import Response
# from rest_framework.views import APIView
# from rest_framework import status
# from .serializers import PlanetsSerializer
# from rest_framework.generics import ListAPIView

# from appli.models import Planets


# # Create your views here.
# def index(request):
	
# 	print 'meet'
# 	return HttpResponse('hello')
# class PlanetsList(ListAPIView):
# 	# def get(request):
# 	 planets_list= Planets.objects.all()
# 	 serializer_class = PlanetsSerializer
# # return Response(serializer.data)










# # def planets(request):

# #   planets_list=Planets.objects.all()
# #   print planets_list
# #   planets_list=serializers.serialize('json',planets_list)
# #   return HttpResponse(planets_list,content_type="application/json")
  
# # def planet_detail(request,id):
# # 	try:
# # 		planet_detail=Planets.objects.get(pk=id)
# # 	except planet_detail.DoesNotExist:
# # 		raise Http404('planet DoesNotExist')
# # 	# return render(request,'pollA/planet_detail.html',{'planet_detail':planet_detail})
	


#  