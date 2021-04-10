# Application-on-ApacheHadoop_WordCount
This work mainly deals with getting all the total &lt;key, value> pairs from the page source code of any webpage. In this project, we are going to extract the source code of a webpage using a python code and take this as an input for the apache hadoop wordcount example and get the output of all &lt;key, value> pairs.> 

Initialy run the sourcecode.py in terminal. Then later on you get a txt file called iiitdm. 

NOTE: In this program, I'm trying to extrax the source code for the website : "https://iiitk.ac.in/"

After getting the iiitdm txt file, start all apache hadoop daemon processes and move this iiitdm file from local disk to HDFS system.
Run the WordCount program on the text file iiitdm, by following the below given command:

>> hadoop jar hadoop-mapreduce-examples-3.1.2.jar wordcount <input_directory> <output_directory>

The above commands runs mapreduce programs on the text file present in some of the <input_directory> and stores the final output in <output_directory>
