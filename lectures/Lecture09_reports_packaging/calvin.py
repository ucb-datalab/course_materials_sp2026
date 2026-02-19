
"""
Broken Behavior ... fix the tests/functions and add another test
"""

class Transmogrifier:

    def transmogrify(self, person):
        """ Transmogrify someone
        """
        
        transmog = {'calvin':'eel',
                     'hobbes':'bug'}
        new_person = transmog[person]
        return new_person


def test_transmogrify():
    TM = Transmogrifier()
    for p in ['Calvin', 'Hobbes']:
        assert TM.transmogrify(p) != None

        
def main():
    TM = Transmogrifier()
    for p in ['Calvin', 'Hobbes']:
        print(p, '->  ZAP!  ->', TM.transmogrify(p))
