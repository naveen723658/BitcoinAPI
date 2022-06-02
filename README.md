# BitcoinAPI
It is a API based program for fetching the price of Bitcoin in real time and every time the price of bitcoin is fetched it is stored in a database table and you can get the list of Bitcoin prices with timestamps with pagination, of 10 items per page by an API.

![image](https://user-images.githubusercontent.com/106751177/171660893-09660e35-eabd-44bb-9ede-f0c9058e8a3d.png)



#####################################################

# Getting  Bitcoin Prices using Python Django
A Django project which uses requests package to hit api and get the Bitcoin prices and save it to database and display the prices with timestamp in json farmat

hit this url to get the Bitcoin Prices
<your_localhost>/bitcoinfatch/

for getting the list of bitcoin prices first you need to login

![image](https://user-images.githubusercontent.com/106751177/171661285-3eb2fee3-308f-482e-a925-da33ea2dc170.png)

after that use this url to get the json file for bitcoin prices
<your_localhost>/bitcoin/?format=json&page=N

where N is 1,2,3...

for logout use 
<your_localhost>/logout/

###############################################

# How to deploy on your local machine

- clone the repo.
- create a virtual environment. Activate it
- Install the dependecies from req.txt file using `pip install -r req.txt` command
- go to project directory where manage.py file 

- you need to run migration first
-`python manage.py makemigration`

-`python manage.py migrate` 
 
- run using python manage.py runserver
 
- Start the server. Go to <localhost>

###################################################
  
