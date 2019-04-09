from moviepy.editor import VideoFileClip, AudioFileClip


def speedup(x, pathSrc, pathDst):
    source_video = VideoFileClip(pathSrc)
    sped_up_video = source_video.speedx(factor=float(x))
    sped_up_video.write_videofile(pathDst)


def trovaFattore():
    pathSrc = input("Inserisci il path del file da velocizzare: ")
    durataReale = pathSrc.duration
    print("Il video dura: "+ durataReale)
    durataDesiderata = input("Inserisci la durata desiderata: ")
    fattore = durataReale / durataDesiderata
    print("Fattore: " + fattore)

pathSrc = input("Inserisci il path del file da velocizzare: ")
pathDst = input("Inserisci il path in cui vuoi salvare il video: ")
x = input("Inserisci il fattore di velocità: ")
speedup(x, pathSrc, pathDst)

#trovaFattore()

