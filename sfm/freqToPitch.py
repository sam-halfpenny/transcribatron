import math
def frequencyToPitch(Frequency):
    notationArray=['A','Bb','B','C','Db','D','Eb','E','F','Gb','G','Ab']
    noteOffset=12*math.log(Frequency/440,2)# compute the number of semitones the note is awway from A4
    Pitch={'note':notationArray[round(noteOffset%12)],'octave':4+math.floor(noteOffset/12),'tuning':noteOffset-round(noteOffset)}
    return Pitch