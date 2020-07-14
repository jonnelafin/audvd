#!/usr/bin/env python3
v = 1.0

print("audvd v. " + str(v))
print("audvd written by (and originally for) Elias Eskelinen aka Jonnelafin.")

print("audvd importing from libraries...")
import os
print("     moviepy...",end="")
from moviepy.editor import *
print("DONE")
print("     soundfile...",end="")
import soundfile as sf
print("DONE")

def getFiles(inp):
    import os
    filelist=os.listdir(inp)
    for fichier in filelist[:]: # filelist[:] makes a copy of filelist.
        if not(fichier.endswith(".wav")):
            filelist.remove(fichier)
    return(filelist)
def getLen(file):
    import math
    f = sf.SoundFile(file)
    l = len(f) / f.samplerate
    return(  int(math.ceil(l)+1)  )
def uic_divider():
    return("---------")
def ui_verify(inp, outp):
    print(uic_divider())
    print("Please verify that the parameters you have given are correct, no files will be deleted:")
    print("     input folder (subfolders not supported): " + inp)
    print("     output folder: " + outp)
    print("Press enter to continue or CTR+C to exit.")
    input("")
    print(uic_divider())

def convert(inp, outp):
    print("Starting edit...")
    
    print("-> Getting the lenght of the soundfile...")
    l = getLen(inp)
    
    #Resolution
    w = 1453#720
    h = 744#w*9/16 # 16/9 screen
    w = int(w)
    h = int(h)
    moviesize = w,h
    
    #Clips
    print("-> Creating clips...")
#    name = os.path.basename(str(inp))
    stars = ImageClip("./img/web.png")
    audioclip = AudioFileClip(inp)
    new_audioclip = CompositeAudioClip([audioclip])
    
    #Compose
    print("-> Composing clips...")
    final = CompositeVideoClip([stars], size = moviesize)
    final.audio = new_audioclip
    
    #Export
    print("-> Exporting clips...")
    final.set_duration(l).write_videofile(outp, fps=5)
    
    #Done
    print("Export done.")
    print(uic_divider())
def ui_main():
    inp = input("Soundfile to read (default ./music/bottles.wav): ")
    outp = input("Output filepath (default ./out.mp4): ")
    if outp == "":
        outp = "./out.mp4"
    if inp == "":
        inp = "./music/bottles.wav"
    ui_verify(inp, outp)
    convert(inp, outp)
if __name__ == "__main__":
    import sys
    minarg = 2
    minarg = minarg + 1
    if len(sys.argv) < minarg:
        print("Necessary parameters not given, parameters: " + str(sys.argv[1:]))
        print("-> Launching user interface...")
        ui_main()
    else:
        inp = sys.argv[1]
        outp = sys.argv[2]
        skip = False
        if len(sys.argv) > 3:
            skip = bool(sys.argv[3])
        if not skip:
            ui_verify(inp, outp)
        files = getFiles(inp)
        for fi in files:
            o = outp + os.path.basename(fi)
            print("     " + fi + " --> " + o)
