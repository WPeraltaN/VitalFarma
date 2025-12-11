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