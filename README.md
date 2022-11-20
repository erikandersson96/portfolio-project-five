# AndWatch's
 
<p align="center">
   <img src="/readme_images/aws.png" width="150px"/>
</p>
 

 
### HINT:
**Remember that all links in this Readme does not open in a new tab. They open in the same window (I have marked them with "(link)").** 
 
![Screenshot of Techsini mockup](/readme_images/mockup-aws.png)
 
To visit `AndWatch's` website please click this [link](https://andwatchs-2022.herokuapp.com/) (link).
 
 
---
## Portfolio Project Four
 
### Intention
 
This website is a fictional website for the purpose of my Fifth Portfolio Project for Code Institute’s Full Stack Software Development Course. I created this website with the knowledge I gained from the `Building an E-commerce Platform, Introduction to Search Engine Optimization and Web Marketing` modules in the last section of the course.
 
The main goal of this project was to test my new knowledge in Building an E-commerce Platform with Django, Bootstrap and Stripe as a payment system. 
 
##### Features I aimed to achieve with this project:
* To make the website easy to understand for the user.
* Make sure so the website has good `UI and UX` throughout the whole website so the user doesn't get confuesed.
* Create a easily navigated website with an easy to understand `navigation menu on top and a nice footer at the bottom`.
* Follow a `black and yellow` theme throughout the whole website design.
 
 
---
## How To Navigate The Website

At the very top is a `banner` with text containg that AndWatches provides `Free shipping on all order worldwide!`.

The website of AndWatch's features a Navigation bar on top underneath the banner that exists on all pages with the following content: 
`Logo, Search Bar, Home link button, Watches dropdown menu, Blog link button, My account dropdown menu, and a Shopping Bag`. The logo acts like a `back to home page` link.
The dropdown menu of `Watches` features a selection between listing watches by their price or if the user wish to see all of the available watches by `All watches`.
`Blog link button` will take the user to a seperate page with all of the blog posts that AndWatch's is publishing, here the user can select a post they want to read by clicking the 
image of the selected blog post, and get directed to the details of that blog post. The user (both register users and non register users) can leave comments underneath the
blog post details page. But be aware of that the `Store Manager` might delete posts that are offensive or inappropriate. At the search bar a user can search for relevant names of wrist 
watches amoung all of the available products in the store. The `My account dropdown menu` features register or login depending on if the user has an existing account or wish to become one.
When the user is logged in they will see `My profile or Logout`, My profile is where the user can see their user information if they have submitted and order in the past or their order 
history listed. At the `Shopping Bag` the user can click when they have added products to the bag or if they are just curios they can see the empty bag aswell, and inside the bag there is
a button for be directed to all the watches if the user wish to do so. 

At the bottom of the page is the footer that also exists on all pages with the following content `A "logo" that just acts like a logo for AndWatch's,`
`A link for signup with the newsletter, Contact us page link, About us page link and the social media icons`. The link to the newsletter will direct the user for signup as mentioned, the newsletter provider is [mailchimp](https://mailchimp.com/) (link). The contact us page link will direct the user to a seperate page with all of the contact information of AndWatch's.
The about us page link works as the contact link but it will direct the user to a page of all the information about AndWatch's. The social media links will direct the user to each 
seperate plattform, `GitHub, LinkedIn, and Facebook`. The GitHub link and LinkedIn link is directing to Erik Andersson (creator of this project) personal pages. The `FaceBook` link
on the other hand directs the user to the FaceBook page of `AndWatch's`. At the very bottom is the `Copyright of AndWatch's - Erik andersson`. 

At the `home page` is a Hero image of a seiko watch, a text for the user to take action and press the `Shop Now` button to get to all watches page.

At the `Watches - All watches` page is all the current available watches listed, if the user wish to sort the list of watches he/she can do so by filtering of 
`Price low to high, Price high to low, Brand A - Z, Brand Z - A`. The user can then reset the sorting/filtering by cklicking the yellow text above all watches to the left. 

At the `watch details page` by cklicking on one of the watches (products) images, is all of the details of each watch like 
`Image, Brand, Model, Price, Description, Case Size, Quantity, Keep Shopping and Add to Bag buttons`. The user can here add the product to the bag or adjust the wanted quantity
of the product before adding it to the bag. When the user have added a product to the bag a successfull message will appear with a preview of the shopping bag with a 
`Go to secure checkout` button. 

When the user has added a product/products to the bag and want to see the bag they can either do so by clicking the `Go to secure checkout` button in the bag preview or click the 
shopping bag in the up right corner. 

At the `shopping bag` the user can adjust the quantity of the products or remove them from the bag or just press the `Secure Checkout` button. 

When the user has clicked the `Secure Checkout` button the user will get to the checkout page. 

At the `checkout page` the user will be asked to fill out the form of details, delivery info and payment card. If the user is logged in and never bought anything they can tick the 
`Save info` checkbox underneath the form to save their information for future purchases. Now the user will need to cklick on `Complete Order` as a final step to process the purchase.
A yellow transparent loading overlay (like in Boutique Ado) will pop up with two spinning arrows and a success message will pop up. The user will now see a thank you text above and
the order, deliver to and billing information below. 

The user can update their information about delivery and so on on their `Profile` page. 

#### Good To Know

As well as there is success messages for every successfull transaction on the site there is also `error messages` in the same way with a short instruction on what might have gone wrong.

### For Store Managers Only!

If you are logged in as a store manager (admin) on AndWatch's you can then manage all products, blog posts and comments by edit or deleting them. You can add new products by 
clicking on `Product Managment` on the profile. **Important! Be aware of:** if you press delete on a product, blog post or comment they will be deleted and this action cannot be undone! 

 
---
## Table of Contents
 
* [Planning](#planning)
  * [Wireframe](#what-to-eat---balsamiq-wireframe)
  * [Trello](#trello---user-stories-board)
 
* [UX](#ux)
  * [User Stories](#user-stories)
  * [Strategy](#strategy)
  * [Scope](#scope)
 
* [Website Design](#website-design)
  * [Design](#design)
  * [Colors](#color-scheme)
  * [Fonts](#fonts)
 
* [Logic](#logic)
  * [Database Diagram](#what-to-eat---database-schema)
  * [Flow Diagram](#what-to-eat---flow-diagram)
 
* [Existing Features](#existing-features)
  * [Start Screen](#start-screen)
  * [Footer](#footer)
  * [Navbar](#navbar)
  * [About modal](#about-modal)
  * [Add recipe](#add-recipe)
  * [User](#user)
  * [Recipes](#recipes)
  * [Edit recipe](#edit-recipe)
  * [Delete recipe](#delete-recipe)
  * [My favorites](#my-favorites)
 
* [Testing](#testing)
  * [Bugs](#bugs)
  * [Unfixed bugs](#unfixed-bugs)
 
* [Technologies Used](#technologies)
 
* [Credits](#credits)
 
* [Deployment](#deployment)
  * [GitHub & Gitpod ](#github--gitpod)
  * [Forking GitHub Repository](#forking-github-repository)
  * [Cloning GitHub Repository](#cloning-github-repository)
  * [Heroku](#heroku)
 
* [Support](#support)
 
 
---
## Planning
 
### AndWatch's - Balsamiq Wireframe
 
I created a Wireframe for this project to showcase for my mentor what my design idea for this project would look like using [Balsamiq - wireframes](https://balsamiq.com/) (link). But I also created this so I could focus more on designing the actual website instead of having to think to much how the design for this project would look like while building the project.
 
Since it would be a lot of images to insert in this `Readme` I decided that you can take a look by this shared link of my wireframes, [AndWatch's - wireframe](https://balsamiq.cloud/sxp607p/plaieoc) (link).
Since the wireframes is a idea of how I think the website would look like before I started coding, the finished website isn't 100% look a like.
 
### Trello - User Stories Board
 
Before I started to work with the code for this project I was requested of my mentor to create a mapping tool for my `user stories` to easier track `what to do when`. So I choose to use [Trello](https://trello.com/en) (link) as my tool for this. During my development I have been moving each user story with it's `EPICS` to the correct stage of the process, and I have made sure that each user story was manualy tested and fully functional before moving on to the next one.
 
If you want to visit my trello board you can do so by visit this [link](https://trello.com/invite/b/e3SZtNeH/834b609e9c7347149b597bb49d09e186/portfolio-project-5) (link).
 
I will demonstrate each step in the process for you down below of my trello board during my development:
 
**Trello board:**
 
![Screenshot of trello board](/readme_images/trelloboard.png)
 
 
**To Do (Admin):**
 
![Screenshot of trello admin to do]()
 
**In-design (Admin):**
 
![Screenshot of trello admin in-design]()
 
**Testing (Admin):**
 
![Screenshot of trello admin testing]()
 
**Done (Admin):**
 
![Screenshot of trello admin done]() 
 
 
---
## UX
 
#### User Stories
As a guest I would like to be able to:
 
* Register an account using username, email, and password.
* Learn more about the website.
* Visit the website's social platforms.
* Visit the website's Facebook page.
* View all of the watches available.
* View the watch details of a selected watch.
* Purchase watches using my credit/debit card.
 
As a registered user I would like to be able to:
 
* Login to my account.
* See order history, and change shipping/billing information.
* See blog posts and comment on them.
* Add watches to my wish list.
* Learn about the website.
* Visit the website's social platforms.
* Visit the website's Facebook page.
* View all of the watches available.
* View the watch details of a selected watch.
* Purchase watches using my credit/debit card.
 
As an admin I need to be able to:
 
* See the entire list of watches available.
* Add watches to the store.
* Edit watches that are available.
* Delete available watches.
* Add and edit blog posts.
* Delete blog posts.


#### Strategy
 
* **Project Goal**
Create a website that allows users to create an account so they can see order history, change shipping and billing information, add comments on blog posts, add watches to their wish list.
And most important purchase products, but this is of course open for all users even for those who isn't registered with an account.
 
#### Scope
 
* A simple and straightforward UX experience. 
* A navigation bar that is easy to navigate the website with.
* A website that is compatible on most screen devices and browsers.
 
 
---
## Website Design
 
### Design
 


### Color Scheme
  
 
**#34A56F - A lighter green (HEX-color)**
 
![Screenshot of green color]()
 
**#20603C - A darker green (HEX-color)**
 
![Screenshot of green color]()
 
**#1C5434 - A dark green (HEX-color)**
 
![Screenshot of green color]()
 
**Red color (Default bootstrap color "btn-danger")**
 
![Screenshot of red color]()
 
**Black color (Default css color)**
 
![Screenshot of black color]()
 
 
### Fonts
 
I choose two different fonts for my website, `"Dancing Script"` for my logo and all headings (h1, h2, h3) and `"Lato"` for all other text. I choose these two fonts because I thought they matched good togheter and for this website. The fonts were taken from `pairfonts.com`.
 
**Dancing Script for my logo and all headings:**
 
![Screenshot of black color]()
 
**Lato for all other text:**
 
![Screenshot of black color]()
 
 
---
## Logic
 
### AndWatch's - Database Schema
 
Before I started to code this project I created a `Diagram Entity Relationship - Database Schema` using [dbdiagram](https://dbdiagram.io/home) (link). I created this to easier understand the database models that I was going to create for this project.
 
![Screenshot of database schema]()
 
### AndWatch's - Flow Diagram
 

[Lucid Chart](https://www.lucidchart.com/pages/) (link). 
 
![Screenshot of flow diagram]()
 
**Explain flow diagram:**
 
 
---
## Existing Features
 
 
---
## Future Features
 
 
---
## Technologies
 
Technologies that I used for `AndWatch's` website project is the following down below.
 
#### Programming Languages
 
* [Python 3](https://www.python.org/) (link): Python is a general-purpose language, meaning it can be used to create a variety of different programs and isn't specialized for any specific problems.
 
#### Frameworks & Programs
 
* [Django](https://www.djangoproject.com/) (link): Django is a high-level `Python web framework` that enables rapid development of secure and maintainable websites.
 
* [Bootstrap 5](https://getbootstrap.com/) (link): Bootstrap is a `CSS framework and toolkit`. Developers can't use it to write programs, but because Bootstrap contains massive amounts of reusable code and website element templates, the framework can remove some of the “busy work” and significantly speed up the process of building a website.
 
* [GitHub](https://github.com) (link): GitHub is used to store all data from the project after it has been pushed using the
`git add . | git commit -m "message here" | git push` command in the GitPod terminal.
 
* [GitPod](https://www.gitpod.io) (link): I used `GitPod` as my `IDE` that stands for `An integrated development environment (IDE) is a software for building applications that combines common developer tools into a single graphical user interface (GUI)`. You can read more about this [here](https://www.gitpod.io/blog/gitpod-launch) (link).
 
* `Git`: This is used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub. Incase someting unexpected happens to your gitpod workspace, everything is committed to your GitHub repository.
 
* [Heroku](https://www.heroku.com) (link): Heroku is a container-based cloud Platform as a Service `(PaaS)`. Developers use Heroku to deploy, manage, and scale modern apps.
 
* [LucidChart](https://www.lucidchart.com/pages/) (link): Lucidchart is the intelligent diagramming application that empowers teams to clarify complexity, logic and more. To get a better visual understanding about how an application work.
 
* [PEP8](http://pep8online.com/) (link): Is a validation tool that I used to validate my code.
 
* [Techsini](https://techsini.com/multi-mockup/index.php) (link). Used to create the mockup image.
 
* [Font Awesome](https://fontawesome.com/) (link). Was used to add icons for my social media links.
 
* [Pair Fonts](https://pairfonts.com/) (link). I used Pair Fonts to add custome fonts for the aesthetic and UX purposes.
 
* [Balsamiq](https://balsamiq.com/) (link). Balsamiq was used to create my wireframe for my design process.
 
* [dbdiagram](https://dbdiagram.io/home) (link). dbdiagram was used to create my database schema before I started to code my project.
 
* [Trello](https://trello.com/) (link). Trello was used for creating my board for mapping my user stories in this project.
 
* [Favicon](https://favicon.io/) (link). Favicon was used to create the little icon that is showing in the browser adress bar to make the user experience more professional for the website.
 
 
---
## Testing
 
All testing of this project has been documented in a seperate file called `TESTING.md` and you can fin it [here](TESTING.md) (internal link).
 
### Bugs

* **Bug 1:**
I noticed that my footer wasn't at the bottom at my watches page, it was amoung the watches like seen in the screenshot below. You can see the name of AndWatch's between the two images in the middle. The screenshot is taken of another page that hasn't been implemented in the final version.
 
**Screenshot:**
 
![Screenshot bug 1](/readme_images/bug-1.png)
 
* **Solution Bug 1:**
The solution to this bug was that I had set the height of my products template to a bootstrap class of `min-vh-100` and in my base template I had did the same. I will show a screenshot of the problem down below. So I just made sure I didn't used that bootstrap class anywhere else then in my base temaplate. And in my base template I changed to just `vh-100`.

![Screenshot bug 1 - problem](/readme_images/bug-1-problem.png)
 
* **Bug 2:**
My sorting for products on the all watches page for `"Brand"` (Brand A-Z, Brand Z-A etc) which I have namned `"watch_make"` in my database for products wasn't working and I got an error for `FieldError at /products/` `Cannot resolve keyword 'name' into field.`. My goal was to get the sorting for A - Z or Z - A working properly.

**Screenshot:**

**Error message:**

![Screenshot bug 2 error message](/readme_images/bug-2.png)

**Sorting selector html:**

![Screenshot bug 2 sorting selector html](/readme_images/sorting-selector.png)

* **Solution Bug 2:**
After I had tried different methods of tweaking the `JavaScript` of this sorting selector I decided to take some help from the Tutors at Code Institute. I got some amazing help from a guy namned `Ed`. After some minutes spent by Ed he discovered that my `JavaScript` function was searching for the underscore to decide what I was trying to do when selecting the A - Z etc, and since I had namned the watch make of brand in my database model to watch_make instead of something like brand the `JavaScript` function was trying to execute at the first underscore in `watch_make_asc` & `watch_make_desc` when it was supposed to execute at the underscore before `asc` or `desc` so therfore I got that error. `Ed` was kind to help my rewrite the `JavaScript` function to execute at correct underscore. I will show two images below with my old function and the new one that `Ed` helped me with.

**Wrong JavaScript Function:**

![Screenshot bug 2 wrong javascript function](/readme_images/bug-2-wrong-js.png)

**Correct JavaScript Function:**

![Screenshot bug 2 correct javascript function](/readme_images/bug-2-correct-js.png)
 
* **Bug 3:**

 
**Screenshot:**
 
![Screenshot bug 3]()
 
* **Solution Bug 3:**

 
### Unfixed Bugs
 
 
---
## Credits
 
#### Media
 
All images for this project was taken from []() (link).
 
#### Inspiration for this project
 
[Code Institute](https://codeinstitute.net/) (link) - I took inspiration to this project from the `Code Institute` walkthrough videos of `Boutique Ado`.

#### Add newsletter - mailchimp guide
 
[Python stacks](https://www.pythonstacks.com/blog/post/integrating-mailchimp-django/) (link) - I used this guide to implement the functionality of `mailchimp` to my newsletter.
  
 
#### Help from Stack Overflow
 
 
---
## Deployment
 
**GitHub:**
 
I frequently used `commit` throughout the whole project, this is the commands used in the terminal:
 
* `git add .` (This command is used for adding files to the staging area before committing).
* `git commit -m “commit message here..”` (This is used to label the commit changes made to the local repository).
* `git push` (This command is used to push all changes to the Github repository).
 
This is all done to prevent any `data` loss in case Gitpod crashes and saves the `data` to GitHub.
 
 
### GitHub & Gitpod
 
For this project I used Code Institutes Python template that can be found [here](https://github.com/Code-Institute-Org/python-essentials-template) (link).
 
**Steps to create a new repository in Github:**
 
1. Sign in or sign up to [GitHub](https://github.com) (link).
1. When you have done that, you will see `"new"` up in the left corner.
**Like this:**
![Screenshot new repository button github](/assets/readme/github.png)
1. Select in the dropdown menu under `Repository template` if you for example would like to use the template provided by `Code Institute` that I did for this project. If you don't see it in the dropdown menu click this [link](https://github.com/Code-Institute-Org/python-essentials-template) (link) to get to the one provided by `Code Institute` and click `Use this template` to the left of the green Gitpod button.
1. When you have done that, give the repository a name. Leave it public if you want anyone on the internet to see your repository (I always do).
1. Click create repository.
1. **Remember** to use the `commit` commands that I explained above so your hard work doesn't get lost if anything happens to Gitpod.
 
### Forking GitHub Repository
 
Forking a Github repository is the process of making a copy of someone else repository and add your own changes to it without changing the original, the original repository is known
as "upstream repository". I will explain the process of forking down below:
 
1. Go to the Github page that hosts the repository you wish to fork.
1. In the top-right corner of the page there is a button that says `"Fork"`.
1. Click this button.
1. This creates a copy of that repository to your Github home page. You can submit and receive changes to your copy by using pull requests and/or syncing with the original upstream repository.
 
This instructions were taken from [Github - Fork a repo](https://docs.github.com/en/get-started/quickstart/fork-a-repo) (link).
 
### Cloning GitHub Repository
 
Cloning a repository inolves making a full copy of a repository on your local machine. This allows you to work on the code easier. Changes can be pushed back up to the Github site or changes from other sources pulled to your local copy. I will explain how to clone down below:
 
1. Go to the repository page on Github.
1. Above the file list click on the green button that says `"Code"`.
1. You can choose to download a zip file of the repository, to unpack it on your local machine and open it in your IDE.
1. Clone using HTTPS by copying the URL under the HTTPS tab.
1. Open a terminal window, set current directory to the one you want to contain the clone from.
1. Type `git clone` and paste the URL copied from the Github page.
1. The repository clone will now be created on your machine.
 
This instructions were taken from [Github - cloning a repository](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository) (link).
 
### Heroku
 
Deploying a project using Heroku:
 
* Don't forget to set your `DEBUG` in your `settings.py` file of your main app in `Django` to `False`.
* Ensure that all of your project dependencies are listed in the `requirments.txt` file.
* If not, then you can use this command in the Gitpod terminal: `pip3 freeze --local > requirments.txt`.
* Visit the [Heroku](https://www.heroku.com) (link) website and click on create an account.
* Click the `"New"` button.
* Click the `"Create new app"` button.
* Provide a name for the app in the `App` name input field.
* Select your region from the `"choose region"` dropdown menu.
* Click the `"Create App"` button.
* Once redirected, proceed to the settings tab.
* Click on the `"config vars"` button.
* Supply a `KEY` of `PORT` and it's value of `8000`. Then click the `"add"` button. Do this with `Cloudinary, Database URL (from Heroku-Postgres) and your secret key`.
* Next step is to add `Buildpacks`, click the `"Add Buildpack"` button.
* The `Heroku Postgress` buildpack need to be added.
* Once the buildpack have completed, go to the deploy tab, once on the deploy screen, select GitHub as the deployment method and connect your GitHub profile.
* Search for the repository that you wish to deploy to `Heroku` and click `"connect"`.
* Once your repository is connected to Heroku you can choose to either automatically or manually deploy your app. 
* By selecting automatic deploy, Heroku will build a new version of the app each time a change has been made and pushed to the repository on `GitHub`.
* Click on manual deploy to build your App. When complete, click on `View` to open up the live site on `Heroku`. 
* Finished.
 
If the `create app` process at `Heroku` website wouldn't work follow these steps:
* When you want to deploy your project to `Heroku`.
* Type `heroku login -i` to login to your existing account (if you have one) in the `Gitpod` terminal.
* Then run the command `heroku create your_app_name_here` to create a new app (the name has to be uniqe).
* Now you can see your new project at `Heroku` dashboard and set the config vars and buildpacks as the steps explained above.
 
 
---
## Support
 
I would like to give an extra `Thank you` to all the kind people I have around me that gave me support in all different ways.
 
* **Code Institute** for their **Tutor** support.
* My mentor [Benjamin Kavanagh](https://github.com/BAK2K3) (link) for being a **Superior** mentor.
* **Google** for always clear things up.
* **Code Institute Slack channel** for always helping out with problems or questions.
* My lovely **Girlfriend** for always supporting and believing in me.
 
### RETURN TO THE [TOP](#andwatch's)