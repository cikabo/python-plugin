
# from users import User as OriginalUser

class User:
    def __init__(self, original_user) -> None:
        self.original = original_user
        pass

    def get_info(*args, **kwargs):
        # self.username = original_user.username
        # self.email = original_user.email
        self = args[0]
        original = args[1]        
        print(f"PLUGIN 2 call to get_info for user {original.username}")
        return f"PLUGIN 2 Username: {self.original.username}, Email: {self.original.email}"
    
    def set_email(*args, **kwargs) -> None:
        self = args[0]
        original = args[1]
        new_email = args[2]
        print(f"PLUGIN 2 call to set_email for user {self.original.username} to {new_email}")
        original.email =  f" {new_email} (modified by plugin 2)"