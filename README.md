# MDSurvey
### Installation Instructions:

1. **Install Visual Studio Code (VSCode):**
   - Visit the [Visual Studio Code website](https://code.visualstudio.com/) and download the installer for your operating system (Windows, macOS, or Linux).
   - Follow the installation instructions provided on the website to install Visual Studio Code on your computer.

2. **Install Python:**
   - Visit the [Python website](https://www.python.org/downloads/) and download the latest version of Python for your operating system.
   - Run the downloaded installer and follow the installation instructions provided.
   - During the installation process, make sure to check the box that says "Add Python to PATH" or "Include Python in PATH" to ensure Python is added to your system's PATH environment variable.

3. **Clone the MDSurvey Repository:**
   - Open VScode look for the tab that says terminal, and press (New Terminal).
   - Run the following command to clone the MDSurvey repository to your local machine:
     ```
     git clone https://github.com/DexterW1/MDSurvey.git 
     ```
   - This will create a new directory called `MDSurvey` in your current location and clone the repository contents into it.

5. **Install Dependencies:**
   - Navigate to the `MDSurvey` directory that you cloned in the previous step (`cd MDsurvey`).
   - Run the following command to install the project dependencies using `pip`:
     ```
     pip install -r requirements.txt
     ```
   - This command will install all the required Python packages specified in the `requirements.txt` file.

6. **Insert Survey Codes:**
   - Open the `voiceReceipts.txt` file located in the `MDSurvey` directory using a text editor (such as VSCode).
   - Insert your survey codes into the file, with each code on a separate line.
   - Save the changes to the `voiceReceipts.txt` file.

7. **Run the Main Script:**
   - In the terminal or command prompt, navigate to the `MDSurvey` directory.
   - Run the following command to execute the main Python script:
     ```
     python main.py
     ```
