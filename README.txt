Recuired programs: Miscrosoft Excel, Python 3.6.1 (or older version of Python 3)

If you don't have Python, please go to the website: https://www.python.org/downloads/ . Downloade and instal program,
following instructions from website (you can find the version and instruction for different OS - Windows, LINUX/UNIX and others).

Rest of instructions are for Windows operating system (for more information about using application with others OS please search in internet) 
*All outputs are default save in folder C:\Users\User

HOW TO OPEN CORRECT_LABEL:
Please find the exact path of file CORRECT_LABEL.py 
To do this you can:
1. open your start menu, 
2. type CORRECT_LABEL.py and press right button of mouse to open properites,
3. in the 'General' window there is the line:'localization'where you can find the exact path (example: C:\Users\Ula\PycharmProjects). 
Now open command line interpreter from your start menu and type:
python path\CORRECT_LABEL.py (where path is the exact path which you already found example: python C:\Users\Ula\PycharmProjects\CORRECT_LABEL.py)
Press 'Enter' to start program. 

Then follow instructions in program CORRECT_LABEL.py (keep in mind that before name of file you want to analise you have to type 
exact path, use the same method to find it as before - example C:\Users\Ula\PycharmProjects\CORRECT_LABEL\first_file_in_english.json).


HOW TO WORK WITH output_labels.csv:
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
Please find the exact path of file CORRECT_LABEL_second_step.py (you can find instruction for it in part 'HOW TO OPEN CORRECT_LABEL')

Now open command line interpreter from your start menu and type:
python path.CORRECT_LABEL_second_step.py (where path is the exact path which you already found)

Then follow instructions in program CORRECT_LABEL_second_step.py (keep in mind that before name of file you want to analise you have to type 
exact path, use the same method to find it as before - example C:\Users\Ula\PycharmProjects\CORRECT_LABEL\good_translated.txt).


Also you can use IDLE for execute whole program if you want.
