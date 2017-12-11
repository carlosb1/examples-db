 docker run -d -p 27017:27017 -p 28017:28017 tutum/mongodb

sudo docker logs <containerid>

sudo mongo admin -u admin -p <passfromlog> 

use admin
db.createUser(
  {
    user: "testadmin",
    pwd: "password",
    roles: [ { role: "root", db: "admin" } ]
  }
);
exit; 
