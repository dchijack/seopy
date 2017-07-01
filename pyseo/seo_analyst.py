import requests

from bs4 import BeautifulSoup


class SEOAnalyst:

    def __init__(self, url):
        self.url = {'text': url, 'size': len(url)}


    def analyse(self):
        ''' 
        Analyse the URL and separate the SEO information by variables
        '''
        
        request = requests.get(self.url['text'])
        html_site = BeautifulSoup(request.text, 'html.parser')

        # Get meta tags
        self.meta_tags = self.get_meta_tags(html_site)

        # Get title
        self.title = self.get_title(html_site)


    def get_meta_tags(self, html_site):
        '''
        Get the meta tags from the website, including Facebook and Twitter tags
        '''

        tags = html_site.find_all('meta')
        meta_tags = {'facebook': [], 'twitter': [], 'meta_tags': []}

        for tag in tags:
            if 'property' in tag.attrs:
                tag_info = {'property': tag.attrs['property'], 'content': tag.attrs['content']}
                meta_tags['facebook'].append(tag_info)
            else:
                if 'name' in tag.attrs:
                    tag_info = {'name': tag.attrs['name'], 'content': tag.attrs['content']}

                    if tag.attrs['name'].startswith('twitter'):
                        meta_tags['twitter'].append(tag_info)
                    else:
                        meta_tags['meta_tags'].append(tag_info)

        return meta_tags


    def get_title(self, html_site):
        '''
        Get the title from the website
        '''

        title = html_site.find('title').getText()
        title_tag = {'text': title, 'size': len(title)}

        return title_tag
