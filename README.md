# BioDiversityHW
## Step 1 (Data Extraction) <br>
For the first step the data needed to be extracted from the sqlite database.<br>
There are 3 tables in the belly_button_diversity database <br>
a. otu <br>
b. samples <br>
c. samples_metadata <br>
The first step is to create routes and write SQLs to query the database and return the results in a JSON format.<br> 
FLASK web server has been used to render the data to the browser.<br>
Initial coding was done in Jupyter notebook, and each route was tested to verify that the data was being rendered correctly.<br>
The following routes were created
a. @app.route("/") : Renders the home page <br>
b. @app.route("/names") : Generates sample names <br>
c. @app.route("/otu") : Generates OTU descriptions <br>
d. @app.route("/otu_descriptions") : Genarates OTU IDs and descriptions <br>
e. @app.route("/metadata/<sample>") : Generates sample Meta Data <br>
f. @app.route('/wfreq/<sample>') : Genarates Wash Frequency <br>
g. @app.route('/samples/<sample>')  : Generates OTU IDs and Sample Values <br>

Next step was to take the Jupyter code and place it all in an editor like Pycharm(to check for formatting). <br>
Save the file with name app.py <br>

## Step 2(Visualisation of the data)
Data has been visualized using JavaScript and Plotly. The following data is diplayed:<br>
a. List of Samples <br>
b. Name value pair of each sample data <br>
c. Pie Chart of Sample <br>
d. Bubble Char of Sample <br>

#### Each of these charts re draw themselves when a Different sample is selected from the Sample dropdown list.

## Steps to execute the program <br>
1. cd to the folder where the app.py is stored <br>
Ensure that the following directory structures are set up a) Datasets for the database b) templates for index.html c) static for the Javascript file (app.js). <br>
2. run command python app.py <br>
3. Data rendering can be individually verified by going to each route separately e.g. <br>
#### http://127.0.0.1/5000/samples/BB_940 <br>
4. To view the plots run URL http://127.0.0.1/5000/. List Drpdowm, pie and bubble charts, key/value pair from the metadata JSON object  will be displayed for the first sample in the dropdown.<br>
5. Choose another sample from the dropdown list and the plots will redraw themselves.




