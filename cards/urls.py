from django.urls import path
from . import views
from django.conf.urls.static import static 
from django.conf import settings
from django.contrib.auth import views  as auth_view
from . forms import LoginForm , MyPasswordResetForm , MyPasswordChangeForm , MySetPasswordForm

urlpatterns = [
    path("",views.home),
    path("about/",views.About,name="about"),
    path("contact/",views.Contact,name="contact"),
    path("category/<slug:val>",views.CategoryView.as_view(), name="category"),
    path("category-title/<val>",views.categoryTitle.as_view(), name="category-title"),
    path("product-detail/<int:pk>",views.ProductDetail.as_view(), name="product-detail"),
    path("profile/",views.ProfileView.as_view(), name="profile"),
    path("address/",views.address, name="address"),
    path("updateAddress/<int:pk>",views.updateAddress.as_view(),name="updateAddress"),
    path("add-to-cart/",views.add_to_cart,name='add-to-cart'),
    path("cart/",views.show_cart,name='showcart'),
    path("chekout/",views.show_cart,name='chekout'),

   #login Authentication
    path('registration/',views.CustomerRegistrationView.as_view(),name='customerregistration'),

    # here we dont need to write view immedietly we write url and  inside this url we have build in view called "auth_view" only we need import it in the up 
    path('accounts/login/',auth_view.LoginView.as_view(template_name='cards/login.html',authentication_form=LoginForm),name='login'),
    path('passwordchange/',auth_view.PasswordChangeView.as_view(template_name='cards/changepassword.html',form_class=MyPasswordChangeForm,success_url='/passwordchangedone'),name='Passwordchange'),
    path('passwordchangedone/',auth_view.PasswordChangeDoneView.as_view(template_name='cards/passwordchangedone.html'),name='Passwordchangedone'),
    path('logout/',auth_view.LogoutView.as_view(next_page='login') , name='logout'),
    
    
    #Forgit Password and reset this password to email address 
    path('password-reset/',auth_view.PasswordResetView.as_view(template_name='cards/password_reset.html',form_class=MyPasswordResetForm),name='password_reset'),
    path('password-reset/done/',auth_view.PasswordResetDoneView.as_view(template_name='cards/password_reset_done.html'),name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',auth_view.PasswordResetConfirmView.as_view(template_name='cards/password_reset_confirm.html',  form_class=MySetPasswordForm) ,name='password_reset_confirm'),
    path('password-reset-complete/',auth_view.PasswordResetCompleteView.as_view(template_name='cards/password_reset_complete.html'),name='password_reset_complete'),

   
    # path("new", views.CardCreateView.as_view(), name="card-create"),
#     path("edit/<int:pk>", views.CardUpdateView.as_view(), name="card-update"),
#     path("box/<int:box_num>", views.BoxView.as_view(), name="box"),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)


