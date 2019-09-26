from django.shortcuts import render, redirect, get_object_or_404
from .models import Article
from .forms import ArticleForm

# 모든 aricle을 보여주는 페이지
def index(request):
    # 모든 article 담는 과정
    articles = Article.objects.all()
    context = {'articles': articles}
    return render(request, 'articles/index.html', context)

# GET으로 들어오면 생성하는 페이지 renderin'
# POST로 들어오면 생성하는 로직 수행
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        # 사용자가 입력한 데이터 유효성 확인
        if form.is_valid():
            # forms.py에서 걸러진 깨끗한 데이터로부터 해당 데이터 가져오는 작업
            title = form.cleaned_data.get('title')
            content = form.cleaned_data.get('content')
            # form 이 valid 한 경우에만 데이터 저장
            article = Article(title=title, content=content)
            article.save()
            return redirect('articles:index')
        # else:
        #     # valid 한 값이 있지 않은 form을 다시 보내주는 작업
        #     # (이상한 값이 있으면 다시 입력하라는 화면 보여주는 것; 중간에 잘못 입력하더라도 입력값을 그대로 넣은 채로 다시 form 보내주면서 다시 입력하라는 요청)
        #     context = {'form': form}
        #     return render(request, 'articles/create.html', context)
    else:
        form = ArticleForm()
    # context = {'form':form}, return이 중복되니까, 코드를 줄일 수 있다.
    context = {'form': form} 
    return render(request, 'articles/create.html', context)

def detail(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    context = {'article': article}
    return render(request, 'articles/detail.html', context)
