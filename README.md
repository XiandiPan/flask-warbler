# Warbler

Warbler is a Twitter-like application where you can implement login, logout, follow a user, and be followed by other users.

### Description :notebook:

Warbler is our first project at Rithm, and it has been an incredible opportunity for my partner and me to enhance our programming skills. We worked with a slightly larger codebase during its development, which was a new and valuable experience for us. Embracing this challenge has helped us expand our abilities, adapt to new situations, and develop our overall skillset.

### Tech Stack :school:

Javascript | Python | Flask | SQLAlchemy | Jinja

### Features (Added by us)

- Implement user authentication and authorization.
- Enable authenticated users to edit and update their profiles.
- Allow users to follow and unfollow other users.
- Implement the ability for users to like and unlike posts.
- Enhance security by implementing password hashing with bcrypt.
- Write comprehensive tests to ensure functionality and reliability.

### Install & Run :runner:

1. Create a virtual environment and install requirements:
```
$ python3 -m venv venv
$ source venv/bin/activate
$ pip3 install -r requirements.txt
```
2. Add a .env file with:
   ```
   SECRET_KEY=(any secret key you want)
   DATABASE_URL=postgresql:///warbler
   ```
3. set up the database (PostgreSQL)
```
$ psql
=# CREATE DATABASE warbler;
(ctrl+D)
$ python3 seed.py
```
4. Start the server
   ```
   $ flask run -p 5001
   ```
5. open a browser tab and paste in the URL "http://localhost:5001"
   

TO-DO's :pencil2:

- Additional testing








 
