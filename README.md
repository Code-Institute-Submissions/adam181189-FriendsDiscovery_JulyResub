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

### Surface Plane

#### *Typography*
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
The font Arvo was used as it is a serif font. Serif fonts are known for their roman types. 
[As music is associated with latin](https://www.fonts.com/content/learning/fontology/level-1/type-anatomy/type-classifications) (as shown with terminology for dynamics), a serif font was appropriate for this project.

1 [Google Font](https://fonts.google.com/) was used throughout this website:
- ["Arvo", serif;](https://fonts.google.com/specimen/Arvo)

#### *Colors*

#### *Foundation colours*
These were used as the main colours. A more monochromic approach 

- "white": "white"
- "black": "black"
- "gray": #707070,
- "gray-dark": #3f3f3f,

#### *Accent colours* 
The red was chosen from a colour picker on the rose itself on the home page image.
The other colours were chosen to compliment the selected red colour. According to this [website](https://www.canva.com/colors/color-wheel/), they are either tetradic or analogous.

 Main accent colour

images created from [here](https://coolors.co/)

<img src="static/images/darkSienna.png">

Tetradic - Chosen for boldness but to compliment the red as the primary colour. Red is used for anything larger, with the smaller buttons having the tetradic colours.

<img src="static/images/tetradic.png"> 



   #421319   433D14   14433D   141A43

#### *Icons*

[Font Awesome 5.13.1](https://fontawesome.com/)

Used for the play and stop button on the music player
Used an icon for each item in the navbar to relate to each word. 
Used icons throughout the entire website for buttons 
Used a search icon to decorate the search music word on music.
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

#### *Image modifications*

- [GIMP](https://www.gimp.org/) was used to tweak the main page image so the top was plain black so title could be added without conflicting with the words on the piano. 
Permissions for editing image ok as a stock image.  

### Information Architecture

#### *Data Structure and Schema*

I used SQLITE to store the data that the website uses. I used the [documentation](https://docs.mongodb.com/manual/) in order to support me with the python coding. 

I have cluster set up called mnCluster and inside that cluster I have a group of collections

These two are created when I the python was set up in order to send music/images/pdfs to mongoDB and they are stored within fs.files. This used the mongo.save_File code.
- fs.chunks
- fs.files

The rest I created for the databases themselves
- genres
- instruments
- music
- reviews
- users

This is a schema ([created with this software](https://dbschema.com/download.html)) to explain how the data responds to each other. 

oid = objectId 

<img src="static/images/mongoDBSchema.png">

I have used GridFS in order to have images,music and pdfs saved to MongoDB. [GridFS](https://docs.mongodb.com/manual/core/gridfs/) is used to allow us to save larger files in MongoDB. These files are saved in newly created folders called fs.chunks and fs.files.

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
  - Able to search through all users
  - Able to view everybodys blog posts/ not just friends
  - Able to Send extra hearts per day to other users
  - Able to sort through the blog posts so you can see just the users/friends/everybodys posts.

- Share blog posts

   - Write a blog post
   - Delete a blog post
    

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

-  

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

  - This project uses Python for the main database related features. It ensures that all information shared between MongoDB and the project are accessible and respond to one another.
  - [Python](https://en.wikipedia.org/wiki/Python_(programming_language))


- Javascript

  - This project uses Javascript to create functions, rules and effects in order to make the certain features work. Features include being able to use a music player. Updating and showing dropdown menus for genre/instruments. Shrink the number of words on a review card until read more is clicked if over a certain amount.
  - [Javascript](https://en.wikipedia.org/wiki/JavaScript)

#### Frameworks Used

- Bootstrap
    - Bootstrap is an open source library with access to reusable bits of code for html, css and javascript.
    - [Bootstrap](https://getbootstrap.com/) 

- jQuery
    - jQuery is an open source library that makes using javascript easier and quicker. It simplifies a variety of multiple lines of javascript code by putting it into a single line of jquery code. 
    - [jQuery](https://jquery.com/)

- Django
    

- Celery


- Allauth


- Stripe


- 
 
##### Back to [top](#table-of-contents)

---

## Testing

---

### Validators

- HTML

  - [W3C HTML Validator](https://validator.w3.org/) 
    
    - Used the deployed website address to check every page throughout website. 
    - Document checking completed. No errors or warnings to show.

- CSS

  - [W3C CSS Validator](https://jigsaw.w3.org/css-validator/) "Congratulations! No Error Found. This document validates as CSS level 3 + SVG !"

  - All warnings relate to the bootstrap code gained from Sass.  

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




### Local Deployment




##### Back to [top](#table-of-contents)
---

## Credits

---

### Content

- All written content was my own.
- [Unsplash](https://unsplash.com/photos/sS0-eF5uy_U) - Main home image
- [pixabay](https://pixabay.com/photos/piano-boy-playing-learning-78492/) - first circle image on home page
- [pixabay](https://pixabay.com/photos/eyeglasses-music-sheet-music-pen-1209707/) - second circle image on home page
- [pixabay](https://pixabay.com/photos/guitar-guitarist-music-756326/) - third circle image on home page

### Media

- Uploaded piano pieces were performed by myself
- Alton towers theme(hall of the mountain King) was downloaded from [here](https://www.youtube.com/watch?v=2fGkrHuNS7k)
- All images used for uploading are found on [google images](www.google.com) by using images/tools/usage rights/commercial and other licenses.
- For the purpose of this project I have used sheet music that is already written and by others as the time constraints for this project dont allow time for writing my own music. 

### Acknowledgements

- I'd like to thank the slack community for their support, particularly the May 2020 cohort group who have given me support and suggestions.
- I'd also like to thank my friends and family for their support, and their support with testing of the website. 

##### Back to [top](#table-of-contents)
