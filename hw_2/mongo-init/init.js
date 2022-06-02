conn = new Mongo();
db = conn.getDB("otus-hw");

db.movies.createIndex({ "year": 1 }, { unique: false });

db.movies.insert({"_id":1,"title":"RuPaul Is: Starbooty!","year":1987,"cast":[""],"genres":["Comedy"]});
db.movies.insert({"_id":2,"title":"The Running Man","year":1987,"cast":["Arnold Schwarzenegger","Richard Dawson","María Conchita Alonso"],"genres":["Science Fiction"]});
db.movies.insert({"_id":3,"title":"Russkies","year":1987,"cast":["Joaquin Phoenix","Peter Billingsley"],"genres":["Comedy"]});
db.movies.insert({"_id":4,"title":"Salvation!","year":1987,"cast":["Viggo Mortensen","Exene Cervenka"],"genres":["Comedy"]});
db.movies.insert({"_id":5,"title":"September","year":1987,"cast":["Mia Farrow","Sam Waterston","Dianne Wiest","Elaine Stritch"],"genres":["Drama"]});
db.movies.insert({"_id":6,"title":"K-9","year":1989,"cast":["James Belushi","Mel Harris"],"genres":["Comedy"]});
db.movies.insert({"_id":7,"title":"Kamillions","year":1989,"cast":[],"genres":["Drama"]});
db.movies.insert({"_id":8,"title":"The Karate Kid, Part III","year":1989,"cast":["Ralph Macchio","Pat Morita","Thomas Ian Griffith"],"genres":["Action"]});
db.movies.insert({"_id":9,"title":"Kickboxer","year":1989,"cast":["Jean-Claude Van Damme"],"genres":["Action"]});
db.movies.insert({"_id":10,"title":"Son in Law","year":1993,"cast":["Pauly Shore","Carla Gugino","Lane Smith"],"genres":["Comedy"]});