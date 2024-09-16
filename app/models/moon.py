from app import db

class Moon(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)
    planet_id = db.Column(db.Integer, db.ForeignKey('planet.id'))
    planet = db.relationship("Planet", back_populates="planet_moons")

    def to_json(self):
        return {
            "id": self.id,
            "name": self.name,
        }

    def update(self, request_body):
        self.name = request_body["name"]
        self.planet_id = request_body["planet_id"]

    @classmethod
    def create(cls, request_body):
        return cls(
            name=request_body["name"],
            planet_id=request_body["planet_id"],
        )
