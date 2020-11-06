from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import products,items,cart,buyed,order_count,allorder,re_views
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
import smtplib
from validate_email import validate_email
import random
def home(request):
	return render(request,'home.html')
def main_page(request):
	f=products.objects.all()
	return render(request,'main_page.html',{'d':f})

def save_reviews(request,id):
	point=request.POST['rate']
	msg=request.POST['msg']
	item=items.objects.get(id=id)
	try:
		point=int(point)
	except:
		point=1
	r=re_views(point=point,name=request.user,product=item,msg=msg)
	r.save()
	return redirect('/details/'+str(id))
def details(request,id):
	try:
		i=items.objects.get(id=id)
		r=re_views.objects.all().filter(product=i).order_by('-datetime')
		return render(request,'details.html',{'i':i,'r':r})
	except:
		return HttpResponse("No record found")
def sub_page(request):
	name=request.GET['search']
	d=products.objects.get(name=name)
	f=d.item.all()
	return render(request,'sub_page.html',{'f':f})

def search_name(request):
	name=request.GET['search'].lower()
	ans=[]
	try:
		t=items.objects.all()
		for i in t:
			print(i)
			if name in i.name.lower() or name in i.desc.lower():
				ans.append(i)
		return render(request,'search_name.html',{'d':ans})
	except:
		return HttpResponse("an error akhda id")
	try:
		d=products.objects.get(name=name)
		return render(request,'search_name.html',{'d':d})
	except:
		return render(request,'search_name.html',{'name':name})
	# d=items.objects.all()
	# return render(request,'search_name.html',{'d':d})
@login_required
def buy(request):
	idd=request.GET['id']
	try:
		try:

			print("hello_1")
			d=items.objects.get(id=idd)
			b=buyed.objects.all().filter(item=d)[0]
			c=cart.objects.get(name=request.user)
			b=c.item.all().filter(item=d)[0]
			c.item.remove(b)
			c.save()
			c.cost-=(b.total_item)*d.price
			b.total_item+=1
			b.save()
			print("hello_1")
			c.item.add(b)

			c.cost+=(b.total_item)*d.price
			c.save()
			return redirect('my_cart')
		except:
			print("hello_2")
			d=items.objects.get(id=idd)
			b=buyed(item=d,total_item=1)
			b.save()
			c=cart.objects.get(name=request.user)
			c.item.add(b)
			c.cost+=(b.total_item)*d.price
			c.save()
			return redirect('my_cart')
	except:
		return HttpResponse("an error accupied")

def log_in(request):
	if request.method=='POST':
		username=request.POST['username']
		passwd=request.POST['passwd']
		u=authenticate(username=username,password=passwd)
		if u is not None:
			auth.login(request,u)
			try:
				c=cart.objects.get(name=request.user)
			except:
				c=cart(name=request.user,cost=0)
				c.save()
			return redirect("main_page")

	return render(request,'log_in.html',{'msg':"invalid user name and password"})

def sign_in(request):
	#if request.method=='POST':
		# username=request.POST['username']
		# pass_1=request.POST['pass_1']
		# pass_2=request.POST['pass_1']
		# email=request.POST['email']
		# first_name=request.POST['first_name']
		# last_name=request.POST['last_name']
		# x=random.randint(1000,9999)
		# # try:
		# # 	server=smtplib.SMTP_SSL("smtp.gmail.com",465)
		# # 	server.login("nitinkolawat1008@gmail.com","NITIN1008saini")
		# # 	server.sendmail("nitinsaini1008@gmail.com",
		# # 					email,
		# # 					"Hello your password is "+str(x))
		# # 	server.quit()
		# # except:
		# # 	return HttpResponse('unable to send mail in your account')
		# u=User.objects.create_user(username=username,email=email,password=pass_2,first_name=first_name,last_name=last_name)
		# return redirect('post_sign/'+u)
		# if pass_1!=pass_2:
		# 	return render(request,'sign_in.html',{'msg':'passwd not matched'})
		# else:
		# 	u=User.objects.create_user(username=username,email=email,password=pass_2,first_name=first_name,last_name=last_name)

		# 	u.save()
		# 	auth.login(request,u)
		# 	try:
		# 		c=cart.objects.get(name=request.user)
		# 	except:
		# 		c=cart(name=request.user,cost=0)
		# 		c.save()
		# 	return redirect('main_page')
	return render(request,'sign_in.html')
def post_sign(request):
	email=request.GET['email']
	x=random.randint(1000,99999)
	try:
		server=smtplib.SMTP_SSL("smtp.gmail.com",465)
		server.login("nitinkolawat1008@gmail.com","NITIN1008saini")
		server.sendmail("nitinsaini1008@gmail.com",
						email,
						"Hello your password is "+str(x))
		server.quit()
	except:
		return HttpResponse('unable to send mail in your account')
	return HttpResponse(str(x))
def sign_2(request):
	username=request.GET['username']
	pass_1=request.GET['pass_1']
	pass_2=request.GET['pass_1']
	email=request.GET['email']
	first_name=request.GET['first_name']
	last_name=request.GET['last_name']
	u=User.objects.create_user(username=username,email=email,password=pass_2,first_name=first_name,last_name=last_name)
	u.save()
	auth.login(request,u)
	try:
		c=cart.objects.get(name=request.user)
	except:
		c=cart(name=request.user,cost=0)
		c.save()
	return redirect('main_page')
@login_required
def log_out(request):
	auth.logout(request)
	return redirect('main_page')
@login_required
def my_cart(request):
	try:
		c=cart.objects.get(name=request.user)
		l=c.item.count()
		return render(request,'my_cart.html',{'c':c,'l':l})
	except:
		c=cart(name=request.user,cost=0)
		c.save()
	return render(request,'my_cart.html',{'c':c,'msg':'not modified'})
@login_required
def delete_cart(request):
	idd=request.GET['id']
	t=items.objects.get(id=idd)
	c=cart.objects.get(name=request.user)
	b=c.item.all().filter(item=t)[0]
	#b=buyed.objects.all().filter(item=t)[0]
	if b.total_item==1:
		b.delete()
		c.item.remove(b)
		c.cost-=t.price
		c.save()
		return redirect('my_cart')
	else:
		b.total_item-=1
		c.item.remove(b)
		b.save()
		c.item.add(b)
		c.cost-=t.price
		c.save()
		return redirect("my_cart")

def about(request):
	return HttpResponse("about page")
@login_required
def account(request):
	d=allorder.objects.all().filter(name=request.user).order_by('-datetime')
	return render(request,'account.html',{'d':d})
@login_required
def pre_buy(request):
	c=cart.objects.get(name=request.user)
	if request.method=='POST':
		country=request.POST['country']
		state=request.POST['state']
		city=request.POST['city']
		address=request.POST['address']
		ad=address+','+city+','+state+','+country
		a=allorder(name=request.user,cost=0,address=ad)
		a.save()
		xx=0
		for i in c.item.all():
			x=i.item
			y=i.total_item
			xx+=(y*x.price)
			z=order_count(item=x,item_count=y)
			z.save()
			a.item.add(z)
		a.cost=xx
		a.save()
		return redirect('account')
	return render(request,'pre_buy.html',{'c':c})