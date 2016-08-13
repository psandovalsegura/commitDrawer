# *commitDrawer* 

A Python script which allows users to write short messages using the GitHub commits visualization.

## Use 

After downloading the repository locally, open terminal, navigate to the commitDrawer directory and run the script:

```bash
$ python commitDrawer.py
```

Enter a message that is less than or equal to 7 characters. For example, at the prompt:

```bash
Enter a message: example
```

That's it!

A file will be created in the same directory and will be titled *commitDatesForMessage_<message>.txt*. 
Use the checklist to commit on the specified dates to display your message.

```bash
The message will be ready on 7/7/2017
                                -------------------------------------                                
. . . . # # # # # . . # . . . # . . . # # # . . . # . . . # . . . # # # . . . # . . . . . . # # # # # .
. . . . # . . . . . . # . . . # . . # . . . # . . # # . # # . . # . . . # . . # . . . . . . # . . . . .
. . . . # . . . . . . . # . # . . . # . . . # . . # . # . # . . # . . . # . . # . . . . . . # . . . . .
. . . . # # # # . . . . . # . . . . # # # # # . . # . . . # . . # # # # . . . # . . . . . . # # # # . .
. . . . # . . . . . . . # . # . . . # . . . # . . # . . . # . . # . . . . . . # . . . . . . # . . . . .
. . . . # . . . . . . # . . . # . . # . . . # . . # . . . # . . # . . . . . . # . . . . . . # . . . . .
. . . . # # # # # . . # . . . # . . # . . . # . . # . . . # . . # . . . . . . # # # # # . . # # # # # .
Your GitHub Profile will look like this after 328 days.
```

*Note: Shorter messages will take less time*
