from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=32, verbose_name='作者姓名')
    age = models.IntegerField(verbose_name='作者年龄')
    authorDetail = models.OneToOneField(verbose_name='外键连接到作者详细信息', to="AuthorDetail", to_field="id",null=True,
                                        on_delete=models.SET_NULL)

    # CASCADE 级联
    # SET_NULL 置空
    def __str__(self):
        return self.name


class AuthorDetail(models.Model):
    birthday = models.DateField(verbose_name='作者生日')
    teltphone = models.BigIntegerField(verbose_name='作者电话')
    addr = models.CharField(max_length=64, verbose_name='作者地址')

    def __str__(self):
        return self.addr


class Publish(models.Model):
    name = models.CharField(max_length=32, verbose_name='出版社名称')
    city = models.CharField(max_length=32, verbose_name='出版社所在地')
    email = models.EmailField(verbose_name='出版社邮箱')

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=50, verbose_name='书名')
    publishDate = models.DateField(verbose_name='出版日期')
    price = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='价格')
    publish_by = models.ForeignKey(to='Publish', to_field='id', on_delete=models.CASCADE)
    author2book = models.ManyToManyField(to='Author')

    def __str__(self):
        return self.title

# class BookToAuthor(models.Model):
#     book_id = models.ForeignKey(to='Book')
#     Author_id = models.ForeignKey(to='Author')
