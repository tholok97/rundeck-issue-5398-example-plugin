# Minimal Rundeck plugin to accompany https://github.com/rundeck/rundeck/issues/5398

## Installation

1. Zip up plugin:
    ```
    zip -r rundeck-issue-5398-example-plugin-1.0.0.zip rundeck-issue-5398-example-plugin-1.0.0/plugin.yaml rundeck-issue-5398-example-plugin-1.0.0/contents/example-script.py
    ```
2. Install plugin by placing it into `$RDECK_BASE/libext`

## Usage

Create a new Rundeck job with one option called "testoption" with some default value, and one workflow Node Step: `Issue 5398 example`. Leave the default value of "Script". Run the job, and observe the behavoir described in the issue.

You should see output like this:

```text
HELLO I AM THE EXAMPLE PLUGIN. I'LL OUTPUT THE SCRIPT I RECEIEVED STARTING ON THE NEXT LINE
# the following will not output the value of the job option, it will
# just output @option.testoption@ literally
echo "@option.testoption@"

# the following will output the value of the job option, but at the
# cost of the next example breaking...
echo "asdfasdfasdf"

# the following will output an empty string, as Rundeck will
# substitute  to an empty string (it thinks that it is
# an  ?)
testvariable='testvalue'
echo ""

# in most cases it's possible to avoid the  syntax by doing
# $var, but sometimes  is needed. For example trying to print a
# Bash array will cause Rundeck substitution to get confused
myarray=(1 2 3)
echo ""
```
