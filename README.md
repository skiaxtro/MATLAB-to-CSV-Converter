# MATLAB-to-CSV-Converter
This project converts a MATLAB file from the [Paderborn Bearing Data Center](https://mb.uni-paderborn.de/kat/forschung/kat-datacenter/bearing-datacenter/data-sets-and-download) into a CSV file, including current phases.

Python version: 3.11.7

**Matlab_to_CSV_Folder.py**

The `Matlab_to_CSV_Folder.py` file takes a folder as input and converts the `.mat` files to CSV. The export is done in a new folder. Each file contains only the measurements for each current phase (it does not contain column titles and times). **Before running the file, make sure you have created the output folder.**
