class RequestRepository(object):
    """
    This generates common request objects which will be sent to the
    google docs api
    """

    @classmethod
    def make_bold_text_request(cls, start_index, end_index):
        """
        Makes the text between the start and end bold
        :param start_index:
        :param end_index:
        :return:
        """
        return {
            'updateTextStyle': {
                'range': {
                    'startIndex': start_index,
                    'endIndex': end_index
                },
                'textStyle': {
                    'bold': True,
                },
                'fields': 'bold'
            }
        }

    @classmethod
    def make_delete_content_request(cls, start_index, end_index):
        return {
            'deleteContentRange': {
                'range': {
                    'startIndex': start_index,
                    'endIndex': end_index
                }
            }
        }

    @classmethod
    def make_insert_text_request(cls, start_index, text):
        return {
            'insertText': {
                'location': {
                    'index': start_index,
                },
                'text': text,
            }
        }

    @classmethod
    def make_left_align_request(cls, start_index, end_index):
        return {
            'updateParagraphStyle': {
                'range': {
                    'startIndex': start_index,
                    'endIndex': end_index
                },
                'paragraphStyle': {
                    'alignment': 'START'
                },
                'fields': 'alignment'
            }
        }

    @classmethod
    def make_normal_text_style_request(cls, start_index, end_index):
        return {
            'updateParagraphStyle': {
                'range': {
                    'startIndex': start_index,
                    'endIndex': end_index
                },
                'paragraphStyle': {
                    'namedStyleType': 'NORMAL_TEXT'
                },
                'fields': 'namedStyleType'
            }
        }

    @classmethod
    def make_title_style_request(cls, start_index, end_index):
        """
        Imposes title (named style) upon the text between the start and end indexes
        :param start_index:
        :param end_index:
        :return:
        """
        return {
            'updateParagraphStyle': {
                'range': {
                    'startIndex': start_index,
                    'endIndex': end_index
                },
                'paragraphStyle': {
                    'namedStyleType': 'TITLE'
                },
                'fields': 'namedStyleType'
            }
        }

    @classmethod
    def make_url_request(cls, start_index, end_index, url):
        return {
                "updateTextStyle": {
                    "textStyle": {
                        "link": {
                            "url": url
                        }
                    },
                    "range": {
                        "startIndex": start_index,
                        "endIndex": end_index
                    },
                    "fields": "link"
                }
            }
