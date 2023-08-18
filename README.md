This is an experiment to utilize [Flask](https://flask.palletsprojects.com/), [Flask JWT Extended](https://flask-jwt-extended.readthedocs.io/en/stable/), and [python-pam](https://pypi.org/project/python-pam/) to provide an light weight user authentication system. From time to time when building very simple web apps, especially those which would otherwise require no database, that the wall I run into is authentication. I got the idea to try directly using linux users and found python-pam to make that work. Obviously one should consider the security implications of this decision (can or should these accounts be able to log in?)

<br>

clone repository
```
git clone https://github.com/vicgarcia/flask-auth-experiment.git
cd flask-rest-experiment
```

build the docker container
```
docker build -t flask-auth-experiment .
```

run the docker container
```
docker run --rm --name flask-auth-experiment -p 3000:3000 flask-auth-experiment
```

import `insomnia.yaml` and interact with the apis via [Insomnia](https://insomnia.rest/)
