<b>I. SUMMARY:</b>
- This was an assignment for my Intro to Cloud Computing class. It demonstrated knowledge of the following AWS services: Elastic Beanstalk, S3, EC2, VPC, and RDS.
- The app tells the weather (in Farenheit) based on the city typed in the search bar. The coordinates of the city and an image denoting the weather are also shown.
- This assignment consists of several files. A report pdf is included in this repository under the name "CarlosMendoza_WeatherWebAppDeploymentDocumentationReport" to further detail what the app is about and how I got it to run with AWS's services.
- Unfortunately, due to my AWS free tier timing out and the monthly costs I would have to pay for setting up the services, I'm unable to have a video of my AWS app in action.
  - As an alternative, I created a version of the web app in the "NonAWSVersion" folder that does exactly what the AWS app does with the exception of database and bucket integration due to a lack of the RDS and S3 services respectively.

<b>II. HOW TO RUN (The non-AWS version):</b>
- First, create a virtual environment in order to use the flask module for the app. This is done by typing "python3 -m venv env" while in the "NonAWSVersion" repository in the cmd terminal. (The commands mentioned in this section apply to Windows only)
- Then, open/ access the virtual environment by typing "env\Scripts\activate"
- Now, in the virtual environment, install flask with "pip install flask"
- Set up the python file as a flask app with "set FLASK_APP=application.py"
- Finally, run the app with "flask run"
  - Copy and paste the localhost address into your browser to use the web app

<b>III. VIDEO OF APP IN ACTION:</b>
- youtube.com
