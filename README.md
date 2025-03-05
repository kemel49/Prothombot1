# Prothombot1
A [telegram bot](https://t.me/prothom1bot) that could convert any twitter/X url into wikipedia {{[Cite tweet](https://en.wikipedia.org/wiki/Template:Cite_tweet)}} Template to use in Wikipedia.
> Required libraries:
> ```python
> pip install re requests tweepy
> ```
> Required credentials:
> - Telegram Bot API
> - Twitter developer bearer token
## Background
[Citer tool on toolforge](https://citer.toolforge.org/) is a perfect example of how ProthomBot exactly works. It was [suggested to include the same facility](https://meta.wikimedia.org/wiki/User_talk:Dalba#Suggestion_to_include_tweeter_template) in citer tool, but twitter/X done very well with their system so it's impossible to get the title parameter for {{Cite tweet}} template.
## Function
This Telegram Bot can convert any twitter/X url into Wikipedia Citation family template {{Cite tweet}}
> Example:
> `https://x.com/anyuser/status/20` will produce
> ```wikitext
> {{Cite tweet |user=anyuser |title=Tweet content |number=20 |access-date={{subst:Date}}}}
> ```
## Known issue
- Due to rate limit in twitter api usage, you may encounter reply like `Tweet not found or doesn't exist.` this is because the twitter API cannot provide required data. You can prevent this issue by removing all tweepy functions and filling the title parameter manually.
- Line breaks will be rendered as it is, while wikipedia would throw error at line break. remember to remove line break in title field.
- You have to add an additional `|date` field with original tweet date, if you are using tweet posted before November 4, 2010 UTC.

## Licence
[![CC BY-SA 4.0][cc-by-sa-shield]][cc-by-sa]

This work is licensed under a
[Creative Commons Attribution-ShareAlike 4.0 International License][cc-by-sa].

[![CC BY-SA 4.0][cc-by-sa-image]][cc-by-sa]

[cc-by-sa]: http://creativecommons.org/licenses/by-sa/4.0/
[cc-by-sa-image]: https://licensebuttons.net/l/by-sa/4.0/88x31.png
[cc-by-sa-shield]: https://img.shields.io/badge/License-CC%20BY--SA%204.0-lightgrey.svg
