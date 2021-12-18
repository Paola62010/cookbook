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
5. As a Site User I want to be able to view a list of recipes so that I can select which one to open and view.
6. As a Site User I want to be able to open a specific recipe so that I can view the details, such as ingredients and intructions.
7. As a Site User I want to be able to view the likes of a recipe post so that I can see which recipes are more popular. 
8. As a Site User I want to be able to view the comments of a recipe post so that I can see the conversation.
9. As a Site / Admin User I want to be able to search for a recipe so that I can easily find it. 
10. As a Site User I want to be able to log into my account so that I can see both the public recipes shared by the community and my own personal recipes. 
11. As a Site User I can create a new recipe post so that it is added to my personal recipes.
12. As a Site User I can edit or delete my recipe posts so that I can manage my own content.  
13. As a Site User I can make my recipe posts public so that they are shared with the community and can be viewed by other users. 
14. As a Site User I want to be able to leave comments on a recipe post so that I can be part of the conversation.
15. As a Site user I want to be able to like/unlike a recipe so that I can interact with the shared content. 
16. As a Site User I want to be able to save a recipe I like into my favourites section so that I can have easy access to it.


## Manual Testing 

### Home Page 

### Public Recipes Page

### Personal Recipes Page

### Recipe Detail Page

### Create Recipe Page

### Update Recipe Page

### Delete Recipe Page

### Favourites Page

### Search Results Page