from djangoapp.models import MyModel


def populate_data():
    data = {
        'name': 'John Doe',
        'age': 30,
        'email': 'john@example.com',
        'address': '1234 Main St',
        'city': 'Metropolis',
        'state': 'CA',
        'zip_code': '90210',
        'phone': '555-1234',
        'country': 'USA'
    }

    # Crear instancia del modelo
    instance = MyModel(
        name=data['name'],
        age=data['age'],
        email=data['email'],
        address=data['address'],
        city=data['city'],
        state=data['state'],
        zip_code=data['zip_code'],
        phone=data['phone'],
        country=data['country']
    )

    instance.save()
