# users = []

# def add_user(name, user_id):
#     users.append({"name": name, "user_id": user_id})
import logging
logging.basicConfig(filename='library_management.log', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
class User:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name

    def __str__(self):
        return f"User ID: {self.user_id}, Name: {self.name}"
class UserManager:
    def __init__(self, storage):
        self.storage = storage

    def add_user(self, user):
        """Add a new user to the storage only if they do not already exist."""
        users = self.storage.list_users()
        if user.user_id in users:
            # Log attempt to add a duplicate user
            logging.error(f"Attempted to add duplicate user with ID: {user.user_id}")
            print(f"User with user ID {user.user_id} already exists.")
            return
        self.storage.add_user(user)
        logging.info(f"Added user: {user}")
    def update_user(self, user_id, new_user):
        """Update an existing user's details."""
        data = self.storage.read_data()
        if user_id in data['users']:
            data['users'][user_id] = new_user.__dict__
            self.storage.write_data(data)
            logging.info(f"User data is updated with user_id : {user_id}")
            
        else:
            print("User with the given user ID does not exist.")
            logging.error("User data failed to update.")
    def remove_user(self, user_id):
        """Remove a user from storage."""
        data = self.storage.read_data()
        if user_id in data['users']:
            del data['users'][user_id]
            self.storage.write_data(data)
            logging.info(f"User removed with user_id : {user_id}")
        else:
            print("User with the given user ID does not exist.")
            logging.error("Failed to remove user.")
    def list_users(self):
        """List all users."""
        return self.storage.list_users()

    def search_users(self, search_term, search_by='name'):
        """Search users by a given attribute (name, user_id)."""
        valid_search_terms = ['name', 'user_id']
        if search_by not in valid_search_terms:
            print("Invalid search type provided. Valid options are: name, user_id.")
        result = {}
        users = self.storage.list_users()
        for user_id, user in users.items():
            if search_term.lower() in user.get(search_by, '').lower():
                result[user_id] = user
        if len(result) == 0:
            print("No user found with given value.")
        return result
