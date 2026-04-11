let((executableWithArgs)
    executableWithArgs = "python -m softworks.workspace.code_workspace"
    ; SOFTWORKS_VSCODE_WORKSPACE optional: Python falls back to
    ; $SOFTWORKS_PROJECT_ROOT/softworks_workspace (or cwd/softworks_workspace if unset) with a warning.
    system(executableWithArgs)
)
