musicalNotesDict = {
  'dó': 'I',
  'ré': 'II',
  'mi': 'III',
  'fá': 'IV',
  'sol': 'V',
  'lá': 'VI',
  'si': 'VII',
}

def solutionChallengeTwo(musicalNotes: list):
    return [musicalNotesDict[musicalNotes[i].lower()] for i in range(len(musicalNotes))]
