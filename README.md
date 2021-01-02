# universityassistanttool.github.io
This repository is an application software that allows user to get information about US universities, covering both the liberal arts colleges and national universities. I have used Python programming for implementing the ideas of speech recognition, google assistant, webscrapping to make a voice assistant that gives information about the rankings (world, US) and additional information (state, city, academics) about the US universities. In this repository, I have shared both the source and executable files. If you have problem downloading the files and running the .exe file, it may be due to your browser restricting to download accounting to the fact that the file comes from an unregistered author and there may be a virus threat. If so, force download while downloading and do run anyway while opening the .exe file. Else, download an IDE (PyCharm of JET Brains will be ideal) and just open the source files using it and then run the files. Here's the official link for the IDE download: https://www.jetbrains.com/pycharm/download/#section=windows.
The main program (main.exe) consists of 4 important things:

Object oriented approach for data scrapping and use: The data from The World University Ranking website, US news, and Niche.com are parsed and accessed from Parsehub server using .API method. Here, the loading of scrapped file and use of the data is modelled by the Data class.

Use of speech recognition: The speech recognition helps to take input from user in form of audio and record it. Google Assistant is used for this purpose.

Use of text to audio convertor: The instructions that the assistant gives to user is helped to be changed to audio.

Use of regular expressions (regx patterns): These expressions are used for pattern recognition and help to identify what exactly the user has said to do a particular task in accordance.
