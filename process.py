import os
import re
import io
import itertools

def process_srt(file_name):
    regex=re.compile(r'^[0-9]+$')
    time_index=re.compile(r'[0-9]{2}[:][0-9]{2}:[0-9]{2}[,][0-9]+\s[-]{2}[>]\s[0-9]{2}[:][0-9]{2}[:][0-9]{2}[,][0-9]+')
    f=io.open(file_name,mode="r",encoding="utf-8")
    new_filename=os.path.splitext(file_name)[0] + ".txt"
    text=f.read()
    text.split('\n')
    text_list=text.split('\n')
    filt=[x for x in text_list if not regex.search(x)]
    filt=[x for x in filt if not time_index.search(x)]
    
    filt=[x.replace(r'</i>','').replace('<i>','') for x in filt]
    filt=[x.replace(r'♪ ','').replace(' ♪','') for x in filt]
    filt=[x.replace(r'<font color="#fffa00"> WWW.MY-SUBS.COM</font>','') for x in filt]
    filt=[x.replace('\ufeff1','') for x in filt]
    filt=[x for x in filt if len(x) != 0]
    return filt
    
def clean_up(word_list):
    ret = [re.sub('[?!:\.,\[\]]$','',x) for x in word_list]
    ret = [re.sub('[?!:\.,\[\]]$','',x) for x in ret]
    ret = [re.sub('^[?!:\.,\[\]]','',x) for x in ret]
    ret = [re.sub('^[?!:\.,\[\]]','',x) for x in ret]
    ret=[re.sub('^[ ]','',x) for x in ret]
    ret=list(set(ret))
    ret.sort()
    return ret

def process_text(raw_words):
     numbers=re.compile(r'[0-9]+')
     ret=[re.sub('^["-?!.,\[\]]','',x) for x in raw_words]
     ret=[x for x in ret if not numbers.search(x)]
     ret=[re.sub('^[ ]','',x) for x in ret]
     ret=[re.sub('["?!:\.,\[\]]$','',x) for x in ret]
     ret=[re.sub('["]$','',x) for x in ret]
     ret=[re.sub('[.]+$','',x) for x in ret]
     ret=[re.sub('^[.]+','',x) for x in ret]
     
     ret=[x for x in ret if len(x) != 0]     
     return ret
          
def main():
    """
    srt_files=['dark-1-1-49116.srt',
    'dark-1-4-50981.srt',
    'dark-1-8-52393.srt',
    'dark-1-10-53751.srt',
    'dark-1-5-50996.srt',
    'dark-1-9-53736.srt',
    'dark-1-2-49123.srt',
    'dark-1-6-52363.srt',
    'dark-1-3-50966.srt',
    'dark-1-7-52378.srt']
    """
    srt_files=['dark-1-4-50981.srt']
    word_list=[]
    srt_files.sort()
    for srt_file in srt_files:
        
        print(srt_file)
        ret=process_srt(srt_file)
        
        ret=list(itertools.chain.from_iterable([x.split() for x in ret]))
        
        ret=list(set(ret))
        ret.sort()
        word_list.extend(ret)
        #print(ret[0:30])
    word_list=process_text(word_list)
    word_list=list(set(word_list))
    word_list.sort()
    print(word_list)
        
if __name__ == "__main__":
    main()
