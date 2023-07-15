#Put in your file names (Include Extention)
Filenamelist = []
#Skipped Files (Include Extention)
SkippedFiles = [
  "poetry.lock", ".breakpoints", "pyproject.toml", "replit.nix", ".replit",
  "NonReplitVersion.py"
]
#If you want a custom output Name change this
OutputFileName = "output.txt"
#Rest Of Script
Files = len(Filenamelist)
FileContents = []
clear = open(OutputFileName, "w")
clear.write("#File Generated With Python Multi File Compiler! ")
clear.close()
for i in range(Files):
  f = open(Filenamelist[i], "r")
  for x in f:
    FileContents.append(x)
  f.close()
  combinedfile = open(OutputFileName, "a")
  FileContents[len(FileContents) -
               1] = FileContents[len(FileContents) - 1] + "\n" + "\n"
  print(FileContents)
  for i in range(len(FileContents)):
    combinedfile.write(FileContents[i])
  FileContents.clear()
  combinedfile.close()
