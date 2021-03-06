The Tech Academy - GUI Drill 3

Drill Description:
For this drill, you will need to gather all of the drills that you have previously completed for this course
and write a new script that will use each of the concepts that you had previously used to complete this 
drill assignment.

Your new script will need to provide the user with a graphical user interface that includes two buttons 
allowing the user to browse their own system and select a source directory and a destination directory. 
Your script should also show those selected directory paths in their own corresponding text fields.

Next, your script will need to provide a button for the user to execute a function that should iterate 
through the source directory, checking for the existence of any files that end with a �.txt� file 
extension and if so, cut the qualifying files and paste them within the selected destination directory.

Finally, your script will need to record the file names that were moved and their corresponding modified 
time-stamps into a database and print out those text files and their modified time-stamps to the console.

Requirements:
Your script will need to use Python 3, the Tkinter module, and the OS module.

Your script will need to use the listdir() method from the OS module to iterate through all files within 
a specific directory.

Your script will need to use the path.join() method from the OS module to concatenate the file name to 
its file path, forming an absolute path.

Your script will need to use the getmtime() method from the OS module to find out the latest date the 
file has been created or last modified.

Your script will need to create a database to record the qualifying file and corresponding modified 
time-stamp.

Your script will need to print each file ending with a �.txt� file extension and its corresponding 
mtime to the console.

Your script will need to use the move() method from the Shutil module to cut all qualifying files 
and paste them within the destination directory.

------------------------------------------------------------------------------------------------------

Please use  the 'test-directory' folder (which has two .txt files) and paste in the any
folder you'd like.

**Try to find the bugs on this program. You Might just find some!

Nicson Martinez
5/17/19

