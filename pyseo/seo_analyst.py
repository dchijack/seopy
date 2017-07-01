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

        # Get header tags
        self.headers = self.get_header_tags(html_site)

        # Get images
        self.images = self.get_images(html_site)

        # Get total frames
        self.frames = self.get_frames(html_site)

        # Get total iframes
        self.iframes = self.get_iframes(html_site)


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


    def get_header_tags(self, html_site):
        '''
        Get all header tags from the website
        '''

        header_tags = {}

        for i in range(1, 7):
            header_type = 'h'+str(i)

            header_tags[header_type] = []
            headers = html_site.find_all(header_type)

            for header in headers:
                header_text = header.getText().strip()
                tag_info = {'text': header_text, 'size': len(header_text)}

                header_tags[header_type].append(tag_info)

        return header_tags


    def get_images(self, html_site):
        '''
        Get all images in the web site
        '''

        images_tags = html_site.find_all('img')
        images = []

        for image in images_tags:
            tag_info = {'src': image.attrs['src']}

            if 'alt' in image.attrs:
                tag_info['alt'] = image.attrs['alt']

            images.append(tag_info)

        return images


    def get_frames(self, html_site):
        '''
        Get total frames in the website
        '''

        return len(html_site.find_all('frame'))


    def get_iframes(self, html_site):
        '''
        Get total iframes in the website
        '''

        return len(html_site.find_all('iframes'))