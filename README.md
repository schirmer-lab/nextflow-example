# HolyQuote

This is a fun little project to get familiar with [Nextflow](https://www.nextflow.io/).

Here you can generate a random quote from the masterpiece "*Monty Python and the Holy Grail.*"

When running this project with:

``` bash
nextflow run .
```
it will:

1. Download the script from https://www.sacred-texts.com/neu/mphg/mphg.htm#Scene%2035,

2. Convert it into a clean .txt file,

3. Pick a random quote.

These steps are connected using Nextflow processes and workflows.

---
## Customizing the quote length
You can adjust the minimum number of words for the selected quote by using the --min_words parameter.
For example, to require a quote with at least 10 words:
```
nextflow run . --min_words 10
```
---
Enjoy - and remember:
```
 GUARD #2:  It could be carried by an African swallow!
 GUARD #1:  Oh, yeah, an African swallow maybe, but not a European swallow, that's my point.
```
