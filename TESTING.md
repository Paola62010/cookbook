# CookBook - Testing Details

[Main README.md file](README.md)

[Deployed site](https://paolas-cookbook.herokuapp.com/)

The following validators were used to check the validity of the website code:

[W3C Makup Validation Service](https://validator.w3.org/)

[W3C CSS Valiation Service](http://jigsaw.w3.org/css-validator/)

[JSHint](https://jshint.com/)

[PEP8online](http://pep8online.com/)

There are no errors for both CSS and HTML. I have a warning for HTML for a missing header for a section, but I believe that the header is not needed in that specific scenario. JSHint is returning warnings for my JavaScript as I have included Jinja template language in it. I do get errors for Python for one only reason: "line too long". I left those not to break the code. 

## User Stories Testing 

User stories can be found in the UX section in the [README.md file](README.md)

1. As an Admin User I want to be able to add new recipe categories so that Site Users can better organise their recipes.

    i. Admin users are able to add new categories throught the admin panel, "Main" section, "Categories". Currently there are 12 categories.

    ii. Admin users can filter the available categories by created_on or updated_on dates. 

    iii. Admin users can search the available categories by name.

2. As an Admin User I can delete recipe posts so that I can manage the site content and make sure it is appropriate.

    i. Admin users have access to all recipes via the admin panel, "Main" section, "Recipes". 

    ii. Admin users can view the whole content of a recipe on the same page, as I have included Ingredients and Steps inlines. 

    iii. Admin users can filter the existing recipes by created_on or updated_on dates.

    iv. Admin users can search the available recipes via title and author. 

    v. Admin users can delete recipes where content is not appropriate. 

3. As an Admin User I can delete comments so that inappropriate comments can be removed.

    i. Admin users have access to all comments via the admin panel, "Main" section, "Comments".

    ii. Admin users can filter the existing comments by created_on date.

    iii. Admin users can search the available recipes via recipe and author.

    iv. Admin users can delete comments where content is not appropriate. 

4. As a Site User I want to be able to have recipes organised in different categories so that I can find what I am looking for more easily.  

    i. Existing recipes are organised by different categories. 

    ii. Users are presented with all the categories in the home page and they can select the category they wish to find recipes for. 

    iii. By clicking on a category, users are redirected to a new page listing all the available recipes for that category.

5. As a Site User I want to be able to view a list of recipes so that I can select which one to open and view.

    i. By clicking on a food category, located in the home page, the user is redirected to a new page listing all the available recipes for that category. 

6. As a Site User I want to be able to open a specific recipe so that I can view the details, such as ingredients and intructions.

    i. Users can click on a recipe in the list of available recipes to open it and view the details.

    ii. Users will be able to view the recipe details: title, author, creation date ingredients, steps, image, servings. 

7. As a Site User I want to be able to view the likes of a recipe post so that I can see which recipes are more popular.

    i. On the recipe_detail page, users will be able to view the number of likes for the recipe they are viewing.

    ii. The number of likes is located just above the comments, next to a heart icon.

8. As a Site User I want to be able to view the comments of a recipe post so that I can see the conversation.

    i. On the recipe_detail page, users will be able to view the comments left by authenticated users. 

    ii. Comments are listed from the most recent on top to the older ones. This is personal preference, they can easily be changed to have the oldest comment on top. 

    iii. Users can view the number of comments, this is located just above the comments, next to a speech bubble icon.

9. As a Site / Admin User I want to be able to search for a recipe so that I can easily find it. 

    i. Admin users can search for recipes as described in user story 2, point iv.

    ii. Site users have a search bar located in different pages that allows them to search for existing recipes.

    iii. Non authenticated users will be able search all the recipes made public by registered users.

    iv. uthenticated users will be able to search all recipes made public by other creators and also their own personal recipes (private and public). 

10. As a Site User I want to be able to log into my account so that I can see both the public recipes shared by the community and my own personal recipes. 

    i. The website has an authentication process so that users can register for an account, login and logout.

    ii. Authenticated users will have access to all the website features, including creating and updating recipes, leaving likes and comments, adding other crators' recipes to their favourites. 

11. As a Site User I can create a new recipe post so that it is added to my personal recipes.

    i. Authenticated users can click on the plus sign icon, located in different pages, to create a new recipe.

    ii. When clicking on the icon, users are redirected to the create_recipe page where they are presented with a form to collect all the recipe details.

    iii. When the recipe is created by clicking on the "submit" button, it will be visible on the user personal_recipes page, and also the public_recipes page if the user checked the "public" option while filing the form. 

12. As a Site User I can edit or delete my recipe posts so that I can manage my own content.  

    i. Authenticated users can delete their recipes. On the recipe_detail page, there is a bin icon located on the top right corner of the page. 

    ii. By clicking on the icon, users are redirected to the delete_recipe page where they are asked to confirm that they want to delete the recipe. 

    iii. Authenticated users can edit their recipes. On the recipe_detail page there is a pencil and paper icon on the top right corner of the page.

    iv. By clicking on the icon, users are redirected on the update_recipe page, where they are presented with a pre-filled form containing the recipe details. 

    v. Users can update their recipe by clicking on submit. 

13. As a Site User I can make my recipe posts public so that they are shared with the community and can be viewed by other users.

    i. Authenticated users can make their recipe public by cliking on the "public" checkbox while filling the form when creating the recipe. 

    ii. Users can also make their recipe public when updating a recipe, by clicking on the "public" checkbox.

14. As a Site User I want to be able to leave comments on a recipe post so that I can be part of the conversation.

    i. Auhenticated users will be able to see a comment form on the recipe_detail page.

    ii. By filling the form and clicking on "submit", the comment will be saved and shown in the comments section below the recipe. 

15. As a Site user I want to be able to like/unlike a recipe so that I can interact with the shared content. 

    i. Authenticated users can like/unlike a recipe post by clicking on the heart icon located on the top right corner of the recipe_deail page. 

    ii. Creators will not be able to like/unlike their own recipes. 

16. As a Site User I want to be able to save a recipe I like into my favourites section so that I can have easy access to it.

    i. Authenticated users have access to a favourites page where they can view the recipes from other creators they saved as favourites.

    ii. To add a recipe to the favourites, users can click on the star icon located on the top right corner of the recipe_detail page. This option is only available to save other creators' recipes and not their own.

    iii. To remove the recipe from their favourites, users can simply click on the star icon again. 


## Manual Testing 

### Home Page 

1. Header and Authentication

    - Click on the website logo and verify that it redirects to the home page.

    - For non authenticated users, verify that the navigation menu contains the following options: "home", "login", "register".

    - Click on "home" and verify that it redirects to the home page.

    - Click on "login" and verify that you are redirected to the login page. Enter your credentials and verify that it redirects you to the home page and that a success message appears on top of the page (message will disappear after 3 seconds). 

    - Try to log in without the required credentials and verify that a message appears asking to fill in the required fields. Try to login with incorrect credentials and veryfy that a message appears to inform that the username and/or password are incorrect.

    - On the login window, click on the "sign-up" link and veryfy that it redirects to the signup page.

    - Click on "register" on the header navigation bar and verify that it redirects you to the signup page. Enter the required details and click on sign-up, veryfy that you are redirected to the home page and that a success message appears on top of the page (message will disappear after 3 seconds).

    - Try to register without filling the required details and verify that a message appears asking to fill in the required fields. Try to register without filling the optional field and verify that you are able to proceed successfully.

    - For authenticated users, verify that the following options are shown in the navigation menu: "home", "favourites", "logout".

    - Click on "home" when authenticated and verify that it redirects you to the home page. 

    - Click on "favourites" and verify that it redirects you to the favourites page.

    - Click on "logout" and verify that you are redirected to the logout page. 

    - In the logout page, verify that you are asked to confirm that you want to logout. Click on the "sign out" button and verify that you are redirected to the home page and a success message appears on top of the page (message will disappear after 3 seconds).

2. Welcome section 

    - For non authenticated users, verify that a welcome message is shown with a short introduction of the website. Call to action is specific for non authenticated users, it advises to create an account to have access to additional features.

    - For authenticated users verify that the title now is different and contains a greeting for the user. Call to action is also different and invites the user to create a new recipe by clicking on the plus sign icon. 

    - For authenticated users verify that a plus sign icon is present on the top right corner of the page. Hover over the icon and verify that it changes colour. Click on the icon and verify that you are redirected to the create_recipe page. 

    - Below the welcome message there is a search bar. For both authenticated and non authenticated users, fill in the search field click on the "search" button, verify that you are redirected to the search_results page. Click on "search" without filling in the field and verify that a message appears asking to fill in the required field. Hover over the "search" button and verify that it changes colour. 

3. Food category cards 

    - For non authenticated users, verify that the 12 available food categories are listed and shown in a grid or cards. Hover over the card text section and verify that it changes colour.  

    - For non authenticated users, click on each category card and verify that you are redirected to the public_recipes page for that specific category (for example: /public/appetizers). 

    - For authenticated users, verify that you have a small navigation menu in the category cards section. Options are: "public" and "personal". Switch beween the two options and verify that all 12 categories are shown for eatch option. Hover over the  text section on the cards and verify that it changes colour.

    - For authenticated users, click on each category card in the "public" section and verify that you are redirected to the public_recipes page for that specific category (for example: /public/appetizers).

    - For authenticated users, click on each category card in the "personal" section and verify that you are redirected to the personal_recipes page for that specific category (for example: /personal/breakfast).

4. Footer 

    - In the footer, there are 4 social media icons. Hover over each icon and verify that it changes colour. 

    - Click on each social media icon and verify that you are redirected to the correct social media page. 

    - Below the social media links, verify that the copyright info is showing correctly (correct year).

#### Home Page (finished site)

![Home page finished site - Non authenticated](readme-images/home-nonauthenticated.png)

![Home page finished site - Authenticated](readme-images/home-authenticated.png)

![Home page finished site - Footer](readme-images/home-footer.png)

### Public Recipes Page

1. Header and Authentication

    - Steps are highlighted in the manual testing of the Home Page section.

2. Top section 

    - For both authenticated and non authenticated users, verify that the top section of the page contains a title that reflects the food category the user has clicked on when in the home page. Right below the title, there is a short sentence also containing the food category name, verify that this is correct. 

    - Below the title and sentence, there is the search bar we saw also in the home page. Follow the same steps highlighted in the manual testing for the home page. 

    - For authenticated users verify that a plus sign icon is present on the top right corner of the page. Hover over the icon and verify that it changes colour. Click on the icon and verify that you are redirected to the create_recipe page.

3. Recipe cards 

    - For both authenticated and non authenticatd users, verify that if recipes are present, a list of cards is shown and organised into a grid. Hover over the text section on the cards and verify that it changes colour. Click on the cards and verify that you are redirected to the recipe_detail page for that specific recipe. 

    - If no recipes are present for the selected category, verify that a message is shown to inform the user. 

4. Footer 

    - Steps are highlighted in the manual testing of the Home Page section.

#### Public Recipes Page (finished site)

![Public Recipes Page finished site - Non authenticated](readme-images/publicrecipes-nonauthenticated.png)

![Public Recipes Page finished site - Authenticated](readme-images/publicrecipes-authenticated.png)

![Public Recipes Page finished site - No recipes](readme-images/publicrecipes-norecipes.png)

### Personal Recipes Page

1. Header and Authentication

    - Steps are highlighted in the manual testing of the Home Page section.

    - Only authenticated users have access to this page. As a non authenticated user, try to navitage to any personal_recipes url (as example /personal/appetizers) and verify that you are redirected to the login page. 

2. Top section 

    - Verify that the top section of the page contains a title that reflects the food category the user has clicked on when in the home page. Right below the title, there is a short sentence also containing the food category name, verify that this is correct. 

    - Below the title and sentence, there is the search bar we saw also in the home page. Follow the same steps highlighted in the manual testing for the home page. 

    - Verify that a plus sign icon is present on the top right corner of the page. Hover over the icon and verify that it changes colour. Click on the icon and verify that you are redirected to the create_recipe page.

3. Recipe cards

    - Verify that if recipes are present, a list of cards is shown and organised into a grid. Hover over the text section on the cards and verify that it changes colour. Click on the cards and verify that you are redirected to the recipe_detail page for that specific recipe. 

    - If no recipes are present for the selected category, verify that a message is shown to inform the user.

4. Footer 

    - Steps are highlighted in the manual testing of the Home Page section.

#### Personal Recipes Page (finished site)

![Personal Recipes Page finished site](readme-images/personal_recipes.png)

![Personal Recipes Page finished site - No recipes](readme-images/personal_recipes-norecipes.png)

### Recipe Detail Page

1. Header and Authentication

    - Steps are highlighted in the manual testing of the Home Page section. 

2. Recipe Detail section

    - For non authenticated users, verify that the recipe information is present: title, creator, creation date, servings, ingredients, steps, recipe image is visible and not distorted. 

    - For users that are authenticted and the recipe is their own, verify the same as for step 1, but also verify that 2 icons are present on the top right corner of the page: the pencil and paper icon and the bin icon. 

        - Hover over the pencil and paper icon and verify that text "Update Recipe" appears.
    
        - Click on the pencil and paper icon and verify that you are redirected to the update_recipe page. 

        - Hover over the bin icon and verify that text "Delete Recipe" appears.
        
        - Click on the bin icon and verify that you are redirected to the delete_recipe page. 

    - For users that are authenticated but the recipe is not their own, verify the same as for step 1, but also that 2 different icons are present on the top right corner of the page: a heart icon and a star icon. 

        - Hover over the heart icon and verify that text "Like" appears.

        - Click on the heart icon and verify that the icon changes from a empty heart to a filled heart. 

        - Verify that the likes count in the comments section is updated to include your like. The likes count is located just above the comments section, next to the heart icon.

        - Hover over the star icon and verify that text "Favourite" appears. 

        - Click on the star icon and verify that the icon changes from a empty star to a filled star.

        - Navigate to your favourites page and verify that the recipe is now listed there. 

3. Comments section 

    - For users that are not authenticated, verify that only the comments are visible (including comments count and likes count) and there is no comment form available.

    - For users that are authenticated verify that in addition to the comments there is also a comment form to submit a new comment. 

        - Hover over the "submit" button and verify that it changes colour. 

        - Try to submit a comment without filling the body field and verify that a message appears asking to fill in the required field. 

        - Fill in the comment body field and click on the "submit" button, verify that the message is successfully added to the comments section, a success message appears on top of the page. 

        - Verify that the message you have added is the first on top of the comments section. 

        - Verify that the comment count is now updated to include your comment. The comment count is located just above the comments section, next to the speech bubble icon. 

    - Admin panel

        - Navigate to the Admin panel and verify that comments are added correctly when submitted and not added when the form is incorrect. 

4. Footer 

    - Steps are highlighted in the manual testing of the Home Page section.

#### Recipe Detail Page (finished site)

![Recipe Detail Page - non authenticated user](readme-images/recipedetail-nonauthenticated.png)

![Recipe Detail Page - non authenticated user 2](readme-images/recipedetail-nonauthenticated2.png)

![Personal Recipes Page - authenticated and own recipe](readme-images/recipedetail-authenticated-ownrecipe.png)

![Personal Recipes Page - authenticated and own recipe 2](readme-images/recipedetail-authenticated-ownrecipe2.png)

![Personal Recipes Page - authenticated and not own recipe](readme-images/recipedetail-authenticated.png)

![Personal Recipes Page - authenticated and not own recipe 2](readme-images/recipedetail-authenticated2.png)

### Create Recipe Page

1. Header and Authentication

    - Steps are highlighted in the manual testing of the Home Page section.

    - Only authenticated users have access to this page. As a non authenticated user, try to navitage to the create_recipe url and verify that you are redirected to the login page. 

2. Create Recipe form 

    - Try to submit a recipe without the following required fields and verify that the form is is not submitted: title, category, servings, image.

    - Fill in the requied fields listed in the previous step and click on submit. The steps and ingredients are not mandatory as I want the user to be able to save the recipe and come back to it later if they prefer. Verify that the recipe is successfully submitted and you are redirected to the recipe_detail page which is showing your new recipe. 

    - Fill in the required fields listed in step 1, but now also try to fill in only one of the fields for the ingredient (as example only ingredient name or ingredient quantity). An error should appear when clicking on the "submit button" advising to fill in the required field. 

    - Fill in both the required fields for the ingredient and click on "submit", verify that you are redirected to the recipe_detail page which is showing your new recipe.

    - Create a new recipe and fill in all the required fields and add both fields for 1 ingredient and add 1 step. Click on "submit", verify that you are redirected to the recipe_detail page which is showing your new recipe.

    - Create a new recipe and fill in all the required fields and add both fields for 1 ingredient and add one step. Now click on "add another" for both the steps and ingredients and verify that new forms are dynamically added. Fill in the additional forms and click on "submit". Verify that you are redirected to the recipe_detail page which is showing your new recipe.

    - Create a new recipe and fill in all the required fields. Click on "add another" for both the steps and ingredients until you reach 25 forms, this is the limit I have chosen. When you have 25 forms for each, the "add another" option is no longer shown. Click on "remove" and verify that the forms are dynamically removed. 

    - Navigate to the Admin panel. Verify that recipes are created successfully only when the form is correctly submitted and the user has been redirected to the recipe_detail page. 

3. Footer

    - Steps are highlighted in the manual testing of the Home Page section.

#### Create Recipe Page (finished site)

![Create Recipe Page - 1](readme-images/createrecipe1.png)

![Create Recipe Page - 2](readme-images/createrecipe2.png)

### Update Recipe Page

1. Header and Authentication

    - Steps are highlighted in the manual testing of the Home Page section.

    - Only authenticated users have access to this page. As a non authenticated user, try to navitage to an update_recipe url and verify that you are redirected to the login page. 

2. Update Recipe Form

    - Verify that the form fields are pre-populted with all details previously submitted during recipe creation, or during a previous update.

    - Try to update any of the fields with new values and click on "submit". Verify that you are redirected to the recipe_detail page which is showing your updated recipe. 

    - Remove the required fields and click on "submit". Verify that you are unable to update the recipe. 

    - If ingredients are present, try to remove one of the 2 required fields and click on "submit". Verify that an error appears asking to fill in the required field. 

    - Click on "Add another" for both steps and ingredients and add additional steps and ingredients, filling in the required fields. Click on "submit". Verify that you are redirected to the recipe_detail page which is showing your updated recipe.

    - Click on "add another" for both the steps and ingredients until you reach 25 forms, this is the limit I have chosen. When you have 25 forms for each, the "add another" option is no longer shown. Click on "remove" and verify that the forms are dynamically removed.  

    - Navigate to the Admin panel. Verify that recipes are updated successfully only when the form is correctly submitted and the user has been redirected to the recipe_detail page. 

3. Footer

    - Steps are highlighted in the manual testing of the Home Page section.

#### Update Recipe Page (finished site)

![Update Recipe Page - 1](readme-images/updaterecipe1.png)

![Update Recipe Page - 2](readme-images/updaterecipe2.png)

### Delete Recipe Page

1. Header and Authentication

    - Steps are highlighted in the manual testing of the Home Page section.

    - Only authenticated users have access to this page. As a non authenticated user, try to navitage to a delete_recipe url and verify that you are redirected to the login page. 

2. Delete Recipe Form

    - Verify that the user is presented with a form asking to confirm that they want to delete the recipe. The recipe title is contained in the message.

    - Hover over the "confirm" button and verify that it changes colour. 

    - Clik on the "confirm" button and verify that the user is redirected to the personal_recipes page. A confirmation message is shown on top of the page (the message will disappear after 3 seconds). 

3. Footer

    - Steps are highlighted in the manual testing of the Home Page section.

#### Delete Recipe Page (finished site)

![Delete Recipe Page](readme-images/deleterecipe.png)

### Favourites Page

1. Header and Authentication

    - Steps are highlighted in the manual testing of the Home Page section.

    - Only authenticated users have access to this page. As a non authenticated user, try to navitage to the favourites url and verify that you are redirected to the login page. 

2. Top section

    - Below the page title and call to action, there is the search bar we saw also in the home page. Follow the same steps highlighted in the manual testing for the home page. 

3. Recipe cards

    - Verify that if recipes are present, a list of cards is shown and organised into a grid. Hover over the text section on the cards and verify that it changes colour. Click on the cards and verify that you are redirected to the recipe_detail page for that specific recipe. 

    - Verify that the recipes you see in the list are the ones you have marked as favourites by clicking on the star icon in the recipe_detail page. 

    - If no recipes are present, verify that a message is shown to inform the user.

4. Footer 

    - Steps are highlighted in the manual testing of the Home Page section.

#### Delete Recipe Page (finished site)

![Favourites Page - with recipes](readme-images/favourites.png)
![Favourites Page - without recipes](readme-images/favourites2.png)

### Search Results Page

1. Header and Authentication

    - Steps are highlighted in the manual testing of the Home Page section.

2. Search results 

    - Verify that the top section of the page displays the word you have searched for.

    - For non authenticate users:

        - Verify that bottom section of the page only contains recipes that have been made public by creators. If no results match your search, verify that a message is displayed advising that your search found no matches.

    - For authenticated users:

        - Verify that bottom section of the page contains: public recipes shared by other creators and personal recipes (public and non public). These are displayed into 2 separate sections. If no results match your search, verify that a message is displayed advising that your search found no matches.

    - For both non authenticated and authenticated users, verify that if recipes are present, a list of cards is shown and organised into a grid. Hover over the text section on the cards and verify that it changes colour. Click on the cards and verify that you are redirected to the recipe_detail page for that specific recipe.

3. Footer

    - Steps are highlighted in the manual testing of the Home Page section.

#### Search Results Page (finished site)

![Search Results Page - non authenticated with recipes](readme-images/search-nonauthenticated.png)
![Search Results Page - non authenticated without recipes](readme-images/search-nonauthenticated-norecipes.png)
![Search Results Page - authenticated](readme-images/search-authenticated.png)

## Bugs

- The main challenge I have had during the development of this project was including two inline formsets (for the recipe ingredients and for the recipe steps) in the form for the recipe creation and the form for recipe update. I also wanted these two inline forms to be dynamic and having the user add as many ingredients or steps as needed. After quite a few attempts I came across [Django-extra-views](https://django-extra-views.readthedocs.io/en/latest/), a Django package that introduced additional class-based views to complement those provide by Django itself. I have used CreateWithInlinesView and UpdateWithInlinesView which made it way easier to handle the forms. The documentation is clear and helpful. For the dynamic forms I have used [Django-dynamic-formset](https://github.com/elo80ka/django-dynamic-formset), a jQuery plugin to dynamically add more inline formsets. This was recommended online by other developers and it seems to do the job quite nicely. 

- An issue I encountered was in the search feature in the Admin panel, for both the Recipes and Comments. The error I received when searching an item was (example for comments): "FieldError at /admin/main/comment/, Related Field got invalid lookup: icontains". This was caused by the fact that I had included foreign keys as "search_fields" for classes RecipeAdmin and CommentAdmin in <span>admin.py</span>. I have corrected the values following the instructions in the [Django documentation](https://docs.djangoproject.com/en/3.2/ref/contrib/admin/#django.contrib.admin.ModelAdmin.search_fields).

### Remaining Bugs

- A small bug the project has is related to recipe creation. When the user fills the form, includes ingredients without filling both required fields (for example filling in only the ingredient name but not the quantity), the user is presented with an error message advising that the missing field is required. This is ok, but the recipe image the user had uploaded disappears, forcing the user to upload it again. I would like to have this corrected in future. 

- Another small bug is related to recipe creation and also update. If the user tries to submit a recipe without a required field (title, category, servings, image), the form is correctly not submitted and the user is redirected to the required field, but the message does not always show. It shows in some browsers (they show on Firefox for example but not Google Chrome). I was not able to find a solution to this, I have checked this with my mentor but we were not able to see what could cause this. 

#### Chrome

![Chrome](readme-images/fielderrormissing.png)

#### Firefox

![Firefox](readme-images/fielderrorfirefox.png)