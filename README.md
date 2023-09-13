### MLH Production Engineering Fellowship (Meta)
This is the repository for my summer 2023 project. This project gave me the opportunity to polish and gain new skills needed to become better at Production/Site Reliability Engineering.

## Features of the project
- Integration of CI/CD using Github Actions to automate repetive tasks.
- Jinja templating engine for dynamic HTML rendering.
- Bootstrap for responsive design.
- Nginx reverse proxy integration for ssl certificate.
- Containerization using Docker to make project more lightweight.
- Database integration with Mariadb.
- HTTP POST and GET method integration for posting and viewing timeline posts.

  

## Installation

Make sure you have python3 and pip installed

Create and activate virtual environment using virtualenv
```bash
$ python -m venv python3-virtualenv
$ source python3-virtualenv/bin/activate
```

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install all dependencies!

```bash
pip install -r requirements.txt
```

## Usage

Create a .env file using the example.env template (make a copy using the variables inside of the template)

Start flask development server
```bash
$ export FLASK_ENV=development
$ flask run
```

You should get a response like this in the terminal:
```
❯ flask run
 * Environment: development
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

You'll now be able to access the website at `localhost:5000` or `127.0.0.1:5000` in the browser! 

*Note: The portfolio site will only work on your local machine while you have it running inside of your terminal. We'll go through how to host it in the cloud in the next few weeks!* 

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.
