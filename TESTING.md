# Testing
 
During my development for this project, each function was tested to work as expected. Each section in this file describes all of the different tests.
 
### HINT:
**Remember that all links in this Testing file does not open in a new tab. They open in the same window (I have marked them with "(link)").**
 
 
---
## Table of contents - testing
 
* [Validation Testing](#validation-testing)
  * [Python PEP8](#python-pep8-validation)
  * [HTML Validation](#html-code-validation)
  * [CSS Validation](#css-code-validation)
  * [Lighthouse](#lighthouse)
  * [WAVE](#wave)
  * [Summary WAVE](#summary-of-wave-reports)
 
* [User Story Testing](#user-story-testing)
 
* [Device Testing](#device-testing)
 
* [Manual Testing](#manual-testing)
 
* [Defensive Programming](#defensive-programming)
 
* [Automated Tests](#automated-tests)
 
 
---
## Validation Testing
 
### Python (PEP8) Validation
 
I have tested my python code at [PEP8ci](https://pep8ci.herokuapp.com/) (link), I will show my results below with images and then a short description below each image of my solution. And I have separated each Django file into its respective Django application within the project, to demonstrate for you down below.
 
### AndWatch's Main Project App

**No errors were found in the following file:**

* urls.py

**The following errors were corrected in the following file:**

* settings.py - The first test I did as you can see in the first image, I got some spacing errors that I solved by just adding those spaces. The line was too long at 86 I just solved by removing a comment that I had missed removing and the last error is for not having a blank line at the bottom which I just added. As you can see in the second image I got four lines too long so I solved that by adding parentheses, breaking the line at the beginning of the parentheses, and then adding quotations around the string.

![Screenshot of settings.py before pep8ci](/testing_images/settings.png)

![Screenshot of settings.py after pep8ci](/testing_images/settings-finished.png)

![Screenshot of fix for settings.py line too long](/testing_images/settings-linetoolong-fix.png)


### bag app

**No errors were found in the following files:**

* bag_tools.py
* contexts.py
* test_views.py
* urls.py
* views.py
 

### blog app

**No errors were found in the following files:**

* admin.py
* forms.py 
* models.py
* urls.py
* views.py


### checkout app

**No errors were found in the following files:**

* admin.py
* forms.py
* models.py
* signals.py
* urls.py
* webhook_handler.py

**The following errors were corrected in the following files:**

* test_views.py - I got one error here for no blank line at the end of the file, so I just added that.

* views.py - I got one error for whitespace at line 11, so I just got rid of that.

* webhooks.py - I got one error at line 45 for the line was too long, I tried to solve this with a backslash and start at a new line but I did not get it to work. So I tested by adding parentheses around it and then breaking the line at the beginning of the parentheses and that solved it.


### home app

**No errors were found in the following files:**

* test_views.py
* urls.py
* views.py


### newsletter app

**No errors were found in the following files:**

* urls.py
* views.py


### products app

**No errors were found in the following files:**

* admin.py
* forms.py
* models.py
* test_views.py
* urls.py
* views.py

**The following errors were corrected in the following file:**

* widgets.py - I got one error in this file for the line too long at line 9, so I fixed that by adding parentheses around and then brake the line at the beginning of the parentheses.


### profiles app

**No errors were found in the following files:**

* forms.py
* models.py
* test_views.py
* urls.py 
* views.py

 
---
### HTML Code Validation
 
I tested my HTML code for this project at [W3C HTML Validator](https://validator.w3.org/) (link).
 
#### Error
 
1. Element `li` not allowed as child of element `nav` in this context.
1. Element `li` not allowed as child of element `nav` in this context.
1. Duplicate ID `user-options`.
1. The first occurrence of ID `user-options` was here.
1. Element `li` not allowed as child of element `nav` in this context.
1. Attribute `alt` not allowed on element `div` at this point.
1. Stray start tag `script`.
1. Cannot recover after last error. Any further errors will be ignored.

![Screenshot of error html validation](/testing_images/html-error-1.png)

![Screenshot of error html validation](/testing_images/html-error-2.png)

#### Warning

1. The `type` attribute is unnecessary for JavaScript resources.

![Screenshot of warning html validation](/testing_images/html-warning.png)
 
#### Solution

**Errors:**

1. I got rid of `li` not allowed as child of element `nav` by adding a `ul` around the html code in my `mobile-top-header.html` template.
1. I got rid of `li` not allowed as child of element `nav` by adding a `ul` around the html code in my `mobile-top-header.html` template.
1. I got rid of Duplicate ID `user-options` by removing my `id="user-options"` in `mobile-top-header.html` since that html code already was a part of my base html which had an `id="user-options"` in it, therfore I got this error to start with.
1. This one was solved when the above error was solved with Duplicate ID `user-options`.
1. I got rid of `li` not allowed as child of element `nav` by adding a `ul` around the html code in my `mobile-top-header.html` template.
1. I got rid of Attribute `alt` not allowed on element `div`, after removing a `alt` that I had added to my div for my hero image in my `index.html` template.
1. I got rid of Stray start tag `script`, after realizing that I had added my `postload_js` in `base.html` template outside my end tags for `body and html`, so I just fixed that.
1. This one disappeared when the above one was fixed with Stray start tag `script`.

**Warning:**

1. I got rid of this one after realizing that the `type` attribute is unnecessary for JavaScript resources.
 
#### Finished result

![Screenshot of no error html validation](/testing_images/html-ok.png)
 
You can take a look at my `approved` HTML validation by clicking this link [here](https://validator.w3.org/nu/?doc=https%3A%2F%2Fandwatchs-2022.herokuapp.com%2F) (link).
 
 
### CSS Code Validation
 
I tested my CSS for this project at [W3C Jigsaw CSS Validator](https://jigsaw.w3.org/css-validator/validator.html.en) (link).

#### I got no CSS errors
 
![Screenshot of css approved validation](/testing_images/css-ok.png)

You can take a look at my `approved` CSS validation by clicking this link [here](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fandwatchs-2022.herokuapp.com%2F&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en) (link).


### JSHint Javascript validation

I have tested all javascript in all apps in this project with [JSHint](https://jshint.com/) (link).
I will list all apps that have some sort of JavaScript in them, whether it is a JavaScript file or JavaScript at the bottom of an HTML template.

#### bag app

I only got warning for missing semicolons.

#### blog app

I only got warning for missing semicolons.

#### checkout app

I only got warning for missing semicolons.

#### newsletter app

I got these warnings when I was testing my JavaScript inside my `newsletter.html` template:

![Screenshot of newsletter template javascript](/testing_images/newsletter-js.png)

But since I got this JavaScript directly from `Mailchimp` I don't know how I should get rid of these warnings so I will leave it like that.

#### products app

I only got warning for missing semicolons.

#### profiles app

I only got warning for one unnecessary semicolon.

#### base.html 

I got no warnings here.


### Lighthouse
 
I have tested the website with `The chrome lighthouse dev tool` to test the website's `performance`. I have tested this in an `incognito` window for better performance while testing. I got an average result of 95,5 for desktops and 86,75 for mobile devices. When I mean average I add up all numbers for `Performance, Accessibility, Best Practices, SEO` and divide by 4. 
 
**Desktop:**
 
![Screenshot of lighthouse devtool on desktop](/testing_images/lighthouse-desktop.png)
 
**Mobile:**
 
![Screenshot of lighthouse devtool on mobile](/testing_images/lighthouse-mobile.png)
 
 
### Wave
 
`AndWatch's` website has been tested at [WAVE Web Accessibility Evaluation Tool](https://wave.webaim.org/) (link). `WAVE` is a suite of evaluation tools that helps authors make their web content more accessible to individuals with disabilities (Taken from the Wave website). I have tested each page individually, and I will demonstrate the results below.

Worth mentioning is I got errors for missing form labels but since my choice of design for this website I included a placeholder, so the errors for this will still exist.

<details>
<summary>Home page</summary>
<br>
 
![Screenshot of contrast error and alerts](/testing_images/wave-home.png)
<br>

**Solution WAVE errors and alert:**

I got errors for no form label, empty button, or no value text, and an alert for skipped heading level. Since the design choice of this website was to not use labels on the form I included a placeholder instead. I fixed the empty button error with adding an aria-label and I fixed the skipped heading level by changing the headings.
</details>

<details>
<summary>Contact page</summary>
<br>

I got one error for heading level skipped, I was using an h5 so I changed that to an h2 and added CSS for it.
</details>

<details>
<summary>About page</summary>
<br>

I got errors for skipping heading levels, so I fixed this by adding an h2 after the h1 and changing all other headings to paragraphs with CSS styling.
</details>

<details>
<summary>Watch page</summary>
<br>

I got errors for skipped heading levels and missed labels on the selector. I added the correct order of headings and added a aria-label to my sort selector `select` element.
</details>

<details>
<summary>Watch detail page</summary>
<br>

I got one error for no heading where the price is and one error for no label on input. I solved the heading issue by adding an h1, but since I have chosen this design for my website there will not be a label for my quantity input.
</details>

<details>
<summary>Shopping bag page</summary>
<br>

I got errors for skipped heading levels for bag total and grand total. I added h2 headings for bag total and grand total, and I removed the empty table.I got an error for using a empty table header. The empty table header is because I wanted the tables for `Product Info, Price, Quantity, and Subtotal` to be moved to the rigth to be in line with each content for these so I will leave this empty table header to get my design correct.
</details>

<details>
<summary>Checkout page</summary>
<br>

I got one error for skipping the heading level, one error for missing image alt text, one error for an empty heading, and errors for a missing label to input and selector. I fixed the skipping heading level by changing the page heading to h1. But for those other errors I won't be able to fix, the missing alt on the image, I have an alt but it is created in this way `{{ product.watch_model }}` to reenter the model of the watch in the alt text. The empty heading is for my loading spinner at the bottom, I tried to change this but the way I have designed this website It will be unsolved. And the missing label for input is the same as before on other input fields, I have them pre-filled from the form, and the same is for my selector.
</details>

<details>
<summary>Checkout success page</summary>
<br>

I got one error for skipping the heading level. I solved this by just adding an h1 instead of h2.
</details>

<details>
<summary>Blog page</summary>
<br>

I got 2 errors for skipping the heading level, I solved these by adding an h1 instead of an h2 and an h2 instead of an h3. And I got contrast errors for the edit blog post button, I solved these by changing the color to a darker color.
</details>

<details>
<summary>Blog post detail page</summary>
<br>

I got 1 error for skipping the heading level, which I solved by adding an h1 for the title. And I got contrast errors for the edit/delete buttons both for the blog post itself and also for the comments. I fixed these by changing the color to color with less contrast error.
</details>

<details>
<summary>Add comment page</summary>
<br>

I got one error for skipping the heading level, which I solved by changing the h2 to h1.
</details>

<details>
<summary>Add product page</summary>
<br>

I got 2 errors for skipping the heading level, I was using an h2 for the first level and an h6 for the second one. I changed these to h1 and a paragraph instead. I got 1 additional error for my image field selector, missing label. But as I have mentioned before I will not change it since I have designed the website the way I have.
</details>

<details>
<summary>Edit product page</summary>
<br>

I got 2 errors for skipping the heading level, I was using an h2 and h6 as on the add product page. So I solved these by adding an h1 and a paragraph.
</details>

<details>
<summary>Add blog post page</summary>
<br>

I got 2 errors for skipping the heading level, I was using an h2 and h6 on the edit product page. So I solved these by adding an h1 and a paragraph.
</details>

<details>
<summary>Edit blog post page</summary>
<br>

I got 2 errors for skipping the heading level, I was using an h2 and h6 as on the add blog post page. So I solved these by adding an h1 and a paragraph.
</details>

<details>
<summary>My profile page</summary>
<br>

I got 1 error for skipping the heading level, I fixed this one by adding an h1 instead of an h2. Then I got errors for the missing label on input fields and also on the select countries, but since these are from a pre-filled form I will not change these since I have designed my website like this.
</details>

<details>
<summary>Wish list page</summary>
<br>

I got 2 errors for skipping the heading level, I solved these by adding an h1 for the page title and an h2 for the watch title on the product card.
</details>

<details>
<summary>Newsletter page</summary>
<br>

I got 1 error for skipping the heading level, I solved this one by changing the h2 for h1 for the title on the page.
</details>

**No errors were found on the following pages:**

* Register page
* Login page
* Logout page

#### Summary of wave reports

As you can see I mostly got `skipping heading level` as an error, but I also got missing form labels for a lot of the input fields and selectors for this website. But as I wrote in some of the pages my design for this website is of my choice, and I have implemented some placeholders but not on everyone. I have inserted forms made in files like `forms.py` for some apps and therefore I haven't been able to fix this issue not at least with my knowledge right now.


---
## User Story Testing

**Here is my user story testing for this project as a guest/user (users can do all that guests can):**
 
* As a **guest** I would like to be able to register an account using a username, email, and password.
 
  * I have installed `allauth` to handle all of my authentications, and then I have been styling each file for `Login, Logout, Sign up` so every guest can `Sign up` for an account or users can `Login/Logout`.
 
* As a **guest** I would like to learn more about the website.
 
  * I have created an `about us` page where all users can read more about this website.
 
* As a **guest** visit the website's social platforms.
 
  * I have added the social media platforms to the footer.
 
* As a **guest** visit the website's FaceBook page.
 
  * I have linked to the FaceBook page in my footer and on our contact page.
 
* As a **guest** I want to be able to view all of the watches available.
 
  * A guest and user can see all of our watches listed on the `All watches` page.

* As a **guest** I would like to watch the details of the watches.
 
  * A guest and user can see all of the individual watch details by clicking on the watch image.

* As a **guest** I want to be able to purchase watches using my credit/debit card.
 
  * Both a guest and a user can purchase watches with the card of their choice.

* As a **guest** I would like to view the blog, all blog posts, and comments.
 
  * A guest and user can see all of our blog posts by clicking on the blog and see the blog post details by clicking on the image. Comments are shown under if there are any, but guests can't add comments, then they would have to login or register first.
 
**Here is my user story testing for this project as a user:**
 
* As a **user** I want to login to my account.
 
  * I have made sure by using `allauth` that a user can log in to their account.
 
* As a **user** I would like to see the order history, and change shipping/billing information.
 
  * I have created a `My profile` page where users can see their shipping/billing information and change it if they wish to. I have also included the order history with the ability to click on a specific order from the past to look at it again.
 
* As a **user** I would like to see blog posts and comment on them.
 
  * I have created the blog so users can add comments but only admin/store owners can delete them.
 
* As a **user** I would like to add/remove watches to my wish list.
 
  * I have created the website so users can add and remove watches to their wish lists.
 
**Here is my user story testing for this project as an admin:**
 
* As an **admin** I would like to see the entire list of watches available.
 
  * Admins have the same access as guests and users but even more so that admins can see all watches.
 
* As an **admin** I would like to be able to add watches to the store.
 
  * Admins can add watches to the store via `Product Management`.
 
* As an **admin** I would like to edit watches that are available.
 
  * Admins can edit all watches that are listed for sale.

* As an **admin** I would like to be able to delete watches.
 
  * Admins can delete watches if they would like to, by `delete product`.

* As an **admin** I would like to be able to add and edit blog posts.
 
  * Admin can add blog posts as well edit available blog posts, via `Blog management` or `edit post`.

* As an **admin** I would like to be able to delete blog posts.
 
  * Admin can delete blog posts if they would like to, by `delete post`.

* As an **admin** I would like to be able to delete blog post comments.
 
  * Admin can delete comments on blog posts, if they aren't relevant or using good language to each other, by `delete comment`.
 
 
---
## Device Testing
 
Something that's worth mentioning is that I've tested the majority of these devices within the Chrome dev tool, but I have not had physical access to test these devices. I have tested the responsiveness and aesthetics on the following devices and browsers:
 
* Apple
  * iPhone SE
  * iPhone XR
  * iPhone 12 Pro
  * iPhone 6/7/8
  * iPhone 6/7/8 Plus
  * iPad
 
* Android
  * Samsung Galaxy S8+
  * Samsung Galaxy S20 Ultra
 
* Moto G4
 
* Desktops/laptops/monitor
  * MacBook Pro 13"
  * Lenovo 24" monitor
 
* Browsers
  * Chrome
 
 
---
## Manual Testing
 
I have manually tested all of my website's functions and features in the browser, so it works as expected. I have used `Google chrome` the whole time, on a `MacBook pro-2016`.
 
 
---
## Defensive Programming

 
#### Function-based views
 
For my function based views I have been using a tyle decorator of `@login_required` above each function to make sure that users must be logged in before using that function.

#### Class-based views

For my class-based views, I have used `LoginRequiredMixin` to make sure that users must be logged in to perform this function.

#### Other ways

Other than those I have implemented an if statement to check if the user is a super user (admin/store owner) or not, I have been taken this as inspiration from Boutique Ado.

 
---
## Automated Tests 

For this project, I have been implementing test cases for views.py to make sure that the view renders the correct page. I haven't done it in all apps or for all views, I am still new to testing and I am not entirely comfortable with it so I haven't been too consistent with always testing before writing HTML for each template. I got ahead of myself with some of the apps. For me it is still a win since I didn't do any automated tests at all in my fourth project, I will keep learning as I continue my web development career in the future. 
 
---
## RETURN BACK TO [TOP](#testing)