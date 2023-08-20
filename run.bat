Sure! Here is the code for the run.bat file:

```
@echo off
echo Installing required packages...
pip install -r requirements.txt

echo Running the program...
python main.py

echo Done.
pause
```

To use this, create a new text file and copy the above code into it. Then, save the file with the name "run.bat". Make sure the "requirements.txt" file and the "main.py" file are in the same directory as the run.bat file.

To run the program, simply double-click the run.bat file, and it will install the required packages specified in requirements.txt and then run the main.py file.