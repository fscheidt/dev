
```bash
#!/bin/bash

# .bash_aliases

alias lsl='ls -ahgo'
alias ..='cd ..'
alias ~='cd ~'
alias cdesk='cd $HOME/Desktop && ls -lhgoa'
alias cdown='cd $HOME/Downloads && ls -lath --color=always | head -15'
alias cdrepos='cd $HOME/Repos && ls -lhgoa'
alias cdtemp='cd $HOME/Temp && ls -lhgoa'
alias dotcd='cd $HOME/.dot && ls -lhgoa'
alias hist_clear='history -c && rm ~/.bash_history'
alias hist_unset='unset HISTFILE && export LESSHISTFILE="-"'
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
