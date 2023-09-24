# iCyPhy Website
Welcome to the website of iCyPhy.

# How to Use
## Jekyll Basics
For those unfamiliar with how Jekyll works, check out [jekyllrb.com](https://jekyllrb.com/) for all the details, 
or read up on just the basics of [front matter](https://jekyllrb.com/docs/frontmatter/), [writing posts](https://jekyllrb.com/docs/posts/), 
and [creating pages](https://jekyllrb.com/docs/pages/).

## Running the website locally
Simply run:
```bash
bundle install && bundle exec jekyll serve
```

## Adding a new publication
To add a new publication entry, simply add a .md file in the `_publication` folder with a front matter containing these
fields:
```
---
collection: publications
author: '...'
title: '...'
journal: '...'
volume: '...'
number: '...'
pages: '...'
abstract: '...'
paperurl: '...'
year: '...'
doi: '...'
---
```

An example entry is:
```
---
collection: publications
author: 'Martin A. Sehr, Marten Lohstroh, Mathew Weber, Ines Ugalde, Martin Witte, Joerg Neidig, Stephan Hoeme, Mehrdad Niknami, and Edward A. Lee'
title: 'Programmable Logic Controllers in the Context of Industry 4.0'
journal: 'IEEE Transactions on Industrial Informatics'
volume: '17'
number: '5'
month: 'May'
abstract: "Programmable Logic Controllers (PLCs) are an established platform, widely used throughout industrial automation but rather poorly understood among researchers. This paper gives an overview of the state of the practice, explaining why this settled technology persists throughout industry and presenting a critical analysis of the strengths and weaknesses of the dominant programming styles for today's PLC-based automation systems. We describe the software execution patterns that are standardized loosely in IEC 61131-3 and, where there are ambiguities in the standard, realized in concrete vendor implementations of PLCs. Ultimately, we identify opportunities for improvements that would enable increasingly complex industrial automation applications under the novel technical requirements associated with Industry 4.0 type environments without compromising the safety and reliability guaranteed by the current industrial automation technology stack."
paperurl: 'https://doi.org/10.1109/TII.2020.3007764'
year: '2021'
doi: '10.1109/TII.2020.3007764'
---
```

# Credits

This Jekyl site is based on the "Forty" theme by [HTML5 UP](https://html5up.net/).  
