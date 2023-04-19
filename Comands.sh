# Comands for install dependencies the project

# Create virtualenv
python -m virtualenv env

# Activate virtualenv
source env\bin\activate

# Deactivate virtualenv
deactivate


# ----------------------------------------------------------------------
# Install dependencies
pip install -r requirements.txt
# or pip install -r requirements.sh



# Create dependencies the project
pip freeze > requirements.txt
# or pip freeze > requirements.sh