# FriendsDiscovery

<img src="static/images/responsive.png">

FriendsDiscovery is a website that allows users to create blog posts, build new friendships, and chat with others.

[*Am I Responsive?*](http://ami.responsivedesign.is/#) was used to test how responsive the website is on different devices.
## Table of Contents

---

1. [UX](#ux)
   - [Strategy Plane](#strategy-plane)
        - [User Stories](#user-stories)
   - [Scope Plane](#scope-plane)
        - [Viability](#project-viability) 
        - [Typography](#typography)
   - [Structure Plane](#structure-plane)          
   - [ Skeleton Plane](#skeleton-plane)
        - [Wireframes](#wireframes)
   - [Surface Plane](#surface-plane)
        - [Colors](#colors)
        - [icons](#icons)
   - [InformationArchitecture](#information-architecture)
        - [Data Structure and Schema](#data-structure-and-schema) 
2. [Features](#features)
   - [Existing Features](#existing-features)
   - [Features left to implement](#features-left-to-implement)
3. [Technologies Used](#technologies-used)
   - [Front End Technologies](#front-end-technology)
   - [Frameworks](#frameworks-used)
4. [Testing](#testing)
   - [Validators](#validators)
   - [Testing Methods](#testing-methods)
5. [Deployment](#deployment)
   - [Local Deployment](#local-deployment)
   - [Remote Deployment](#remote-deployment)
6. [Credits](#credits)
   - [Content](#content)
   - [Media](#media)
   - [Acknowledgements](#acknowledgements)

---

## UX

### Design Process

--- 

### Strategy Plane

#### *Developer Stories*

 - As the developer, I want to create a website so users can share aspects of their lives with others. 

 - As the developer, I want the website to be aesthetically pleasing to those who visit the website making good use of HTML, CSS and Bootstrap. 

 - As the developer, I want the website to function in the intended ways using Javascript/JQuery and Python.

 - As the developer, I want everything shared to be stored in a back end data network, in this case I will be using SQLite3, with AWS for static files. 

#### *Site Owner Stories*

- As the site owner, I want users to have a positive experience so that the number of users grows continually. 

- As the site owner, I want to have premium options to encourage some users to pay for an extra service. 

#### *User Stories*

This is created so users can share music they have arranged or composed, sharing the audio and the sheet music.

- As a user, I want to be able to share stories and anecdotes with friends.

- As a user, I want to be able to add new friends and communicate with them

- As a user, I want to have a way to reward other users I find interesting

- As a user, I want to share information about myself so other users know more about me

- As a user, I want to be able to share an image of myself, or of something that I enjoy and want others to see. 

- As a user, I want to see an attractive website that makes me want to use it. 

- As a user, I want to see other users profile pages, and see what they have shared

- As a user, I want to be able to hide people I don't want to see. 

### Scope Plane

After deciding on the main aims of the project, I considered the features that were realistic in the time frame of the project. I used the user stories to come up with a list of features, their importance and their viability. Anything less viable will be considered as more likely being added as a future feature (will be viewable in the features section).

#### *Project Viability*

|     | Feature                          | Importance | Viability |
| --- | ---------------------------------| :--------: | --------: |
| A   | Blog Posts                       |     5      |         5 |
| B   | Give heart to user               |     5      |         5 |
| C   | Search users                     |     5      |         5 |
| D   | Premium service                  |     5      |         5 |
| E   | Profile page and updatable info  |     4      |         4 |
| F   | Add Friends                      |     4      |         4 |
| E   | Block Users                      |     4      |         4 |
| F   | Messaging service                |     3      |         2 |
|     | ---------------------------------|            |           |
|     | Total                            |     35     |       34  |

### Structure Plane

The following is how the website will be structured, based on the scope of the project:

-On the Navbar the left side Navbar is for user information, such as user profile and login. The second Navbar is for navigating around the website. 

- The Navbar will have a login/register on the account details tab if user isnt logged in to the site. 
    - login/register sends user to a login page, with option to register underneath the login form. 
    - If a new user registers, after completion it will return to the login and ask the user to login for the first time

- If the user is logged in the Navbar will say the profile page and logout. 
    - In the profile page, users can view their details and change their details. 
    - They can see their blog posts and add a new blog post. 
- the right side of the navbar will also have the membership details. 
    - Membership allows a user to purchase a subscription either every month, or every year. 
    - Membership allows a user to cancel their auto renewel if already subscribed or restart the resubscription option. 
- In the middle of the navbar is Friends and Profiles.
    - In  Friends, users will see all their friend requests (received and sent) with the option to cancel a request or accept a request. 
    - In friends, users have a list of all the friends on their friend list. 
    - In profiles, users can see all the users (3 at a time) 
    - Premium users have the option to search through all users.


### Skeleton Plane

#### *Wireframes*

Click here to see the project [Wireframes](wireframes.md) (added to seperate file due to size)

The project mostly follows the wireframe, however, there is a variation from the wireframe. There is no longer a messenging service, as the deadline is no longer allowing it. This will be a future feature that will be added shortly after. 

I also changed the nav bar so the links were all together, as profile and friends looked out of place by themselves. Once Messages have been added, they will all go to the middle.

### Surface Plane

#### *Typography*
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
The font Roboto was used as it is a sans type font. Sans are useful for simplcity and for a modern look.  

1 [Google Font](https://fonts.google.com/) was used throughout this website:
- ["Josefin+Sans";](https://fonts.google.com/specimen/Josefin+Sans)

#### *Colors*

#### *Foundation colours*
These were used as the main colours. A simple calming effect is what I wanted the site to give. 

- "white": "white"
- "black": "black"
- "dark blue (Main)": rgb(43, 96, 156)
- "light blue (Accents)": rgb(88, 129, 175)

#### *Accent colours* 


<img src="dark-blue">

<img src="light-blue">


  

#### *Icons*

[Font Awesome 5.13.1](https://fontawesome.com/)

Font awesome icons have been used throughout. There is on attached to every link in the navbar, and there are user + or user - icons for accepting requests or cancelling friend requests. 
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

#### *Image modifications*

- [GIMP](https://www.gimp.org/) was used to remove the white from the heart image to make it transparent background. 
Permissions for editing image ok as a stock image.  

### Information Architecture

#### *Data Structure and Schema*

I used SQLITE to store the data that the website uses.  



##### Back to [top](#table-of-contents)
---

### Features

---

#### Existing Features

- Friend Requests

  - Able to send a friend request from other users profile pages. 
  - Able to reject friend requests
  - Able to Accept Friend requests
  - Able to remove friends
  - Able to view blogs of all friends

- Subscription Options 

  - Able to sign up for a premium subscription
  - Able to Send extra hearts per day to other users
  - Able to remove friend requests
  - Will be able to send messages to users. Non subscribed will be able to reply.

- Share blog posts

   - Write a blog post
   - Delete a blog post
   - Update a blog post
    

- Profile Page

  - Share Profile details
  - The users can edit their profile details by clicking the buttons on their own profile. 
  - The users blog posts are all available on their own profiles when viewing as another user

- Edit profile Page

  -  Change profile picture 
  -  Change about me information
  -  Update changes button updates all information changed in the form

-  Sign up
  - Users signup and have to accept via email
  - Users can then log in when authenticated

#### Features to Implement

-  Messaging Service
  - Users will be able to send messages to one another
  - Users will be able to have a list of all their current messages
  - Users will receive an email if they have had a message waiting for one week
  - Users can delete messages from both sides

I was not able to fulfill this as I ran out of time. I intend to add it later on. 

##### Back to [top](#table-of-contents)

---

## Technologies Used

---

- HTML

  - This project uses HTML to create the main functions of the website.
  - [HTML](https://en.wikipedia.org/wiki/HTML)

- CSS

  - This project uses CSS to add styling to features. It is also used to tweak some of the bootstrap. (Sass is also used to achieve this.)
  - [CSS](https://en.wikipedia.org/wiki/CSS)

- Python

  - This project uses Python for the main database related features. I build models, views, urls and forms to build objects which the front end can react and respond to.
  - [Python](https://en.wikipedia.org/wiki/Python_(programming_language))


- Javascript

  - This project uses Javascript to create functions, rules and effects in order to make the certain features work. I used this mostly to get stripe to work as a subscription service. 
  - [Javascript](https://en.wikipedia.org/wiki/JavaScript)

#### Frameworks and Libraries Used

- Bootstrap
    - Bootstrap is an open source library with access to reusable bits of code for html, css and javascript.
    - [Bootstrap](https://getbootstrap.com/) 

- jQuery
    - jQuery is an open source library that makes using javascript easier and quicker. It simplifies a variety of multiple lines of javascript code by putting it into a single line of jquery code. 
    - [jQuery](https://jquery.com/)

- Django
    - is a Python-based free and open-source web framework that follows the model–template–views (MTV) architectural pattern.
    - [Django](https://www.djangoproject.com/)

- Allauth
   - Integrated set of Django applications addressing authentication, registration, account management as well as 3rd party (social) accounts
   - [Allauth](https://django-allauth.readthedocs.io/en/latest/)

- Stripe
    - Stripe is a payment processing platform
    - [Stripe](https://stripe.com/docs)

- Friendship
    - A library built by developers to allow simple implementation of Friend Social requests
    - [Friendship](https://pypi.org/project/django-friendship/)
 
##### Back to [top](#table-of-contents)

---

## Testing

---

### Self testing during development 

- Error: After changing user details, photos weren't showing up next to users. 
- Expected: Photos should have been next to the users name
- Fix: the term user details had changed to the name that was given to the model, and userprofile was required instead. 

- Error: Friend Remove wasn't working as it couldnt remove two users.
- Expected: Able to remove the relationship between two users. 
- Fix: Found the Friendship github had been updated, but the pip didn't include the new code in the template, so in the created views, I added the new files to it manually.

- Error: Couldnt push to Heroku.
- Expected: After adding AWS, site would use the static files
- Needed to permanenetly delete the static files from AWS, then deploy again on Heroku. 

### Testing after deployment

- Error: if statements not working on others profile
- Expected: if a user was a friend, theyd be able to give a heart to their friend. Rules dependent on subcription too. 
- Fix: the if statement had moved over onto two lines, meaning it couldn't be read. 

- Error: Users couldn't send a certain user a friend request if another user had sent that person a request already.
- Expected: To be able to send friend requests to every other user at the same time as another user
- Fix: Added a for loop to the request_sent value which checks if the current user is in the list of friend requests relating to the profile page user. 

### Validators

- HTML

  - [W3C HTML Validator](https://validator.w3.org/) 
    
    - Used the deployed website address.. 
    - Document checking completed. No errors to show.

- CSS

  - [W3C CSS Validator](https://jigsaw.w3.org/css-validator/) 
  
  - "Congratulations! No Error Found. This document validates as CSS level 3 + SVG !"

- Javascript

  - [JSHint javascript Validator](https://jshint.com/) There are no critical errors, but there are warnings for $ used in jquery.
    It also said there were unused variables, but its due to them being on-clicks.

- Python
  - [PEP8 online](http://pep8online.com/) "All right"
    No errors found.

### Testing Methods

For information on the testing, follow the link to the document [here](testing.md)

##### Back to [top](#table-of-contents)
---

## Deployment

---

### Remote Deployment

heroku was used for the live deployment of this project, through the master branch of my github repository. The following steps were implemented to deploy this project:

Install gunicorn package to run the application on Heroku.
sudo pip3 install gunicorn
Install pycopg2 to connect to PostgreSQL
sudo pip3 install psycopg2
Create a requirements.txt file
sudo pip3 freeze --local > requirements.txt
Create a new Heroku application
Sign up to a new account if you do not already have one.
Create a new application by clicking on new then create new app.
Set the name of your application and select your region and click on create app to finalize the creation of your app.
Install PostgreSQL add-on
heroku addons:create heroku-postgresql:hobby-dev
Create a Procfile in the root directory
content: web: gunicorn spacex.wsgi:application
Set the following config variables as environment variables:

Config Vars	Value
AWS_ACCESS_KEY_ID	<AWS_ACCESS_KEY_ID>
AWS_SECRET_ACCESS_KEY	<AWS_SECRET_ACCESS_KEY>
DATABASE_URL	<DATABASE_URL>
SECRET_KEY	<SECRET_KEY>
STRIPE_PUBLISHABLE_KEY	<STRIPE_PUBLISHABLE_KEY>
STRIPE_SECRET_KEY	<STRIPE_SECRET_KEY>
STRIPE_WH_SECRET	<STRIPE_WH_SECRET>
EMAIL HOST USER <EMAIL_HOST_USER>
EMAIL HOST PASS <EMAIL_HOST_PASS>
USE_AWS	<TRUE>
DEVELOPMENT <FALSE>

In the Deploy tab, choose Connect Github as Deployment Method and I had to make sure I had disabled Automatic Deployment from the Github master branch as my AWS rights interfered with it, so I had to delete my static files on every re deployment. However this ensured it worked correctly after deletion and was the only way around the bug I was able to find. 


### Local Deployment

To run the project locally. Install:

Git
Django
After installing these you need to:

Download this repository clicking in ‘Clone or Dowload’ on top of this page, then click on ‘Download ZIP’ and extract the files in the folder you will be working on.
Open the folder where you download the repository in your code editor
Create a .env file containing the following credentials:

Env Vars	Value
AWS_ACCESS_KEY_ID	<AWS_ACCESS_KEY_ID>
AWS_SECRET_ACCESS_KEY	<AWS_SECRET_ACCESS_KEY>
DATABASE_URL	<DATABASE_URL>
SECRET_KEY	<SECRET_KEY>
STRIPE_PUBLIC_KEY	<STRIPE_PUBLIC_KEY>
STRIPE_SECRET_KEY	<STRIPE_SECRET_KEY>
STRIPE_WH_SECRET	<STRIPE_WH_SECRET>
USE_AWS	<TRUE>

Install the required modules using this command: pip -r requirements.txt
You can run the app by running: python manage.py runserver The project will run at http://127.0.0.1:8000


##### Back to [top](#table-of-contents)
---

## Credits

---

### Content

- All written content was my own.
- [Unsplash]() - Main home image
- 

### Media

- 

### Acknowledgements

- I'd like to thank the slack community for their support, particularly the May 2020 cohort group who have given me support and suggestions.
- I'd also like to thank my friends and family for their support, and their support with testing of the website. 

##### Back to [top](#table-of-contents)
