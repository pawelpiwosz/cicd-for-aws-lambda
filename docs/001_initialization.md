# How to initialize your project

## Prerequisities

In order to start this tutorial,  you need to configure:

### AWS CLI

[Installation](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-install.html)

[Configuration](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-configure.html)

### SSH Key for CodeCommit

Let's generate a new key

```bash
ssh-keygen -t rsa -b 4096
```

I named mine `codecommit`.

Go to the AWS console, navigate to IAM, Users, select created user, navigate to Security credentials and upload new ssh key in section `SSH key for AWS CodeCommit`.

For more convenient way, let's follow AWS documentation, and add this section to your `~/.ssh/config` file at your machine:

```bash
Host git-codecommit.*.amazonaws.com
  User myUser
  IdentityFile ~/.ssh/codecommit
```

Remember, the user here is the one listed as "name" of your SSH key ID. 

Please, be noted, there is a possible issue with creating ssh key on Windows and powershell. Use Gitbash for it.