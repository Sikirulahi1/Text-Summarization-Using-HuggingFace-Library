class UserModel:
    def __init__(self, text):
        self.text = text

    def __repr__(self):
        return f'UserModel(name={self.text})'
