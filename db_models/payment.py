from repository.database import db

class Payment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.Float)
    paid = db.Column(db.Boolean, default=False)
    bank_payment_id = db.Column(db.String(200), nullable=True)
    qr_code = db.Column(db.String(100), nullable=True)
    expiration_data = db.Column(db.DateTime)

    def to_dict(self):
        return {
            "id" : self.id,
            "value" : self.value,
            "paid" : self.paid,
            "qr_code" : self.qr_code,
            "bank_payment_id" : self.bank_payment_id,
            "expiration_data" : self.expiration_data,
        }