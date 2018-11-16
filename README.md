# Logs Analysis Project
This project is the first project in Udacity's Full Stack Web Developer Nanodegree.

## Project Description
Develop a reporting tool written in Python program by using psycopg2 module to connect with newspaper articles database and answering three questions:
1. What are the most popular three articles of all time?
2. Who are the most popular article authors of all time?
3. On which days did more than 1% of requests lead to errors?

## Requirements
1. Python3
2. psycopg2
3. [Vagrant](https://www.vagrantup.com/)
4. [VirtualBox](https://www.virtualbox.org/)
5. Download	a	[FSND	virtual	machine](https://github.com/udacity/fullstack-nanodegree-vm)
6. Download the [newsdata.sql](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdat) and move them to your **vagrant** directory within your VM

#### Once	you	get	the	above	software	installed, run these commands from the terminal in the folder where your vagrant is installed in:
1. ```vagrant up``` to start up the VM.
2. ```vagrant ssh``` to log into the VM.
3. ```cd /vagrant``` to change to your vagrant directory.
4.  Clone this repository to your vagrant directory.
5. ```psql -d news -f newsdata.sql``` to load the data and create the tables.
6. ```python3 newsdata.py``` to run the reporting tool.
