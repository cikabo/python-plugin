class User:
    def __init__(self, username: str, email: str) -> None:
        self.username = username
        self.email = email
    
    def get_info(self):
        return f"Username: {self.username}, Email: {self.email}"
    
    def set_email(self, new_email: str) -> None:
        self.email = new_email