# playlistProject

## Contents:


## Project Brief
To create a CRUD application with utilisation of supporting tools, methodologies and technologies that encapsulate all core modules covered during training.

## Playlist Project
For my project I have created a web application that allows a user to create songs and/or playlists. The user also has the option to update and view songs, and also delete playlists.

## Risk Assessment

!https://github.com/Catherine1000/playlistProject/blob/master/DocImages/Risk%20Assessment.png

## ERDs (Entity Relationship Diagrams)

**Initial Plan**

I originally decided to create a many to many relationship, which would allow users to create many songs and also many playlists containing many songs.



The diagram above shows the relationship for the final application. I had difficulties with allowing users to add many songs in a single playlist, therefore I revised the initial tables and changed the relationship to one to many.


## Project Tracking
To track my progress and to monitor tasks, I used [Trello](https://trello.com/b/4hpZ6MKn/playlist-project) to manage my project tracking. 

## Front End Design


## Testing

The results from my tests are %.


## Deployment
To deploy my Playlist project I used gunicorn.
My web application can be accessed via a virtual machine.


## Evaluation
Currently my web application only allows users to add one song per playlist. This is something I would develop in my next sprint as this provides the user with more flexibility to make their playlist with as many songs as they like. I would like to incorporate a feature where users can click a button to add a song and another button to remove songs.

In further sprints I would as a user login feature to make the web app more personal and secure for each user.
