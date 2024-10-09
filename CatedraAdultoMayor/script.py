# Rellenar la base de datos con roles, menús y accesos
from CatedraAdultoMayor.models import Role, Menu, RoleAccess

# Datos para los roles
roles_data = [
    {"code": "usuario", "name": "Usuario"},
    {"code": "trabajador", "name": "Trabajador"},
    {"code": "admin", "name": "Admin"},
]

# Crear roles
for role in roles_data:
    Role.objects.create(**role)

# Datos para los menús
menus_data = [
    {"code": "apartamento", "name": "Apartamento"},
    {"code": "residencia", "name": "Residencia"},
]

# Crear menús
for menu in menus_data:
    Menu.objects.create(**menu)

# Datos para accesos por rol
role_access_data = [
    {"role": "admin", "menu": "residencia", "haveedit": True, "haveadd": True, "havedelete": True},
    {"role": "admin", "menu": "apartamento", "haveedit": True, "haveadd": True, "havedelete": True},
    {"role": "usuario", "menu": "residencia", "haveedit": False, "haveadd": False, "havedelete": False},
    {"role": "trabajador", "menu": "residencia", "haveedit": True, "haveadd": True, "havedelete": False},
    {"role": "trabajador", "menu": "apartamento", "haveedit": False, "haveadd": True, "havedelete": False},
]

# Crear accesos por rol
for access in role_access_data:
    role_instance = Role.objects.get(code=access["role"])
    menu_instance = Menu.objects.get(code=access["menu"])
    RoleAccess.objects.create(
        role=role_instance,
        menu=menu_instance,
        haveedit=access["haveedit"],
        haveadd=access["haveadd"],
        havedelete=access["havedelete"],
    )
