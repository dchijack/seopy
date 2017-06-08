from seopy.seo_analyst import SEOAnalyst


if __name__ == '__main__':
    url = 'http://www.informador.com.mx'
    
    seo_analyst = SEOAnalyst(url)
    seo_analyst.analyse()
    
    print(seo_analyst.url)
    print(seo_analyst.meta_tags)