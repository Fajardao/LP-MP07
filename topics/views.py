from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .models import Topic, Comment
from .forms import *
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth import logout

user = None

def index(request):
    global user 
    if user is None:
        user = request.user

    # Obtém a lista de tópicos ordenados pela data de criação
    list = Topic.objects.order_by("created_at")
    template = loader.get_template("app/index.html")

    context = { "list": list , 'user': user}

    if request.method == "POST":
        form = TopicForm(request.POST)
        if form.is_valid():
            # Cria um novo tópico com os dados do formulário
            title = form.cleaned_data["title"]
            description = form.cleaned_data["description"]
            topic = Topic(title=title, description=description, author=user)
            topic.save()

            context.update({ "message": "Topic created successfully" })

    return HttpResponse(template.render(context, request))

def detail(request, topic_id):
    # Obtém o tópico pelo ID
    topic = Topic.objects.get(id=topic_id)
    template = loader.get_template("app/details.html")

    # Obtém os comentários associados ao tópico
    comments = Comment.objects.filter(topic=topic)

    context = { "topic": topic, "comments": comments, 'user': user}

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            # Cria um novo comentário com os dados do formulário
            comment = form.cleaned_data["comment"]
            comment = Comment(text=comment, author=user, topic=topic)
            comment.save()
            context.update({ "message": "Comment created successfully" })

    if request.method == "POST":
        form = TopicForm(request.POST)
        if form.is_valid():
            # Atualiza o tópico com os novos dados do formulário
            title = form.cleaned_data["title"]
            description = form.cleaned_data["description"]
            topic.title = title
            topic.description = description
            topic.save()
            context.update({ "message": "Topic updated successfully" })

    return HttpResponse(template.render(context, request))

def new(request):
    global user
    template = loader.get_template("app/new.html")
    content = { 'user': user, 'form': TopicForm() }
    return HttpResponse(template.render(content, request))

def login(request):
    global user

    context = { "user": user }
    template = loader.get_template("app/login.html")

    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            # Autentica o utilizador com os dados do formulário
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            
            user = authenticate(username=username, password=password)
            if user is not None:
                context.update({ "message": "Login successful" })
                return redirect('index')
            else:
                context.update({ "message": "Login failed" })

    return HttpResponse(template.render(context, request))

def logout_view(request):
    # Faz logout do utilizador
    logout(request)
    global user
    user = None
    return redirect('index')

def register(request):
    global user

    template = loader.get_template("app/register.html")
    context = {'user': user}

    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            # Regista um novo utilizador com os dados do formulário
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            password2 = form.cleaned_data["password2"]
            email = form.cleaned_data["email"]
            if password != password2:
                context.update({ "message": "Passwords do not match" })
                return HttpResponse(template.render(context, request))
            if User.objects.filter(username=username).exists():
                context.update({ "message": "Username already exists" })
                return HttpResponse(template.render(context, request))
            user = User.objects.create_user(username=username, password=password, email=email)
            user.save()
            return redirect('index')
        
    return HttpResponse(template.render(context, request))

def delete(request, topic_id):
    # Elimina o tópico pelo ID
    topic = Topic.objects.get(id=topic_id)
    topic.delete()
    return redirect('index')

def edit(request, topic_id):
    # Obtém o tópico pelo ID para edição
    topic = Topic.objects.get(id=topic_id)
    template = loader.get_template("app/edit.html")
    context = { "topic": topic, "user": user }

    return HttpResponse(template.render(context, request))