# TreeMap
Tree Map is a simple tool that shows the positions of previously identified trees as a coloured dots on a map using GPS coordinates. The colour of each dot is determined by the score assigned to the tree from 0-10.

TreeMap runs on Python (v3.10) and uses several libraries including click, pandas and plotly (see requirements.txt for all information).

## Installation
Download [Python (3.10)](https://www.python.org/downloads/release/python-3109/) and the TreeMap repository. All dependencies for TreeMap are shown in the requirements.txt and can be installed using pip or anaconda. The command to install dependencies using pip is shown below.

    pip3 install -r requirements.txt

## Input Data

A blank data sheet with the required headers is available as part of this repository (example_data.xlsx). All data for TreeMap must provided using this exact format (or a dataset containing identically formatted headers). The standard data format has four headers:

#### 1. Tree
All trees must have a unique name. However, trees belonging to the same coppice should all have the same name.

#### 2. Score (0-10)
A score for each tree ranging from 0-10. This can represent any information (E.g Disease susceptibility) but MUST be included. If this is not required score all trees with the same number (E.g 0).

#### 3. North
The latitude GPS coordinate in decimal degrees format (E.g 40.689263)

#### 4. East
The longitude GPS coordinate in decimal degrees format (E.g 40.689263)

## Using TreeMap

TreeMap can be run using a single command (see below). When the command is run TreeMap will open a tab in your default web browser containing an interactive map of all the tree in the provided excel spreadsheet.

    python3 TreeMap.py <path to excel file>

## Additional Information

If you wish to discuss TreeMap, raise issues or collaborate please contact me [here](mailto:treemap@oliverpowell.com)

TreeMap was entirely developed by Oliver Powell (24/07/23).