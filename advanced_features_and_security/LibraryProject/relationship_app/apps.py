
from django.apps import AppConfig

class RelationshipAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'relationship_app'
# from django.apps import AppConfig
# from django.shortcuts import render
# from django.contrib.auth.decorators import user_passes_test


# @user_passes_test(lambda u: u.is_authenticated and u.userprofile.role == 'Admin')
# def admin_view(request):
#     return render(request, 'relationship_app/admin_view.html')

# # Librarian view
# @user_passes_test(lambda u: u.is_authenticated and u.userprofile.role == 'Librarian')
# def librarian_view(request):
#     return render(request, 'relationship_app/librarian_view.html')

# # Member view
# @user_passes_test(lambda u: u.is_authenticated and u.userprofile.role == 'Member')
# def member_view(request):
#     return render(request, 'relationship_app/member_view.html')


# class RelationshipAppConfig(AppConfig):
#     default_auto_field = 'django.db.models.BigAutoField'
#     name = 'relationship_app'
