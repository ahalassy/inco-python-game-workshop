# Git cheatsheet

| Phrase       | Meaning                                                                                  |
|--------------|------------------------------------------------------------------------------------------|
| repository   | The database of your version controlled work.                                            |
| working copy | The editable version of you work.                                                        |
| local        | Your local repository stored in the .git directory.                                      |
| remote       | Somebody other's repository or a repository in the cloud<br/>like GitHUB or Azure DevOps |
| commit       | A single batch of changes                                                                |
| push         | Send your local changes to a remote repository                                           |

# Snippets
Some useful commands and processes with git.

## Cloning manually
This commands can be used for cloning a remote GIT repository manually.

```shell
# Initialize an empty git repository in the current directory:
git init

# Add a remote with the default name 'origin' to the path {url-of-the-repo}:
git remote add origin {url-of-the-repo}

# Download everything from the default (origin) remote:
git fetch

# Checkout and track the origin/{branch} branch:
git checkout origin/{branch} --track
```

## The commit & push process
Use this commands to commit and push your changes.

```shell
# Check the status of the working copy:
git status

# Add a single file to the staging area:
git add {path-to-the-file}

# ...or add everything at once:
git add --all

# Commit the contents of the staging area:
git commit -m {message}

# Push your commits to the remote:
git push
```