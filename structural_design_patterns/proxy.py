class Image:
    def show(self):
        pass


class RemoteImage(Image):
    def load_from_source(self):
        pass

    def is_loaded(self):
        pass


class DiskImage(Image):
    def load_from_source(self):
        pass

    def is_loaded(self):
        pass

    def show(self):
        pass


class InternetImage(RemoteImage):
    def load_from_source(self):
        pass

    def is_loaded(self):
        pass

    def show(self):
        pass


class ImageProxy(Image):
    def __init__(self, remote_image):
        self._remote_image = remote_image

    def show(self):
        if not self._remote_image.is_loaded():
            print('Loading image.')
            self._remote_image.load_from_source()
        return self._remote_image.show()


disk_image_proxy = ImageProxy(DiskImage())
internet_image_proxy = ImageProxy(InternetImage())  # lazy loading

disk_image_proxy.show()

# until show method on internet_image_proxy is called we do not load the image from the internet
# internet_image_proxy.show()  # if we want to load the image from internet we just call show method
