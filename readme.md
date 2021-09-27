# pixiv-bookmarks-sync
## Synchronize your Pixiv favorite bookmarks to local storage

Have you ever got into such a circumstance: you want to find a brilliant illust which you have saved to your favorite bookmarks, but only to find nothing excepet a line "削除済みまたは非公開"?

Here this tool, based on [pixivpy](https://github.com/upbit/pixivpy), can help you download your favorite illusts in bookmarks to local storage, where you can always find what you want.

### Start

1. Firstly clone this tool, of course.
```
git clone https://github.com/BeautyYuYanli/pixiv-bookmarks-sync.git
cd pixiv-bookmarks-sync
```
2. Get your Pixiv `refresh_token`, see [this article](https://gist.github.com/ZipFile/c9ebedb224406f4f11845ab700124362)
3. Run `cp config_example.py config.py`, then edit `config.py` following the comments in it.
4. For your first use, run `python main_first.py`, to download all your bookmarks.
5. Run `python main.py`, to download your recently added bookmarks.
6. Check your favorite illusts in the folder `download/imgs/`, with sort by "modified time", recommended.

### Other

A similar tool is [music-down-bili](https://github.com/BeautyYuYanli/music-down-bili)