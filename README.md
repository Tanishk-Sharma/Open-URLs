<div id="top"></div>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->


<!-- PROJECT LOGO -->
<br />
<div align="center">
    <img src="https://user-images.githubusercontent.com/32167236/137460481-3b7fb839-a59f-4c38-b24b-99088982a42d.png">
  <p align="center">
     A simple tool to open multiple URLs in your web browser at the click of a button!
  </p>
  <p align="center">
    This Repository contains the script as well as the standalone version for Windows.
  </p>
</div>

<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
    </li>
      <li>
      <a href="#usage">Usage</a>
    </li>
  </ol>
</details>

## About The Project

![logo](https://user-images.githubusercontent.com/32167236/137458368-473ce346-d295-4476-9eeb-2a51ab7cd3a9.png)

There can be times when we need to open many URLs but copy-paste every URL in a single tab and then opening another tab is just too tiring.
Instead, using python's webbroswer package, we can simple loop through our list of URLs and let the application open them for us.

<p align="right">(<a href="#top">back to top</a>)</p>

### Built With

The tool is very simple and built with the following:

* [Python 3.8.5](https://www.python.org/)
* [tkinter](https://docs.python.org/3/library/tkinter.html)
* [webbrowser](https://docs.python.org/3/library/webbrowser.html)
* [pyinstaller](https://pyinstaller.readthedocs.io/en/stable/index.html)

Command used to build standalone:
```pyinstaller --clean --onefile --name="Open URLs" --icon="logo.ico" --noconsole application.py ```

<p align="right">(<a href="#top">back to top</a>)</p>

## Getting Started

You may clone the repository and run the application.py script using:
python application.py

OR

You can download the Standalone .exe file and double click it. For Windows OS only.

## Usage

* Open the application.
* Enter URLs into the Text box.
* Click on 'Open URLs' button at the bottom.
* The application will open each URL in a new tab of your Default Browser.
* The application will close by itself after all URLs are loaded.

Note: If present, empty lines in input are skipped.
