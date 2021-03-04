class BadRequest(Exception):
    def __init__(self, description,location,type_,status=400):
        self.type_ = type_
        self.location = location
        self.description = description
        self.status = status



 
     
