import os
#Put in your file names (Include Extention)
Filenamelist = []
#Do you wish to Scan For Files in your Current Directory? Make Sure to Edit Files to skip over below
ScanForFiles = True
#Skipped Files (Include Extention)
SkippedFiles = [
  "poetry.lock", ".breakpoints", "pyproject.toml", "replit.nix", ".replit",
  "NonReplitVersion.py", "BasicVersion.py", "MoreFeatures.py"
]
#If you want a custom output Name change this
OutputFileName = "output.txt"
#Include a Comment in the final Code where a File ends and starts
ShowWhereFileEnds = True
#Custom Path to Folder to Scan for files (Full Path), default is dirpath
Custompath = 'dirpath'
#Debugger
DebugMode = True
#Name of Log File (Only used in debug Mode)
logfilename = "Log.txt"
#Rest Of Script


def ScanFiles():
  SkippedFiles.append(logfilename)
  SkippedFiles.append(OutputFileName)
  dirname, filename = os.path.split(os.path.abspath(__file__))
  SkippedFiles.append(filename)
  if Custompath == "dirpath":
    for path in os.scandir(dirname):
      if path.is_file() and path.name not in SkippedFiles:
        Filenamelist.append(path.name)
        if DebugMode:
          print(path.name)
  else:
    for path in os.scandir(Custompath):
      if path.is_file() and path.name not in SkippedFiles:
        Filenamelist.append(path.name)
        if DebugMode:
          print(path.name)


def ClearOutputFile():
  clear = open(OutputFileName, "w")
  clear.write("#File Generated With Python Multi File Compiler! ")
  clear.close()


def CombineFiles():
  for i in range(Files):
    if not Custompath == "dirpath":
      os.chdir(Custompath)

    f = open(Filenamelist[i], "r")

    if ShowWhereFileEnds:
      FileContents.append("\n" + "#Start of " + Filenamelist[i - 1] + "\n" +
                          "\n")
    for x in f:
      FileContents.append(x)
    f.close()
    combinedfile = open(OutputFileName, "a")
    FileContents[len(FileContents) -
                 1] = FileContents[len(FileContents) - 1] + "\n"
    if ShowWhereFileEnds:
      FileContents.append("\n" + "#End of " + Filenamelist[i - 1] + "\n")
    else:
      FileContents.append("\n")
    if DebugMode:
      print(FileContents)
    for i in range(len(FileContents)):
      combinedfile.write(FileContents[i])
    FileContents.clear()
    combinedfile.close()


def log():
  logfile = open(logfilename, "w")
  logfile.write("Start of Log" + "\n" + "\n")
  logfile.close()
  logfile = open(logfilename, "a")
  logfile.write("Files Combined:" + "\n")
  for i in range(Files):
    logfile.write(Filenamelist[i] + "\n")
  logfile.write("\n" + "Files Skipped:" + "\n")
  for i in range(len(SkippedFiles)):
    logfile.write(SkippedFiles[i] + "\n")
  if ShowWhereFileEnds:
    logfile.write("\n" + "Showing Where Files Ends and Starts" + "\n")
  else:
    logfile.write("\n" + "Not Showing Where Files Ends and Starts" + "\n")
  if Custompath == "dirpath":
    logfile.write("\n" + "Not Using a Custom Path" + "\n")
  else:
    logfile.write("\n" + "Using a Custom Path of " + Custompath + "\n")
  if ScanForFiles:
    logfile.write("\n" + "Scanning for Files" + "\n")
  else:
    logfile.write("\n" + "Not Scanning for Files")
  logfile.close()


if ScanForFiles:
  ScanFiles()
Files = len(Filenamelist)
FileContents = []
ClearOutputFile()
CombineFiles()
if DebugMode:
  log()