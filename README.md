## codebot - a code execution plugin for Errbot

This plugin allow you to make the bot "execute" C, CPP and python snippets.
It is actually backed by codepad, so nothing is executed on the bot itself.

For more information about err you can find it here: https://github.com/errbotio/errbot

### Installation

If you have the admin rights on an Errbot simply use this in a one-to-one chat:

```
!repos install https://github.com/errbotio/err-code
```

Then `!help` to see the available commands and their explanation.

### example

Execute a Python snippet.

```
>>> !python print(range(10))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```
