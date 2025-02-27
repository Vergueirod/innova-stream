import uuid

class Category:
    def __init__(
            self,
            name,
            id = "",
            description = "",
            is_active = True,
    ):
        
            
        if len(name) >= 255:
            raise ValueError("name must have less than 256 characters")
        self.name = name
    

        self.id = id or uuid.uuid4()
        self.name = name
        self.description = description
        self.is_active = is_active

        self.validate()

    def validate(self):
        if len(self.name) >= 255:
            raise ValueError("name must have less than 256 characters")
        
        if not self.name:
             raise ValueError("name cannot be empty")

    def __str__(self):
            return f"{self.name} - {self.description} - {self.is_active}"
    def __repr__(self):
         return f"<Category {self.name} ({self.id})>"
    
    def update_category(self, name, description): 
        self.name = name
        self.description = description

        self.validate()

    def activate(self):
        self.is_active = True

        self.validate()

    def desactivate(self):
        self.is_active = False

        self.validate()