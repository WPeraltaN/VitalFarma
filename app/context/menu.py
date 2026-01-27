def menu_principal(req):
    return{
        'menu':[
            {'name':'Inicio', 'url':'inicio'},
            {'name':'Productos', 'url':'productos'},
            {'name':'Contacto', 'url':'contacto'},
            
            # {'name':'Carrito', 'url':'carrito'},
            
            {'name':'Login', 'url':'login'},
            {'name':'Register', 'url':'register'},
        ]
    }

def menu_empleados(req):
    return{
        'menu2':[
            {'name':'Dashboard', 'url':'dashboard', 'img':'assets/icon/empleado/aside/dashboard.svg'},
            {'name':'Pedidos', 'url':'pedidos', 'img':'assets/icon/empleado/aside/pedidos.svg'},
            {'name':'Inventario', 'url':'inventario', 'img':'assets/icon/empleado/aside/inventario.svg'},
            {'name':'Clientes', 'url':'clientes', 'img':'assets/icon/empleado/aside/clientes.svg'},
            {'name':'Empleados', 'url':'empleados', 'img':'assets/icon/empleado/aside/pedidos.svg'},
        ]
    }
