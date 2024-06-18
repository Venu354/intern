from flask_restful import Resource, reqparse
from app import api, db
from models import Client, Domain

class ClientResource(Resource):
    def get(self, client_id):
        client = Client.query.get_or_404(client_id)
        return {
            'name': client.name,
            'email': client.email,
            'phone': client.phone,
            'address': client.address
        }

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name', required=True)
        parser.add_argument('email', required=True)
        parser.add_argument('phone')
        parser.add_argument('address')
        args = parser.parse_args()

        new_client = Client(
            name=args['name'],
            email=args['email'],
            phone=args['phone'],
            address=args['address']
        )
        db.session.add(new_client)
        db.session.commit()
        return {'message': 'Client created successfully'}, 201

class DomainResource(Resource):
    def get(self, domain_id):
        domain = Domain.query.get_or_404(domain_id)
        return {
            'domain_name': domain.domain_name,
            'expiry_date': domain.expiry_date.isoformat()
        }

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('client_id', required=True)
        parser.add_argument('domain_name', required=True)
        parser.add_argument('expiry_date', required=True)
        args = parser.parse_args()

        new_domain = Domain(
            client_id=args['client_id'],
            domain_name=args['domain_name'],
            expiry_date=args['expiry_date']
        )
        db.session.add(new_domain)
        db.session.commit()
        return {'message': 'Domain created successfully'}, 201

api.add_resource(ClientResource, '/clients', '/clients/<int:client_id>')
api.add_resource(DomainResource, '/domains', '/domains/<int:domain_id>')

