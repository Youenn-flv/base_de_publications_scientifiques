
class Publication:

    
    def __init__(self, publis):
        self.id = publis['_id']
        self.type = publis.get('type', '')  # Handle missing 'type' field
        self.title = publis.get('title', '')
        self.year = publis.get('year', 0)
        self.publisher = publis.get('publisher', '')
        self.series = publis.get('series', '')
        self.booktitle = publis.get('booktitle', '')
        self.url = publis.get('url', '')
        self.authors = publis.get('authors', [])
        self.isbn = publis.get('isbn', [])

        # Handle 'editor' and 'pages' fields
        self.editor = publis.get('editor', '')
        self.pages_start = publis.get('pages', {}).get('start', 0)
        self.pages_end = publis.get('pages', {}).get('end', 0)

# Convert a Publication object to a JSON object. It will display only available data
    def to_json(self):
        data = {'_id': self.id}

        if self.type:
            data['type'] = self.type
        if self.title:
            data['title'] = self.title
        if self.year:
            data['year'] = self.year
        if self.publisher:
            data['publisher'] = self.publisher
        if self.series:
            data['series'] = self.series
        if self.booktitle:
            data['booktitle'] = self.booktitle
        if self.url:
            data['url'] = self.url
        if self.authors:
            data['authors'] = self.authors
        if self.isbn:
            data['isbn'] = self.isbn
        if self.editor:
            data['editor'] = self.editor
        if self.pages_start or self.pages_end:
            data['pages'] = {'start': self.pages_start, 'end': self.pages_end}

        return data
