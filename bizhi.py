

import os
import requests
import time
import logging
import sys
import threading


logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def get_image_url(api_url):
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.66 Mobile Safari/537.36 Edg/103.0.1264.44'}
        response = requests.get(api_url, headers=headers)
        data = response.json()
        image_url = data.get('data', [{}])[0].get('urls', {}).get('original')
        return image_url
    except Exception as e:
        logging.error(f"Failed to get image URL: {e}")
        return None

def download_image(image_url, filename):
    try:
        response = requests.get(image_url)
        response.raise_for_status()
        with open(filename, 'wb') as f:
            f.write(response.content)
        logging.info(f"Image downloaded: {filename}")
        return True
    except Exception as e:
        logging.error(f"Failed to download image: {e}")
        return False

def main():
    api_url = 'https://api.lolicon.app/setu/v2?r18=1'
    image_url = get_image_url(api_url)
    if not image_url:
        return

    filename = os.path.basename(image_url)
    try:
        download_image(image_url, filename)
    except Exception as e:
        logging.error(f"Failed to process image: {e}")

def show_progress():
    symbols = ['\\', '|', '/', '—']
    i = 0
    
    while True:
        sys.stdout.write(f"\r程序正在运行 {symbols[i % len(symbols)]}")
        sys.stdout.flush()
        time.sleep(0.25)
        i += 1

if __name__ == "__main__":
    try:
        progress_thread = threading.Thread(target=show_progress)
        progress_thread.start()
        
        while True:
            main()
            time.sleep(10*60)  # Download image every 10 minutes
            
        progress_thread.join()
    except KeyboardInterrupt:
        logging.info("程序已停止")
