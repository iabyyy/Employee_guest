from django.urls import path
from new_app import views

urlpatterns = [
    path('', views.dash, name='home'),
    path('contractor_reg', views.contractor_reg, name='contractor_reg'),
    path('guest_reg', views.guest_reg, name='guest_reg'),
    path('login_view', views.login_view, name='login_view'),
    path('guest_profile', views.guest_profile, name='guest_profile'),
    path('contractor_profile', views.contractor_profile, name='contractor_profile'),
    path('postjob', views.postjob, name='postjob'),
    path('admin_profile', views.admin_profile, name='admin_profile'),
    path('contractor_list', views.contractor_list, name='contractor_list'),
    path('contractor_update<int:id>', views.contractor_update, name='contractor_update'),
    path('contractor_delete<int:id>', views.contractor_delete, name='contractor_delete'),
]
