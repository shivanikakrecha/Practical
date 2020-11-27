# Practical 
practical of product and category

# Please follow below link for more details. 
https://docs.google.com/document/d/1d_g-otVveDvoQJ2P1_6JAjTpPYWlYbuW2-l1eSFSvbY/edit?usp=sharing

# Steps
git clone <https link of git repo>

# Create Virtual Environment
virtualenv -p python3 <venv_name>

# Install requirements 
pip install -r requirements.txt

# Project structure

Root folder -> acqu_practical
Files:- 
- Authentication ( Provide authentication for product and category )
- Celery App ( Declare the celery settings )
  - Periodic task which executes every 24 hours and remove all deleted status products.
- Settings ( Holds celery and other settings )

App folder -> practical
Files:- 
- Permission ( Manage permission based on the users )
- Serializers ( Create serializers for apis )
- Models ( Create models )
- Tasks ( Holds celery tasks )
- Views ( API viewsets )
- Urls ( API Routings )

