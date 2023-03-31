# frettabladid-scraper

`frettabladid-scraper` is a Python script to download editions of Fréttablaðið in bulk from [Fréttablaðið.is](www.frettabladid.is).

## Features

The script will iterate over a date period defined by the user and download a pdf file containing [Fréttablaðið](www.frettabladid.is) for a given day. The pdf-files download in a `pdfs` folder and a log of the download is saved in `log.txt`. Job status is printed to the console.

The script only downloads the main pdf file with containing whole paper. Special editions or subsets of the newspaper (_sérblöð_ etc.) are not downloaded.

## Installation and settings

1. Start by cloning the repository

`$ git clone https://github.com/thrkll/frettabladid-scraper.git`

2. Open `scraper.py` and define date range to be downloaded (year, month, day).

`start_date = datetime(2005, 12, 3)`

`end_date = datetime(2023, 3, 31)`

3. Run the script

`$ python3 scraper.py`

## Requirements

Python 3

[Requests](https://pypi.org/project/requests/)

## License

MIT License

Copyright (c) 2023 Þorkell Einarsson

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
