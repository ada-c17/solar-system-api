from app import db

class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    has_moon = db.Column(db.Boolean, nullable=False, default=False)

    def to_dict(self):
        return dict(
            id = self.id,
            name = self.name,
            description = self.description,
            has_moon = self.has_moon,)

    @classmethod
    def from_dict(cls, data_dict):
        return cls(name=data_dict["name"],
                        description=data_dict["description"],
                        has_moon=data_dict["has_moon"],)

    def replace_details(self, data_dict):
        self.name = data_dict["name"]
        self.description = data_dict["description"]
        self.has_moon = data_dict["has_moon"]
