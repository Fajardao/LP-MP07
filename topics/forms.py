from django import forms

class TopicForm(forms.Form):
    # Campo para o título do tópico
    title = forms.CharField(label="title", max_length=100)
    # Campo para a descrição do tópico
    description = forms.CharField(label="description", widget=forms.Textarea)

class CommentForm(forms.Form):
    # Campo para o comentário
    comment = forms.CharField(label="comment", widget=forms.Textarea)

class LoginForm(forms.Form):
    # Campo para o nome de utilizador
    username = forms.CharField(label="username", max_length=100)
    # Campo para a palavra-passe
    password = forms.CharField(label="password", widget=forms.PasswordInput)

class RegisterForm(forms.Form):
    # Campo para o nome de utilizador
    username = forms.CharField(label="username", max_length=100)
    # Campo para a palavra-passe
    password = forms.CharField(label="password", widget=forms.PasswordInput)
    # Campo para confirmar a palavra-passe
    password2 = forms.CharField(label="password2", widget=forms.PasswordInput)
    # Campo para o email
    email = forms.EmailField(label="email", max_length=100)