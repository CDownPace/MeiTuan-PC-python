from rest_framework.views import APIView
from django.contrib.auth import authenticate
from rest_framework.authtoken.serializers import AuthTokenSerializer
from django.utils.timezone import now
# 获取带有时区的时间
from apps.mtauth.authentications import generate_jwt,JWTAuthentication
from apps.mtauth.serializers import UserSerializer
from rest_framework.response import Response
# from rest_framework import viewsets
# # from apps.meituan.serializers import MerchantSerializer,GoodsCategorySerializer,GoodsSerializer
# # from apps.meituan.models import Merchant,GoodsCategory,Goods
# from rest_framework import permissions
# from rest_framework.pagination import PageNumberPagination
# import shortuuid
# import os
# from django.conf import settings
# from rest_framework import mixins
# from rest_framework.decorators import action
# from rest_framework import status
# from apps.mtauth.permissions import IsEditorUser,IsFinanceUser

# class MerchantPagination(PageNumberPagination):
#     page_size = 12
#     page_query_param = "page"

# class CmsBaseView(object):
#     permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]

class LoginView(APIView):
    def post(self,request):
        serializer = AuthTokenSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data.get('user')
            user.last_login = now()
            user.save()
            token = generate_jwt(user)
            user_serializer = UserSerializer(user)
            return Response({"token":token,"user":user_serializer.data})
        else:
            print(dict(serializer.errors))
            return Response({"message":"用户名或密码错误！"}
                            # ,status=status.HTTP_400_BAD_REQUEST
            )
 #
 # class MerchantViewSet(viewsets.ModelViewSet):
 #    queryset = Merchant.objects.order_by("-create_time").all()
 #    serializer_class = MerchantSerializer
 #    pagination_class = MerchantPagination
 #    permission_classes = [permissions.IsAuthenticated,IsEditorUser]

# Create,Update,Destroy,Retrieve
# class CategoryViewSet(
#     CmsBaseView,
#     viewsets.GenericViewSet,
#     mixins.CreateModelMixin,
#     mixins.UpdateModelMixin,
#     mixins.DestroyModelMixin,
#     mixins.RetrieveModelMixin
# ):
    # queryset = GoodsCategory.objects.all()
    # serializer_class = GoodsCategorySerializer
    # permission_classes = [permissions.IsAuthenticated, IsEditorUser]

    # def destroy(self, request, *args, **kwargs):
    #     instance = self.get_object()
    #     if instance.goods_list.count() > 0:
    #         return Response(status=status.HTTP_400_BAD_REQUEST)
    #     else:
    #         self.perform_destroy(instance)
    #         return Response(status=status.HTTP_204_NO_CONTENT)

    # # /cms/category/merchant/<int:merchant_id>
    # @action(['GET'],detail=False,url_path="merchant/(?P<merchant_id>\d+)")
    # def merchant_category(self,request,merchant_id=None):
    #     queryset = self.get_queryset()
    #     seriazlier_class = self.get_serializer_class()
    #     categories = queryset.filter(merchant=merchant_id)
    #     serializer = seriazlier_class(categories,many=True)
    #     return Response(serializer.data)

# class GoodsViewSet(
#     CmsBaseView,
#     viewsets.GenericViewSet,
#     mixins.CreateModelMixin,
#     mixins.UpdateModelMixin,
#     mixins.DestroyModelMixin,
#     mixins.RetrieveModelMixin
# ):
    # queryset = Goods.objects.all()
    # serializer_class = GoodsSerializer
    # permission_classes = [permissions.IsAuthenticated, IsEditorUser]

# class PictureUploadView(CmsBaseView,APIView):
#     def save_file(self,file):
#         # 肯德基.jpg = ('肯德基,'.jpg')
#         filename = shortuuid.uuid() + os.path.splitext(file.name)[-1]
#         filepath = os.path.join(settings.MEDIA_ROOT,filename)
#         with open(filepath,'wb') as fp:
#             for chunk in file.chunks():
#                 fp.write(chunk)
#         # http://127.0.0.1:8000/media/abc.jpg
#         return self.request.build_absolute_uri(settings.MEDIA_URL + filename)
#
#     def post(self,request):
#         file = request.data.get('file')
#         file_url = self.save_file(file)
#         return Response({"picture":file_url})
#
# from django.contrib.auth import get_user_model
# from django.contrib.auth.models import Group
# MTUser = get_user_model()
#
# class InitStaff(APIView):
#     permission_classes = []
#     def get(self,request):
#         users = MTUser.objects.all()
#         for user in users:
#             user.set_password("111111")
#             user.save()
#
#         edit_group = Group.objects.get(name="编辑")
#         user1 = MTUser.objects.get(telephone="18899990000")
#         user1.groups.add(edit_group)
#         user1.save()
#
#         finance_group = Group.objects.get(name="财务")
#         user2 = MTUser.objects.get(telephone="18800009999")
#         user2.groups.add(finance_group)
#         user2.save()
#         return Response("success")