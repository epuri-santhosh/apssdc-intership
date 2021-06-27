from django.shortcuts import render
from django.http import HttpResponse
from .models import Register
# Create your views here.
def home(request):
	return HttpResponse("hi all") 
def htmltag(request):
	return HttpResponse("<h2>Hi all</h2>")

def usernameprint(request,uname):
	return HttpResponse("<h2> hi welcome <span style='color:green'>{}</span></h2".format(uname))

def usernameage(request,un,ag):
	return HttpResponse("<h3 style='text-align:center'>Hi user <span style='color:red'> {} </span> and your ages is <span style='color:green'>{}</span>".format(un,ag))

def htm(request):
    return render(request,'html/sample1.html')	

def registerform(req):
	if req.method =="POST":
		firstname=req.POST['firstname']
		lastname=req.POST['lastname']
		phonenumber=req.POST['phonenumber']
		email=req.POST['email']
		adress=req.POST['adress']
		gender=req.POST['gender']
		language=req.POST['language']
		data={'user1':firstname,'user2':lastname,'user3':phonenumber,'user4':email,'user5':adress,'user6':language,'user7':gender}
		return render (req,'html/display.html',data)
	return render(req,'html/registerform.html')
	

def bt(request):
	return render(request,'html/bt.html')


def register1(req):
	name="siva"
	email="S@1"
	reg=Register(name="siva",email="S@1")
	reg.save()
	return HttpResponse("coloumn is inserted")

def register2(request):
	if request.method == 'POST':
		name = request.POST['name']
		email = request.POST['email']
		reg = Register(name = name, email = email)
		reg.save()
		return HttpResponse("Record inserted successfully....")
	return render(request,"html/register2.html")

def display(request):
	data = Register.objects.all()
	return render(request,'html/display1.html',{'data':data})
def sview(request,y):
	w = Register.objects.get(id=y)
	return render(request,'html/sview.html',{'y':w})
	#return HttpResponse("Your Name is: {} and your email id is: {}".format(w.name,w.email))

def supt(request,q):
	t = Register.objects.get(id=q)
	if request.method == "POST":
		na = request.POST['n']
		em = request.POST['e']
		t.name = na
		t.email = em
		t.save()
		return redirect('/display/')
	return render(request,'html/update.html',{'p':t})

