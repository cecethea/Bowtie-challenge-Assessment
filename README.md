


Backend take home assessment 

# necktie

### Table of Contents
- [Quickstart](#quickstart)
  * [Clone the project](#clone-the-project)
  * [Create a virtual environment](#create-a-virtual-environment)
  * [Install all requirements](#install-all-requirements)
  * [Configure the database](#configure-the-database)
  * [Test the installation](#test-the-installation)
  * [Test your changes](#test-your-changes)

---

## Quickstart

We're going to install and configure the latest develop build of this API.

### Clone the project

First of all, you need to clone the project on your computer with :

```
git clone https://github.com/cecethea/Martin_Cece_Thea_Backend_engineer_Technical_Assessment
```

You can now move in the newly created folder:

```
cd necktie
```

### Create a virtual environment

[Virtualenv](https://virtualenv.pypa.io/) provides an isolated Python environment, which are more practical than installing packages system-wide. They also allow packages to be installed without administrator privileges.

1. Create a new virtual environment
```
virtualenv env
```

2. Activate the virtual environment
```
. env/bin/activate
```

You need to ensure the virtual environment is active each time you want to launch the project.

### Install all requirements

Requirements of the project are stored in the `requirements.txt` file.
You can install them with:

**WARNING** : Make sure your virtual environment is active or you will install the packages system-wide.
```
pip install -r requirements.txt
```

The `requirements-dev.txt` file contains packages that are only needed during
development. You should execute the previous command with this file too, unless
you are deploying in production.

### Configure the database

Django has a system of database migration. You first need to apply all existing "migrations" to update your local database.

```
python manage.py migrate
```

**Note:** The project uses a squlite3 file as database to simplify developement.
Once in production, feel free to switch to whatever suits you.

### Launch the API

You can now launch an instance of the API and visit the built-in admin website.

To login into the admin page, you'll need to create a superuser first:
```
python manage.py createsuperuser
```
Launch a local API instance with:
```
python manage.py runserver
```

You can now visit these links to validate the installation:

- The root of the API: [http://localhost:8000/](http://localhost:8000/),

use the following credential to access the admin site:
```
username: test

password: Test1234@
```
- The admin site: [http://localhost:8000/admin/](http://localhost:8000/admin),

### Test 

You can run the tests with:

```
python manage.py test
```
