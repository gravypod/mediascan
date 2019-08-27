from glob import iglob
from mediascan import config, sanity

for extension in config.MEDIA_EXTENSIONS:
    for media_file in iglob(config.MEDIA_FOLDER + '/**/*.' + extension, recursive=True):
        if sanity.check(media_file):
            # This file has passed our sanity check. Ignore it
            continue

        print(media_file)
