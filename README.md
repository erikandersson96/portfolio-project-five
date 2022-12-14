<h1 align=center>AndWatch's</h1> 
 
<p align="center">
   <img src="/readme_images/aws.png" width="150px"/>
</p>
 

 
### HINT:
**Remember that all links in this Readme does not open in a new tab. They open in the same window (I have marked them with "(link)").** 
 
![Screenshot of Techsini mockup](/readme_images/mockup-aws.png)
 
To visit `AndWatch's` website please click this [link](https://andwatchs-2022.herokuapp.com/) (link).
 
 
---
## Portfolio Project Five
 
### Intention
 
This website is a fictional website for the purpose of my Fifth Portfolio Project for Code Institute’s Full Stack Software Development Course. I created this website with the knowledge I gained from the `Building an E-commerce Platform, Introduction to Search Engine Optimization and Web Marketing` modules in the last section of the course.
 
The main goal of this project was to test my new knowledge in Building an E-commerce Platform with Django, Bootstrap, and Stripe as a payment system.
 
##### Features I aimed to achieve with this project:
* To make the website easy to understand for the user.
* Make sure the website has good `UI and UX` throughout the whole website so the user doesn't get confused.
* Create an easily navigated website with an easy-to-understand `navigation menu on top and a nice footer at the bottom`.
* Follow a `black and yellow` theme throughout the whole website design.
 
 
---
## How To Navigate The Website

At the very top is a `banner` with text containing that AndWatches provides `Free shipping worldwide!`.

The website of AndWatch's features a Navigation bar on top underneath the banner that exists on all pages with the following content: 
`Logo, Search Bar, Home link button, Watches dropdown menu, Blog link button, My account dropdown menu, and a Shopping Bag`. The logo acts like a `back to home page` link.
The dropdown menu of `Watches` features a selection between listing watches `By Price` or if the user wishes to see all of the available watches by `All watches`.
`Blog link button` will take the user to a separate page with all of the blog posts that AndWatch's is publishing, where the user can select a post they want to read by clicking the 
image of the selected blog post and get directed to the details of that blog post. The user (only registered users) can leave comments underneath the
blog post details page. But be aware that the `Store Manager` might delete posts that are offensive or inappropriate. At the search bar, a user can search for relevant names of wrist 
watches among all of the available products in the store. The `My Account dropdown menu` features register or login depending on if the user has an existing account or wishes to become one.
When the user is logged in they will see `My Profile, Wish list or Logout`, My profile is where the user can see their user information if they have submitted an order in the past or their order history listed. The `Wish list` is a page where all of their chosen "favorite" watches are displayed. At the `Shopping Bag` the user can click when they have added products to the bag or if they are just curious they can see the empty bag as well, and inside the bag, there is a button to be directed to all the watches if the user wishes to do so.

On smaller screen sizes the menu for `Home, Watches, Blog` will be in a `"hamburger menu"` on the left.

At the bottom of the page is the footer that also exists on all pages with the following content `A "logo" that just acts like a logo for AndWatch's,`
`A link for signup with the newsletter, Contact us page link, About us page link, Privacy Policy, and the social media icons`. The link to the newsletter will direct the user to signup as mentioned, the newsletter provider is [mailchimp](https://mailchimp.com/) (link). The contact us page link will direct the user to a separate page with all of the contact information of AndWatch's. The about us page link works as the contact link but it will direct the user to a page with all the information about AndWatch's. The social media links will direct the user to each separate platform, `GitHub, LinkedIn, and Facebook`. The GitHub link and LinkedIn link are directed to Erik Andersson's (creator of this project) personal pages. The `FaceBook` link
on the other hand directs the user to the FaceBook page of `AndWatch's`. At the very bottom is the `Copyright of AndWatch's - Erik Andersson`. 

At the `home page` is a Hero image of a Seiko watch, a text for the user to take action and press the `Shop Now` button to get to all watches page.

The `Watches - All watches` page is all the current available watches listed, if the user wishes to sort the list of watches he/she can do so by filtering of 
`Price low to high, Price high to low, Brand A - Z, Brand Z - A`. The user can then reset the sorting/filtering by clicking the yellow text above all watches to the left. 

On the `watch details page` by clicking on one of the watches (products) images, all of the details of each watch like 
`Image, Brand, Model, Price, Description, Case Size, Quantity, Keep Shopping, and Add to Bag buttons`. The user can here add the product to the bag or adjust the wanted quantity
of the product before adding it to the bag. When the user has added a product to the bag a successful message will appear with a preview of the shopping bag with a 
`Go to secure checkout` button. 

When the user has added a product/products to the bag and wants to see the bag they can either do so by clicking the `Go to secure checkout` button in the bag preview or by clicking the 
shopping bag in the up-right corner. 

At the `shopping bag` the user can adjust the quantity of the products or remove them from the bag or just press the `Secure Checkout` button. 

When the user has clicked the `Secure Checkout` button the user will get to the checkout page. 

At the `checkout page` the user will be asked to fill out the form with details, delivery info, and payment card. If the user is logged in and never bought anything they can tick the 
`Save info` checkbox underneath the form to save their information for future purchases. Now the user will need to click on `Complete Order` as a final step to process the purchase.
A yellow transparent loading overlay (like in Boutique Ado) will pop up with two spinning arrows and a success message will pop up. The user will now see a thank you text above and
the order, delivery to, and billing information below. The user will get a confirmation email about their order.

The user can update their information about delivery and so on their `My Profile` page.

To access the `blog` the user clicks on the blog button. At the blog, all the blog posts are listed, and all of them are created by the team at `AndWatch's`. If the user clicks on one of the blog posts he/she will then be displayed with the details of the blog post. If the user scrolls down there is a `comment` section where (only registered users) can add comments on the blog post. All users (even those who aren't logged in or registered) can see the comments section. Only `"Store Managers/Admin"` can delete comments that have been posted on blog posts, to ensure friendly language from users.

Logged-in users can add watches to their `wish list` if they want to, they can do so at each `watch details` page. They can then remove each individual watch from the `wish list` as they wish to do.

#### Good To Know

As well as there being success messages for every successful transaction on the site there is also `error messages` in the same way with short instruction on what might have gone wrong.

### For Store Managers Only!

If you are logged in as a store manager (admin) on AndWatch's you can then manage all products, and blog posts by editing or deleting them, and comments can be deleted. 
You can add new products or blog posts by clicking on `Product Management/Blog Management` on the profile. As an admin, you can edit/delete products and blog posts, and comments you can only delete. 

**Important! Be aware of:** if you press delete on a product, blog post, or comment they will be deleted and this action cannot be undone!

 
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
  * [Profiles](#profiles)
  * [Products](#products)
  * [Newsletter](#newsletter)
  * [Home](#home)
  * [Checkout](#checkout)
  * [Blog](#blog)
  * [Bag](#bag)
  * [Wish list](#wish-list)
  * [Responsive Layout and Design](#responsive-layout-and-design)

* [Future Features](#future-features)
  * [Django Admin panel to Front end](#django-admin-panel-to-front-end)

* [Marketing Strategy](#marketing-strategy)
  * [FaceBook page](#facebook-page-of-andwatchs)
  * [Mailchimp](#mailchimp)
  * [robots.txt](#robotstxt)
  * [sitemap.xml](#sitemapxml)
  * [Privacy Policy](#privacy-policy)

* [Technologies Used](#technologies)
 
* [Testing](#testing)
  * [Bugs](#bugs)
  * [Unfixed bugs](#unfixed-bugs) 
 
* [Credits](#credits)
 
* [Deployment](#deployment)
  * [GitHub & Gitpod ](#github--gitpod)
  * [Forking GitHub Repository](#forking-github-repository)
  * [Cloning GitHub Repository](#cloning-github-repository)
  * [Heroku](#heroku)
  * [ElephantSQL](#elephantsql)
 
* [Support](#support)
 
 
---
## Planning
 
### AndWatch's - Balsamiq Wireframe
 
I created a Wireframe for this project to showcase for my mentor what my design idea for this project would look like using [Balsamiq - wireframes](https://balsamiq.com/) (link). But I also created this so I could focus more on designing the actual website instead of having to think too much about how the design for this project would look while building the project.
 
Since it would be a lot of images to insert in this `Readme` I decided that you can take a look at this shared link of my wireframes, [AndWatch's - wireframe](https://balsamiq.cloud/sxp607p/plaieoc) (link). Since the wireframes are an idea of how I think the website would look like before I started coding, the finished website isn't 100% look alike.
 
### Trello - User Stories Board
 
Before I started to work with the code for this project I was requested by my mentor to create a mapping tool for my `user stories` to easier track `what to do when`. So I choose to use [Trello](https://trello.com/en) (link) as my tool for this. During my development, I have been moving each user story with its `EPICS` to the correct stage of the process, and I have made sure that each user story was manually tested and fully functional before moving on to the next one.
 
If you want to visit my Trello board you can do so by visiting this [link](https://trello.com/invite/b/e3SZtNeH/834b609e9c7347149b597bb49d09e186/portfolio-project-5) (link). 
 
**Trello board:**
 
![Screenshot of trello board](/readme_images/trelloboard.png)

Instead of including each `user story` card here, I will explain how these cards are set up by demonstrating one `user story`.
But if you wish to see all of the cards you can then just visit the link to the board above.

Each `user story` are grouped together with other cards that they are relevant by with an `EPIC - Heading` and a unique label color.

**EPIC:**
 
![Screenshot of trello epic](/readme_images/epic-heading.png)
 
**User story card:**
 
![Screenshot of trello user story card](/readme_images/card-blue.png)

As you can see above the `EPIC-Products` is "linked" together with the `user story card` that has the same blue label above them. So each `user story` that is related to the products of AndWatch's will have that blue label above them, this goes on for each `EPIC` and the attached label color that is related to each `user story` card with their own unique label color.

If you click on each `user story card` a bigger view will be displayed with `Given, When, Then` to act like a description for the use of that particular `user story`. Like this:

**User story card details:**
 
![Screenshot of trello card details](/readme_images/card-open.png)

The `user stories` for admin is set up in the same way.


---
## UX
 
### User Stories

As a guest I would like to be able to:
 
* Register an account using username, email, and password.
* Learn more about the website.
* Visit the website's social platforms.
* Visit the website's Facebook page.
* View all of the watches available.
* View the watch details of a selected watch.
* Purchase watches using my credit/debit card.
* View the blog, all blog post details, and comments. 
 
As a registered user I would like to be able to:
 
* Login to my account.
* See order history, and change shipping/billing information.
* See blog posts and comment on them.
* Add/remove watches to my wish list.
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
* Delete blog post comments.


### Strategy
 
#### Project Goal
Create a website that allows users to create an account so they can see order history, change shipping and billing information, add comments on blog posts, and add watches to their wish list. And most important purchase products, but this is of course open for all users even for those who aren't registered with an account.


### Scope
 
* A simple and straightforward UX experience. 
* A navigation bar that is easy to navigate the website with.
* A website that is compatible with most screen devices and browsers.
 
 
---
## Website Design
 
### Design

<details>
<summary>Logo Design</summary> 
<br>
I decided to go with `AndWatch's` because I think it is simple and clean. But also since I named my first-milestone project in this course "Andersson's" and that site was related to wristwatches as well, I thought it was a little nostalgic to use something similar that relates to my name "Erik Andersson".
<br>

Here you can take a look at [first-milestone](https://github.com/erikandersson96/first-milestone) (link).

![Screenshot of logo design](/readme_images/logo.png)
</details>

<details> 
<summary>Background Image</summary>
<br>
I downloaded the background image/hero image from Unsplash which is a website with free images. I have used the background image only on the Home page of this project. The background color is set to black since no text on the whole website is black, and if the background image wouldn't load the text would still be visible.
<br>

Here you can take a look at [Unsplash](https://unsplash.com/) (link).
<br>

![Screenshot of hero image](/readme_images/hero-image.png)
</details>

<details>
<summary>Navigation Bar</summary>
<br>
My navigation bar for this website is relatively clean, with just the most necessary text/buttons/search bar/menus to give the website an overall clean look.
<br>

![Screenshot of navigation bar](/readme_images/nav-bar.png)
</details>

<details>
<summary>Headings</summary>
<br>
Almost all pages existing on this website use the same design with a heading on top, a yellow line under, and then the relevant body of that page.
<br>

![Screenshot of a page heading](/readme_images/heading.png)
</details>

<details>
<summary>Buttons</summary>
<br>
The design of the buttons on this website of course varies depending on the background and the surrounding (if the button is next to another button etc). Most of the buttons are black with text and a white border around them, but some buttons are white with black text, yellow with black text, white text, yellow text, blue text, and red text. The buttons that are a solid color are not really buttons they are most often a link but they act like a button. Almost all buttons/links change their color when you hover over them giving them an effect that makes the user aware of clicking. 
<br>
**Remember:** All buttons/links that are colored with red is either a delete button or a remove button.   
<br>

![Screenshot of buttons](/readme_images/btn-1.png)
![Screenshot of buttons](/readme_images/btn-2.png)
![Screenshot of buttons](/readme_images/btn-3.png)
![Screenshot of buttons](/readme_images/btn-4.png)
![Screenshot of buttons](/readme_images/btn-5.png)
</details>

<details>
<summary>Footer</summary>
<br>
I choose a footer that would melt into the rest of of the design theme (black/white/yellow). The footer holds the "Logo", "Newsletter link", "Contact link", "About us link", "social media links", "Privacy Policy link" and the "copyright information".
<br>

![Screenshot of footer](/readme_images/footer.png)
</details>

<details>
<summary>Dropdown Menus</summary>
<br>
I choose to go for dropdown menus for "Watches (products)" and "My profile" as in the Code Institute - Boutique Ado Walkthrough Project.
<br>

![Screenshot of dropdown watches](/readme_images/dropdown-watches.png)
![Screenshot of dropdown profile](/readme_images/dropdown-profile.png)
</details>

<details>
<summary>My Profile</summary>
<br>
My profile page is the same layout as in Code Institute - Boutique Ado Walkthrough Project, but with the correct color theme for this website. This page holds all the saved delivery information of the user (if the user has made purchases before) where the user can update the information and the page also lists order history with all orders made with that user account.
<br>

![Screenshot of profile page](/readme_images/profile.png)
</details>

<details>
<summary>Register/Login/Log out</summary>
<br>
The register, login, and logout pages hold the relevant input boxes for users to either create an account, log in, or log out. The styling for these is almost the same with the correct color scheme of the website black/white/yellow.
<br>

![Screenshot of register page](/readme_images/register.png)
![Screenshot of login page](/readme_images/login.png)
![Screenshot of logout page](/readme_images/logout.png)
</details>

<details>
<summary>Wish list</summary>
<br>
The wish list has the same layout as the Watches/Blog posts pages. All the watches the user adds to the wish list will be displayed in the following order newest first etc and the user can remove the watches from the list via the remove button. The user can click on the specific watch image and will then be displayed with the watch details.
<br>

![Screenshot of wish list](/readme_images/wish-list.png)
</details>

<details>
<summary>Toasts (messages)</summary>
<br>
For each transaction made on the website, regardless of whether it is adding a watch to the shopping bag, editing a blog post, or triggering an error the user/admin will get a message in the up-right corner with the relevant information if the transaction was successful or not. The different toasts used are success, info, warning, and error with all of them wearing it's own color relating to the message (like error = red, success = green). These toasts were taken as inspiration from the Code Institute - Boutique Ado Walkthrough Project.
<br>

![Screenshot of toast success](/readme_images/toast.png)
</details>

<details>
<summary>Shopping Bag pop-up</summary>
<br>
Every time when a user adds a watch to the shopping bag or when a user removes a watch from the bag if he or she has more than one in the bag. The user can use the button in this pop-up bag to get to the real shopping bag. This feature is taken as inspiration from the Code Institute - Boutique Ado Walkthrough Project but I have styled it to match the rest of this website.
<br>

![Screenshot of pop-up bag](/readme_images/pop-up.png)
</details>

<details>
<summary>Shopping Bag</summary>
<br>
The shopping bag displays all the watches that have been added to the bag, the quantity of each watch, an update/remove quantity input, price, subtotal, bag total, grand total, and buttons for shop more or secure checkout. This page is taken as inspiration from Code Institute - Boutique Ado Walkthrough Project but I have styled it to match the rest of this website.
<br>

![Screenshot of shopping bag](/readme_images/bag.png)
</details>

<details>
<summary>Checkout</summary>
<br>
The checkout page displays a form for submitting the delivery and billing information (this form can be pre-filled if the user is logged in and has saved past purchase info), an order summary that shows the watches the user has added, quantity, subtotal, order total, grand total and buttons for either adjusting the bag if the user wants to add more watches or remove watches. The other button is for complete orders (confirm the purchase!). This page is taken as inspiration from the Code Institute - Boutique Ado Walkthrough Project but I have styled it to match the rest of this website.
<br>

![Screenshot of checkout page](/readme_images/checkout-1.png)
![Screenshot of checkout page](/readme_images/checkout-2.png)
</details>

<details>
<summary>Checkout Success/Order Information</summary>
<br>
When the user has clicked the button to complete the order a new page will show up with the order information. This page displays order info, order details, delivery to, billing info, and a button for shopping for more watches. A success message will show up on this page after the purchase was completed with information about the order. This page is taken as inspiration from the Code Institute - Boutique Ado Walkthrough Project but I have styled it to match the rest of this website.
<br>

![Screenshot of checkout success page](/readme_images/checkout-success.png)
</details>

<details>
<summary>Add/edit products/blog posts</summary>
<br>
The pages for add/edit products/blog posts are almost the same in layout as CI - Boutique Ado, but they follow the color theme of this website. With a form for either adding or editing the related product/blog post.  
<br>

![Screenshot of add/edit products/blog posts](/readme_images/add-1.png)
![Screenshot of add/edit products/blog posts](/readme_images/add-2.png)
![Screenshot of add/edit products/blog posts](/readme_images/edit-1.png)
![Screenshot of add/edit products/blog posts](/readme_images/edit-2.png)
![Screenshot of add/edit products/blog posts](/readme_images/add-blog.png)
![Screenshot of add/edit products/blog posts](/readme_images/add-blog2.png)
![Screenshot of add/edit products/blog posts](/readme_images/edit-blog.png)
![Screenshot of add/edit products/blog posts](/readme_images/edit-blog2.png)
</details>

<details>
<summary>Add comments on blog posts</summary>
<br>
All registered and logged-in users can add comments on blog posts, this is done by first seeing the details of a blog post details, scrolling down, clicking the button to add a comment, filling out the form on the new page with content for the comment and click on add a comment. The user will be redirected to the blog post details and the comment will appear in an order of added first on top. Only admin/store owners can delete comments.
<br>

![Screenshot of add comments](/readme_images/add-comment.png)
![Screenshot of add comments](/readme_images/comments.png)
</details>

<details>
<summary>Delete watches/blog post/comments (Only admin/Store owner)</summary>
<br>
Only the admin/Store owner of AndWatch's can delete watches, blog posts, and comments. Important to remember here is that when deleting, the action can not be undone! The buttons for this look like the images below. The delete button for watches is the same as used in Code Institute - Boutique Ado Walkthrough Project, the styling for the other two blog posts/comments are fairly the same in the looks.
<br>

![Screenshot of delete watches](/readme_images/delete-product.png)
![Screenshot of delete blog posts](/readme_images/delete-post.png)
![Screenshot of delete comments](/readme_images/delete-comment.png)
</details>


### Color Scheme
  
The main colors of this website are black, white, and yellow but I have also used a variation of other colors as well. I have displayed them all underneath

* The white color is used for almost all text, the grey color is used for the arrows used in the toast messages, and the black color is used as the background color, navigation bar, footer, and on some of the buttons.

![Screenshot of white to black colors](/readme_images/white-black.png)

* The first yellow color is used the most on this website, such as the banner on top, all yellow text, buttons, etc. The middle color is used for the yellow overlay that pops up before a user is directed to the checkout success page with spinning white arrows. The orange color is used for one of the arrows in the toast messages. 

![Screenshot of yellow to orange colors](/readme_images/yellow-orange.png)

* The first red color is used for some links such as `reset sorting` on the watches page, the second red color is used for an arrow in the toast messages and for the checkbox used on the edit product page, the third red color is used as a hover effect to the delete button, the last red color is used for the delete button.

![Screenshot of red colors](/readme_images/red.png)

* Both of the blue colors are used for the arrows on the toast messages.

![Screenshot of blue colors](/readme_images/blue.png)

* The green color is used for the success toast arrow.

![Screenshot of green color](/readme_images/green.png)

* Stripe colors from checkout.css.

![Screenshot of stripe checkout colors](/readme_images/stripe-colors.png)

* Darkblue for edit button on both products page and blog page.

**rgb(0,0,139):**

![Screenshot of darkblue color](/readme_images/darkblue.png)

* Bootstrap colors for editing/deleting products/blog posts detail pages on a black background and for deleting comments on blog posts.

![Screenshot of bootstrap colors](/readme_images/bootstrap-color-1.png)

![Screenshot of bootstrap colors](/readme_images/bootstrap-color-2.png)

I created these color paletts at [color-hex](https://www.color-hex.com/user/add-palette.php) (link).
 
### Fonts
 
I choose two different fonts for my website, `"Comforter+Brush"` for my logo and `"Lato"` for all other text including all headings. I choose these two fonts because I thought they matched well together for this website. The fonts were taken from [pairfonts.com](https://pairfonts.com/) (link).
 
**Comforter+Brush for my logo:**
 
![Screenshot of comforter brush font for logo](/readme_images/logo.png)
 
**Lato for all other text:**
 
![Screenshot of font lato on text](/readme_images/font-text.png)

![Screenshot of font lato on heading](/readme_images/font-heading.png)
 
 
---
## Logic
 
### AndWatch's - Database Schema
 
Before I started to code this project I created a `Diagram Entity Relationship - Database Schema` using [dbdiagram](https://dbdiagram.io/home) (link). I created this to easier understand the database models that I was going to create for this project.
 
![Screenshot of database schema](/readme_images/db-schema.png) 
 
### AndWatch's - Flow Diagram

Before I started to write any code for this project I made sure to create an easy and straightforward `Flow Diagram` with all the logic for this project. The `Flow Diagram` was created with the use of [Lucid Chart](https://lucid.co/) (link). I used a paid version to get more features but you can access the free version that is available for anyone that registers an account on their website.
 

**Flow diagram for users & admin/site owners:**

![Screenshot of flow diagram all](/readme_images/flowchart.png)

**Flow diagram for admin/site owners only:**

![Screenshot of flow diagram admin only](/readme_images/site-owner-flowchart.png)
 
 
---
## Existing Features

### Profiles

User management is handled through the external package [django-allauth](https://django-allauth.readthedocs.io/en/latest/) (link). All user profiles are registered at AndWatch's website when the user has verified the email address that was used when creating the account. When a user is doing a purchase at the store all the information the user filled into the checkout process will be saved to the user's profile (if the user leaves the "save info" checkbox as it is) for future purchases. 
The user will have access to a `My Profile` page where they can do the following:

* Edit their delivery information.
* View order history and click on an order number for past orders to view the details of that order.

### Products

All watches are stored in a database within the product's app models. All watches are stored with images, prices, descriptions, watch brands, watch models, watch sizes, and their individual sku.  Admin/store owner can edit all watches via the front end instead of going via the standard admin panel that is provided by Django. Admin/store owner can also add new watches to the website via the `Product Managment` page. Each watch can be clicked on for displaying the details of the selected watch. Admin/store owner can also delete watches from the website, but be careful because this action can not be undone. All watches have their own sku, which is the following: PP001, PP002, PP003, etc. So if an Admin/store owner wants to add a new watch he or she should remember to follow that pattern.

### Newsletter

The newsletter app for this project is set up with [Mailchimp](https://mailchimp.com/) (link), I decided to use Mailchimp because they have an already robust product with all sorts of templates, etc for when signing up. So when a user decides to submit their email address to the newsletter, they will be added to the email list of AndWatch's and be sent a `Thank You` email to the provided email address. 

### Home

The home app holds the views for rendering the index page, the about us page, and the contact us page templates. The home page is the page that the user will see first of all when visiting AndWatch's also called the "hero image" with a call to action button for the all-watches page. The about us page holds all the information about AndWatch's company and the history behind it, and with a call to action button here as well to direct the user to the all watches page. The contact us page holds information about AndWatch's FaceBook page, email, and phone number.

### Checkout

The checkout app has all of the database models for `Order` and `OrderLineitem` to store orders for users. Even if a user who makes a purchase at the website isn't a registered user the order will be saved, and the admin/store owner can see it in the Django admin panel. The `Order` holds all of the order information and the `OrderLineItem` hold all the information about orders that have been made by a registered user, so users can see their history for old order information. The checkout app also renders the checkout page and checkout success page.

### Blog 

All blog pages and blog posts are stored in the blog app. The database models in the blog app hold `BlogPost` and `BlogComment` models for storing all the blog posts and the comments that are made on each blog post. Admin/store owner can edit blog posts and add new blog posts to the blog. Here the user can see all blog posts that have been created, click on a blog post to see the details, or comment on blog posts (if the user is logged in). When the admin/store owner wants to add a blog post they can select an author in the add blog post form, the author list is of all users but only the admin/store owner will be displayed on the blog post as the author. Admin/store owner can delete both blog posts and comments that have been made by users but be careful because this action can not be undone.

### Bag

The bag app is for rendering the bag page template so the user can see all of the watches that have been added to the shopping bag before checkout. Here the user can update the quantity via the `blue` update link of the selected watches or remove watches from the bag via the `red` remove link.

### Wish list

The wish list (favorite watches) doesn't have its own app, it is included in the profiles app for storing the selected watches to be added to the user's wish list. There is a database model for adding watches to the wish list of `FavouriteWatch` that stores the user and the selected watch.

### Responsive Layout and Design

Using Bootstrap 4, the project has been designed to be fully responsive on most viewports, ensuring all functionality is maintained from 360px width and up. The targeted media queries are custom-made to make the website look good on most screen devices. All features have been developed with most viewports in mind.
 
---
## Future Features

#### Django admin panel to Front end

I would like to add a better and more robust Management panel for the admin/store owner to check orders, see users that have made accounts, and essentially everything that has to be done via the Django admin panel at this stage would be nice to have on the front end. This would make the website easier to maintain by all the staff at AndWatch's, with a nice looking and easy-to-understand interface. 

I would also like to add a page for admin/store owners to see the profits and income of the store, to get an understanding of what the team at AndWatchs should focus more on in their marketing to gain more customers. 


---
## Marketing Strategy

The business model of `AndWatch's` is B2C (Business to Customer), this website sells wristwatches from all kinds of brands in a price range of $90 - $50.000. The main focus of this website is to educate users via our blog, where we post blog posts regarding watches we sell or watches that we are about to add to our store so the users can gain a bigger understanding of which wristwatch to buy since we have a big variation of watches in all kind of price ranges. The goal is to sell as many watches as possible.

The marketing aspect of AndWatch's has been done via creating a real [FaceBook](https://www.facebook.com/profile.php?id=100088231741635) (link) page that you can take a look at. Creating a newsletter via [mailchimp](https://mailchimp.com/) (link) for storing email addresses from users and visitors at `AndWatch's` Mailchimp email list so we can send email campaigns to these subscribers like new watches or nice deals on watches. I used a paid version of Mailchimp to access their automation tool for subscribers. I have added `rel` attributes to all external links on the website, added a `robots.txt` file and a `sitemap.xml` file, descriptive meta tags, and `alt` on all images.

The marketing strategy of `AndWatch's` is to post posts on our FaceBook page, send emails to our email subscribers and post informative blog posts on our blog on the website.

### FaceBook page of AndWatch's

![Screenshot of AndWatchs facebook page](/readme_images/facebook.png)

### Mailchimp

The thank you for subscribing email that is being sent from Mailchimp to users who submits their email address looks like this:

![Screenshot of AndWatchs mailchimp thank you email](/readme_images/email-1.png) 
![Screenshot of AndWatchs mailchimp thank you email footer part](/readme_images/email-2.png) 

### robots.txt

`Robots.txt` is a text file webmasters create to instruct web robots (typically search engine robots) how to crawl pages on their websites. The robots.txt file is part of the robots exclusion protocol (REP), a group of web standards that regulate how robots crawl the web, access, and index content, and serve that content up to users.

This description of `robots.txt` was taken from [moz](https://moz.com/learn/seo/robotstxt) (link).

### sitemap.xml

An XML sitemap is a file that lists a website’s essential pages, making sure Google can find and crawl them all. It also helps search engines understand your website structure. You want Google to crawl every important page of your website. But sometimes, pages end up without internal links pointing to them, making them hard to find. A sitemap can help speed up content discovery.

This description of `sitemap.xml` was taken from [yoast](https://yoast.com/what-is-an-xml-sitemap-and-why-should-you-have-one/) (link).

### Privacy Policy

I have added an external link for `AndWatch's` Privacy Policy, which I generated with a free online tool that you can check out [here](https://www.privacypolicygenerator.info/) (link). The actual link to `AndWatch's` Privacy Policy, you can find [here](https://www.privacypolicygenerator.info/live.php?token=2r3kttLY1iBeLBY32YwFSRImjgB0unCt) (link).


---
## Technologies
 
The technologies that I used for `AndWatch's` website project are the following down below.
 
#### Programming Languages
 
* [Python 3](https://www.python.org/) (link): Python is a general-purpose language, meaning it can be used to create a variety of different programs and isn't specialized for any specific problems.
 
#### Frameworks & Programs
 
* [Django](https://www.djangoproject.com/) (link): Django is a high-level `Python web framework` that enables rapid development of secure and maintainable websites.
 
* [Bootstrap 4](https://getbootstrap.com/) (link): Bootstrap is a `CSS framework and toolkit`. Developers can't use it to write programs, but because Bootstrap contains massive amounts of reusable code and website element templates, the framework can remove some of the “busy work” and significantly speed up the process of building a website.
 
* [GitHub](https://github.com) (link): GitHub is used to store all data from the project after it has been pushed using the
`git add . | git commit -m "message here" | git push` command in the GitPod terminal.
 
* [GitPod](https://www.gitpod.io) (link): I used `GitPod` as my `IDE` which stands for `An integrated development environment (IDE) is a software for building applications that combines common developer tools into a single graphical user interface (GUI)`. You can read more about this [here](https://www.gitpod.io/blog/gitpod-launch) (link).
 
* `Git`: This is used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub. In case something unexpected happens to your gitpod workspace, everything is committed to your GitHub repository.
 
* [Heroku](https://www.heroku.com) (link): Heroku is a container-based cloud Platform as a Service `(PaaS)`. Developers use Heroku to deploy, manage, and scale modern apps.

* [ElephantSQL](https://www.elephantsql.com/) (link): I used ElephantSQL as my database for this project since Heroku has become a paid service only.

* [LucidChart](https://www.lucidchart.com/pages/) (link): Lucidchart is an intelligent diagramming application that empowers teams to clarify complexity, logic, and more. To get a better visual understanding of how an application work.
 
* [PEP8ci](https://pep8ci.herokuapp.com/) (link): This is a validation tool that was used to validate my python code.
 
* [Techsini](https://techsini.com/multi-mockup/index.php) (link). Used to create the mockup image.
 
* [Font Awesome](https://fontawesome.com/) (link). Was used to add icons for my social media links.
 
* [Pair Fonts](https://pairfonts.com/) (link). I used Pair Fonts to add custom fonts for aesthetic and UX purposes.
 
* [Balsamiq](https://balsamiq.com/) (link). Balsamiq was used to create my wireframe for my design process.
 
* [dbdiagram](https://dbdiagram.io/home) (link). DB diagram was used to create my database schema before I started to code my project.
 
* [Trello](https://trello.com/) (link). Trello was used for creating my board for mapping my user stories in this project.
 
* [Favicon](https://favicon.io/) (link). Favicon was used to create the little icon that is showing in the browser address bar to make the user experience more professional for the website.

* [Stripe](https://stripe.com/) (link). Stripe was used for my checkout functionality in this project so visitors and users can make successful payments at the store.

* [Mailchimp](https://mailchimp.com/) (link). Mailchimp was used for my newsletter.

* [Unsplash](https://unsplash.com/) (link). Unsplash was used for downloading all of the product images/blog images, and the hero image.
 
 
---
## Testing
 
All testing of this project has been documented in a separate file called `TESTING.md` and you can find it [here](TESTING.md) (internal link).
 
### Bugs

#### Bug 1

I noticed that my footer wasn't at the bottom of my watches page, it was among the watches as seen in the screenshot below. You can see the name of AndWatch's between the two images in the middle. The screenshot is taken of another page that hasn't been implemented in the final version.
 
**Screenshot bug:**
 
![Screenshot bug 1](/readme_images/bug-1.png)
 
**Solution Bug 1:**

The solution to this bug was that I had set the height of my products template to a bootstrap class of `min-vh-100` and in my base template I had done the same. I will show a screenshot of the problem down below. So I just made sure I didn't use that bootstrap class anywhere else than in my base template. And in my base template, I changed to just `vh-100`.

![Screenshot bug 1 - problem](/readme_images/bug-1-problem.png)


#### Bug 2

My sorting for products on the all watches page for `"Brand"` (Brand A-Z, Brand Z-A, etc) which I have named `"watch_make"` in my database for products wasn't working and I got an error for `FieldError at /products/` `Cannot resolve keyword 'name' into field.`. My goal was to get the sorting for A - Z or Z - A working properly.

**Error message:**

![Screenshot bug 2 error message](/readme_images/bug-2.png)

**Sorting selector html:**

![Screenshot bug 2 sorting selector html](/readme_images/sorting-selector.png)

**Solution Bug 2:**

After I had tried different methods of tweaking the `JavaScript` of this sorting selector I decided to take some help from the Tutors at Code Institute. I got some amazing help from a guy named `Ed`. After some minutes spent by Ed he discovered that my `JavaScript` function was searching for the underscore to decide what I was trying to do when selecting the A - Z etc, and since I had named the watchmakers of the brand in my database model to watch_make instead of something like the brand the `JavaScript` function was trying to execute at the first underscore in `watch_make_asc` & `watch_make_desc` when it was supposed to execute at the underscore before `asc` or `desc` so, therefore, I got that error. `Ed` was kind to help me rewrite the `JavaScript` function to execute at the correct underscore. I will show two images below with my old function and the new one that `Ed` helped me with.

**Wrong JavaScript Function:**

![Screenshot bug 2 wrong javascript function](/readme_images/bug-2-wrong-js.png)

**Correct JavaScript Function:**

![Screenshot bug 2 correct javascript function](/readme_images/bug-2-correct-js.png)


#### Bug 3

When I was submitting an order at `AndWatch's` development website, I was getting an error for placing an order as a logged-in user, but not as a random user (not logged in). I did not get a confirmation email when submitting the order on the live Heroku website either.

**Screenshot error:**

![Screenshot of error message in terminal](/readme_images/bug-error-1.png)

![Screenshot of error message in terminal](/readme_images/bug-error-2.png)

**Solution bug 3:**

The problem was related to my `webhook_handler.py` file for saving the user's profile information again in the checkout process, a lot of thanks to `Alex` at the tutor support for helping me find this issue. I used `commas` to separate the lines and backslash for some reason when I was setting up this function. I removed these and made sure that everything looked good, saved, added to git, and pushed. The first problem was solved. The other problem with me not getting any confirmation emails when submitting an order at the live Heroku website was related to me not adding a `webhook endpoint` in Stripe for my deployed website at Heroku. I added this and then this problem was also solved. I will provide images of the first problem, but for the second problem, I can't share any images of them since I would expose my Stripe account for webhooks then.

**Problem regarding webhook_handler.py file:**

![Screenshot of error pointing to webhook_handler.py file](/readme_images/bug-3-solution.png)

![Screenshot of problem in webhook_handler.py file](/readme_images/bug-3-solution2.png)

#### Bug 4

**Problem:**

I could not add the `humanize` intcomma to all prices of the website like for `pop-up bag total` and `bag total and grand total in bag view` without getting an error for 
`invalid filter "intcomma"`.

![Screenshot of invalid filter: intcomma](/readme_images/bug-4.png)

**Solution bug 4:**

I added `{% load humanize %}` at the top of my `bag-total.html` template, and the error was fixed now I got intcomma on `bag total and grand total` as well. At first, I had just tried to have the `{% load humanize %}` in my `bag.html` template but I got this error for that too so then I tried this method and it worked.

 
### Unfixed Bugs

**Bug 1:**

Since I have set my background color to all black and for my navigation bar, my `"Hamburger menu"` for smaller screen devices wasn't showing. I tried to style the CSS for the `CSS` for my `navbar-toggler` and `navbar-toggler-icon` to set the correct value so the `navbar-toggler` would have a white background color and the `navbar-toggler-icon` would have a black color but this didn't work out for me. So I decided to add a `Font awesome` icon of that exact look to go around this problem and then set the `margin-top` to 4px so it would be centered in the white `navbar-toggler`. I have checked and it looks good on smaller screen devices with the chrome developer tool set to responsive, so remember that I haven't had access to test this on real devices.

**Bug 2:**

When editing a blog post, if there is an image added to the blog post before (before starting to edit). The admin/store owner can't use the `clear` box shown in the image shown below to delete the existing image. But if the admin/store owner intends to do so they can just click `Add image` and the new image will replace the old one when they hit `save`.

![Screenshot of clear box not working while edit blog post](/readme_images/unfixed-bug.png) 

 
---
## Credits
 
#### Media
 
All images for this project were taken from [Unsplash](https://unsplash.com/) (link).
 
#### Inspiration for this project
 
[Code Institute](https://codeinstitute.net/) (link) - I took inspiration to this project from the `Code Institute` walkthrough videos of `Boutique Ado`.

#### Add newsletter - Code Institute 
 
[Code Institute](https://codeinstitute.net/) (link) - I used this guide to implement the functionality of `Mailchimp` to my newsletter, I used `Mailchimp` embedded HTML form.

#### Tutors

* `Ed` - For helping me with my sorting selector JavaScript function.
* `Alex and Ed` - For helping me get my webhook_handler.py to work correctly.
  
#### Help from Stack Overflow

I used this [post](https://stackoverflow.com/questions/346467/format-numbers-in-django-templates) (link) for adding a `floatformat:2|intcomma` with Django [humanize](https://docs.djangoproject.com/en/4.1/ref/contrib/humanize/) (link) added to the relevant templates where I wanted to use `intcomma` on prices to get the human way of writing prices in the correct way.
Like `$30,000.00` instead of `30000.00`. 
 
 
---
## Deployment
 
**GitHub:**
 
I frequently used `commit` throughout the whole project, this is the command used in the terminal:
 
* `git add .` (This command is used for adding files to the staging area before committing).
* `git commit -m “commit message here..”` (This is used to label the commit changes made to the local repository).
* `git push` (This command is used to push all changes to the GitHub repository).
 
This is all done to prevent any `data` loss in case Gitpod crashes and saves the `data` to GitHub.
 
 
### GitHub & Gitpod
 
For this project, I used the Code Institute Python template that can be found [here](https://github.com/Code-Institute-Org/python-essentials-template) (link).
 
**Steps to create a new repository in Github:**
 
1. Sign in or sign up to [GitHub](https://github.com) (link).
1. When you have done that, you will see `"new"` up in the left corner.
**Like this:**
![Screenshot new repository button github](/readme_images/github.png)
1. Select in the dropdown menu under `Repository template` if you for example would like to use the template provided by `Code Institute` that I did for this project. If you don't see it in the dropdown menu click this [link](https://github.com/Code-Institute-Org/python-essentials-template) (link) to get to the one provided by `Code Institute` and click `Use this template` to the left of the green Gitpod button.
1. When you have done that, give the repository a name. Leave it public if you want anyone on the internet to see your repository (I always do).
1. Click create a repository.
1. **Remember** to use the `commit` commands that I explained above so your hard work doesn't get lost if anything happens to Gitpod.
 
### Forking GitHub Repository
 
Forking a GitHub repository is the process of making a copy of someone else repository and adding your own changes to it without changing the original, the original repository is known
as the "upstream repository". I will explain the process of forking down below:
 
1. Go to the GitHub page that hosts the repository you wish to fork.
1. In the top-right corner of the page there is a button that says `"Fork"`.
1. Click this button.
1. This creates a copy of that repository on your GitHub home page. You can submit and receive changes to your copy by using pull requests and/or syncing with the original upstream repository.
 
These instructions were taken from [Github - Fork a repo](https://docs.github.com/en/get-started/quickstart/fork-a-repo) (link).
 
### Cloning GitHub Repository
 
Cloning a repository involves making a full copy of a repository on your local machine. This allows you to work on the code easier. Changes can be pushed back up to the GitHub site or changes from other sources pulled to your local copy. I will explain how to clone down below:
 
1. Go to the repository page on Github.
1. Above the file list click on the green button that says `"Code"`.
1. You can choose to download a zip file of the repository, unpack it on your local machine, and open it in your IDE.
1. Clone using HTTPS by copying the URL under the HTTPS tab.
1. Open a terminal window, and set the current directory to the one you want to contain the clone from.
1. Type `git clone` and paste the URL copied from the GitHub page.
1. The repository clone will now be created on your machine.
 
These instructions were taken from [Github - cloning a repository](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository) (link).
 
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
* Supply a `KEY` of `PORT` and its value of `8000`. Then click the `"add"` button. Do this with `Cloudinary, Database URL (from Heroku-Postgres) and your secret key`.
* Next step is to add `Buildpacks`, click the `"Add Buildpack"` button.
* The `Heroku Postgress` buildpack need to be added.
* Once the buildpack has been completed, go to the deploy tab, once on the deploy screen, select GitHub as the deployment method and connect your GitHub profile.
* Search for the repository that you wish to deploy to `Heroku` and click `"connect"`.
* Once your repository is connected to Heroku you can choose to either automatically or manually deploy your app. 
* By selecting automatic deploy, Heroku will build a new version of the app each time a change has been made and pushed to the repository on `GitHub`.
* Click on manual deploy to build your App. When complete, click on `View` to open up the live site on `Heroku`. 
* Finished.
 
If the `create app` process at `Heroku` website wouldn't work follow these steps:
* When you want to deploy your project to `Heroku`.
* Type `Heroku login -i` to log in to your existing account (if you have one) in the `Gitpod` terminal.
* Then run the command `Heroku create your_app_name_here` to create a new app (the name has to be unique).
* Now you can see your new project on the `Heroku` dashboard and set the config vars and buildpacks as the steps explained above.

### ElephantSQL

Since `Heroku` now only offers paid plans for their service, the use of `ElephantSQL` exists as a free option for `Heroku Postgress`. For creating an `ElephantSQL` account these are the steps:

**Create an account:**

* Navigate to [ElephantSQL.com](https://www.elephantsql.com/) (link) and click on `Get a managed database today` (green button).
* Then select `Try now for FREE` in the TINY TURTLE database plan.
* Select `Login with GitHub` and authorize ElephantSQL with your selected GitHub account.
* In the Create new team form:
  * Add a team name (your own name is fine)
  * Read and agree to the Terms of Service
  * Select Yes for GDPR
  * Provide your email address
  * Click “Create Team”
* Your account is now `successfully` created.


---
## Support
 
I would like to give an extra `Thank you` to all the kind people I have around me that gave me support in all different ways.
 
* **Code Institute** for their amazing **Tutor** support.
* My mentor [Benjamin Kavanagh](https://github.com/BAK2K3) (link) for being a **Superior** mentor.
* **Google** for always clear things up.
* **Code Institute Slack channel** for always helping out with problems or questions.
* My lovely **Girlfriend** for always supporting and believing in me.
 
### RETURN TO THE [TOP](#portfolio-project-five)