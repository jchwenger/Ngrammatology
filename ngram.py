corpora = {
    'English': 15,
    'British English': 18,
    'American English': 17,
    'French': 19,
    'German': 20,
    'Italian': 22
}

def ngram_url(kwords,
              year_start='1900',
              year_end='2008',
              corpus='English'):
    
    params = { 
        'year_start': year_start,
        'year_end': year_end,
        'corpus': corpora[corpus],
        'kwords': kwords
    }

    content = '%2C'.join(params['kwords']).replace(' ', '+')
    direct_url = '.'.join(['t1%3B%2C' + kword.replace(' ', '%20') + '%3B%2Cc0' for kword in params['kwords']])
    
    ngram_string = "https://books.google.com/ngrams/interactive_chart?content={}&\
                    year_start={}&\
                    year_end={}&\
                    corpus={}&\
                    smoothing=3&\
                    share=&\
                    direct_url={}"\
                        .format(content, 
                                params['year_start'], 
                                params['year_end'],
                                params['corpus'],
                                direct_url)\
                        .replace(' ', '') # remove all white space

    return ngram_string
