# <div align="center"> Weather Report </div>

Weather Report is a Python program that returns a range of weather information for a given zip-code using the Weather Underground API.

This program can return the following weather information:
* Current conditions for the given location
* 10 day forecast for the given location
* Sunrise and sunset times for the given location
* Any current weather alerts for the given location
* A list of all active named tropical storms

## <div align="center"> Instructions </div>

* Before the user can run the Weather Report program on their computer, the user must first clone the `weather-report` repo onto their computer. The user will need to create a virtual environment running Python 3 in the `weather-report` repo folder.
* To properly run the program, the contents of requirements.txt must be installed.
  * After navigating to the folder containing `requirements.txt`, enter `pip install -r requirements.txt` on the command-line to download the contents of requirements.txt.
* This program requires the user to apply for a Weather Underground API key. After acquiring the key the user must set that key as an environmental variable. Currently this program is setup to use the environmental variable 'WUNDER_KEY' to represent the API key.
* The user can then enter `python weather_report_output.py` on the command-line to open the Signs of Regression notebook.
