

# SEPTA Broad Street Line (BSL) Consolidated Schedule - with color added!

Welcome to my first *something-I-want* Python project. I sporadically use SEPTA's online consolidated BSL schedule to plan downtown excursions.  I don't use those lines regularly.  I had a terrible time figuring out which row on the chart represents the Express and which is the 8th-&-Market.  
 
---
## Specifications

So the goal was to *color-tint* rows on chart; use Septa BSL color scheme: Orangey-Yellow=8th & Market, Green=Express. 


---
## Results
 
Septa Schedule - Before

![BSL no color](images/Before.png)

Septa Schedule - After

![BSL color](images/After.png)


---
## My Take-Aways with this Project
 
- I never heard of regular expressions before doing this project.  Very useful parsing tool
- I learn more AND faster when learning in context with a specific goal

---
## Status

Before starting this project: 

- I took a $25 weekend Python course
- I watched 25 Django videos and did the exercises

I wrote the code with methods I knew of at the time. My project is giving me the results I want, but I know the code could be better.  I purchased TalkPython's `10 Python Apps` course, and Wow!....what  I did not know.  https://training.talkpython.fm/

Some of the future improvements will be:
- use BeautifulSoup to pull the original webpage, instead of copy pasting; add status checking
- Use RegEx more accurately
- replace some of the looping with list comprehensions and generator expressions
- use truthiness in my IFs
- use more function construction
- create a cronjob to run the process

The work is never DONE.


 