from .permissions import ADMIN, MANAGER, has_role, user_role


def roles(request):
    return {
        "role": user_role(request.user),
        "can_manage": has_role(request.user, MANAGER),
        "can_admin": has_role(request.user, ADMIN),
    }
