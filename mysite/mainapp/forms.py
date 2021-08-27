from django import forms
from .models import Comment, User, Post, PostCategory
from django.forms import fields, widgets
from captcha.fields import CaptchaField

# если делать так, как строчкой ниже - то это хардкодинг: когда будет добавляться новая категория, нужно
# будет лезть сюда и добавлять отдельно созданную категорию в этот список

#choices = [('Рецептуры коктейлей', 'Рецептуры коктейлей'), ('Рецептуры настоек', 'Рецептуры настоек'), ('Заведения', 'Заведения'),]

# поэтому нужно сделать таким обазом - от модели запросить все элементы, создать список пустой, в который
# динамически будут добавлены автоматом все новые записи от админки, которые будут иметь отношение к категории
choices = PostCategory.objects.all().values_list('name', 'name')
choice_list = []

for item in choices:
    choice_list.append(item)


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title','post_category','author','body','uploaded_image','short_description')
        # так как каждая строка в форме - это TextInput или Textarea, если просмотреть в режиме разработчика HTML-страницу,
        # то, чтобы изменить стиль - в виджетах устанавливается класс, который имеет название, использующееся в
        # файле CSS. Оно (название) может быть рандомным
        widgets = {
            'title' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Введите краткий заголовок'}),
            'post_category': forms.Select(choices=choice_list, attrs={'class':'form-control-select'}),
            # закомментирована строка автора с Select-выбором для того, чтобы не давать пользователю
            # возможность выбора автора поста. ID приписан для того, чтобы сказать JavaScript, какую из
            # форм TextInput нужно заполнять атоматически
            # value пустое, чтобы дать возможность скрипту самому вставлять автоматически ID пользователя
            # type:hidden попросту скрывает данную форму для отображения в браузере (но она есть)
            'author' : forms.TextInput(attrs={'class':'form-control', 'id':'user_id', 'value':'', 'type':'hidden'}),
            #'author': forms.Select(attrs={'class':'form-control-select'}),
            'body' : forms.Textarea(attrs={'class':'form-control-body', 'placeholder':'Введите текст'}),
            'short_description': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Краткое описание поста'})
        }


class ForumPostUpdateForm(forms.ModelForm):
    
    class Meta:
        model = Post
        fields = ('title','body')
        # так как каждая строка в форме - это TextInput или Textarea, если просмотреть в режиме разработчика HTML-страницу,
        # то, чтобы изменить стиль - в виджетах устанавливается класс, который имеет название, использующееся в
        # файле CSS. Оно (название) может быть рандомным
        widgets = {
            'title' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Введите краткий заголовок'}),
            'body' : forms.Textarea(attrs={'class':'form-control-body', 'placeholder':'Введите текст'}),
        }


class ForumPostCategoryAdd(forms.ModelForm):
    
    class Meta:
        model = PostCategory
        fields = ('name',)
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Введите название новой категории'})
        }