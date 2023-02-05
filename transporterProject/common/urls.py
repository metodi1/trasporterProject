from django.urls import path, include

from transporterProject.common import views
from transporterProject.common.views import Production_Line_View, Home_page

urlpatterns = (
    path('', views.Home_page, name='home page'),
    path('warehouse/', views.Warehouse_page_View.as_view(), name='warehouse page'),
    path('warehouse/<int:pk>', views.Warehouse_Edit_View.as_view(), name='warehouse page edit'),
    path('warehouse/<int:pk>/delete', views.Warehouse_Delete_view.as_view(), name='warehouse page delete'),

    path('line_catalog', views.Production_line_catalog.as_view(), name='lines catalog'),
    path('line_catalog/<int:pk>', views.Production_line_catalog_edit.as_view(), name='lines catalog edit'),
    path('line_catalog/<int:pk>/delete', views.Production_line_catalog_delete.as_view(), name='lines catalog delete'),

    path('production_line/<int:pk>/details', Production_Line_View, name='production line'),
    path('production_line/<int:pk>', views.Production_Line_Edit_View.as_view(), name='production line edit'),
    path('production_line/<int:pk>/delete', views.Production_Line_Delete_View.as_view(), name='production line delete'),

    path('production_line/<int:pk>/task/', include('transporterProject.tasks.urls')),

)
