import json, re, os
from pixivpy3 import AppPixivAPI
from config import refresh_token, userid

def login(refresh_token):
    global api
    api = AppPixivAPI()
    try: 
        api.auth(refresh_token=refresh_token)
    except:
        print('login error!')
        return 0
    else:
        return 1

def initDown():
    json_result = api.user_bookmarks_illust(userid)
    result = [json_result['illusts']]
    while 1:
        try:
            max_bookmark_id = json_result['next_url'].split('max_bookmark_id=')[1]
            print(max_bookmark_id)
            json_result = api.user_bookmarks_illust(userid, max_bookmark_id=max_bookmark_id)
            tmp_result = []
            for i in json_result['illusts']:
                tmp_result.insert(0, i)
            result.insert(0, [x for x in tmp_result])
        except:
            break
    print('done')
    result = [j for i in result for j in i]
    # download result
    final_result = []
    for i in result:
        try:
            download(i)
        except:
            print('error ' + str(i['id']))
        else:
            final_result.append(i)
    with open('result.json', 'w') as f:
        f.write(json.dumps(final_result))

def appendDown():
    json_result = api.user_bookmarks_illust(27956418)
    new_result = json_result['illusts']
    with open('result.json', 'r') as f:
        result = json.loads(f.read())
    for i in new_result:
        if i['id'] not in [j['id'] for j in result]:
            try:
                download(i)
            except:
                print('error ' + str(i['id']))
            else:
                result.append(i)
                # pass
    with open('result.json', 'w') as f:
        f.write(json.dumps(result))

def download(i):
    # download result
    artname = re.sub(r'[\/\\:*?"<>|]', '', (i['title']+i['user']['name']))
    if i['page_count'] == 1:
        url = i['meta_single_page']['original_image_url']
        api.download(url, path='./download/imgs', name=artname+os.path.basename(url))
    else:
        for k in i['meta_pages']:
            url = k['image_urls']['original']
            api.download(url, path='./download/imgs', name=artname+os.path.basename(url))
    with open(os.path.join('./download/info/', artname + str(i['id']) + '.json'), 'w') as f:
        f.write(json.dumps(i))
    print('done: ' + i['title'])

def main():
    if not os.path.exists('download'):
        os.makedirs('download')
    if not os.path.exists('download/imgs'):
        os.makedirs('download/imgs')
    if not os.path.exists('download/info'):
        os.makedirs('download/info')
    if (login(refresh_token) == 1):
        # initDown()
        appendDown()

if __name__ == '__main__':
    main()