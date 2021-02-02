from bing_image_downloader import downloader

query_string = input('what do you want images of?\n')
downloader.download(query_string, limit=100, adult_filter_off=True, force_replace=False)