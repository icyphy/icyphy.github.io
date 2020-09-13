import scrapy
import bibtexparser
import os
import re
from bibtexparser.bparser import BibTexParser
import hashlib

class IcyphySpider(scrapy.Spider):
    name = 'icyphy_pub'
    custom_settings = {
        'CONCURRENT_REQUESTS': '16'
    }

    count = 0
    start_urls = [
        'https://ptolemy.berkeley.edu/projects/icyphy/pubs/search/2012.html',
        'https://ptolemy.berkeley.edu/projects/icyphy/pubs/search/2013.html',
        'https://ptolemy.berkeley.edu/projects/icyphy/pubs/search/2014.html',
        'https://ptolemy.berkeley.edu/projects/icyphy/pubs/search/2015.html',
        'https://ptolemy.berkeley.edu/projects/icyphy/pubs/search/2016.html',
        'https://ptolemy.berkeley.edu/projects/icyphy/pubs/search/2017.html',
        'https://ptolemy.berkeley.edu/projects/icyphy/pubs/search/2018.html',
    ]
    # start_urls = ['https://ptolemy.berkeley.edu/projects/icyphy/pubs/search/2017.html']

    # Create manifest file, which provides a reference in case future scrapes
    # yield 

    # This also generate Request for sidebar buttons.
    # But it is fine since they do not have <pre> tags.
    def parse(self, response):
        for pub in response.css('li'):
            pub_page = pub.css('a::attr(href)').get()
            if pub_page is not None:
                pub_page = response.urljoin(pub_page)
                yield scrapy.Request(pub_page, callback=self.parse_pub)

    # Parse BibTex and generate .md file with respective fields
    def parse_pub(self, response):
        
        # Declare a custom parser to accept @presentation
        parser = BibTexParser()
        parser.ignore_nonstandard_types = False

        for citation in response.css('li pre'):
            pre = citation.css('pre::text').get()
            # print(pre)
            if "@article" in pre or "@presentation" in pre:
                bib = bibtexparser.loads(pre, parser).entries_dict
                print(bib)

                # Search for links
                links = response.css('li a::attr(href)').getall()
                # print(links)

                # Save the ones that contain links to papers 
                keywords = ['pdf', 'pptx', 'ieee', 'doi']
                lnks = [l for l in links if any(kw in l for kw in keywords)]
                for i in range(len(lnks)):
                    if 'https' not in lnks[i]:
                        lnks[i] = 'https://ptolemy.berkeley.edu' + lnks[i]
                print(lnks)

                # Extract id from dictionary
                _id = list(bib.keys())[0]

                # Replace Ptolemy link with the new link
                bib[_id]['url'] = 'http://icyphy.org/publications/' + _id

                # Remove "and" in authors
                bib[_id]['author'] = bib[_id]['author'].replace(' and', ',')
                for k in list(bib[_id].keys()):
                    bib[_id][k] = bib[_id][k].replace('\n', '')
                    bib[_id][k] = bib[_id][k].replace('\\', '')

                # Creates a unique filename
                self.count = self.count + 1
                _author = bib[_id]['author'].split(',')
                if len(_author) > 1:
                    _author = _author[0].split()[-1] + 'EtAl'
                elif len(_author) == 1:
                    _author = _author[0].split()[-1]
                else:
                    print('Expect author field to be non-empty.')
                    raise ValueError
                filename = '../_publications/' + bib[_id]['year'] + '_' \
                            + _author + '.md'

                subscript = 1
                while(os.path.exists(filename)):
                    subscript += 1
                    filename = '../_publications/' + bib[_id]['year'] + '_' \
                                + _author \
                                + '_' + str(subscript) \
                                + '.md'
                print(filename)

                # Generate markdown
                with open(filename, 'a') as f:
                    f.write('---\n')
                    f.write('collection: publications\n')
                    for k, v in bib[_id].items():
                        f.write(k + ': ' + '\'' + v + '\'' + '\n')
                    f.write('paperurl: ' + str(lnks) + '\n')
                    f.write('---\n')

