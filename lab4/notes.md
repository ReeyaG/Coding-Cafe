<<<<<<< HEAD
# Lab 4: Git & GitHub

## Question 1

The `--global` option saves the setting for my user account, so it applies to all the Git repositories I use unless I change it for a particular repository. Without `--global`, the setting applies only to the current repository if I am inside one.

## Question 2

The `ls -a` command shows all the files and folders, including hidden ones that normally do not appear with `ls`. I could see the `.git` directory, which stores information about my repository and its history.

## Question 3

When I ran git status, Git showed me the files and folders in my coding-cafe folder that were not being tracked yet. My output showed .venv/, Readme.md, week02/, and week04/ as untracked files and folders. It also showed that I had not made any commits yet and that nothing had been added to the staging area.

git status
On branch master

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)
    .venv/
    Readme.md
    week02/
    week04/

nothing added to commit but untracked files present (use "git add" to track)



## Question 4

After I created the `.gitignore` file, Git stopped showing the `.venv/` folder as untracked. This is because I added rules to ignore unnecessary files and folders like `.venv/`, `__pycache__/`, `*.pyc`, and `.DS_Store`.

## Question 5

Yes, I should commit the `.gitignore` file because it tells Git which files and folders to ignore. This also helps other people working on the same repository follow the same rules. I should not ignore the `.gitignore` file itself.

## Question 6

After I ran `git add README.md`, the file moved from the untracked files section to the changes to be committed section in `git status`. This means Git added the file to the staging area, where it was ready to be included in my next commit.

## Question 7

After I ran git commit -m "Lab work so far", Git saved my staged changes as a commit with the message Lab work so far. The commit hash shown in my output was fcd8529e50c9036fb985ced027b3ca8246ddab49. I could use git log to view the commit details, including the author, date, and commit message.

git log --oneline
commit fcd8529e50c9036fb985ced027b3ca8246ddab49 (HEAD -> master)
Author: reeya Gokulgandhi <reeya.g.ug26@plaksha.edu.in>
Date:   Mon Oct 11 15:35:02 2026 +0530

    Lab work so far
fcd9076 (HEAD -> master) Lab work so far

## Question 8

The first seven characters of a commit hash are an abbreviated version of the full commit ID. They make it easier to refer to a commit without typing out the entire hash, as long as the shorter version uniquely identifies it.

## Question 9

The four steps are edit, stage, commit, and repeat. First, I make changes to my files, then use `git add` to stage the changes. After that, I use `git commit` to save them in the repository's history and repeat the process whenever I make more changes.

## Question 10

`README.md` is used to explain what a project is about and what it contains. GitHub automatically displays this file on the repository's front page, so people can understand the project without having to open every file.

## Question 11

The `gh auth login` command logged me into GitHub through the GitHub CLI. It set up authentication so I could interact with my GitHub account and push my local commits to my online repository without entering my account password every time.

## Question 12

When I opened my repository on GitHub, I could see the `README.md` file displayed as formatted text. GitHub automatically recognises the filename and renders the Markdown, making the project description easier to read.

## Question 13

No, pushing did not change my local commit history. The `git push` command uploaded my existing commits to the remote repository on GitHub. My local commits and their IDs stayed the same.

## Question 14

A private repository is stored on GitHub but can only be accessed by its owner and people who have been given permission. A repository that does not exist on GitHub has no online repository page or remote copy. Making a repository private restricts who can access it, but it does not delete the repository.
=======
# Lab 4 Notes

Q1. `--global` means the configuration applies to all Git repositories for my user account. Without it, Git applies the setting to the current repository only, assuming I am inside one.

Q2. The `ls -a` command showed the hidden `.git` directory, which stores Git's repository data and history.

Q3. Git listed the project files and folders, including the README, notebook, and the `week01/` and `week02/` directories.

Q4. `.DS_Store` disappeared from the untracked files after adding it to `.gitignore`.

Q5. `.gitignore` should be committed because it shares the rules for excluding unnecessary files with anyone using the repository.

Q6. `README.md` moved from Untracked files to Changes to be committed. It was added to Git's staging area.

Q7. Git reported the number of files changed in the first commit. I need to record the exact count shown in my terminal.

Q8. The first seven characters are an abbreviated commit hash. They identify the commit in Git's history.
>>>>>>> ba1817b (Add lab 4 notes)
