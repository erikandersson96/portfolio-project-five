# Testing
 
During my development for this project each function were tested to work as expected. Each section in this file describes all of the different tests.
 
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
 
* [User Story Testing](#user-story-testing)
 
* [Device Testing](#device-testing)
 
* [Manual Testing](#manual-testing)
  * [Standard Elements](#standard-elements)
  * [Home Page](#home-page)
  * [Recipe Details](#recipe-details)
  * [Add Recipe](#add-recipe)
  * [Authentication](#authentication)
  * [About Modal](#about-modal)
  * [My favorites](#my-favorites)
 
* [Defensive Programming](#defensive-programming)
 
* [Automated Tests](#automated-tests)
 
 
---
## Validation Testing
 
### Python (PEP8) Validation
 
I have tested my python code at [PEP8ci](https://pep8ci.herokuapp.com/) (link), I will show my results below with images and then a short description below each image of my solution. And I have seperated each django file to their respective django application within the project, to demonstrate for you down below.
 
### AndWatch's Main Project App

<details>
<summary>andwatch settings.py</summary>
<br>

**settings.py before:**
<br>

![Screenshot of settings.py before pep8ci](/testing_images/settings.png)
<br>

**settings.py after:**
<br>

![Screenshot of settings.py after pep8ci](/testing_images/settings-finished.png)
<br>

![Screenshot of fix for settings.py line too long](/testing_images/settings-linetoolong-fix.png)
<br>

##### Solution for settings.py

The first test I did as you can see in the first image above, I got some spacing errors that I solved by just adding those spaces. Line too long at 86 I just solved by removing a comment that I had missed to remove and the last error is for not having a blank line at the bottom which I just added. As you can see in the second image I got four line too long so I solved that by adding a parentheses, break the line at the begginning of the parentheses and then add quotation around the string.
</details>

<details>
<summary>andwatch urls.py</summary>

I got no errors found in this file.
</details>

### bag app

<details>
<summary>bag_tools.py</summary>
<br>

I got no errors found in this file.
</details>

<details>
<summary>contexts.py</summary>
<br>

I got no errors found in this file.
</details>

<details>
<summary>test_views.py</summary>
<br>

I got no errors found in this file.
</details>

<details>
<summary>urls.py</summary>
<br>

I got no errors found in this file.
</details>

<details>
<summary>views.py</summary>
<br>

I got no errors found in this file.
</details>
 

### blog app

<details>
<summary>admin.py</summary>
<br>

I got no errors found in this file.
</details>

<details>
<summary>forms.py</summary>
<br>

I got no errors found in this file.
</details>

<details>
<summary>models.py</summary>
<br>

I got no errors found in this file.
</details>

<details>
<summary>urls.py</summary>
<br>

I got no errors found in this file.
</details>

<details>
<summary>views.py</summary>
<br>

I got no errors found in this file.
</details>


### checkout app

<details>
<summary>admin.py</summary>
<br>

I got no errors found in this file.
</details>

<details>
<summary>forms.py</summary>
<br>

I got no errors found in this file.
</details>

<details>
<summary>models.py</summary>
<br>

I got no errors found in this file.
</details>

<details>
<summary>signals.py</summary>
<br>

I got no errors found in this file.
</details>

<details>
<summary>test_views.py</summary>
<br>

I got one error here for no blank line at the end of the file, so I just added that.
</details>

<details>
<summary>urls.py</summary>
<br>

I got no errors found in this file.
</details>

<details>
<summary>views.py</summary>
<br>

I got one error for whitespace at line 11, so I just got rid of that.
</details>

<details>
<summary>webhook_handler.py</summary>
<br>

I got no errors found in this file.
</details>

<details>
<summary>webhooks.py</summary>
<br>

I got one error at line 45 for line too long, I tried to solve this with a backslash and start at a new line but I did not get it to work. So I tested by adding a parentheses around it and then break the line at the beginning of the parentheses and that solved it.
</details>


### home app

<details>
<summary>test_views.py</summary>
<br>

I got no errors found in this file.
</details>

<details>
<summary>urls.py</summary>
<br>

I got no errors found in this file.
</details>

<details>
<summary>views.py</summary>
<br>

I got no errors found in this file.
</details>


### newsletter app

<details>
<summary>urls.py</summary>
<br>

I got no errors found in this file.
</details>

<details>
<summary>views.py</summary>
<br>

I got no errors found in this file.
</details>


### products app

<details>
<summary>admin.py</summary>
<br>

I got no errors found in this file.
</details>

<details>
<summary>forms.py</summary>
<br>

I got no errors found in this file.
</details>

<details>
<summary>models.py</summary>
<br>

I got no errors found in this file.
</details>

<details>
<summary>test_views.py</summary>
<br>

I got no errors found in this file.
</details>

<details>
<summary>urls.py</summary>
<br>

I got no errors found in this file.
</details>

<details>
<summary>views.py</summary>
<br>

I got no errors found in this file.
</details>

<details>
<summary>widgets.py</summary>
<br>

I got one error in this file for line too long at line 9, so I fixed that by adding a parentheses around and then brake the line at the beginning of the parentheses.
</details>


### profiles app

<details>
<summary>forms.py</summary>
<br>

I got no errors found in this file.
</details>

<details>
<summary>models.py</summary>
<br>

I got no errors found in this file.
</details>

<details>
<summary>test_views.py</summary>
<br>

I got no errors found in this file. 
</details>

<details>
<summary>urls.py</summary>
<br>

I got no errors found in this file.
</details>

<details>
<summary>views.py</summary>
<br>

I got no errors found in this file.
</details>

 
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
I will list all apps that has some sort of JavaScript in it, whether it is a JavaScript file or JavaScript at the bottom of a html template.

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
 
I have tested the website with `Chrome lighthouse dev tool` to test the website `performance`. I have tested this in a `incognito` window for better performance while testing. I got an average result of 95,5 for desktop and 86,75 for mobile devices. When I mean average I add up all numbers for `Performance, Accessibillity, Best Practices, SEO` and divide by 4. 
 
**Desktop:**
 
![Screenshot of lighthouse devtool on desktop](/testing_images/lighthouse-desktop.png)
 
**Mobile:**
 
![Screenshot of lighthouse devtool on mobile](/testing_images/lighthouse-mobile.png)
 
 
### Wave
 
`AndWatch's` website has been tested at [WAVE Web Accessibility Evaluation Tool](https://wave.webaim.org/) (link). `WAVE` is a suite of evaluation tools that helps authors make their web content more accessible to individuals with disabilities (Taken from Wave website). I have tested each page individually, and I will demonstrate the results below.

Worth mentioning is I got errors for missing form label but since my choice of design of this website I included a placeholder, so the errors for this will still exist.

<details>
<summary>Home page</summary>
<br>
 
![Screenshot of contrast error and alerts](/testing_images/wave-home.png)
<br>

**Solution WAVE errors and alert:**

I got error for no form label, empty button or no value text, and alert for skipped heading level. Since the design choice of this website was to not use labels on form I included a placeholder instead. I fixed the empty button error with adding aria-label and I fixed the skipped heading level with changing the headings.
</details>

<details>
<summary>Contact page</summary>
<br>

I got one error for heading level skipped, I was using a h5 so I changed that to a h2 and added css for it.
</details>

<details>
<summary>About page</summary>
<br>

I got errors for skipping heading levels, so I fixed this by adding a h2 after the h1 and change all other headings to paragraphs with css styling.
</details>

<details>
<summary>Watch page</summary>
<br>

I got errors for skipped heading levels and missed label on selector. I added the correct order of headings and added a aria-label to my sort selelctor `select` element.
</details>

<details>
<summary>Watch detail page</summary>
<br>

I got one error for no heading where the price is and one error for no label on input. I solved the heading issue by adding a h1, but since I have choosen this design for my website there will not be a label for my quantity input.
</details>

<details>
<summary>Shopping bag page</summary>
<br>

I got errors for skipped heading levels for bag total and grand total, and a empty tabel. I added h2 headings for bag total and grand total, and I removed the empty tabel.
</details>

<details>
<summary>Checkout page</summary>
<br>

I got one error for skipping heading level, one error for missing image alt text, one error for empty heading, and errors for missing label to input and selector. I fixed the skipping heading level by change the page haeding to h1. But for those other errors I wont be able to fix, the missing alt on image, I have an alt but it is created in this way `{{ product.watch_model }}` to reneder the model of the watch in the alt text. The empty heading is for my loading spinner at the bottom, I tried to change this but the way I have designed this website It will be unsolved. And the missing label for input is the same as before on other input fields, I have them pre filled from the form, the same is for my selector.
</details>

<details>
<summary>Checkout success page</summary>
<br>

I got one error for skipping heading level. I solved this by just adding a h1 instead of h2.
</details>

<details>
<summary>Blog page</summary>
<br>

I got 2 errors for skipping heading level, I solved these by adding a h1 instead of h2 and a h2 instead of a h3. And I got contrast errors for edit blog post button, I solved these by changing color to a darker color.
</details>

<details>
<summary>Blog post detail page</summary>
<br>

I got 1 error for skipping heading level, which I solved by adding a h1 for the title. And I got contrast errors for the edit/delete buttons both for the blog post it self but also for the comments. I fixed these by changing the color to a color with less contrast error.
</details>

<details>
<summary>Add comment page</summary>
<br>

I got one error for skipping heading level, which I solved by change the h2 to h1.
</details>

<details>
<summary>Add product page</summary>
<br>

I got 2 errors for skipping heading level, I was using a h2 for the first level and a h6 for the second one. I changed these to h1 and a paragraph instead. I got 1 additional error for my image field selector, missing label. But as I have mentioned before I will not change it since I have designed the website the way I have.
</details>

<details>
<summary>Edit product page</summary>
<br>

I got 2 errors for skipping heading level, I was using a h2 and h6 as on the add product page. So I solved these by adding a h1 and a paragraph.
</details>

<details>
<summary>Add blog post page</summary>
<br>

I got 2 errors for skipping heading level, I was using a h2 and h6 as on the edit product page. So I solved these by adding a h1 and a paragraph.
</details>

<details>
<summary>Edit blog post page</summary>
<br>

I got 2 errors for skipping heading level, I was using a h2 and h6 as on the add blog post page. So I solved these by adding a h1 and a paragraph.
</details>

<details>
<summary>My profile page</summary>
<br>

I got 1 error for skipping heading level, I fixed this one by adding a h1 instead of h2. Then I got errors for missing label on input fields but also on select country, but since these are from a pre filled in form I will not change these since my design for this website is the way it is.
</details>

<details>
<summary>Wish list page</summary>
<br>

I got 2 errors for skipping heading level, I solved these by adding a h1 for the page title and a h2 for the watch title on the product card.
</details>

<details>
<summary>Register page</summary>
<br>

I got no errors for this page.
</details>

<details>
<summary>Login page</summary>
<br>

I got no errors for this page.
</details>

<details>
<summary>Logout page</summary>
<br>

I got no errors for this page.
</details>

<details>
<summary>Newsletter page</summary>
<br>

I got 1 error for skipping heading level, I solved this one by change the h2 for h1 for title on page.
</details>

#### Summary of wave reports

As you can see I mostly got `skipping heading level` as an error, but I also got missing form label for a lot of the input fields and selectors for this website. But as I wrote in some of the pages my design for this website is of my choice, and I have implemented some placeholders but not on everyone. I have inserted forms made in files like `forms.py` for some apps and therfore I haven't been able to fix this issue not at least with my knowledge right now.


---
## User Story Testing
 
Here is my user story testing for this project as a **guest**:
 
1. As a **guest** I would like to be able to register an account using a username, email and password.
 
- I have installed `allauth` to handle all of my authentication, and then I have been styling each file for `Login, Logout, Sign up` so a every guest can `Sign up` for an account or users can `Login/Logout`.
 
1. As a **guest** .
 
- .
 
1. As a **guest** .
 
- .
 
1. As a **guest** .
 
- .
 
1. As a **guest** .
 
- .
 
Here is my user story testing for this project as a **user**:
 
1. As a **user** .
 
- I have made sure by using `allauth` that a user can login to their account.
 
1. As a **user** .
 
- .
 
1. As a **user** .
 
- .
 
1. As a **user** .
 
- .
 
Here is my user story testing for this project as a **admin**:
 
1. As a **admin** .
 
- .
 
1. As a **admin** .
 
- .
 
1. As a **admin** .
 
- .
 
 
---
## Device Testing
 
Something that's worth mentioning is that I've tested the majority of these devices within Chrome dev tool, I have not had physical access to test these devices. I have tested the responsiveness and aesthetics on the following devices and browsers:
 
* Apple
 * iPhone 4
 * iPhone SE
 * iPhone XR
 * iPhone 12 Pro
 * iPhone 6/7/8
 * iPhone 6/7/8 Plus
 * iPad Mini
 
* Android
 * Samsung Galaxy S8+
 * Samsung Galaxy S20 Ultra
 
* Motorola
* Moto G4
 
* Desktops/laptops/monitor
 * MacBook Pro 13"
 * Lenovo 24" monitor
 
* Browsers
 * Chrome
 * Safari
 
 
---
## Manual Testing
 
### Standard Elements
 
I have manualy tested so my most common elements of my website is working correct, such as:
 
* Make sure so my Logo of `AndWatch's` always direct the user back to the home page.
* Test so my navigation links work as expected.
* Test so my social media links in the `footer` works correctly and opens in a new tab.
 
### Home Page
 
I have manualy tested my home page for these elements:
 
* When a user.
* Make sure so.
* Make sure so.
 
### Recipe Details
 
I have manualy tested so these functions and elements works correct:
 
* Make sure so.
* Make sure so.
* Make sure so.
* Make sure that.
 
### Add Recipe
 
I have manualy tested so the elements of this page works correct:
 
* Make sure so.
* Make sure so.
* Make sure.
* Make sure that.
 
### Authentication
 
I have manualy tested so the authentication for each page works correct:
 
* Make sure so the.
* Make sure so the.
* Make sure so the.
 
### About Modal
 
I have manualy tested so the about modal works correct:
 
* Make sure so . 
* Make sure so .
 
### My favorites
 
I have manualy tested so these functions and elements works correct:
 
* Make sure so the.
* Make sure so the.
* Make sure so the.
* Make sure so.
* Make sure so.
 
 
---
## Defensive Programming

 
#### Function based views
 
For my function based views I have been using a tyle decorator of `@login_required` above each function to make sure that users must be logged in before using that function.

#### Class based views

For my class based views I have used `LoginRequiredMixin` to make sure that users must be logged in to perform this function.

#### Other ways

Other than those I have implemented an if statement to check if the user is a super user (admin/store owner) or not, this I have been taken as inspiration from Boutique Ado.

 
---
## Automated Tests 

For this project I have been implementing test cases for views.py to make sure that the view renders the correct page. I haven't done it in all apps or for all views, I am still new to testing and I am not entirely comfortable with it so I haven't been to consistent with always testing before writing html for each template. I got ahead of my self for some of the apps. For me it is still a win since I didn't do any automated tests at all in my fourth project, I will keep learning as I countinue my web development career in the future. 
 
---
## RETURN BACK TO [TOP](#testing)