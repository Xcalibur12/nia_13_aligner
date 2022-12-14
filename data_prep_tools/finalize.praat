clearinfo

wd$ = "./converted/"
sd$ = "./final/"
inDirTgd$ = wd$ + "*.TextGrid"
tgdList = Create Strings as file list: "tgdList", inDirTgd$

selectObject: tgdList

numFiles = Get number of strings
for fileNum from 1 to numFiles
  tgdName$ = Get string: fileNum
  tgd = Read from file: wd$ + tgdName$
  numberOfIntervals = Get number of intervals: 1
  sent$ = ""
  for intervalNumber from 1 to numberOfIntervals
    text$ = Get label of interval: 1, intervalNumber
    if text$ != ""
      sent$ = sent$ + text$ + " "
    endif
  endfor
  sent$ = sent$ - " "
  Insert interval tier: 1, "canonical sentence"
  Set interval text: 1, 1, sent$
  Remove tier: 2
  Set tier name: 2, "canonical alignment"
  Duplicate tier: 2, 3, "발음전사"
  Insert point tier: 4, "오류 패턴"
  Insert interval tier: 5, "어조"
  Insert interval tier: 6, "더듬"
  Save as text file: sd$ + tgdName$ - ".canonical.TextGrid" + ".TextGrid"
  # Save as text file: wd$ + tgdName$ - ".TextGrid" + ".concatenated.TextGrid"
  selectObject: tgd
  Remove
  selectObject: tgdList
endfor

# appendInfoLine: "Done!"

selectObject: tgdList
Remove
