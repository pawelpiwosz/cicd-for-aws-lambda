We will use AWS CodeCommit to keep our files.  

Let's call this repository `cicd-demo`.

Run  

```bash
aws --profile demo codecommit create-repository --repository-name cicd-demo --repository-description "Demonstration" --tags Environment=Demo,Purpose=Demo,Conference="cicd-demo"
```

to create repository.

As you can see, I am using not default profile to work with CLI

Now it is time to initialize the repo.

```bash
mkdir cicd-lambda
cd cicd-lambda

git init
git remote add origin ssh://git-codecommit.eu-central-1.amazonaws.com/v1/repos/cicd-lambda
```

create a simple `README.md` file in this repository and run

```bash
git add .
git commit -m "initial commit"
git push --set-upstream origin master
```

And your first commit is visible in AWS CodeCommit repository.
