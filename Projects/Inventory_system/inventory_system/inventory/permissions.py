"""Role-based access control built on Django groups.

Staff   - view products, record stock movements, view transactions
Manager - everything Staff can do + add/edit products and categories, reports, CSV export
Admin   - everything Manager can do + delete products
Superusers are always treated as Admin.
"""
from functools import wraps

from django.contrib.auth.views import redirect_to_login
from django.core.exceptions import PermissionDenied

ADMIN, MANAGER, STAFF = "Admin", "Manager", "Staff"
ALL_ROLES = (STAFF, MANAGER, ADMIN)

# A role also grants every role listed after it in this hierarchy.
HIERARCHY = {STAFF: 1, MANAGER: 2, ADMIN: 3}


def user_role(user):
    if not user.is_authenticated:
        return None
    if user.is_superuser:
        return ADMIN
    names = set(user.groups.values_list("name", flat=True))
    ranked = [r for r in ALL_ROLES if r in names]
    return max(ranked, key=HIERARCHY.get) if ranked else None


def has_role(user, minimum):
    role = user_role(user)
    return role is not None and HIERARCHY[role] >= HIERARCHY[minimum]


def role_required(minimum):
    """View decorator: login needed (redirects) and at least `minimum` role (403 otherwise)."""
    def decorator(view):
        @wraps(view)
        def wrapper(request, *args, **kwargs):
            if not request.user.is_authenticated:
                return redirect_to_login(request.get_full_path())
            if not has_role(request.user, minimum):
                raise PermissionDenied
            return view(request, *args, **kwargs)
        return wrapper
    return decorator
