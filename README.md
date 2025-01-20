# oac_recommendations
A repo that houses the recommendation workflow built to aid better identification of gaps in the OAC's funding

<br/>

## Event Recommender System - “How to” Guide

This project implements a recommender system to suggest what kind of events will benefit more diverse people in a specific county in Oklahoma.

<br/>

### Project Structure

The project is organized into several folders:
- **Utils.py**: This file contains custom functions for calculating diversity and the core recommender system code.
- **models.py**: This file provides methods to load data from and save data to pickle files.
- **Counties.py**: This file contains a list of counties in Oklahoma.
- **app.py**: This file contains the Flask implementation for the web application.
- **Data**: This folder stores the clean and processed data used by the application. (data removed before the repo is made public)
- **templates**: This folder contains the HTML files that define the web interface design.
 
<br/>

### How to Use the Project
1.	**Prerequisites**: Ensure you have Python and any required libraries installed (these can be found in the project's requirements.txt file).
2.	**Running the Application**: 
    - Navigate to the project directory in your terminal.
    - Run the command python app.py.
    - This will start the Flask development server, typically accessible at http://127.0.0.1:5000/ in your web browser.

<br/>

### Please watch the demo video to get a quick idea of how it's supposed to look if you end up running it. 
#### **Note**: The video will not capture the dropdown menu
