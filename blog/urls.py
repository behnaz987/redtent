from django.urls import path, re_path
from rest_framework.urlpatterns import format_suffix_patterns
from blog import views

urlpatterns = [
    path('signin/', views.get_token_for_login),
    path('signup/', views.get_token_for_signup),

    re_path(r'designs/(_from=(?P<_from>[0-9]*)&_row=(?P<_row>[0-9]*)/)?$', views.list_of_design),
    re_path(r'designs/(_from=(?P<_from>[0-9]*)/)?$', views.list_of_design),
    re_path(r'designs/(_from=(?P<_from>[0-9]*)&_row=(?P<_row>[0-9]*)&_order_by=(?P<_order_by>[a-zA-z]*)/)?$',
            views.list_of_design),
    re_path(r'designs/(_order_by=(?P<_order_by>[a-zA-z]*)/)?$',
            views.list_of_design),

    path('designs/<int:design_id>', views.get_design),
    re_path('designs/((?P<design_id>[0-9]+))/tags/$', views.list_of_design_tags),

    path('designs/<int:design_id>/tags/<int:tag_id>', views.delete_design_tag),#[DELETE]


    path('designs/<int:design_id>/my_rate_for_design/', views.get_myrate),  # [GET]
    re_path(r'designs/((?P<design_id>[0-9]+))/rate_for_design/(_from=(?P<_from>[0-9]*)&_row=(?P<_row>[0-9]*)/)?$',
            views.list_of_rates_for_design),  # [GET,POST]

    path('rate_for_design/', views.all_rate_for_user),

    path('designs/<int:design_id>/rate_for_design/<int:rate_for_design_Id>', views.rate_for_design_operations),
    # [DELETE, PUT, GET]


    re_path(r'designs/((?P<design_id>[0-9]+))/comments_for_design/(_from=(?P<_from>[0-9]*)&_row=(?P<_row>[0-9]*)/)?$',
            views.list_of_comments_for_design),  # [POST,GET]


    path('designs/<int:design_id>/comments_for_design/<int:comment_Id>', views.comment_for_design_operations),
    # [PUT,DELETE,GET],

    path('designs/<int:design_id>/designers', views.list_of_a_post_designers),  # [GET,POST] -token

    re_path(r'designers/(_from=(?P<_from>[0-9]*)&_row=(?P<_row>[0-9]*)/)?', views.list_of_all_designers),  # [GET,POST]
 ####   path('designers/<int:designer_id>', views.test),#[GET, PUT, DELETE]


    re_path(r'designers/rates_for_designer/(_from=(?P<_from>[0-9]*)&_row=(?P<_row>[0-9]*)/)?', views.test),
    # [GET, POST]
    path('designers/rates_dor_designer/<int: rates_for_designer_id>', views.test),  # [DELETE, PUT, GET]
    re_path(r'designers/comments_for_designer?(_from=(?P<_from>[0-9]*)&_row=(?P<_row>[0-9]*)/)?', views.test),
    # [GET, POST]
    path('designers/comments_dor_designer/<int: rates_for_designer_id>', views.test),  # [DELETE, PUT, GET]
    #
    re_path(r'collections_of_designs/(_from=(?P<_from>[0-9]*)&_row=(?P<_row>[0-9]*)/)?',
            views.user_collection_of_designs),  # [GET, POST]
    path('collections_of_designs/<int:collection_of_design_id>', views.test),  # [GET, PUT, DELETE]
    #
    re_path(r'collections_of_designers/(_from=(?P<_from>[0-9]*)&_row=(?P<_row>[0-9]*)/)?', views.test),  # [GET,POST]
    path('collections_of_designers/<int:collection_of_designer_id>', views.test),  # [GET, PUT, DELETE]

    re_path(r'tags/<int:tag_id>/designs/(_from=(?P<_from>[0-9]*)&_row=(?P<_row>[0-9]*)/)?', views.test),  # [GET]
    path('tags/<int:tag_id>/designs/<design_id>', views.test),  # [GET]

    re_path(r'files/(?P<_path>[0-9a-z-A-Z]*)?', views.image)


]