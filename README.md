# VleRoute
VLE Route Planning Project.
In this Project , When we run the Django server we have to go to /upload URL to upload a Excel file containing all the details of the Villages for which the Route is to be Planned.
After Uploading the file, we then come back to our main/default URL to execute our python script which also takes the following Inputs - 1) Radius, 2) Latitude of VLE, 3) Longitude of VLE. 
The Python script contains an Algorithm that takes in Data from the Excel file just Uploaded and calculates the Distance between the VLE and the Villages using their coordinates and creates a Sorted list of Villages in Ascending order of its Distance from the VLE and Displays this list on the web. The VLE can then visit the villages According to the Order provided as that will be the most optimal path for him.
