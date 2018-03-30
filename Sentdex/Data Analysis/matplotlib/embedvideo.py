from datetime import timedelta

class YouTubeVideo(object):
    def __init__(self, id, width=560, height=315, start=timedelta(hours=0, minutes=0, seconds=0)):
        self.id = id
        self.width = width
        self.height = height
        self.start = start.total_seconds()

    def _repr_html_(self):
        return """
            <iframe
                width="%i"
                height="%i"
                src="http://www.youtube.com/embed/%s?start=%i"
                frameborder="0"
                allowfullscreen
            ></iframe>
        """%(self.width, self.height, self.id, self.start)

# Insert Pull Request		
YouTubeVideo("id")
