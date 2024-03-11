# local_leetcode
A util to automate pulling information from leetcode for a problem into a local project directory. 

## Usage
The script takes two parameters positionally. Call the script with -h for more info but in short, they're a URL to a leetcode problem and a filepath to the directory where you want the output in that order. 

Example Usage:
```
python3 ./local_leetcode/script.py "https://leetcode.com/problems/count-elements-with-maximum-frequency/description" "~/Documents"
```

## TODO
- make the browser headless
    - chrome headless gets blocked by cloudflare, try firefox
    - try undetected-chromedriver https://pypi.org/project/undetected-chromedriver/
    - try silenium stealth
- make scraping more stable and pessimistic
- add error handling
- add support for scraping images?
- parameterize language
- add option to scrape more than one language