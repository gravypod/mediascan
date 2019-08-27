import ffmpeg


def check(file_name: str) -> bool:
    """
    Perform a sanity check on a media file.
    :param file_name:
    :return:
    """
    stream = ffmpeg.input(file_name)
    stream = ffmpeg.output(stream, '-', format='null')
    try:
        ffmpeg.run(stream, quiet=True)
        return True
    except:
        return False
