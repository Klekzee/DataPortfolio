# End-to-End Data Portfolio 02
This also serve as my personal notes on working with Git and Github.

## Instructions
Clone this repository.

`git clone SSH` # Copy SSH key from GitHub

Create a virtual environment.

`python -m venv env_name` # Best practice for name is `env`

Install the packages.

`pip install -r requirements.txt` # Best practice for filename is `requirements.txt`

## Commonly used Git commands
* `git init .` # dot for current directory
* `git add .` # dot for all changes
* `git commit -m "This is my commit message"`
* `git rm file_name.txt`
* `git push`
* `git pull`
* `git clone`

## Connecting Git with GitHub
* `git remote add origin SSH_link` # SSH_link can be copied from GitHub
* `git branch -M main`
* `git push -u origin main`