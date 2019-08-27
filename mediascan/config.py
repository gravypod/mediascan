from os import getenv

default_media_extensions = 'mkv,mp4,m4a,m4v,f4v,f4a,m4b,m4r,f4b,mov,ogg,oga,ogv,ogx,webm,flv,avi,wmv,mov'

MEDIA_EXTENSIONS = getenv('APP_MEDIA_EXTENSIONS', default_media_extensions).split(',')
MEDIA_FOLDER = getenv('APP_MEDIA_FOLDER', '/data')
