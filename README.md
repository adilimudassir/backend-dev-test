# AFEX Backend Dev Test

### Your Task

1. Get this app to work
   > Installed the basic requirements and packages

2. Change the database config to use PostgreSQL
   > Added the required packages and settings to enable Django connect to PostgreSQL
3. Config settings for dev, staging and production servers
   > Changed the settings by creating a python module and splitted the settings in to the afformentioned environment based on the specific setting for each envorinment  
4. Add Two(2) security updates to the settings file
   > Removed hardcoded SECRET_KEY.

   > Added an env file to segregate the settings that changes based on environment and to avoid pushing sensitive settings to version control systems(VCS).

   > Added SECURE_SSL_REDIRECT, SESSION_COOKIE_SECURE, CSRF_COOKIE_SECURE and SECURE_BROWSER_XSS_FILTER for production environment

A Django app has been created under `/apps/` called `crm`

1. Configure this app to work with the main project
   > Fixed The BASE_DIR setting to match the actual directory traversion

   > Installed the app in the INSTALLED_APPS settings 

   > Fixed The database migration conflict by making the base model abstract

2. Two models has been created for you: "Client" and "ClientWallet": <br/>
   a. Write a CRUD option with the Client Model <br/>
      > Added Two(2) app menus: Dashboard and Clients. The Clients contains the CRUD operations.

   b. Write a PUT/POST option for the Client Wallet model (i.e ability to fund a particular client's wallet) <br/>
      > The Clients's Detail page contains a sub-section with the client wallet information. Added a link to fund the client's wallet

   c. Write/Configure API endpoints to fetch client (including their wallet balance) <br/>
      > Added two(2) endpoints: 

      > [/api/](http://18.170.225.200/api/)(for listing of the available endpoints with their appropriate verb), 
      
      > [/api/clients](http://18.170.225.200/api/clients) (for fetching the lists of clients with their appropriate wallet balance)

      > [/api/clients/{id}](http://18.170.225.200/api/clients/5) (for fetching of a particular client with their appropriate wallet balance)

   N:B You are to design an appropriate frontend for task in a & b above using <b>Django Template</b> <br/>
3. Set-up a web socket for the client wallet model
   > Added a websocket that updates the client's wallet balance in realtime whenever the balance gets updated
4. Write a background task that populates the Client model with users from this [endpoint](https://62c2c06cff594c656764970a.mockapi.io/users). This task should run every hour.
   > Added a scheduler that populates the client model with users. Figured the endpoint contains duplicate records but exceptions have been contained
5. Deploy your code to any of these cloud servers (A.W.S, Google Cloud, Azure or Heroku)
   > Deployed to AWS servers. [Link Here](http://18.170.225.200/)

\*\*\* Optional

1. Configure Docker for this project
   > Dockerized the application and configured docker-compose to run various services of the application
