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

**settings.py what's left:**
<br>

![Screenshot of settings.py whats left](/testing_images/settings-left.png)
<br>

##### Solution for settings.py

The first test I did as you can see in the first image above, I got some spacing errors that I solved by just adding those spaces. Line too long at 86 I just solved by removing a comment that I had missed to remove and the last error is for not having a blank line at the bottom which I just added. As you can see in the second image and the last one I have left four line too long errors, but I don't know a way of getting rid of them so I will leave them as that.
</details>

<details>
<summary>andwatch urls.py</summary>

I got no errors for this file when testing.
</details>

### bag app

<details>
<summary>contexts.py</summary>
<br>

I got no errors in this file.
</details>

<details>
<summary>test_views.py</summary>
<br>

I got no erros in this file.
</details>

<details>
<summary>urls.py</summary>
<br>

I got no errors in this file.
</details>

<details>
<summary>views.py</summary>
<br>

I got no errors in this file.
</details>
 

### blog app

<details>
<summary>admin.py</summary>
<br>

I got no errors in this file.
</details>

<details>
<summary>forms.py</summary>
<br>

I got no errors in this file.
</details>

<details>
<summary>models.py</summary>
<br>

I got no errors in this file.
</details>

<details>
<summary>urls.py</summary>
<br>

I got no errors in this file.
</details>

<details>
<summary>views.py</summary>
<br>

I got no errors in this file.
</details>


### checkout app

<details>
<summary>admin.py</summary>
<br>

I got no errors in this file.
</details>

<details>
<summary>forms.py</summary>
<br>

I got no errors in this file.
</details>

<details>
<summary>models.py</summary>
<br>

I got no errors in this file.
</details>

<details>
<summary>signals.py</summary>
<br>

I got no errors in this file.
</details>

<details>
<summary>test_views.py</summary>
<br>

**settings.py before:**
<br>

**settings.py before:**
<br>

**settings.py before:**
<br>

**settings.py before:**
<br>

</details>

<details>
<summary>urls.py</summary>
<br>

**settings.py before:**
<br>

**settings.py before:**
<br>

**settings.py before:**
<br>

**settings.py before:**
<br>

</details>

<details>
<summary>views.py</summary>
<br>

**settings.py before:**
<br>

**settings.py before:**
<br>

**settings.py before:**
<br>

**settings.py before:**
<br>

</details>

<details>
<summary>webhook_handler.py</summary>
<br>

**settings.py before:**
<br>

**settings.py before:**
<br>

**settings.py before:**
<br>

**settings.py before:**
<br>

</details>

<details>
<summary>webhooks.py</summary>
<br>

**settings.py before:**
<br>

**settings.py before:**
<br>

**settings.py before:**
<br>

**settings.py before:**
<br>

</details>


### home app

<details>
<summary>test_views.py</summary>
<br>

**settings.py before:**
<br>

**settings.py before:**
<br>

**settings.py before:**
<br>

**settings.py before:**
<br>

</details>

<details>
<summary>urls.py</summary>
<br>

**settings.py before:**
<br>

**settings.py before:**
<br>

**settings.py before:**
<br>

**settings.py before:**
<br>

</details>

<details>
<summary>views.py</summary>
<br>

**settings.py before:**
<br>

**settings.py before:**
<br>

**settings.py before:**
<br>

**settings.py before:**
<br>

</details>


### newsletter app

<details>
<summary>urls.py</summary>
<br>

**settings.py before:**
<br>

**settings.py before:**
<br>

**settings.py before:**
<br>

**settings.py before:**
<br>

</details>

<details>
<summary>views.py</summary>
<br>

**settings.py before:**
<br>

**settings.py before:**
<br>

**settings.py before:**
<br>

**settings.py before:**
<br>

</details>


### products app

<details>
<summary>admin.py</summary>
<br>

**settings.py before:**
<br>

**settings.py before:**
<br>

**settings.py before:**
<br>

**settings.py before:**
<br>

</details>

<details>
<summary>forms.py</summary>
<br>

**settings.py before:**
<br>

**settings.py before:**
<br>

**settings.py before:**
<br>

**settings.py before:**
<br>

</details>

<details>
<summary>models.py</summary>
<br>

**settings.py before:**
<br>

**settings.py before:**
<br>

**settings.py before:**
<br>

**settings.py before:**
<br>

</details>

<details>
<summary>test_views.py</summary>
<br>

**settings.py before:**
<br>

**settings.py before:**
<br>

**settings.py before:**
<br>

**settings.py before:**
<br>

</details>

<details>
<summary>urls.py</summary>
<br>

**settings.py before:**
<br>

**settings.py before:**
<br>

**settings.py before:**
<br>

**settings.py before:**
<br>

</details>

<details>
<summary>views.py</summary>
<br>

**settings.py before:**
<br>

**settings.py before:**
<br>

**settings.py before:**
<br>

**settings.py before:**
<br>

</details>

<details>
<summary>widgets.py</summary>
<br>

**settings.py before:**
<br>

**settings.py before:**
<br>

**settings.py before:**
<br>

**settings.py before:**
<br>

</details>


### profiles app

<details>
<summary>forms.py</summary>
<br>

**settings.py before:**
<br>

**settings.py before:**
<br>

**settings.py before:**
<br>

**settings.py before:**
<br>

</details>

<details>
<summary>models.py</summary>
<br>

**settings.py before:**
<br>

**settings.py before:**
<br>

**settings.py before:**
<br>

**settings.py before:**
<br>

</details>

<details>
<summary>test_views.py</summary>
<br>

**settings.py before:**
<br>

**settings.py before:**
<br>

**settings.py before:**
<br>

**settings.py before:**
<br>

</details>

<details>
<summary>urls.py</summary>
<br>

**settings.py before:**
<br>

**settings.py before:**
<br>

**settings.py before:**
<br>

**settings.py before:**
<br>

</details>

<details>
<summary>views.py</summary>
<br>

**settings.py before:**
<br>

**settings.py before:**
<br>

**settings.py before:**
<br>

**settings.py before:**
<br>

</details>

 
---
### HTML Code Validation
 
When testing my markup HTML code at [W3C HTML Validator](https://validator.w3.org/) (link)
 
**Error:**
 
I had missed to erase a `"closing i element (</i>)"`, for my `What To Eat` logo at the top of the website.
 
**Solution:**
 

 
**After I applied the HTML solution:**
 
Now you can take a look at my `approved` HTML validation by clicking this link [here]() (link).
 
 
### CSS Code Validation
 
[W3C Jigsaw CSS Validator](https://jigsaw.w3.org/css-validator/validator.html.en) (link), 
 
**First wrong attempt with errors:**
 
![Screenshot of css wrong attempt]()
 
**The correct attempt with no errors:**
 
Now you can take a look at my `approved` CSS validation down below:
 
![Screenshot of css approved validation]()
 
 
### Lighthouse
 
I have tested the website with `Chrome lighthouse dev tool` to test the website `performance`. I have tested this in a `incognito` window for better performance while testing. I got an average result of  for desktop and  for mobile devices.
 
**Desktop:**
 
![Screenshot of lighthouse devtool on desktop]()
 
**Mobile:**
 
![Screenshot of lighthouse devtool on mobile]()
 
 
### Wave
 
`AndWatch's` website has been tested at [WAVE Web Accessibility Evaluation Tool](https://wave.webaim.org/) (link). `WAVE` is a suite of evaluation tools that helps authors make their web content more accessible to individuals with disabilities (Taken from Wave website). And I got `` contrast errors and `` alert for `` for the start page like demonstrated in the image below:
 
**WAVE errors and alert:**
 
![Screenshot of contrast error and alerts]()
 
**Solution WAVE errors and alert:**
 
You can look at the approved result [here]() (link).
 
 
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

 
**Here are some screenshots of my function based views in views.py for my recipes app:**
 
**Add recipe:**
 
![Screenshot ]()
 
**Edit recipe:**
 
![Screenshot ]()
 
**Delete recipe:**
 
![Screenshot ]()
 
**Here are a screenshot of my function based views in views.py for my profiles app:**
 
![Screenshot ]()
 
 
---
## Automated Tests 
 
 
---
## RETURN BACK TO [TOP](#testing)