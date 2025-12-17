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
            {'name':'Dashboard', 'url':'dashboard'},
            {'name':'Productos', 'url':'productos'},
            {'name':'Categorías', 'url':'categorias'},
        ]
    }
