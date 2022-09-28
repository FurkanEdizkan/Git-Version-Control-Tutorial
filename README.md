<!-- Logos -->
<p align="center">

  <img src="assets/images/git_name_logo_transparent.png" width="200"  />
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  <img src="assets/images/GitHub-Mark-Light-120px-plus.png" /> 
  <img src="assets/images/gitlab-logo-200.png" width="300" />

</p>

<!-- Shields -->

<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->
[![All Contributors](https://img.shields.io/badge/all_contributors-4-orange.svg?style=flat-square)](#contributors-)
<!-- ALL-CONTRIBUTORS-BADGE:END -->

![GitHub forks](https://img.shields.io/github/forks/FurkanEdizkan/Git-GitHub-GitLab-Tutorial?style=social)
![GitHub Repo stars](https://img.shields.io/github/stars/FurkanEdizkan/Git-GitHub-GitLab-Tutorial?style=social)
![GitHub](https://img.shields.io/github/license/FurkanEdizkan/Git-GitHub-GitLab-Tutorial)


<!-- Badges -->
![Git](https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white)
![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)
![GitLab](https://img.shields.io/badge/gitlab-%23181717.svg?style=for-the-badge&logo=gitlab&logoColor=white)



## !!! Work in Progress !!!

# Git, GitHub & GitLab Guide
This repository contains
- Quick and Advanced Git guide
- GitHub and GitLab usage guide
- Version Control examples and recommendations 

#
<!-- Table of Contents -->
<details>
  <summary>Table of Contents</summary>
    <li><a href="#Git">Git</a></li>
    <li><a href="#GitLab">GitHub</a></li>
    <li><a href="#GitLab">GitLab</a></li>
    <li><a href="#Contribute">Contribute</a></li>
    <li><a href="#License">License</a></li>
    <li><a href="#References">References</a></li>
    <li><a href="#Contributors">Contributors</a></li>
  </ol>
</details>

<!-- Guide -->
#

## Git

- Download & install [Git](https://git-scm.com/downloads)

For Debian/Ubuntu
```bash
apt-get install git
```
#
- Check git installation
```bash
git --version
```
#
- Initialize git configurations
```bash
git config --global user.name "user_name"
git config --global user.email "email"
```
#
- Configure main branch name as "main" (For older Git versions)
  
  Latest version of git comes with defaultBranch name as "main".
```bash
git config --global init.defaultBranch main
```
#
- Configure Visual Studio Code for Git functions
```bash
git config --global core.editor 'code --wait --new-window'
git config --global diff.tool vscode
git config --global difftool.vscode.cmd'code --wait --diff $LOCAL $REMOTE'
git config --global merge.tool vscode
git config --global mergetool.vscode.cmd'code --wait $MERGED'
```
- Unset a git configuration
```bash
git config --global --unset <option>
git config --global --unset core.editor # Remove core.editor from configuration
```
#
In order to work on the GitHub repositories, we either need to create PAT or generate a SSH key pair. If we are not planning to use GitHub we can skip this step.

- [Personal Access Token (PAT)](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token)
  
  Generated PAT will be used instead of user password for Git operations connected to GitHub. Don't forget it and store it in a safe place.

  GitHub :arrow_right: Settings :arrow_right: Developer Settings :arrow_right: [Personal Access Token](https://github.com/settings/tokens)


- [SSH](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account)

  We need to create a new SSH key, generated key pair will be used to authenticate to GitHub. Generate a new ssh-key and add public key to [GitHub-SSH and GPG keys](https://github.com/settings/keys).

  GitHub :arrow_right: Settings :arrow_right: [SSH and GPG keys](https://github.com/settings/keys)
  
```bash
ssh-keygen -t ed25519 -C "email" # Create a new SSH key
```
```bash
eval "$(ssh-agent -s)" # Start SHH-agent
```
```bash
ssh-add ~/.ssh/id_ed25519 # Add SSH key 
```
```bash
cat ~/.ssh/id_ed25519.pub # Copy the ed25519 public key
```
#

- Create a new Git repository
```bash
git init
```

- Clone Git repository
```bash
git clone <repository_link(HTTPS or SSH)>
```

- Create a gitignore file
  
  Gitignore file used to ignore files in the repository that we don't want toı track changes or aboid uploading them to remote repositories.

| .gitignore | Description |
| ----------- | ----------- |
| venv/ | Ignore all "venv" folders |
| *.orig | Ignore all files ending with ".orig" |
| *.py[cod] | Ignore all files ending with ".pyc", "pyo" and "pyd" |
| !dont_ignore_this_file | Don't ignore this file |
| ignore_this_file | Ignore this file |
| /database | Ignore "database" named folder under "/" |
| doc/*.txt | Ignore all files ending with ".txt" under "doc/" folder |
| doc/**/*.pcd | Ignore all files ending ".pcd" under "doc/" and it's sub folders |

```bash
touch .gitignore
```
#### [GitHub .gitignore templates](https://github.com/github/gitignore)
#
- Create a git commit message template file
  
  In order to keep git history clean and understandable, every commit done to any repository needed to be in a clear format. We need to use commit templates, repositories suggest we use.

```bash
touch .gitmessage
```
```bash
git config --global commit.template ~/.gitmessage
```
#### [Example git commmit message template](.gitmessage)
#
- Create a github pull request template file

  GitHub pull request used for adding new feature branches to repositories. It is a review state of the feature. To keep a feature or change clear and understanable, we use given pull request template.
  
```bash
mkdir .github
touch .github/pull_request_template.md
```
#### [Example pull request template](.github/pull_request_template.md)
#### [Creating a pull request template for your repository](https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/creating-a-pull-request-template-for-your-repository)
#
- Create a contributing.md template file
```bash
touch .contributing.md
```
#### [Example contributing.md file](contributing.md)


- Check git repository status
```bash
git status
```

## GitHub

## GitLab

#

<!-- Contribuing to Project -->
## Contribute
We welcome every contribution, suggestion and improvement

We will try to address all issues as soon possible

See [the contributing guide](contributing.md) for more details

#
For those who attended the tutorial session and want to be inside contributors list check [Comments.md](Comments.md) for details.


<!-- License -->
## License

Distributed under the MIT License. See [LICENSE](LICENSE) for more information.

# References

## Learning
- [Git Tutorial](https://git-scm.com/docs/gittutorial)
- [Pro Git book](https://git-scm.com/book/en/v2)
- [GitHub Docs](https://docs.github.com/en)
- [GitLab Docs](https://docs.gitlab.com/)
- [Atlassian Bitbucket Tutorial](https://www.atlassian.com/git)

## Logos & Images
- [Git](https://git-scm.com/downloads/logos)
- [GitHub](https://github.com/logos)
- [GitLab](https://about.gitlab.com/press/press-kit/)


<!-- Contributors -->
## Contributors

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tbody>
    <tr>
      <td align="center"><a href="https://github.com/FurkanEdizkan"><img src="https://avatars.githubusercontent.com/u/65301915?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Furkan Edizkan</b></sub></a><br /><a href="https://github.com/FurkanEdizkan/Git-GitHub-GitLab-Tutorial/commits?author=FurkanEdizkan" title="Code">💻</a> <a href="#content-FurkanEdizkan" title="Content">🖋</a> <a href="https://github.com/FurkanEdizkan/Git-GitHub-GitLab-Tutorial/commits?author=FurkanEdizkan" title="Documentation">📖</a> <a href="#design-FurkanEdizkan" title="Design">🎨</a> <a href="#maintenance-FurkanEdizkan" title="Maintenance">🚧</a> <a href="#tutorial-FurkanEdizkan" title="Tutorials">✅</a></td>
      <td align="center"><a href="https://allcontributors.org"><img src="https://avatars.githubusercontent.com/u/46410174?v=4?s=100" width="100px;" alt=""/><br /><sub><b>All Contributors</b></sub></a><br /><a href="#design-all-contributors" title="Design">🎨</a> <a href="#tool-all-contributors" title="Tools">🔧</a></td>
      <td align="center"><a href="https://github.com/Akerdogmus"><img src="https://avatars.githubusercontent.com/u/44196950?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Alim Kerem Erdoğmuş</b></sub></a><br /><a href="#tool-Akerdogmus" title="Tools">🔧</a> <a href="https://github.com/FurkanEdizkan/Git-GitHub-GitLab-Tutorial/commits?author=Akerdogmus" title="Tests">⚠️</a> <a href="#userTesting-Akerdogmus" title="User Testing">📓</a> <a href="#talk-Akerdogmus" title="Talks">📢</a></td>
      <td align="center"><a href="https://github.com/ramazanakkulak"><img src="https://avatars.githubusercontent.com/u/78980365?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Ramazan Akkulak</b></sub></a><br /><a href="#tutorial-ramazanakkulak" title="Tutorials">✅</a> <a href="https://github.com/FurkanEdizkan/Git-GitHub-GitLab-Tutorial/commits?author=ramazanakkulak" title="Tests">⚠️</a></td>
    </tr>
  </tbody>
</table>

<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->

<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->
