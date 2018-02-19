CSCI5828 - Spring 2018
Homework 2
Team members: Bu Sun Kim, Arcadia(Xiaozhe) Zhang

We created the repo on github.com and cloned it
`git clone https://github.com/arcadiaz/hw2_csci5828.git` <br/>
`git add * ` <br/>
`git commit -am "0: added readme and project file"` <br/>
`git commit -am "1: changed project file"` <br/>
`git commit -am "2: changed the project file again"` <br/>
`git log --graph` <br/>
`git push`<br/>
`git checkout 7bf3dd8b0df147ef6961145f095c2066af8b77b0` <br/>
`git checkout -b bug-fix` <br/>
`git commit -am "3: edited project file (changed the name for a game mode)"` <br/>
`git log --graph --all` <br />
`git commit -am "4: edited readme and added a new line in project file"`<br />
`git log --graph --all` <br />
`git push --set-upstream origin bug-fix`<br />
`git log --graph --all`<br />
`git merge master`<br />
`git commit -am "5: resolved merge conflicts and edited readme" ` <br />
`git log --graph --all`<br />
`git commit -am "6: edited readme and introduced a bug in the project"`<br />
`git push`<br />
`git checkout c1f46cf685e5068937519e7f0ad3cba29c7ffa8d` <br />
`git checkout -b bug-fix-experimental`<br />
`git commit -am "7: edited readme and modified project"`<br />
`git commit -am "8: changed readme and added a new import to the project"`<br />
`git commit -am "9: changed readme; deleted a line from the project"`<br />
`git push --set-upstream origin bug-fix-experimental`<br />
`git checkout master`<br />
`git commit -am "10: switched to master branch, changed readme"` <br />
`git checkout bug-fix`<br />
`git branch`<br />
`git merge bug-fix-experimental`<br />
`git commit -am "11: fixed conflicts"`<br />
`git commit -am "12: made a change in readme"`<br />
`git checkout master`<br />
`git push`<br />
`git merge bug-fix`<br />
`git commit -am "13: changed readme agian"`<br />
`git add *` <br />
`git commit -am “14: added commit graph and added all commands to readme”`<br />

0: added readme and project file
1: changed project file
2: changed project file again
3: changed readme and changed project file
4: changed readme and edited the project fike again in a different way
5: resolved merge conflicts
6: edited readme and keep editing the project file
7: changed readme and modified project 
8: changed readme and added a new line project
9: changed readme; deleted a line from the project
10: switched back to the master branch, edited readme
11: fixed comflicts
12: made a change in readme
13: learnt how to cut text in nano; changed readme
