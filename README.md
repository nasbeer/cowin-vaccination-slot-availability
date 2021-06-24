# CoWIN vaccination slot availability using Python

Script to check the available slots for Covid-19 Vaccination Centers from CoWIN API in India. This CANNOT book slots automatically. The Indian Government had blocked the API for crawlers, but we are good to go.

<p align="center">
  <img src=https://socialify.git.ci/bhattbhavesh91/cowin-vaccination-slot-availability/image?font=KoHo&forks=1&language=1&owner=1&pattern=Charlie%20Brown&stargazers=1&theme=Dark>
</p>

**If you like my work, you can support me by buying me a coffee by clicking the link below**

<a href="https://www.buymeacoffee.com/bhattbhavesh91" target="_blank"><img src="https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png" alt="Buy Me A Coffee" style="height: 41px !important;width: 174px !important;box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;-webkit-box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;" ></a>

<!---
[Click to view the Website](https://bit.ly/3eQkvgl)
[Click to view the Website](https://bit.ly/3ob9l94)
-->

The [CoWin API](https://apisetu.gov.in/public/marketplace/api/cowin) currently states : "Further, these APIs are subject to a rate limit of 100 API calls per 5 minutes per IP". I tried deploying the Web Application but the API is blocking the request. You can easily run the web application on your machine by following the steps mentioned below.
&nbsp;
# Update
I am humbled to see the overwhelming response that this project has received so far. Feel free to create amazing applications on top of this project. Due to my schedule, I won't be able to allot more time to this project. So there won't be any additional commits to this project.

# Installing Python
Python is a programming language that is powerful but easy to learn. It is free, platform-independent, and popular among scientists.

## Recommended Method: Anaconda
The Anaconda Python distribution is an easily-installable bundle of Python and many of the libraries used throughout this class. Unless you have a good reason not to, we recommend that you use Anaconda.

### Mac/Linux users
1. Download the [appropriate version](https://www.anaconda.com/products/individual) of Anaconda
2. Follow the instructions on that page to run the installer
3. Test it out: open a terminal window, and type ``python``, you should see something like
```
Python 3.8.3 (default, Jul  2 2020, 17:30:36) [MSC v.1916 64 bit (AMD64)] :: Anaconda, Inc. on win32
```
If `Anaconda` doesn't appear on the first line, you are using a different version of Python. See the troubleshooting section below.

1. Test out the IPython notebook: open a Terminal window, and type `ipython notebook`. A new browser window should pop up. 
2. Click `New Notebook` to create a new notebook file
3. Update IPython to the newest version by typing `conda update ipython` at the command line

### Windows Users
1. Download the [appropriate version](https://www.anaconda.com/products/individual) of Anaconda
2. Follow the instructions on that page to run the installer.
3. Go to Start and Run Jupyter Notebook.
4. Click `New Notebook`, which should open a new page.

# Usage
- Clone the repository. using `! Git Clone https://github.com/bhattbhavesh91/cowin-vaccination-slot-availability.git `
- The tool only works with Indian IP addresses so disconnect your VPN if needed.
- Enter the command - `cd cowin-vaccination-slot-availability/`
- Install all the dependencies - `! pip3 install -r requirements.txt`
- Run Anaconda Promt (Run as Administrator) From Start Menu.
- Go to your Directory Eg `cd C:\Users\lenovo\Desktop\Jupyter Notebooks\2021\Cowin\cowin-vaccination-slot-availability`
- Run `streamlit run app.py`

-   You can now view your Streamlit app in your browser.

  Local URL: http://localhost:8501
  Network URL: http://192.168.1.7:8501
