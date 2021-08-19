import requests
import os

def download_user_contents(data):
    full_name = data['results'][0]['name']['first']+" "+data['results'][0]['name']['last']
    try:
        large_pic = data['results'][0]['picture']['large']
        lg_r = requests.get(large_pic)
        # os.makedirs(f'/{full_name}/large_pic/', exist_ok=True) 
        with open('large_pic/{0}.jpg'.format(full_name),'wb') as f:
            f.write(lg_r.content)
        print(f'Large Picture of user {full_name} is downloaded')
    except Exception as ex:
        print(ex)
    finally:
        pass
    try:
        medium_pic = data['results'][0]['picture']['medium']
        md_r = requests.get(medium_pic)
        # os.makedirs(f'/{full_name}/medium_pic/', exist_ok=True) 
        with open('medium_pic/{0}.jpg'.format(full_name),'wb') as f:
            f.write(md_r.content)
        print(f'Medium Picture of user {full_name} is downloaded')
    except Exception as ex:
        print(ex)
    finally:
        pass
    try:
        thumbnail = data['results'][0]['picture']['thumbnail']
        thumb_r = requests.get(thumbnail)
        # os.makedirs(f'/{full_name}/thumb_r/', exist_ok=True) 
        with open('thumb_r/{0}.jpg'.format(full_name),'wb') as f:
            f.write(thumb_r.content)
        print(f'Thumbnail Picture of user {full_name} is downloaded')
    except Exception as ex:
        print(ex)
    finally:
        pass

