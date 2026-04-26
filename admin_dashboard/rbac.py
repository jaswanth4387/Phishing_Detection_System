def is_provider(user):
    return user.is_authenticated and (
        user.is_superuser or user.groups.filter(name='provider').exists()
    )

def is_user(user):
    return user.is_authenticated and user.groups.filter(name='User').exists()