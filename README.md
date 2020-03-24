# Playlist Application

## Project Brief
To create a CRUD application with utilisation of supporting tools, methodologies and technologies that encapsulate all core modules covered during training.

## Playlist Project
For my project I have created a web application that allows a user to view and create songs and/or playlists.
The user also has the option to update and view songs, and also delete playlists.

## Risk Assessment

![](/DocImages/RiskAssessment.jpg)

## ERDs (Entity Relationship Diagrams)

**Initial Plan**

![](/DocImages/ManyToManyERD.jpg)

I originally decided to create a many to many relationship, which would allow users to create many songs and also many playlists containing many songs.

**Revised ERD**



The diagram above shows the relationship for the final application. I had difficulties with allowing users to add many songs in a single playlist, therefore I revised the initial tables and changed the relationship to one to many. This has unfortunately limited the user to only adding one song per playlist. However, in order to create an MVP, I felt it was necessary to make the change and improve the feature later if I had time.


## Project Tracking
To track my progress and to monitor tasks, I used [Trello](https://trello.com/b/4hpZ6MKn/playlist-project) to manage my project tracking. 

![](/DocImages/Trello.jpg)

## Front End Design

![](/DocImages/FrontDesign1.jpg)

![](/DocImages/FrontDesign2.jpg)

## Testing

The coverage test results from my tests are 40%.
I would have liked to have tested more of the functionality of my application. However, this would be something that I would do in later sprints.


## Deployment
To deploy my Playlist project I used gunicorn.
My web application can be accessed via a virtual machine.

![](/DocImages/CIPipeline.jpg)

## Evaluation
Currently my web application only allows users to add one song per playlist. This is something I would develop in my next sprint as this provides the user with more flexibility to make their playlist with as many songs as they like.
I would like to incorporate a feature where users can click a button to add a song and another button to remove songs.

In further sprints I would add a user login feature to make the web application more personal and secure for each user.
