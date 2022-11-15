
#################################################################
#   Python 3 script
#   Parse a given repository to identify all branches
#   and download each of them into dedicated folder.
#   Each folder is named according to the name of the banch
#################################################################

import git
import os
import shutil

#Display DEBUG MODE
DEBUG_DISP = False


workingPath = "/media/Stock/Projets/Suratram/Cours_UV/INFO/AP4A_LO43/TP_Perso_C++/correction/AP4A/"
branchFolders = "/home/promet/Documents/AP4A/branchFolders/"


myRepo = git.Repo(workingPath)
git = myRepo.git


#list all remote branches
allBranches = git.branch("-r")

#create an array containing all line of the retreive terminal line
array = allBranches.split("\n")

if DEBUG_DISP:
    print(array)

#delete "HEAD" from the list
array.remove("  origin/HEAD -> origin/main")
array.remove("  origin/main")

#parse each remote branch
for elm in array:
    #slipt path to get branch name
    array = elm.split("/")

    #subString path to display current branch name
    if DEBUG_DISP:
        print(array[1])

    #move to the given branch
    git.checkout(array[1])

    #pull the content of the branch to the git repository
    git.pull

    #create a folder according to the name of the branch,
    #in a different path
    if not os.path.exists(branchFolders + array[1]):
        output = branchFolders + array[1] + "/"
        shutil.copytree(workingPath, output)