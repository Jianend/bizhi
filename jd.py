'''访问url'''
def get_json(url):
    try:
        hasattr = {'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.66 Mobile Safari/537.36 Edg/103.0.1264.44'}
        r = requests.get(url, headers=hasattr)
        return r.text
    except:
        print('完成')
        return 0


def main():
    
