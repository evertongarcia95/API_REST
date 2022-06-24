from flask_restplus import fields
from server.instance import server

api = server.api



not_found = api.model('NotFoundErrorResponse', {
"message": fields.String(example="Sorry, your application was not identified or not found")
})

invalid_syntax = api.model('InvalidSyntaxErrorResponse', {
"message": fields.String(example="Syntax or mandatory field not added, try again!")
})

internal_server_error = api.model('InternalServerErrorResponse', {
"message": fields.String(example="The server has encountered a situation it doesn't know how to handle.")
})

duplicate_error = api.model('DuplicateErrorResponse', {
"message": fields.String(example="Data already exists.")
})
