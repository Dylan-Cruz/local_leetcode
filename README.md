# local_leetcode
A util to automate pulling information from leetcode for a problem into a local project directory. 

## Usage
The script takes two parameters positionally. Call the script with -h for more info but in short, they're a URL to a leetcode problem and a filepath to the directory where you want the output in that order. 

Example Usage:
```
python3 ./local_leetcode/script.py "https://leetcode.com/problems/count-elements-with-maximum-frequency/description" "/home/dylan/Documents"
```
## Output
There are four files generated:
1. **problem.md** - a markdown version of the leetcode problem description
2. **solution.py** - a py file containing the solution stub from the leetcode code editor
3. **write_up.md** - a markdown file containing a stub to do a write up on the problem
4. **meta.json** - a json file containing the scraped data for future processing

## Todo
- handle cases where the class isn't named solution
- parameterize the browser
- make the browser headless
    - chrome headless gets blocked by cloudflare, try firefox
    - try undetected-chromedriver https://pypi.org/project/undetected-chromedriver/
    - try silenium stealth
- make scraping more stable and pessimistic
- add error handling
- add support for saving images locally for in descriptions?
- parameterize language
- add option to scrape more than one language
