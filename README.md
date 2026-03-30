python script to transfer google keep notes (extracted from [google takeout](https://takeout.google.com/)) to [siyuan ](https://github.com/siyuan-note/siyuan)

# Currently working
- bulk convert from keep .json -> .sy page
- keep note parraraph -> siyuan multi text node structure
- keep original created and edited timestamp (since siyuan uses individual edited dates for each node, all nodes will have the same edited timestamp from keep)

# TODO (PR's welcome)
[issues](https://github.com/Gambled23/quevedo/issues?q=sort%3Aupdated-desc+is%3Aissue+is%3Aopen)

# Requirements
- python
- google keep data from [takeout](https://takeout.google.com/) (be sure to download the one that includes json format)

# Instructions
1. [Download your google keep data](https://takeout.google.com/)
2. Clone this repository
3. Create a `/Keep` folder in the project directory and copy all you .json files there (no need to copy html and image files)
4. Run `main.py`
5. Copy all your .sy from `/output` folder to your siyuan notebook folder (in linux defaults to `~/SiYuan/data/notebook-folder/`)

# How to contribute
- Star
- Clone the repo and PR
- open [issues](https://github.com/Gambled23/quevedo/issues?q=sort%3Aupdated-desc+is%3Aissue+is%3Aopen) with bugs
