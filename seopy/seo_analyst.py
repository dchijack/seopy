import requests

from bs4 import BeautifulSoup


class SEOAnalyst:

    def __init__(self, url):
        self.url = url


    def analyse(self):
        request = requests.get(self.url)
        html_site = BeautifulSoup(request.text, 'html.parser')
        
        # Get meta tags
        self.meta_tags = self.get_meta_tags(html_site)


    def get_meta_tags(self, html_site):
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