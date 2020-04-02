from django.shortcuts import render, HttpResponse, reverse, redirect

# Create your views here.
from app01 import models


def db_test(request):
    # print(reverse('part1:main'))
    # 1、增加
    # 1.1、一对一增加
    # new_author_detial = models.AuthorDetail.objects.create(
    #     birthday = '2019-05-02',
    #     teltphone = '14560',
    #     addr = '东北莲花乡池水沟子'
    # )
    # 方式1
    # models.Author.objects.create(
    #     name='王涛',
    #     age = '40',
    #     authorDetail=new_author_detial
    # )

    # 方式2
    # models.Author.objects.create(
    #     name='王涛',
    #     age = '40',
    #     authorDetail_id=new_author_detial.id
    # )

    # #  1.2 一对多
    # new_book = models.Book.objects.create(
    #     title='bottle',
    #     publishDate = '2020-8-8',
    #     price = '123.45',
    #     publish_by = models.Publish.objects.get(id=1),
    # )
    # #  1.3 多对多
    # book = models.Book.objects.get(id=3)
    # book.author2book.add(*[1,2,3,4])

    # 删除
    # 一对一、一对多
    # author = models.AuthorDetail.objects.get(id=5)
    # author.delete()
    # 多对多
    # book = models.Book.objects.get(id=3)
    # # # book.author2book.remove(*[1,2])
    # # book.author2book.clear()
    # book.author2book.set(['1','2','3','4'])

    # 更新
    # 一对一
    # author = models.Author.objects.filter(id=4).update(authorDetail_id=4)

    return render(request, 'index.html')


def book(requests):
    all_obj = models.Book.objects.all()
    return render(requests, 'book.html', {'all_obj': all_obj})


def add(request):
    if request.method == "GET":
        publishs = models.Publish.objects.all()
        return render(request, 'add_data.html',{'publishs':publishs})
    else:
        models.Book.objects.create(
            title=request.POST['book_title'],
            publishDate=request.POST['book_pub_date'],
            price=request.POST['book_price'],
            publish_by=models.Publish.objects.filter(name=request.POST['book_publish']).first(),
        )
        return redirect('app01:book')


def edit(requst,book_id):
    if requst.method == "GET":
        publishs = models.Publish.objects.all()
        obj = models.Book.objects.filter(id=book_id).first()
        return render(requst, 'edit_data.html',{'obj':obj,'publishs':publishs})
    else:
        models.Book.objects.filter(id=book_id).update(
            title = requst.POST['book_title'],
            publishDate = requst.POST['book_pub_date'],
            price = requst.POST['book_price'],
            publish_by_id = models.Publish.objects.filter(name=requst.POST['book_publish']).first(),
        )
        return redirect('app01:book')


def delete(request,book_id):
    models.Book.objects.filter(id=book_id).delete()
    return redirect('app01:book')
