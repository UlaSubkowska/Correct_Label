Recuired programs: Miscrosoft Excel, Python 3.6.1 (or older version of Python 3)

If you don't have Python, please go to the website: https://www.python.org/downloads/ . Downloade and instal program,
following instructions from website (you can find the version and instruction for different OS - Windows, LINUX/UNIX and others).

Rest of instructions are for Windows operating system (for more information about using application with others OS please search in internet) 
Please paste the folder CORRECT_LABEL at your Desktop (check if you have all required files inside folder CORRECT_LABEL)
List of reguired files in CORRECT_LABEL folder:
-CORRECT_LABEL.py
-CORRECT_LABEL_second_step.py
-first_file_in_english.json
-second_file_in_spanish.json
-folder .idea
-README.txt


HOW TO OPEN CORRECT_LABEL:
Please open command line interpreter from your start menu.
You will see "C:\Users\User>", where User is name of user at your computer (example: C:\Users\Ula>)
Type 'cd Desktop' after sigh '>' and press enter (type text without ' )
Type 'cd CORRECT_LABEL' and press enter
Now you should see "C:\Users\User\Desktop\CORRECT_LABEL>" at your command line interpreter.
*If path you see is different (except the name of user) please check that you have CORRECT_LABEL folder at you Desktop and try agin from beggining. 
**If you still have a problem, please find solution in internet your goal is to get this path - "C:\Users\User\Desktop\CORRECT_LABEL>" on the screen. 

Now please type 'python CORRECT_LABEL.py' and press enter to start program. 

Then follow instructions in program CORRECT_LABEL.py (keep in mind that files which you want to attache to program (first_file_in_english.json and second_file_in_spanish.json)
have to be in CORRECT_LABEL folder and you have to type filname extension).


HOW TO WORK WITH output_labels.csv:
Program CORRECT_LABEL.py saved a new file at your computer output_labels.csv. You can find the file in folder CORRECT_LABEL.
Open the file by Microsof Excel.
To split columns (instructions for Microsoft Excel 2010):
1. mark whole 'A' column,
2. press 'Data' on the front menu and then 'Text to Columns',
3. first window 'delimited' and next,
4. second window change delimiters for 'Comma' and next,
5. don't change anything, finish

In column 'D' you can find STATUS of label (MISSING, UNTRANSLATED, DELETED).
Now please fill empty fields for MISSING and UNTRANSLATED status label and delete unnecessary rows (with status -DELETED and without data,
by opption delete->shift cells up - for whole row).
*status DELETED - they are labels which program didn't find in english translation, they could be old and unnecessary label. Please check them and in 
case they are not required please delete whole row (by opption delete->shift cells up). 
When work is finish save all changes and close csv file. Go to next step 'HOW TO OPEN CORRECT_LABEL_second_step'.


HOW TO OPEN CORRECT_LABEL_second_step:
Please make sure that you are still at the same pleace in command line interpreter ('C:\Users\User\Desktop\CORRECT_LABEL>').
*If you have a problem, please find solution in internet your goal is to get this path - "C:\Users\User\Desktop\CORRECT_LABEL>" on the screen. 
Now please type 'python CORRECT_LABEL_second_step.py' and press enter to start program. 

Then follow instructions in program CORRECT_LABEL_second_step.py (keep in mind that files which you want to attache to program (output_labels.csv) have to be in CORRECT_LABEL 
folder and you have to type filname extension.

Also you can use IDLE for execute whole program if you want.
