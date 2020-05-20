ADMIN_PERMISOS = [
    'students_index',
    'students_new',
    'students_destroy',
    'students_update',
    'students_show',
    'user_index',
    'user_new',
    'user_destroy',
    'user_update',
    'user_show',
    'teachers_index',
    'teachers_new',
    'teachers_destroy',
    'teachers_update',
    'teachers_show',
    'configurations_index',
    'configurations_new',
    'configurations_destroy',
    'configurations_update',
    'configurations_show',
    'administration_index',
    'administration_new',
    'administration_destroy',
    'administration_update',
    'administration_show',
]

DOCENTE_PERMISOS = [
    'students_index',
    'students_update',
    'students_show',
    'teachers_index',
    'teachers_show',
    'administration_index',
    'administration_show',
]

PRECEPTOR_PERMISOS = [
    'students_index',
    'students_update',
    'students_show',
]

ROLES = {
    'administrador': False,
    'docente': False,
    'preceptor': False,
}
