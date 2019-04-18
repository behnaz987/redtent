from django.urls import path, re_path
from rest_framework.urlpatterns import format_suffix_patterns
from blog import views

urlpatterns = [
    path('login/', views.get_token_for_login),
    path('signup/', views.get_token_for_signup),

    path('users/', views.users_list),
    path('users/<int:UserID>', views.user),
    path('users/<int:UserID>/collection_of_designs', views.ListOfCollectionOfDesign),
    path('users/<int:UserID>/collection_of_designs/<int:CollectionOfDesignsID>', views.CollectionOfDesign),
    path('users/<int:UserID>/comment_for_designer', views.ListOfCommentForDesigner),
    path('users/<int:UserID>/comment_for_design', views.ListOfCommentForDesign),
    path('users/<int:UserID>/Tag', views.ListOfTags),



    re_path(r'designs/(_from=(?P<_from>[0-9]*)&_row=(?P<_row>[0-9]*)/)?$',views.list_of_design),#[POST,GET]
    path('designs/<int:design_id>', views.get_design),#[GET,PUT,DELETE]

    re_path(r'designs/<int:design_id>/tags/(_from=(?P<_from>[0-9]*)&_row=(?P<_row>[0-9]*)/)?$', views.test),#[POST, GET]
    path('designs/<int:design_id>/tags/<int:tag_id>', views.test),#[DELETE]

    re_path(r'designs/<int:design_id>/rate_for_design/(_from=(?P<_from>[0-9]*)&_row=(?P<_row>[0-9]*)/)?$', views.test),#[GET,POST]
    path('designs/<int:design_id>/rate_for_design/<int:rate_for_design_Id>', views.test),#[DELETE, PUT, GET]

    re_path(r'designs/<int:design_id>/comments_for_design/(_from=(?P<_from>[0-9]*)&_row=(?P<_row>[0-9]*)/)?$', views.test),#[POST,GET]
    path('designs/<int:design_id>/comments_for_design/<int:comment_Id>', views.test),#[DELETE,GET],

    path('designs/<int:design_id>/designers', views.test),#[GET,POST] -token

    re_path(r'designers/(_from=(?P<_from>[0-9]*)&_row=(?P<_row>[0-9]*)/)?',views.test),#[GET,POST]
    path('designers/<int:designer_id>',views.test),#[GET, PUT, DELETE]
    re_path(r'designers/rates_for_designer/(_from=(?P<_from>[0-9]*)&_row=(?P<_row>[0-9]*)/)?', views.test),#[GET, POST]
    path('designers/rates_dor_designer/<int: rates_for_designer_id>', views.test),#[DELETE, PUT, GET]
    re_path(r'designers/comments_for_designer?(_from=(?P<_from>[0-9]*)&_row=(?P<_row>[0-9]*)/)?', views.test),#[GET, POST]
    path('designers/comments_dor_designer/<int: rates_for_designer_id>', views.test),#[DELETE, PUT, GET]
    #
    re_path(r'collections_of_designs/(_from=(?P<_from>[0-9]*)&_row=(?P<_row>[0-9]*)/)?', views.test),#[GET, POST]
    path('collections_of_designs/<int:collection_of_design_id>', views.test),#[GET, PUT, DELETE]
    #
    re_path(r'collections_of_designers/(_from=(?P<_from>[0-9]*)&_row=(?P<_row>[0-9]*)/)?', views.test),#[GET,POST]
    path('collections_of_designers/<int:collection_of_designer_id>', views.test),#[GET, PUT, DELETE]

    re_path(r'tags/<int:tag_id>/designs/(_from=(?P<_from>[0-9]*)&_row=(?P<_row>[0-9]*)/)?', views.test),#[GET]
    path('tags/<int:tag_id>/designs/<design_id>', views.test),# [GET]

    re_path(r'files/(?P<_path>[0-9a-z-A-Z]*)?', views.image)

]