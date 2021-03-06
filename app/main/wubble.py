from kik.messages.keyboard_message import KeyboardMessage
from kik.messages.attributable_message import AttributableMessage
import os

KIKDATA = os.environ.get("KIKDATA")
send_type = os.environ.get("KIK_SEND_TYPE")


class WubbleMessage(KeyboardMessage, AttributableMessage):
  
    def __init__(self, to=None, chat_id=None, url=None, no_forward=None,
                 kik_js_data=None, keyboards=None, attribution=None, mention=None, delay=None, width=None, height=None,
                 **kwargs):
        super(WubbleMessage, self).__init__(type=send_type, to=to, chat_id=chat_id, mention=mention, delay=delay,
                                            keyboards=keyboards, attribution=attribution, **kwargs)
        self.url = url
        self.no_forward = no_forward
        self.kik_js_data = kik_js_data
        self.width = width
        self.height = height

    @classmethod
    def property_mapping(cls):
        mapping = super(WubbleMessage, cls).property_mapping()
        mapping.update({
            'url': 'url',
            'no_forward': 'noForward',
            'kik_js_data': KIKDATA,
        })
        return mapping

    def to_json(self):
        ret = super(WubbleMessage, self).to_json()
        if self.width and self.height:
            ret['size'] = {
                'width': self.width,
                'height': self.height
            }
        return ret
