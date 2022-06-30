from django.shortcuts import render,HttpResponse,redirect
from . models import Posts
from django.utils import timezone
import math

# Create your views here.
def index(request):
    #nop=1
    posts=Posts.objects.filter(applicable="accept").all()
    '''last=math.ceil(len(posts)/int(nop)
    #page=request.args.get("page")
    if(not str(nop).isnumeric()):
        nop=1
    page=int(page)
    posts=posts[(page-1)*int(nop): (page-1)*int(nop)+int(nop)]
    if(page==1):
        prev="#"
        new="/?page="+str(page+1)
        
    elif(page==last):
        prev="/?page="+str(page-1)
        new="#"
          
    else:
        new="/?page="+str(page+1)
        prev="/?page="+str(page-1)
    
    #return render_template("index.html",params=params,posts=posts,new=new,prev=prev)
    '''
    return render(request,'index.html',{'posts':posts})#,{'new':new},{'prev':prev})

def post(request,slug):
    post=Posts.objects.filter(slug=slug).first


    return render(request,'post.html',{'post':post})

def add(request):
    if (request.method=='POST'):
        name=request.POST['name']
        title=request.POST['title']
        content=request.POST['content']
        slug=request.POST['slug']
        p=Posts.objects.filter(slug=slug).first
        if(p==None):
            message="This slug is taken"
            return render(request,'add.html',{"message":message})
        post=Posts.objects.create(name=name,title=title,content=content,slug=slug,applicable="accept",likes=0,dislikes=0,date=timezone.now())
        post.save()
        return redirect("/")

    else:
        return render(request,'add.html')
