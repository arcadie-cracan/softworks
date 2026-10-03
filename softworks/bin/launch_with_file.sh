#!/bin/sh
# Run "$@" with the file in $SOFTWORKS_LAUNCH_FILE as its last argument.
# Used by SdmLaunchWithFile (Softworks.ils): the path never appears on the
# ipcBeginProcess command line, which cannot quote it.
exec "$@" "$SOFTWORKS_LAUNCH_FILE"
