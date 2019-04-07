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
    comments = models.ManyToManyField(UserAccount, through='CommentForDesigner',related_name='Designer1')
    rates = models.ManyToManyField(UserAccount, through='RateForDesigner',related_name='Designer2')


class RateForDesigner(models.Model):
    rate = models.IntegerField()
    userAccount = models.ForeignKey(UserAccount, related_name='rates_for_designer', on_delete=models.CASCADE)
    designer = models.ForeignKey(Designer, related_name='rates_for_designer', on_delete=models.CASCADE)

#
# class Designer(models.Model):
#     user = models.OneToOneField(UserAccount, related_name='designer', on_delete=models.CASCADE)
#     phoneNumber = models.IntegerField(validators=[RegexValidator(regex='')])
#     city = models.CharField(max_length=20,validators=[RegexValidator(regex='')])
#     address = models.CharField(max_length=150)
#


class CommentForDesigner(models.Model):
    body = models.CharField(max_length=500)
    isvalid = models.BooleanField()
    userAccount = models.ForeignKey(UserAccount, related_name='comments_for_designer', on_delete=models.CASCADE)
    designer = models.ForeignKey(Designer, related_name='comments_for_designer', on_delete=models.CASCADE)


class Design(models.Model):
    pic = models.ImageField()
    comments = models.ManyToManyField(UserAccount, through='CommentForDesign' )
    tag = models.ManyToManyField(Tag, related_name='designs')
    designer = models.ManyToManyField(Designer, related_name='designs')


class CommentForDesign(models.Model):
    body = models.CharField(max_length=500)
    isValid = models.BooleanField()
    userAccount = models.ForeignKey(UserAccount, related_name='comments_for_design', on_delete=models.CASCADE)
    design = models.ForeignKey(Design, related_name='comments_for_design', on_delete=models.CASCADE)


class RateForTag(models.Model):
    rate = models.IntegerField()
    userAccount = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)


class CollectionOfDesign(models.Model):
    title = models.CharField(max_length=20)
    collPic = models.ImageField(upload_to=None,)
    userAccount = models.ForeignKey(UserAccount, related_name='collections_of_design',on_delete=models.CASCADE)


class CollectionOfDesigner(models.Model):
    title = models.CharField(max_length=20)
    collectionPicture = models.ImageField(upload_to=None,)
    designer = models.ManyToManyField(Designer)


class DesignerRecord(models.Model):
    pic = models.ImageField()
    description = models.CharField(max_length=500)
    designer = models.ForeignKey(Designer, related_name='designer_records', on_delete=models.CASCADE)


