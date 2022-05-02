from app import db

class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    description = db.Column(db.String)
    has_moon = db.Column(db.Boolean, default=False)

    def to_dict(self):
        return dict(
            id = self.id,
            name = self.name,
            description = self.description,
            has_moon = self.has_moon,
        )
    
    @classmethod
    def validate_fields(cls):
        pass