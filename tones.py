'''
Solution by: Anjoli Podder
December 2016

http://www.cse.msu.edu/~cse231/PracticeOfComputingUsingPython/01_Beginnings/SecondWeekProjects/Tones/proj02.pdf

One of the oldest problems of music is how to map the notes of a musical piece to a set of audio
frequencies. There are various ``tuning approaches'' that state slightly different ways of assigning
notes to a particular frequency. This project will require that you write a program that does one
particular kind of this mapping

'''

import winsound

def get_sound_input():
    valid_octave = False
    valid_pitch = False
    octave = 0
    pitch = 0
    while not(valid_octave):
        octave_str = input("Give me an octave: ")
        try:
            octave = int(octave_str)
            valid_octave = True
        except:
            print("That was not a valid octave. Please enter a whole integer")
    while not(valid_pitch):
        pitch_str = input("Pive me a pitch class: ")
        try:
            pitch = int(pitch_str)
            valid_pitch = True
        except:
            print("That was not a valid pitch. Please enter a whole integer")
    return octave, pitch

def sound_formula(octave, pitch):
    return 440*2**(octave-4+(pitch-9)/12)


def sound_convert():
    print("This program can convert octave/pitchclass pairs into their appropriate Hertz values. It uses the tempered "
          "scale conversions")
    octave1, pitch1 = get_sound_input()
    try:
        winsound.Beep(int(sound_formula(octave1, pitch1)), 500)
    except:
        print("Sorry, I can't play that sound as it's not in the allowed frequency range")
    print("%i . %i equals %f \n" % (octave1, pitch1, sound_formula(octave1, pitch1)))
    print("Let's do that again shall we")
    octave2, pitch2 = get_sound_input()
    try:
        winsound.Beep(int(sound_formula(octave2, pitch2)), 500)
    except:
        print("Sorry, I can't play that sound as it's not in the allowed frequency range")
    print("%i . %i equals %f \n" % (octave2, pitch2, sound_formula(octave2, pitch2)))
    print("One more time")
    octave3, pitch3 = get_sound_input()
    try:
        winsound.Beep(int(sound_formula(octave3, pitch3)), 500)
    except:
        print("Sorry, I can't play that sound as it's not in the allowed frequency range")
    print("%i . %i equals %f \n" % (octave3, pitch3, sound_formula(octave3, pitch3)))
    print("Thanks for using my program.")

if __name__ == "__main__":
    sound_convert()