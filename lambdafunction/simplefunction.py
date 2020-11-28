""" Demo lambda """

import json

def sumnumbers(a, b):
    """ simple function """
    result = a + b
    return result

def mutiplynumbers(a, b):
    """ simple function """
    result = a * b
    return result

def subnumbers(a, b):
    """ simple function """
    result = a - b
    return result

def divisionnumbers(a, b):
    """ simple function """
    result = a / b
    return result


def handler(event, context):
    """ A very simple Lambda function """
    numa = 5646
    numb = 3446
    firstoperation = sumnumbers(numa, numb)
    secondoperation = mutiplynumbers(numa, numb)
    thirdoperation = subnumbers(numa, numb)
    fourthoperation = divisionnumbers(numa, numb)
    response = "sum {}, multiply {}, substraction {}, division {}".format(
        firstoperation,
        secondoperation,
        thirdoperation,
        fourthoperation
    )
    return {
        'statusCode': 200,
        'body': json.dumps(response)
    }

