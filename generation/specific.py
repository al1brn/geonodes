# Specific classes


class SpecificNode:

    @classmethod
    def constructors(cls):
        return []

    @classmethod
    def methods(cls):
        return []

    @classmethod
    def setters(cls):
        return []

    @classmethod
    def getters(cls):
        return []

    @classmethod
    def static_signature(cls):
        return None

    @classmethod
    def class_signature(cls):
        return None
    
# Format String

class FormatStringNode(SpecificNode):

    @classmethod
    def static_template(cls, *strings, **kwstrings):
        """ > Node <&Node Format String>

        Arguments
        ---------
        - strings (list of Strings) : auto named String sockets
        - kwstrings (dict of Strings) : named String socket

        Returns
        -------
        - String
        """

        format_string = None
        if 'format' in kwstrings.keys():
            format_string = kwstrings['format']
            del kwstrings['format']
        elif len(strings):
            format_string = strings[0]
            strings = [strings[1:]]

        node = Node('Format String', format=format_string)

        # ----- Socket name

        sock_index = [ord('a'), 0]
        def next_sock_name():
            while True:
                sock_name = chr(sock_index[0])
                if sock_index[0] == ord('z'):
                    if sock_index[1] != 0:
                        sock_name += f".{sock_index[1]:03d}"
                    sock_index[1] += 1
                else:
                    sock_index[0] += 1

                if sock_name not in kwstrings.keys():
                    return sock_name
                
        # ----- Add sockets

        for s in strings:
            node._bnode.format_items.append(next_sock_name())

        for k, v in kwstrings.items():
            node._bnode.format_items.new(k)

            

        


        


        return node._out



    @classmethod
    def constructors(cls):
        return [{
            'class_name': 'String',
            'args': [{*strings, }],
        }]

    @classmethod
    def class_names(cls):
        return ['String']

    @classmethod
    def static_signature(cls):
        return "format, *strings, **kwstrings"

    @classmethod
    def class_signature(cls):
        return "self, *strings, **kwstrings"
