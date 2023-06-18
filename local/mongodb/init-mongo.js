print('Collecting credentials...');

//var credentials_ff_interface = require('./../../credentials/ff_interface.json');
var credentials = {
    "driver": "pymssql",
    "server": "MSSQL01",
    "database": "movies-api-db",
    "user": "burrito",
    "password": "admin",
    "port": "27017"
}

print('Credentials collected.');

print('Creating databases....');
db = db.getSiblingDB('movies-api-db');
db.createUser({user: credentials.user, pwd: credentials.password, roles: [{role: "readWrite", db: "movies-api-db" }]});
db.createCollection('movies');
db.createCollection('cinemas');
db.createCollection('users');

// Import movies.json and add to collection
var file = cat('/docker-entrypoint-initdb.d/movies.json');
var o = JSON.parse(file);
db.movies.insert(o);


print('Databases created.')
