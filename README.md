# bsg2024
Code to optimize portions of the Business Strategy Game 2024 season

Dependencies:
 - selenium.py
 - Firefox
 - geckodriver
 - Python 3.7 or greater
 - 
This code expects geckodriver to exist at `C:\Program Files\geckodriver\geckodriver.exe`. You can change this location at the top of `bsg2\sel_context.py`

Files:
`bsg.ipynb`: An IPython notebook that contains cells related to optimizing the BSG. Remmeber to set the username and password cell before opening. 
`sel_context.py`: sets up a BSG session. If future versions of the BSG move where the decisions page is located, change this file. 
`algs.py`: Basic algorithms that can optimize parts of the BSG. These are highly unoptimized, nasty as heck, and generally just there to get the job done. `target_two_select` is probably safe against the BSG changing but the rest isn't.
`bsg.py`: Contains environmental classes related to the BSG. This should be relatively safe against the BSG changing.
`bsg_actual.py`: Basically a big dictionary tree that mirrors the elements of the BSG. **IF THE BSG CHANGES THIS WILL PROBABLY BREAK.** It's not everything either (just the things I found useful). 

This codebase was built with multithreading in mind. All of the BSG algorithms take an `environment`, and `environment` keeps track of what changes were made. Doing `env <<= rhs` will apply the changes in `rhs` to `env`. 
Since multithreading in python is kind of junk, I've kept all the code out of this codebase. It was mostly useful to apply `optimize_production` to multiple regions at the same time. 


-----------------------------
This program is provided "as is" without warranty of any kind. I make no claims that it'll be useful in future iterations of the BSG, but I hope it helps. 
