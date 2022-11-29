# Dark Knight Reads

# INSERT IMAGE OF RESPONSIVE WEBSITE HERE

Dark Knight Reads is an online graphic novel store.

It is aim at the graphic novel fan regardless of the their publishing allegiance, as they have both DC and Marvel in the store.

As well as the big two publishers they also sell voels from the smaller publishers. These title have a cult following of their own and are enjoyed around the world.

## Table of contents

- [UX](#UX)
    - [Business goals](#Business-goals)
    - [User goals](#User-goals)
    - [Wireframes layout](#Wireframes-layout)
    - [Website pallette](#Website-pallette)
- [Features](#Features)
- [Technology](#Technology)
- [Testing](#Testing)
    - [Funcionality testing](#Functionality-testing)
    - [Compatability testing](#Compatability-testing)
    - [Code validation](#Code-validation)
    - [Issues found during testing](#Issues-found-during-testing)
    - [Performance testing](#Performance-testing)
- [Deployment](#Deployment)
- [Credits](#Credits)
- [Screenshots](#Screenshots)

## UX

### Business goals

The aim of the site is to allow users to browse the store with ease in order to pick out the titles they wish to buy.

The site allows users to filter the novels in the store by categories, including publisher, some of the main heros as well as by price. The users also have the ability to search the store by key words of their choosing.

Users are also able to create a userprofile which, should they choose, gives them the ability to pick an alter-ego which customises their user experiece (a little bit).

The sites superusers have some CRUD functionality in order to maintain the store, they have the ability to add / edit and remove ites from the store.

### User goals

User can either enter the store with a title in mind or just to browse and see whats available, either way they will find many titles that appeal to them.

### Wireframes layout

As part of the design process, I simplly planned the layout using a whiteboard and a pen - I did alot of the planning while commuting.

# INSERT IMAGES OF WHITE BOARD PAGE LAYOUTS HERE

<img src="static/images/Wireframes.jpg" alt="Wireframe layout images">

### Website pallette

The pallet was driven by Batmans costume colors. Therefore the site has a dark and edgy feel, while also including a touch of fun - with the font choice.

- Background color: #000 Which is black
- Font color: #d7e81e Which is a slightly darker yellow than the standard yellow.
- Font choice: Bangers for the titles, Oswald for the body text

## Features

The site has 6 main pages that users will navigate through. These pages are;

- Landing page

- Product list page

- Product detail page

- Basket page

- Checkout page

- User profile page

As well as the normal login, logout, signin pages.

### Existing Features

- Navigation Bar

    - Navigation bar is presented in the same format on all pages to avoid any confusion when navigating the site.
    
    - Featured on all pages within the site to allow navigation from any page to any other page as the site title, search and navbar sections stay visible on each page.

- Social media links

    - These, like the navbar, are present on all pages and link to the sites social media pages. The links open in a new tab.

- Mailchimp newsletter sign up

    - There is a section at the  bottom of each page that allows users to sign up for  a newsletter subscription via MailChimps embeded sign up panel.

# INSERT IMAGE OF LANDING PAGE HERE

<img src="media/Landing-Page.jpg" alt="The landing page">

- The landing page image banner

    - This landing page banner provides the user with a snap shot of the three main pages within the site.

    - The text within the image is clickable and navigates to the text stated destination.

<img src="static/images/Banner-Link-Text.jpg" alt="Banner text that acts as a link on the site" style="height: 100px;">

The above image shows the banner text that can be clicked - in this case it would take the user to the cafe page.

- The landing page trail message

    - This line of text either indicates that the trails are open or gives the user a message stating how mnay hours until the trails open again.

<img src="static/images/Trail-Status.jpg" alt="A message showing the trails are open" style="height: 65px;">

- Landing page 'About' section

    - This section gives the user some basic information about the Black Mountain MTB trails.

    - It also provides the ability, via links in the text, to navigate to the trails page, the signup page, login page and the Cafe page.

    - There is also an image set to the right of the text to break up the text section and continue to stimulate the user.

<img src="static/images/Trails-Page.jpg" alt="The trails page">

- The Trails page

    - This page is the main hub of the site. It begins by showing 2 large images from the trail as well as a small map image.

    - There is some key information about the trail, such as its name and difficulty. Each trail name is a link to the article page designed for that trail.

    - There is then the article which gives further information about the trail.

    - There are further trail images, information and articles below for the user to pick the trail they wish to read about.

<img src="static/images/Trail-Article-Page.jpg" alt="The trails article page">

- The trail articles

    - These pages load the trail information from the database and present it to the user so they can read the detail, apply likes and comment on the articles.

    - Similar to the trails page these specific trail pages begin with the name and images.

    - There is then the article detail, which is written and posted by the site superusers, via the admin page. followed by the existing comments section.

    - If the user has signed up for an account they also have the ability to comment and like articles, these sections are below the article section.

    - As part of the commenting process users can indicate how long they have been riding for, this gives riders with a similar level of experience a bench mark to judge the comments by.

    - Once posted, the user comments are then passed to the admin (superuser) for authorisation and posting to the site.

<img src="static/images/The-Cafe-Page.jpg" alt="The Cafe page">

- The cafe page

    - This gives the user a brief overview of the cafe facilities and some of the item that can be found there.

    - There is cake, lots of cake.

<img src="static/images/Gallery-Page.jpg" alt="The Gallery page">

- The gallery page

    - This shows some of the images that have been taken of riders riding the trails.

    - The images are positioned in a grid system where there are large images positioned next to smaller images.

    - The idea is to inspire riders to come and rider the trails.

- User accounts

    - Users can create there own accounts in order to unlock other features on the site, including commenting on articles and liking posts.

<img src="static/images/Sign-Up-Page.jpg" alt="Account signup page">

- Account signup

    - This is a free account and the users simply need to give their desired username, password - this is optional and set a password.

<img src="static/images/Sign-Out-Page.jpg" alt="Account signout page">

- Account signout

    - Once users wish to leave the site they have the option to signout.

<img src="static/images/Sign-In-Page.jpg" alt="Account signin page">

- Account signin

    - User can then signin when they return to the site.

## Technology

### Python / Django

- The programming language and framework.
### HTML

- The structure language of the site.

### Bootstrap / CSS

- The styling language and framework.

### Font Awesome

- The library for the icons used within the site

### Cloudinary Storage

- The image storage for the site.

### Allauth

- User authentication, verification and account management.

### Crispy Forms

- Used for form context, styling and rendering.

### Gunicorn

- Web server for Python.

### Summernote

- Editor for comments and text fields.

## Testing

### Functionality testing

- The site was developed using the Chrome developer tools for the HTML and styling elements.

- The Python testing was carried out using coverage.

<img src="static/images/coverage-report.jpg" alt="Coverage report">

#### Model Testing

    -""" Imports TestCase from django.test"""
    from django.test import TestCase
    from django.contrib.auth.models import User
    from .models import Post, Comment


    class TestBlogModels(TestCase):
        """ Inherits TestCase for all functions below
        """

        def test_post_str(self):
            """ Tests a post can be created and title is returned.
            """
            user = User.objects.create(username="Name",)
            post = Post.objects.create(title="Test Title", author=user)
            self.assertEqual(post.title, "Test Title")

        def test_comment_str_(self):
            """ Tests a comment can be created and that the body and
                author can be returned.
            """
            user = User.objects.create(username="Name",)
            post = Post.objects.create(title="Test Title", author=user)
            comment = Comment.objects.\
                create(post=post, body="Some text", name="Me", approved=True)
            self.assertEqual(comment.body, "Some text")
            self.assertEqual(comment.name, "Me")

The above tests were used to test the models were setup to handle the required data in order to manage to trail posts.

### Views Testing

    -   """ Imports TestCase from django.test """
        from django.test import TestCase
        from django.contrib.auth.models import User
        from .models import Post, Comment


        class TestViews(TestCase):
        """ Inherits TestCase for all functions below
        """

        def test_post_list_opens_trail_list(self):
            """ Test the corrrect template is used
            """
            response = self.client.get('/trails/')
            self.assertEqual(response.status_code, 200)
            self.assertTemplateUsed(response, 'trails.html')

        def test_post_detail_operates_as_expected(self):
            """ Tests the post detail creates a post as expected
            """
            user = User.objects.create(username="Name")
            post = Post.objects.\
                create(title="Test Title", author=user, status=1)
            comment = Comment.objects.\
                create(post=post, body="Some text", name="Me", approved=True)
            self.assertEqual(comment.body, "Some text")
            self.assertEqual(post.status, 1)

        def test_open_home_page_works(self):
            """ Test the corrrect template is used
            """
            response = self.client.get('/')
            self.assertEqual(response.status_code, 200)
            self.assertTemplateUsed(response, 'index.html')

        def test_open_cafe_page_works(self):
            """ Test the corrrect template is used
            """
            response = self.client.get('/cafe/')
            self.assertEqual(response.status_code, 200)
            self.assertTemplateUsed(response, 'cafe.html')

        def test_open_gallery_page_works(self):
            """ Test the corrrect template is used
            """
            response = self.client.get('/gallery/')
            self.assertEqual(response.status_code, 200)
            self.assertTemplateUsed(response, 'gallery.html')

While I am happy with the tests carried out on the views it is still short of where I wanted to be (50%). I struggled to carry out these tests as thourghly as I would have liked.

#### Forms Testing

    -   """ Imports Testcase from django.test"""
        from django.test import TestCase
        from .forms import CommentForm


        class TestCommentForm(TestCase):
            """ Inherits TestCase for all functions below
            """
            def test_coment_body_is_required(self):
                """ Tests name is a required field in form
                """
                form = CommentForm({'body': ''})
                self.assertFalse(form.is_valid())
                self.assertIn('body', form.errors.keys())
                self.assertEqual(form.errors['body'][0], 'This field is required.')

            def test_years_riding_default_is_working(self):
                """ Tests years riding default value is valid
                """
                form = CommentForm({'body': 'my comment', 'years_riding': 0})
                self.assertTrue(form.is_valid())

            def test_form_fields_are_explicit_in_form_metaclass(self):
                """ Tests form fields are in place and in order
                """
                form = CommentForm()
                self.assertTrue(form.Meta.fields, ['body', 'years_riding'])

The forms were 100% tested, although the form is small and required very little testing.
### Compatability testing

- The site has been tested on multiple screen sizes and is responsive throughout.

### Code validation

- The HTML and CSS have been tested using jigsaw.w3.org with no errors showing.

- The Python was also tested online with no errors showing.

### Issues found during testing

- When testing the models, views and forms with TestView I had an issue in getting the tests to run. This was because I had already deplyed the site to Heroku and so had the database pointed to Postgres and not SQLite3.

- Once the database was reset to SQLite the test ran ok.

- I would have liked to do more tests but time has caught up with me and I can't risk missing this deadline, so the testing was focused as much as possible. The items that haven't been covered in the coverage report have been manually tested in deployment.

### Performance testing

- Site has been evaluated by Lighthouse and the report is below.

<img src="static/images/Lighthouse-report.jpg" alt="Lighthouse report">

## Deployment

The site is deployed from Heroku.

1. Click deploy from app home page

<img src="static/images/Click-Deploy.jpg" alt="Click deploy section">

2. Click GitHub link in deployment method and link the repository

<img src="static/images/Link-Repo.jpg" alt="Link the GitHub Repo section">

3. Click deploy branch button

<img src="static/images/Deploy-Branch.jpg" alt="Deploy branch button">

4. Click open app button

<img src="static/images/View.jpg" alt="View button">

# Credits

- The site is influenced by Komoot, which I use and find easy to navigate and use.

- The national trusts cycling sites were also an influence, in regards to page content.

- The Code Institute Blog and ToDo app walkthoughs were the basis for the inner workings of the site, such as Django and Python functions.

- uLearn on YouTube were the guide used for getting more familiar with Wireframes.

- All of the images came from Pexels and the owners of the images are;
    - Axel Brunst
    - Hendrik Morkel
    - Jeremy Bishop
    - Nick Rickerts
    - Marina Kuznetsova
    - Luca Dross
    - Pixabay
    - Anastasia Shuraeva
    - Darcy Lawrey
    - Jan Kopriva
    - Lars Mai
    - Viktoria Alipatova

- The other students on Slack helped me with the testing issues, clearly some had faced the same issue.

## Screenshots

### Landing Page
<img src="static/images/Landing-Page.jpg" alt="The landing page">

### Trails Page
<img src="static/images/Trails-Page.jpg" alt="The trails page">

### Trail Article Page
<img src="static/images/Trail-Article-Page.jpg" alt="The trails article page">

### Cafe Page
<img src="static/images/The-Cafe-Page.jpg" alt="The Cafe page">

### Signup Page
<img src="static/images/Sign-Up-Page.jpg" alt="Account signup page">

### Signout Page
<img src="static/images/Sign-Out-Page.jpg" alt="Account signout page">

### Signin Page
<img src="static/images/Sign-In-Page.jpg" alt="Account signin page">