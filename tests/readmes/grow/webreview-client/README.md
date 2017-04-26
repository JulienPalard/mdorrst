# webreview-client

## Overview

webreview-client is the client library for the webreview
(https://github.com/grow/webreview) web application. It's designed to be used
by programs that need to communicate with a webreview server.

The webreview client is a simple API client, but it's primarily used to do
the heavy-lifting involved with generating signed URLs for filesets and
managing a fileset upload.

Once a fileset has been uploaded, the client finishes with a finalize command
that indicates to the webreview server that the upload is finishde and post-
upload tasks can be kicked off (such as notifications or builds).
