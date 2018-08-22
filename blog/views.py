from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone
from .models import Post
from .forms import PostForm

# Create your views here.

def post_list(request):
    qs = Post.objects.all() # 전체에서
    qs = qs.filter(published_date__lte=timezone.now()) # 현재시각보다 전에 시각으로 필터를 거치고
    qs = qs.order_by('published_date') # 퍼블리싱 날짜에 대해 오름차순으로 가져오려고 한다
    
    return render(request, 'blog/post_list.html',{ 
        'post_list':qs, # post_list에 qs를 가져가겠다
    })
    # render는 장고가 지원하는 템플릿 시스템
    # 동적데이터를 뷰 단에서 준비해서 넘기는 코드를 작성하였다.

def post_detail(request,pk): # pk라는 이름으로 post_detail 함수에 넘기겠다
    post = get_object_or_404(Post,pk=pk)
    #try:
     #   post = Post.objects.get(pk=pk)
    #except Post.DoesNotExist:
     #   raise Http404 # Page not found : from django.http import Http404
    # pk = 1이면 
    #post = Post.objects.get(pk=pk) # 앞의 pk는 어떤 필드를 뜻하는 것이고 뒤의 pk는 인자로 받은 매개변수 pk
    return render(request, 'blog/post_detail.html',{ # url로 pk에 1을 넘겨주면 post_detail.html로 넘겨준다
    'post' : post,
    })

# @login_required -> 로그인 인증 관련

def post_new(request):
    # request.POST, request.FILES 

    if request.method == 'POST': # 현재요청이 POST라면
        form = PostForm(request.POST, request.FILES) # PostForm을 생성할 때 매개변수에서 그 값을 가져와서 폼을 만든다
        if form.is_valid(): # 유효성 검사
            post = form.save(commit=False)
            post.author = request.user #로그인 유저 정보를 가져오는 코드인데 비인증유저라면 오류가 발생한다
            post.published_date = timezone.now()
            post.save() # 통과가 되면 데이터베이스에 저장을 시도한다
            return redirect('post_detail',pk = post.pk)
    else:
        form = PostForm()  # 실패하게 되면 그냥 form으로 빠진다

    return render(request, 'blog/post_edit.html', {'form': form})
    #현재 글을 써서 보내면 처음에 post_new form이 뜰때는 get방식으로 보내고 
    #댓글을 작성해서 보내면 같은 url로 POST방식으로 보낸다
    #양식을 작성한 데이타가 request.POST, request.FILES에 담기게 된다

    # 그런 값들을 처리하는 로식을 return위에 적었다
    # 여기까지 해도 글이 추가되지 않는다
    

# 들여쓰기 꼭 신경쓸 것

def post_edit(request,pk): # pk라는 이름으로 post_detail 함수에 넘기겠다
    post = get_object_or_404(Post,pk=pk)

    if request.method == 'POST': # 현재요청이 POST라면
        form = PostForm(request.POST, request.FILES, instance = post) # PostForm을 생성할 때 매개변수에서 그 값을 가져와서 폼을 만든다
        # instance = post 는 수정할 대상 타입
        if form.is_valid(): # 유효성 검사
            post = form.save(commit=False)
            post.author = request.user #로그인 유저 정보를 가져오는 코드인데 비인증유저라면 오류가 발생한다
            post.published_date = timezone.now()
            post.save() # 통과가 되면 데이터베이스에 저장을 시도한다
            return redirect('post_detail',pk = post.pk)
    else:
        form = PostForm(instance = post)  # 수정에 들어가게된다
    
    return render(request, 'blog/post_edit.html',{ # url로 pk에 1을 넘겨주면 post_detail.html로 넘겨준다
    'form' : form, # 이 form을 템플릿에 넘기는 것 
    })