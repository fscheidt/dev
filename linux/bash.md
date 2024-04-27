
```bash
#!/bin/bash
alias lsl='ls -ahgo'
alias lsdir="ls -lhagoa --color=always | grep '^d'"
alias cdown='cd ~/Downloads && ls -lhgoa'
alias cdrop='cd ~/Dropbox && ls -lhgoa'
alias cdesk='cd ~/Desktop && ls -lhgoa'
alias cdprojects='cd ~/Projects && ls -lhgoa'
alias cdmarket='cd ~/Projects/market/deepmk && poetry shell'
alias cdrepos='cd ~/Repos && ls -lhgoa'
alias cdsw='cd ~/Softwares && ls -lhgoa'
alias cdtemp='cd ~/Temp && ls -lhgoa'
alias dotcd='cd ~/bin && ls -lhgoa'
alias hist_clear='history -c && rm ~/.bash_history'
alias hist_unset='unset HISTFILE && export LESSHISTFILE="-"'
alias ..='cd ..'
alias ~='cd ~'
alias x_hashall='find . -type f -print0 | xargs -0 sha256sum'

```


```bash
#!/bin/bash

# .bashrc

export EDITOR=vim
export PATH="$HOME/.dot:$PATH"

PROMPT_DIRTRIM=2
parse_git_branch() {
     git branch 2> /dev/null | sed -n 's/^* \(.*\)/(\1)/p'
}
export PS1="${debian_chroot:+($debian_chroot)}\[\033[01;32m\]\u@\h\[\033[00m\]:\[\033[01;34m\]\w\[\033[00m\]\[\e[91m\] \$(parse_git_branch)\[\e[00m\]\n$ "

stty -ixon

```
