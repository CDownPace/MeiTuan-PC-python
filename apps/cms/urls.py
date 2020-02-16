from django.urls import path
# from . import views
# from rest_framework.routers import DefaultRouter

from .views import LoginView
app_name = 'cms'

# router = DefaultRouter(trailing_slash=False)
# # router.register('merchant',views.MerchantViewSet,basename='merchant')
# # router.register('category',views.CategoryViewSet,basename='category')
# # router.register('goods',views.GoodsViewSet,basename='goods')
# /cms/merchant

urlpatterns = [
    # path('login',views.LoginView.as_view(),name="login"),
    path('login',LoginView.as_view(),name="login"),
    # path('upload',views.PictureUploadView.as_view(),name='upload'),
    # path('initstaff',views.InitStaff.as_view(),name="initstaff")
]
# ] + router.urls