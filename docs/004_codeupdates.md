# Work with the project

## Lambda function

The function's code is in the `lambdafunction` directory. The Lambda function itself 
is very simple, but contains all neeeded elements.

In order to create some test cases, also very simple, The Lambda function contains some functions to be easily tested. Test are defined in `tests` directory.

### Reports

During the pipeline execution tests are conducted, and test reports, as well as code coverage reports are generated. They can be found in CodeBuild part of CodePipeline service. 

## Code changes

Every change commited to `master` branch will trigger the build.
