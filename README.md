#### Note: Postgresql is integrated with the current app. Check out it at index.py. Follow the instructions safely before running the code. Scroll to bottom for instructions

# your MOVIEBOOK
Collection of all of your favorite movies

# Forgot what movies you've watched?

No problem. Here is the simple solution. Add all the movies you've watched and keep them safe with you. The next time, you can view all the movies you have watched at one place. Sounds Interesting? Check out our project.

# Not only you've watched!!!

You can add any movie to your list and you can view the list at any time. 

Many filters have been added to ease your hurdles. Even a search bar is also added in order to make your efforts little but with big results in a short time. For the next movie time, you can just open the application and find what movies you've watched or the movies of your interested genre or language.

# Tell me more!!!!!!!!!

Ok. Here we go! 
Add all movies you're interested in using this application. If you are checking for a particular genre or language or you've some part of the movie name or actors in your mind, you can go straight into the application and apply filters and hit the search or return button. Tada!!! You got what you're looking for.

# How it Works?

Works too simple. A default movie list can be downloaded along with the code. 

# Search through applied filters
1. Run the code
2. Apply filters of your choice
3. Hit the Search button.
4. You'll get the results for the filters you've applied. 
5. Use 'Next' and 'Previous' buttons to navigate through the results.

# Search through search bar
Have something in mind? Don't worry. We've added the search bar to ease your efforts.
1. Run the code
2. Type what you're looking for in search bar
3. Hit Enter button in your keyboard. (Hitting the Search button doesn't work. Sorry for that!)
4. You'll get the results for the given input.
5. Use 'Next' and 'Previous' buttons to navigate through the results.

# Add a new movie to your list
Is the default list boring? You can wipe all data from the given file. Then you can add new movies to your list through the following steps.
1. Run the code
2. Click 'Add' button. 
3. A new window pop ups and you can enter your inputs in the given fields.(If you want to enter two inputs for the same data like (Genre: comedy and action), separate the two entities by a comma)
4. Tada!! Your new movie list is ready.

# Liked it? 
Thanks for showing interest.

# What's next?

A number of features are in testing mode and will be made available shortly. The upcoming features includes:
1. Create lists of your choice and name the list.
2. Classify the movie as watched or to be watched.
3. Recommendations from your previous usage.
4. The most exciting one is this! Seamlessly connect your data to a database and import it from anywhere at anytime.

# Have suggestions in mind?

We'd love to hear them. Tell us what's in your mind.

# Don't do's
1. Do not keep the code and txt file in separate folders. Keep them in same folder.
2. Do not delete or rename the txt file. You can wipe the data in the txt file. This will be nullified when we connect the data to the database. (sorry for that! Thanks for your patience).
3. Keep a comma if you're giving multiple entities for a same entry. Otherwise, your data might not be processed too well.

# Instructions for sql integrated index.py

The following instructions must be followed before running the index.py file
1. Install Postgresql and create a localhost at port '5432'.
2. Create a database in psql with the name 'moviebook'
3. Create a table in the moviebook database by using the following command =>a create table movies (name text, actor text[ ], genre text[ ], language text[ ])

Now headover to the downloaded index.py file. 
1. Make a new folder and place index.py in it.
2. Create virtualenv and activate it.
3. Install psycopg2 package
4. Run the index.py file in the (env)

If you find any of the instructions not working or for any assistnace, please do contact 

# Thanks! Have a Great Day
