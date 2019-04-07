from django.core.validators import RegexValidator
from django.db import models


class Tag(models.Model):
    body = models.CharField(max_length=20)


class UserAccount (models.Model):
    firstName = models.CharField(max_length=20, validators=[
        RegexValidator(
            regex='^[a-zA-Z]*$',
        ),
    ])

    lastName = models.CharField(max_length=20, validators=[
        RegexValidator(
            regex='^[a-zA-Z]*$',
        ),
    ])

    username = models.CharField(max_length=20, validators=[
        RegexValidator(
            regex='^[a-zA-Z0-9]*$',
        ),
    ])

    password = models.CharField(max_length=40, validators=[RegexValidator(regex='')])

    isDesigner = models.BooleanField()
    tag = models.ManyToManyField(Tag)


class Designer(models.Model):
    user = models.OneToOneField(UserAccount, related_name='designer', on_delete=models.CASCADE)
    phoneNumber = models.IntegerField(validators=[RegexValidator(regex='')])
    city = models.CharField(max_length=20, validators=[RegexValidator(regex='')])
    address = models.CharField(max_length=150)
    comments = models.ManyToManyField(UserAccount, through='CommentForDesigner',
                                      through_fields=('userAccount', 'designer'))
    rates = models.ManyToManyField(UserAccount, through='RateForDesigner',
                                   through_fields=('userAccount', 'designer'))


class RateForDesigner(models.Model):
    rate = models.IntegerField()
    userAccount = models.ForeignKey(UserAccount, related_name='rates_for_designer')
    designer = models.ForeignKey(Designer, related_name='rates_for_designer')


class CommentForDesigner(models.Model):
    body = models.CharField(max_length=500)
    isvalid = models.BooleanField()
    userAccount = models.ForeignKey(UserAccount, related_name='comments_for_designer')
    designer = models.ForeignKey(Designer, related_name='comments_for_designer')


class Design(models.Model):
    pic = models.ImageField( )
    comments = models.ManyToManyField(UserAccount, through='CommentForDesign',
                                      through_fields=('userAccount', 'design'))
    tag = models.ManyToManyField(Tag, related_name='designs')
    designer = models.ManyToManyField(Designer, related_name='designs')


class CommentForDesign(models.Model):
    body = models.CharField(max_length=500)
    isValid = models.BooleanField()
    userAccount = models.ForeignKey(UserAccount, related_name='comments_for_design')
    design = models.ForeignKey(Design, related_name='comments_for_design')


class RateForTag(models.Model):
    rate = models.IntegerField()
    userAccount = models.ForeignKey(UserAccount)
    tag = models.ForeignKey(Tag)


class CollectionOfDesign(models.Model):
    title = models.CharField(max_length=20)
    collPic = models.ImageField(upload_to=None,)
    userAccount = models.ForeignKey(UserAccount, related_name='collections_of_design')


class CollectionOfDesigner(models.Model):
    title = models.CharField(max_length=20)
    collectionPicture = models.ImageField(upload_to=None,)
    designer = models.ManyToManyField(Designer)


class Designer(models.Model):
    user = models.OneToOneField(UserAccount, related_name='designer', on_delete=models.CASCADE)
    phoneNumber = models.IntegerField(validators=[RegexValidator(regex='')])
    city = models.CharField(max_length=20,validators=[RegexValidator(regex='')])
    address = models.CharField(max_length=150)


class DesignerRecord(models.Model):
    pic = models.ImageField()
    description = models.CharField(max_length=500)
    designer = models.ForeignKey(Designer, related_name='designer_records')


