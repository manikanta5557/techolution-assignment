import json
# The Storage class in our code could be considered an example of the Singleton pattern 
# we ensure that only one instance of this class handles the file storage throughout the application. 
class SingletonType(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]
    
class Storage(metaclass=SingletonType):
    def __init__(self, filename):
        self.filename = filename

    def read_data(self):
        try:
            with open(self.filename, 'r') as file:
                data = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            data = {'books': {}, 'users': {}, 'checkout': {}}
        return data

    def write_data(self, data):
        with open(self.filename, 'w') as file:
            json.dump(data, file, indent=4)

    def add_book(self, book):
        data = self.read_data()
        data['books'][book.isbn] = book.__dict__
        self.write_data(data)

    def add_user(self, user):
        data = self.read_data()
        data['users'][user.user_id] = user.__dict__
        self.write_data(data)

    def list_books(self):
        data = self.read_data()
        return data.get('books', {})

    def list_users(self):
        data = self.read_data()
        return data.get('users', {})
