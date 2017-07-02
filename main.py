from pyseo.seo_analyst import SEOAnalyst


if __name__ == '__main__':
    url = 'http://www.informador.com.mx'
    
    seo_analyst = SEOAnalyst(url)
    seo_analyst.analyse()
    

    # print(seo_analyst.url)
    # print(seo_analyst.meta_tags)
    # print(seo_analyst.title)
    # print(seo_analyst.headers)
    # print(seo_analyst.images)
    # print(seo_analyst.frames)
    print(seo_analyst.links)