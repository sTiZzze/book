from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt import views as jwt_views
from rest_framework_swagger.views import get_swagger_view
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

schema_view = get_swagger_view(title='Pastebin API')

urlpatterns = [
    path('swagger/', schema_view),
    path('admin/', admin.site.urls),
    path('api/library/', include('src.book.urls')),
    # path('api/dealerships/', include('src.dealership.urls')),
    # path('api/customer/', include('src.customer.urls')),
    path('api/login/', include('rest_framework.urls')),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]
urlpatterns += staticfiles_urlpatterns()
