import os
from PIL import Image
import STRING

def extractFrames(inGif, outFolder):
    frame = Image.open(inGif)
    nframes = 0
    while frame:
        frame.save('%s/%s-%s' % (outFolder, nframes, os.path.basename(inGif)), 'GIF')
        nframes += 1
        try:
            frame.seek(nframes)
        except EOFError:
            break;
    return True


extractFrames(STRING.Images.PATH + 'ai3000.gif', STRING.LOCAL + '/resource/image/gif/')