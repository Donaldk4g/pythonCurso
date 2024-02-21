import requests
def get_categories():
    r = requests.get('https://api.escuelajs.co/api/v1/categories')
    print(r.status_code) #respuesta de la consulta 

    print(r.text)  
    #print(type(r.text)) # los datos aqui son un string
    categoria=r.json() # convierte los datos para poderlos manipular
    print(categoria)
    print(type(categoria))
    '''
        print(type(r.text))
    categories = r.json()
    for category in categories:
        print(category['name'])
    
    '''
