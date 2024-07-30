import argparse
import gtts
from xml.dom import minidom
import xml.etree.cElementTree as et
import io # log whats used

def main(community):
    more = True
    doc = minidom.parse(community + ".xml")
    
    while more:
        tts = """"""
        try:
            root = doc.documentElement
            print(root)
            print(root.firstChild)
            
            doc.removeChild(root.firstChild)
            print(root)
            print(root.firstChild)
            print(root.firstChild.firstChild)
            tts += root.firstChild.getAttribute("title")
            tts += ("\n -" + root.firstChild.firstChild.getAttribute("text"))
            doc.removeChild(root.firstChild.firstChild)
            tts += ("\n\n\n")
            print(root.firstChild.getAttribute("title"))
        except Exception as e:
            print(tts)
            print(e)
            print("fail")
            more = False
            
    
    #names = doc.getElementsByTagName("")
    
    
    
def prettify(elem):
    """Return a pretty-printed XML string for the Element.
    """
    rough_string = et.tostring(elem, 'utf-8')
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent="\t")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", help='xml file to parse and tts', required=True)
    args = parser.parse_args()

    main(args.file)