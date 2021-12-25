# PyPass

PyPass is a GUI password manager written in Python, using tkinter

# About repo

The master branch is the DEV branch, and has all the newest code. If you want stable source code, you can find it under the Releases section.

If you want to contribute:
 - Don't clean up the code. Please. It's a waste of time
 - I will be the most grateful for double-checking translations and adding new ones

# Known Errors:
 - Deleting entries in different order than from last to first might cause errors (should be fixed by now)
 - There can be issues regarding loading data when some entries were deleted in the previous session (should be fixed by now)

# Milestones:

1. 
 - Replace current "Delete" button with an "Edit" button, which will bring a screen to edit the login and password
 - Add an ability to generate a random password while creating an entry (DONE in 0.6)
 - [OPTIONAL] Create a CLI installer scripts

2. 
 - Add encryption
 - When language not set, make the program load system language instead of defaulting to English (DONE in 0.6)
 - Create an icon

3. 
 - Auto-open a site for 2FA if specified
 - Support for more languages
 - Fix theming

4.
 - Add an option to sync passwords between devices using a cloud sharing service like MEGA
