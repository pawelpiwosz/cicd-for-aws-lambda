We will use AWS CodeCommit to keep our files.  

Let's call this repository `pyconf_hydpy`.

Run  

```bash
aws --profile pyconf codecommit create-repository --repository-name pyconf_hydpy --repository-description "Demonstration" --tags Environment=Demo,Purpose=Demo,Conference="Pyconf_hydby"
```

to create repository.

As you can see, I am using not default profile to work with CLI

Now it is time to initialize the repo.

```bash
mkdir pyconf_hydpy
cd pyconf_hydby

git init
git remote add origin ssh://git-codecommit.eu-central-1.amazonaws.com/v1/repos/pyconf_hydpy
```

create a simple `README.md` file in this repository and run

```bash
git add .
git commit -m "initial commit"
git push --set-upstream origin master
```

And your first commit is visible in AWS CodeCommit repository.