import urllib.request

def dl_jpg(url,file_path,file_name):
    full_path = file_path + file_name + '.jpg'
    urllib.request.urlretrieve(url,full_path)

url = input('Enter URL:')
file_name = input('Enter file name save as:')

dl_jpg(url,'Images/',file_name)