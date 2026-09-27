# Module 1 — Git & GitHub

**Student:** Eliyah Rieluis J. De leon
**Date:** September 27, 2026

---

## What is Git? What is GitHub? (explain like you're teaching a friend who's never used either)

[Write your own explanation here. What problem does Git actually solve? How is GitHub different from Git itself?]

Git is a tool I use to keep track of changes in my code. It helps me save my progress and go back to an older version if I make a mistake.

GitHub is where I can upload my Git projects online. Git is mainly used on my computer, while GitHub lets me store and share the project online.

---

## Key vocabulary (in your own words)

- repository: Basically, it's the project folder that Git is tracking.
- commit: A way of saving the changes I made.
- branch: A separate copy of the project where I can work without 
  affecting the main branch.
- push / pull: Push sends my changes to GitHub, while pull gets
   changes from GitHub.
- pull request: A request to add my changes to another branch.
- merge conflict: It happens when Git finds different changes in  
   the same part of a file.   

---

## Walking through what I did

[Describe, step by step, a real branch → commit → push → PR you did. Include the actual commands you used.]

```
# paste your actual commands here
```
git status 
git checkout (my branch) 
git add . 
git commit -m "my commit message" 
git push -u origin (my branch)
---

## A mistake I made (or one I want to avoid)

[What tripped you up? A confusing error message, committing to the wrong branch, a merge conflict — explain it so a classmate reading this avoids the same mistake.]

I used the wrong GitHub URL when I tried to push my project. I accidentally included /tree/main/..., so Git couldn't find the repository.
I learned that I should check my remote using:
git remote -v
before pushing.
---

## How this connects to something else

[Optional: how does version control relate to anything else you've learned or used before?]

Git is useful in programming because it lets me keep track of my code and makes it easier to recover my old work if I mess something up.