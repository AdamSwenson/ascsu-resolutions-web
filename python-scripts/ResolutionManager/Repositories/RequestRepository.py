from ResolutionManager.config.Configuration import Configuration


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
    def make_align_center_request(cls, start_index, end_index):
        return {
            'updateParagraphStyle': {
                'range': {
                    'startIndex': start_index,
                    'endIndex': end_index
                },
                'paragraphStyle': {
                    'alignment': 'CENTER'
                },
                'fields': 'alignment'
            }
        }

    @classmethod
    def make_align_left_request(cls, start_index, end_index):
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
    def make_insert_text_request(cls, start_index, text, segmentId=None):
        r = {
            'insertText': {
                'location': {
                    'index': start_index,
                },
                'text': text,
            }
        }
        if segmentId is not None:
            r['insertText']['location']['segmentId'] = segmentId

        return r

    # ------------------------- Named styles
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
    def make_header_style_request(cls, start_index, end_index):
        config = Configuration()

        return {
            'updateTextStyle': {

                'range': {
                    'segmentId': config.TEMPLATE_HEADER_ID,
                    'startIndex': start_index,
                    'endIndex': end_index
                },
                'textStyle': {
                    'weightedFontFamily': {
                        'fontFamily': 'Atkinson Hyperlegible'

                    },
                    'fontSize': {
                        'magnitude': 11,
                        'unit': 'PT'
                    },
                },
                'fields': 'weightedFontFamily,fontSize'
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

    # ---------------------------- Spacing
    @classmethod
    def make_single_space_request(cls, start_index, end_index, segmentId=None):
        """
        Creates a request object for making the given indicies double spaced.
        Used to create the objects used in a batch update
        :param document_id:
        :param start_index:
        :param end_index:
        :return:
        """
        r = {
            'updateParagraphStyle': {
                'range': {
                    'startIndex': start_index,
                    'endIndex': end_index
                },
                'paragraphStyle': {
                    'lineSpacing': 100
                },
                'fields': 'lineSpacing'
            }
        }
        if segmentId is not None:
            r['updateParagraphStyle']['range']['segmentId'] = segmentId

        return r

    @classmethod
    def make_double_space_request(cls, start_index, end_index):
        """
        Creates a request object for making the given indicies double spaced
        :param document_id:
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
                    'lineSpacing': 200
                },
                'fields': 'lineSpacing'
            }
        }
