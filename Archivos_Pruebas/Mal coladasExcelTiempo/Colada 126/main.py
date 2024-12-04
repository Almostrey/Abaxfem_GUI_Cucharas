from PIL import Image
from datetime import timedelta, datetime
def get_date_taken(path):
    exif = Image.open(path)._getexif()
    if not exif:
        raise Exception('Image {0} does not have EXIF data.'.format(path))
    return exif[36867]

if __name__ == '__main__':
    year = int(get_date_taken("126C.jpg").split(" ")[0].split(":")[0])
    month = int(get_date_taken("126C.jpg").split(" ")[0].split(":")[1])
    day = int(get_date_taken("126C.jpg").split(" ")[0].split(":")[2])
    hour = int(get_date_taken("126C.jpg").split(" ")[1].split(":")[0])
    minute = int(get_date_taken("126C.jpg").split(" ")[1].split(":")[1])
    second = int(get_date_taken("126C.jpg").split(" ")[1].split(":")[2])
    print(get_date_taken("126C.jpg"))
    fecha1 = datetime(year, month, day, hour, minute, second)
    fecha2 = datetime(year, month, day, hour, minute, second)
    