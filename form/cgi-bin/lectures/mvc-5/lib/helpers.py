import imp
import os

def render(template, data):
    filePath = os.path.join(os.path.dirname(__file__), '..', 'templates', template + '.py')
    l = imp.load_source(template, filePath)
    return l.render(data)
